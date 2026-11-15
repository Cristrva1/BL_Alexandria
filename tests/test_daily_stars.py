"""Prevent lost stars, duplicate identities, private imports and invented source evidence."""
import base64
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

spec=importlib.util.spec_from_file_location('daily_stars',Path(__file__).resolve().parents[1]/'scripts/daily_stars.py')
daily=importlib.util.module_from_spec(spec)
spec.loader.exec_module(daily)


def star(identity,name,private=False):
    return dict(id=identity,full_name=name,html_url='https://github.com/'+name,private=private)


def test_renames_and_transfers_keep_identity_and_colliding_names_stay_distinct():
    entries=[dict(id='app',github_id=1,gh='old/app'),dict(id='owner-app',gh=None)]
    candidates,conflicts=daily.plan_candidates([star(1,'new/renamed'),star(2,'owner/app'),star(3,'another/app')],entries)
    assert not conflicts
    assert [r['id'] for r in candidates]==['owner-app-2','another-app']
    assert {r['github_id'] for r in candidates}=={2,3}


def test_reused_repository_name_cannot_overwrite_an_existing_identity():
    candidates,conflicts=daily.plan_candidates([star(99,'owner/app')],[dict(id='app',github_id=1,gh='Owner/App')])
    assert not candidates and conflicts[0]['github_id']==99


def test_all_pages_are_scanned_and_nonpublic_repositories_are_excluded():
    pages=[[star(i,'owner/repo'+str(i)) for i in range(100)],
           [star(100,'owner/new'),star(101,'owner/private',True),dict(id=102)]]
    stars=daily.public_stars(pages)
    assert len(stars)==101 and stars[-1]['id']==100
    with pytest.raises(ValueError,match='pagination'):
        daily.public_stars([pages[0][:50],pages[1]])
    with pytest.raises(ValueError,match='during pagination'):
        daily.public_stars([pages[0],pages[0][:1]])
    with pytest.raises(ValueError):
        daily.public_stars({'message':'rate limited'})


def test_a_newly_private_repository_is_not_fetched_or_exposed(tmp_path,monkeypatch):
    calls=[]
    def github(endpoint):
        calls.append(endpoint)
        return dict(id=1,private=True)
    monkeypatch.setattr(daily,'github',github)
    record=daily.collect_source(dict(id='app',github_id=1,gh='owner/app'),tmp_path,'2026-11-15')
    assert len(calls)==1 and record['status']=='unavailable'
    assert not (tmp_path/'sources/app/readme.md').exists()
    assert 'metadata' not in record


def test_readme_evidence_is_verified_against_blob_sha(tmp_path,monkeypatch):
    raw=b'# Official documentation\n'
    sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    def github(endpoint):
        if endpoint.endswith('/readme'):
            return dict(content=base64.b64encode(raw).decode(),encoding='base64',sha=sha,path='README.md',html_url='https://github.com/owner/app/blob/main/README.md')
        return dict(id=1,private=False,full_name='owner/app')
    monkeypatch.setattr(daily,'github',github)
    record=daily.collect_source(dict(id='app',github_id=1,gh='owner/app'),tmp_path,'2026-11-15')
    assert record['status']=='available' and record['blob_sha']==sha
    assert (tmp_path/'sources/app/readme.md').read_bytes()==raw
    assert json.loads((tmp_path/'sources/app/source.json').read_text())['blob_sha']==sha
