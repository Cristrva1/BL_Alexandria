"""Techniques are original summaries with public sources, kept apart from the repo inventory."""
import copy
import json
import subprocess
from pathlib import Path

import pytest

from repo_intelligence.core.techniques import load_techniques, render_techniques
from repo_intelligence.web.catalog import build_catalog

ROOT = Path(__file__).resolve().parents[1]
ASSET = ROOT / 'src/repo_intelligence/web/assets/techniques.js'


def test_techniques_are_complete_sourced_and_linked_to_existing_repos():
    catalog = build_catalog(ROOT)
    t = catalog['techniques']
    repo_ids = {r['id'] for r in catalog['repos']}
    areas = {a['id'] for a in t['areas']}
    assert len(t['items']) >= 60
    assert len(t['rules']) == 10
    assert {i['area'] for i in t['items']} <= areas
    assert all(set(i['repo_ids']) <= repo_ids for i in t['items'])
    assert any(i['repo_ids'] for i in t['items'])
    assert any(i['commands'] for i in t['items'])
    for item in t['items']:
        assert 60 <= len(item['summary']) <= 260, item['id']
        assert all(s['url'].startswith('https://') and 'docs.google.com' not in s['url'] for s in item['sources'])
    assert catalog['counts']['repos'] == len(catalog['repos'])


@pytest.mark.parametrize('breakage', ['private-source', 'area', 'duplicate', 'command', 'site'])
def test_techniques_reject_private_sources_and_broken_references(tmp_path, breakage):
    data = copy.deepcopy(json.loads((ROOT / 'data/techniques.json').read_text(encoding='utf-8')))
    if breakage == 'private-source':
        data['items'][0]['sources'][0]['url'] = 'https://docs.google.com/document/d/x/edit'
    elif breakage == 'area':
        data['items'][0]['area'] = 'no-existe'
    elif breakage == 'duplicate':
        data['items'][1]['id'] = data['items'][0]['id']
    elif breakage == 'command':
        data['items'][0]['commands'] = [{'title': 'x', 'text': 'x', 'where': 'x', 'effect': 'x', 'source': 'javascript:alert(1)'}]
    else:
        data['sites'][0]['url'] = 'http://example.com'
    (tmp_path / 'data').mkdir()
    (tmp_path / 'data/techniques.json').write_text(json.dumps(data), encoding='utf-8')
    with pytest.raises(ValueError):
        load_techniques(tmp_path)


def test_techniques_markdown_is_generated_from_the_same_content(tmp_path):
    (tmp_path / 'data').mkdir()
    (tmp_path / 'data/techniques.json').write_text((ROOT / 'data/techniques.json').read_text(encoding='utf-8'), encoding='utf-8')
    markdown = render_techniques(tmp_path).read_text(encoding='utf-8')
    for item in load_techniques(ROOT)['items']:
        assert item['title'] in markdown
        assert item['sources'][0]['url'] in markdown


def test_techniques_pages_filter_and_escape_untrusted_queries():
    catalog = build_catalog(ROOT)
    script = r'''
const assert=require('node:assert/strict'),t=require(process.argv[1]);
const c=JSON.parse(require('node:fs').readFileSync(0,'utf8'));
const dangerous='<img src=x onerror=alert(1)>';
const html=t.index(c,new URLSearchParams({q:dangerous}));
assert.ok(!html.includes(dangerous));assert.ok(html.includes('&lt;img'));
const area=c.techniques.items[0].area;
assert.ok(t.select(c,new URLSearchParams({area})).items.every(i=>i.area===area));
assert.equal(t.select(c,new URLSearchParams({area:'<x>'})).area,'');
assert.ok(t.index(c,new URLSearchParams()).includes('Diez reglas'));
for(const item of c.techniques.items){
  const d=t.detail(c,item.id);assert.ok(d.includes('tech-fuentes'));assert.ok(d.includes('tech-pasos'));
  if(item.commands.length)assert.ok(d.includes('data-action="copy"'));
}
assert.ok(t.detail(c,'missing').includes('no está disponible'));
'''
    result = subprocess.run(['node', '-e', script, str(ASSET)], input=json.dumps(catalog),
                            capture_output=True, text=True, encoding='utf-8')
    assert result.returncode == 0, result.stderr


def test_site_ships_the_techniques_script_before_the_app(tmp_path):
    from repo_intelligence.web.build import build_site
    build_site(ROOT, tmp_path)
    html = (tmp_path / 'index.html').read_text(encoding='utf-8')
    assert (tmp_path / 'techniques.js').exists()
    assert html.index('src="techniques.js') < html.index('src="app.js')
    assert 'name="color-scheme" content="light dark"' in html
