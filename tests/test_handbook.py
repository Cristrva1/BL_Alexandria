import copy
import json
from pathlib import Path
import subprocess

import pytest

from repo_intelligence.core.handbook import load_handbook, render_handbook
from repo_intelligence.web.catalog import build_catalog

ROOT = Path(__file__).resolve().parents[1]


def test_handbook_is_separate_from_repository_inventory_and_keeps_verified_identities():
    catalog = build_catalog(ROOT)
    h = catalog['handbook']
    assert len(h['resources']) == 57
    assert len(h['prompts']) == 48
    topics = {p['topic'] for p in h['prompts']}
    assert {'disenar', 'lanzar', 'contenido', 'negocio', 'aprender', 'diagnosticar'} <= topics
    assert all('docs.google.com' not in p.get('inspired_by', {}).get('url', '') for p in h['prompts'])
    assert len(h['paths']) == 8
    assert catalog['counts']['repos'] == len(catalog['repos'])
    by_id = {r['id']: r for r in h['resources']}
    assert by_id['muse']['sources'][0]['url'] == 'https://muse.ai/'
    assert by_id['muse']['repo_ids'] == []
    assert 'Muse bot' in by_id['muse']['aliases']
    assert by_id['opencode']['repo_ids'] == ['opencode']
    assert by_id['deepseek-harness']['group'] == 'agentes'
    assert by_id['deepseek-api']['group'] == 'modelos'
    assert 'macOS' in by_id['dsh-ios']['prepare'][0]
    assert 'Android' in by_id['scrcpy']['summary']
    assert all(p['authorship'] == 'Plantilla original de Alexandría' for p in h['prompts'])


@pytest.mark.parametrize('breakage', ['duplicate', 'source', 'repository', 'path'])
def test_handbook_rejects_broken_provenance_or_references(tmp_path, breakage):
    data = copy.deepcopy(load_handbook(ROOT))
    if breakage == 'duplicate':
        data['resources'][1]['id'] = data['resources'][0]['id']
    elif breakage == 'source':
        data['resources'][0]['sources'][0]['url'] = 'javascript:alert(1)'
    elif breakage == 'repository':
        data['resources'][0]['repo_ids'] = ['nonexistent-repo']
    else:
        data['paths'][0]['steps'][0]['resource'] = 'not-a-guide'
    (tmp_path/'data').mkdir()
    (tmp_path/'data/handbook.json').write_text(json.dumps(data), encoding='utf-8')
    ids = {r['id'] for r in build_catalog(ROOT)['repos']}
    with pytest.raises(ValueError):
        load_handbook(tmp_path, ids)


def test_handbook_markdown_is_generated_from_the_same_content(tmp_path):
    (tmp_path/'data').mkdir()
    (tmp_path/'data/handbook.json').write_text((ROOT/'data/handbook.json').read_text(encoding='utf-8'), encoding='utf-8')
    markdown = render_handbook(tmp_path).read_text(encoding='utf-8')
    for r in load_handbook(ROOT)['resources']:
        assert f'<a id="{r["id"]}"></a>' in markdown
        assert r['sources'][0]['url'] in markdown
    assert 'docker compose config --quiet' in markdown
    assert 'Diseñar un atajo de iPhone' in markdown


def test_handbook_search_routes_and_rendering_escape_untrusted_queries():
    catalog = build_catalog(ROOT)
    script = r'''
const assert=require('node:assert/strict'),h=require(process.argv[1]);
const c=JSON.parse(require('node:fs').readFileSync(0,'utf8'));
assert.deepEqual(h.selectResources(c,'configurar','','commancode').map(r=>r.id),['command-code']);
assert.deepEqual(h.selectResources(c,'configurar','','Muse bot').map(r=>r.id),['muse']);
assert.deepEqual(h.selectResources(c,'configurar','','t3code').map(r=>r.id),['t3code']);
assert.ok(h.selectResources(c,'configurar','movil','iPhone').some(r=>r.id==='atajos'));
assert.ok(!h.selectResources(c,'servicios').some(r=>r.id==='codex'));
assert.equal(h.sectionOf(c,'supabase'),'servicios');
assert.equal(h.sectionOf(c,'ruta-android'),'configurar');
const dangerous='<img src=x onerror=alert(1)>';
for (const render of [()=>h.index(c,'configurar',new URLSearchParams({q:dangerous})),()=>h.prompts(c,new URLSearchParams({q:dangerous}))]){
 const html=render();assert.ok(!html.includes(dangerous));assert.ok(html.includes('&lt;img'));
}
for(const resource of c.handbook.resources){
 const html=h.detail(c,resource.id);assert.ok(html.includes(resource.name));
 assert.ok(html.includes('manual-sources'));assert.ok(html.includes('manual-start'));
}
for(const path of c.handbook.paths)assert.ok(h.detail(c,path.id).includes('Recorrido sugerido'));
const commands=h.prompts(c,new URLSearchParams({type:'commands',q:'qwen'}));
assert.ok(commands.includes('/auth'));assert.ok(commands.includes('Dentro de una sesión'));
assert.ok(!h.detail(c,'muse').includes('#/repo/muse-spark'));
assert.ok(h.detail(c,'missing').includes('Esta guía no está disponible'));
'''
    result = subprocess.run(['node', '-e', script, str(ROOT/'src/repo_intelligence/web/assets/handbook.js')],
                            input=json.dumps(catalog), capture_output=True, text=True, encoding='utf-8')
    assert result.returncode == 0, result.stderr
