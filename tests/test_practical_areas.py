"""The human, web and portable catalog must agree on practical discovery."""
from copy import deepcopy
import json
from pathlib import Path
import subprocess

import pytest

from repo_intelligence.core.catalog import load_catalog
from repo_intelligence.core.taxonomy import build_areas
from repo_intelligence.web.catalog import build_catalog

ROOT=Path(__file__).resolve().parents[1]


def test_practical_work_areas_cover_every_identity_once_per_collection():
    catalog=build_catalog(ROOT)
    ids={r['id'] for r in catalog['repos']}
    areas=catalog['discovery']['areas']
    work=[a for a in areas if a['kind']=='work']
    assert {'frontend','ciberseguridad','audiovisual','trading'} <= {a['id'] for a in work}
    assert {rid for a in work for rid in a['repo_ids']} == ids
    for a in areas:
        assert len(a['repo_ids']) == len(set(a['repo_ids'])) == a['count']
        assert set(a['repo_ids']) == {rid for t in a['topics'] for rid in t['repo_ids']}
        for t in a['topics']:
            assert t['count'] == len(t['repo_ids']) > 0
    assert sum(a['count'] for a in work) > len(ids)  # useful cross-listing, no duplicate records
    assert sum(len(a['topics']) for a in areas) == catalog['counts']['topics']


def test_setup_collections_distinguish_documented_clients_from_reference_material():
    c=build_catalog(ROOT)
    areas={a['id']:a for a in c['discovery']['areas']}
    assert {'configurar-claude-code','configurar-codex','configurar-antigravity'} <= set(areas)
    codex=areas['configurar-codex']
    assert {'codex','superpowers','context7'} <= set(codex['repo_ids'])
    assert 'openai-python' not in codex['repo_ids']  # model provider is not client setup
    antigravity=areas['configurar-antigravity']
    assert {'antigravity-awesome-skills','stitch-skills','prompt-master','context7','impeccable'} <= set(antigravity['repo_ids'])
    references={rid for t in antigravity['topics'] for rid in t.get('reference_repos',[])}
    assert 'prompt-master' in references
    assert all(r['access']['antigravity'] in {'native','host','connector','project_integration'} for r in c['repos'] if r['id'] in set(antigravity['repo_ids'])-references)
    for a in areas.values():
        for source in a.get('evidence',[]):
            r=next(r for r in c['repos'] if r['id']==source['repo_id'])
            assert source['readme_blob_sha'] == r['access']['source_blob_sha']
            assert source['source'] in r['access']['sources']
    claude=areas['configurar-claude-code']
    assert any('claude-code-hooks-mastery' in t.get('reference_repos',[]) for t in claude['topics'])


def test_invalid_selectors_and_new_uncovered_projects_fail_instead_of_disappearing():
    c=load_catalog(ROOT)
    repos=[r for r in c.repos if r['cat']>0 and not r.get('alias_of')]
    changed=deepcopy(c.compact)
    changed['discovery']['areas'][0]['topics'][0]['selectors'][0]['subs']=['nonexistent']
    with pytest.raises(ValueError,match='unknown sections'):
        build_areas(changed,repos)
    with pytest.raises(ValueError,match='without a practical work area'):
        build_areas(c.compact,repos+[dict(id='unclassified-new-project',cat=999,sub='unknown')])


def test_cross_area_setup_claims_do_not_promote_unsupported_runtime_projects():
    c=load_catalog(ROOT)
    repos=[r for r in c.repos if r['cat']>0 and not r.get('alias_of')]
    changed=deepcopy(c.compact)
    codex=next(a for a in changed['discovery']['areas'] if a['id']=='configurar-codex')
    codex['topics'][0]['repos'].append('openai-python')
    with pytest.raises(ValueError,match='no documented client support'):
        build_areas(changed,repos)


def test_search_combines_practical_topics_access_and_legacy_filters():
    script=r'''
const fs=require('fs'), search=require(process.argv[1]);
const c=JSON.parse(fs.readFileSync(0,'utf8'));
const find=q=>search.search(c.repos,c.categories,c.discovery.goals,new URLSearchParams(q));
const ids=q=>find(q).map(r=>r.id);
const voice=find('area=audiovisual&topic=av-voz');
if(!voice.length||voice.some(r=>r.cat!==29||r.sub!=='tts'))throw Error('Voice topic includes other media');
if(find('area=audiovisual&topic=av-voz&route=codex').length)throw Error('Voice topic invents Codex access');
const web=ids('area=frontend&topic=web-componentes');
if(!web.includes('tailwindcss')||!web.includes('ui')||web.includes('ffmpeg'))throw Error('Frontend components');
const trading=ids('area=trading&topic=trading-backtesting');
if(!trading.includes('qlib')||!trading.includes('backtrader')||trading.includes('openwa'))throw Error('Trading topic');
const setup=ids('q='+encodeURIComponent('configuración Antigravity'));
if(!setup.includes('stitch-skills')||JSON.stringify(setup.sort())!==JSON.stringify(ids('area=configurar-antigravity').sort()))throw Error('Natural setup search');
const codexSetup=ids('q='+encodeURIComponent('configuración de Codex')).sort();
if(JSON.stringify(codexSetup)!==JSON.stringify(ids('area=configurar-codex').sort()))throw Error('Codex setup confused with model providers');
if(!ids('q=frontend').includes('penpot'))throw Error('Practical domain vocabulary missing');
if(find('area=frontend&topic=av-voz').length||find('area=nonexistent').length)throw Error('Unknown or contradictory facet ignored');
if(find('cat=32&sub=bibliotecas').length!==3)throw Error('Old links broken');
console.log(JSON.stringify({voice:voice.length,web:web.length,trading:trading.length,setup:setup.length}));
'''
    result=subprocess.run(['node','-e',script,str(ROOT/'src/repo_intelligence/web/assets/search.js')],input=json.dumps(build_catalog(ROOT)),capture_output=True,text=True,encoding='utf8')
    assert result.returncode==0,result.stderr
