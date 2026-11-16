"""Prepare new public GitHub stars for an editorial agent, without changing the catalog.

Run ``uv run python scripts/daily_stars.py``. Complete pagination and numeric GitHub
identities prevent missing or duplicating renamed repositories. Source snapshots and
the queue stay in ignored data/reviews/. This script does not infer categories,
costs or client compatibility, and never executes catalogued software.
"""
from __future__ import annotations

import argparse
import base64
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+")


def github(endpoint: str, *, paginate: bool = False):
    args = ['gh', 'api']
    if paginate:
        args += ['--paginate', '--slurp']
    result = subprocess.run(args + [endpoint], capture_output=True, encoding='utf8', timeout=180)
    if result.returncode:
        raise RuntimeError(f'GitHub request failed ({result.returncode}); no catalog changes made.')
    return json.loads(result.stdout)


def public_stars(pages: list) -> list[dict]:
    """Reject partial, malformed and unstable pagination; never include private repos."""
    if not isinstance(pages, list) or not pages or any(not isinstance(p, list) for p in pages):
        raise ValueError('Expected all pages of GitHub stars')
    if any(len(page) != 100 for page in pages[:-1]) or len(pages[-1]) > 100:
        raise ValueError('Unexpected pagination; repeat the complete scan')
    stars, seen = [], set()
    for page in pages:
        for repo in page:
            if not isinstance(repo, dict) or not isinstance(repo.get('id'), int):
                raise ValueError('Missing stable GitHub identity')
            if repo['id'] in seen:
                raise ValueError('Stars changed during pagination; repeat the scan')
            seen.add(repo['id'])
            # Missing visibility is not evidence of a public repository.
            if repo.get('private') is not False:
                continue
            name = repo.get('full_name') or ''
            if not NAME.fullmatch(name) or repo.get('html_url', '').casefold() != ('https://github.com/' + name).casefold():
                raise ValueError('Unexpected public repository identity')
            stars.append(repo)
    return stars


def load_retired(root: Path = ROOT) -> list[dict]:
    """Repos removed on purpose (data/retired.json); a remaining star must not bring them back."""
    path = root / 'data' / 'retired.json'
    return json.loads(path.read_text(encoding='utf8'))['repos'] if path.exists() else []


def plan_candidates(stars: list[dict], entries: list[dict], retired: list[dict] = ()) -> tuple[list, list]:
    identities = {r['github_id']: r for r in entries if r.get('github_id')}
    names = {(r.get('gh') or '').casefold(): r for r in entries if r.get('gh')}
    retired_ids = {r['github_id'] for r in retired if r.get('github_id')}
    retired_names = {(r.get('gh') or '').casefold() for r in retired if r.get('gh')}
    used = {r['id'] for r in entries} | {r['id'] for r in retired}
    candidates, conflicts = [], []
    for repo in stars:
        name = repo['full_name']
        if repo['id'] in identities:
            continue  # A transfer or rename keeps its existing Alexandria id.
        if repo['id'] in retired_ids or name.casefold() in retired_names:
            continue  # Retired after review; restoring one needs an explicit editorial decision.
        previous = names.get(name.casefold())
        if previous:
            if previous.get('github_id') and previous['github_id'] != repo['id']:
                conflicts.append(dict(github_id=repo['id'], gh=name, existing_id=previous['id']))
            continue
        owner, short = name.split('/')
        rid = short.lower()
        if rid in used:
            rid = owner.lower() + '-' + rid
        if rid in used:
            rid += '-' + str(repo['id'])
        used.add(rid)
        candidates.append(dict(id=rid, github_id=repo['id'], gh=name, repo_url=repo['html_url']))
    return candidates, conflicts


def save(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.tmp')
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    temporary.replace(path)


def collect_source(candidate: dict, output: Path, checked_at: str) -> dict:
    """Collect public primary evidence; the scheduled agent still must read and curate it."""
    folder = output / 'sources' / candidate['id']
    record = dict(id=candidate['id'], checked_at=checked_at, status='unavailable')
    try:
        repo = github('repos/' + candidate['gh'])
        if repo.get('private') is not False or repo.get('id') != candidate['github_id']:
            raise ValueError('Repository is no longer a verified public identity')
        readme = github('repos/' + repo['full_name'] + '/readme')
        if readme.get('encoding') != 'base64' or not readme.get('content'):
            raise ValueError('README needs manual retrieval from the official documentation')
        raw = base64.b64decode(readme['content'])
        blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        if blob != readme.get('sha'):
            raise ValueError('README content does not match its GitHub blob SHA')
        url = readme.get('html_url') or ''
        if not url.casefold().startswith(('https://github.com/' + repo['full_name'] + '/blob/').casefold()):
            raise ValueError('Unexpected README source URL')
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'readme.md').write_bytes(raw)
        record.update(status='available', url=url, blob_sha=blob, path=readme['path'],
                      metadata={k: repo.get(k) for k in ('id','full_name','html_url','description','homepage','private','archived','disabled','license','language','stargazers_count','default_branch')})
    except (RuntimeError, ValueError, KeyError, OSError, subprocess.TimeoutExpired):
        # Keep failures actionable without leaking auth output or a newly private README.
        record['note'] = 'Primary source unavailable or identity changed; review manually before adding.'
    save(folder / 'source.json', record)
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--user', default='Cristrva1')
    parser.add_argument('--no-sources', action='store_true', help='Only detect missing identities')
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9-]+', args.user):
        parser.error('Expected a GitHub username')
    checked_at = datetime.now(timezone.utc).isoformat()
    compact = json.loads((ROOT / 'INDICE_IA.json').read_text(encoding='utf8'))
    stars = public_stars(github(f'users/{args.user}/starred?per_page=100&sort=created&direction=desc', paginate=True))
    candidates, conflicts = plan_candidates(stars, compact['repos'], load_retired())
    output = ROOT / 'data/reviews/daily-stars'
    if not args.no_sources:
        for candidate in candidates:
            candidate['source'] = collect_source(candidate, output, checked_at)
    queue = dict(user=args.user, checked_at=checked_at, public_stars=len(stars),
                 new=candidates, identity_conflicts=conflicts,
                 stars=[dict(github_id=r['id'], gh=r['full_name']) for r in stars],
                 scope='Detection and primary-source collection only; editorial review still required.')
    save(output / 'latest.json', queue)
    print(json.dumps(dict(public_stars=len(stars), new=len(candidates), identity_conflicts=len(conflicts), queue=str(output / 'latest.json'))))
    if conflicts:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
