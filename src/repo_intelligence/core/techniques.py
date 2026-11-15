"""Techniques, ideas and recommendations: original summaries with public sources."""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

KINDS = {'Técnica', 'Recomendación', 'Idea'}
LEVELS = {'inicial', 'intermedio', 'avanzado'}
_SLUG = re.compile(r'[a-z0-9-]+')
_PRIVATE_HOSTS = ('docs.google.com', 'drive.google.com', 'messenger.com', 'm.me')


def _public_https(value: str) -> bool:
    parsed = urlparse(value or '')
    host = parsed.netloc.lower()
    return parsed.scheme == 'https' and bool(host) and not any(host == h or host.endswith('.' + h) for h in _PRIVATE_HOSTS) \
        and not (host.endswith('facebook.com') and '/messages' in parsed.path)


def _empty() -> dict:
    return {'updated_at': '', 'areas': [], 'site_groups': [], 'rules': [], 'items': [], 'sites': []}


def load_techniques(root: Path, repos_by_gh: dict[str, str] | None = None) -> dict:
    """Load and validate data/techniques.json; link GitHub references to catalog ids."""
    path = Path(root) / 'data' / 'techniques.json'
    if not path.exists():
        return _empty()
    data = json.loads(path.read_text(encoding='utf-8'))
    areas = {a['id']: a for a in data['areas']}
    groups = {g['id'] for g in data.get('site_groups', [])}
    if len(areas) != len(data['areas']) or any(not _SLUG.fullmatch(a) for a in areas):
        raise ValueError('Technique areas must be unique slugs')
    ids = [item['id'] for item in data['items']]
    if len(ids) != len(set(ids)) or any(not _SLUG.fullmatch(i) for i in ids):
        raise ValueError('Technique identifiers must be unique, lower-case slugs')
    lookup = {k.lower(): v for k, v in (repos_by_gh or {}).items()}
    for item in data['items']:
        if item['area'] not in areas:
            raise ValueError(f"Unknown technique area: {item['id']}")
        if item['kind'] not in KINDS or item['level'] not in LEVELS:
            raise ValueError(f"Invalid kind or level: {item['id']}")
        for key in ('title', 'summary', 'why', 'caution'):
            if not str(item.get(key, '')).strip():
                raise ValueError(f"Missing {key}: {item['id']}")
        if not item.get('steps') or not item.get('sources'):
            raise ValueError(f"Missing steps or sources: {item['id']}")
        if any(not _public_https(s.get('url', '')) or not s.get('title') for s in item['sources']):
            raise ValueError(f"Invalid source: {item['id']}")
        for command in item.get('commands', []):
            if not all(command.get(k) for k in ('title', 'text', 'where', 'effect')) or not _public_https(command.get('source', '')):
                raise ValueError(f"Invalid command: {item['id']}")
        item.setdefault('commands', [])
        item.setdefault('tools', [])
        item['repo_ids'] = sorted({lookup[g.lower()] for g in item.get('github', []) if g.lower() in lookup})
    for site in data.get('sites', []):
        if site.get('area') not in groups or not _public_https(site.get('url', '')) or not site.get('name') or not site.get('purpose'):
            raise ValueError(f"Invalid site: {site.get('name')}")
    if any(not r.get('title') or not r.get('text') for r in data.get('rules', [])):
        raise ValueError('Incomplete rule')
    return data


def render_techniques(root: Path) -> Path:
    """GitHub-readable companion generated from the same data as the site."""
    data = load_techniques(root)
    areas = {a['id']: a for a in data['areas']}
    lines = ['# Técnicas, ideas y recomendaciones', '',
             'Generado desde `data/techniques.json`. Textos propios de Alexandría a partir de publicaciones y documentación pública; '
             'las cifras citadas por terceros no se verificaron y ninguna técnica se ejecutó aquí.', '',
             f"Revisión: {data['updated_at']}.", '', '## Diez reglas para empezar', '']
    lines += [f"{i}. **{r['title']}.** {r['text']}" for i, r in enumerate(data['rules'], 1)]
    for area in data['areas']:
        items = [i for i in data['items'] if i['area'] == area['id']]
        if not items:
            continue
        lines += ['', f"## {area['icon']} {area['title']}", '', area['description'], '']
        for item in items:
            lines += [f"### {item['title']}", '', f"*{item['kind']} · nivel {item['level']}*", '', item['summary'], '']
            lines += [f'{n}. {step}' for n, step in enumerate(item['steps'], 1)]
            lines += ['', f"**Por qué ayuda:** {item['why']}", '', f"**Antes de usarla:** {item['caution']}", '']
            for command in item['commands']:
                lines += [f"**Comando — {command['title']}** ({command['where']}):", '', '```text', command['text'], '```', '', command['effect'], '']
            lines.append('Fuentes: ' + ' · '.join(f"[{s['title']}]({s['url']})" for s in item['sources']))
            lines.append('')
    if data.get('sites'):
        lines += ['## Sitios y servicios útiles', '']
        for group in data.get('site_groups', []):
            sites = [s for s in data['sites'] if s['area'] == group['id']]
            if sites:
                lines += [f"### {group['icon']} {group['title']}", '']
                lines += [f"- [{s['name']}]({s['url']}): {s['purpose']}" for s in sites]
                lines.append('')
    output = Path(root) / 'human' / 'TECNICAS.md'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return output
