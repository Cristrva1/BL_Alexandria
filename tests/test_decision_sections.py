"""Decision paths must preserve evidence and help distinguish functions, not pick winners."""
import json
from pathlib import Path
import re
import subprocess

from repo_intelligence.web.catalog import build_catalog

ROOT=Path(__file__).resolve().parents[1]


def test_objective_groups_cover_each_goal_once_and_link_to_existing_recipes():
    catalog=build_catalog(ROOT)
    goals=catalog['discovery']['goals']
    grouped=[gid for group in catalog['discovery']['goal_groups'] for gid in group['goals']]
    assert len(grouped)==len(set(grouped))==len(goals)
    assert set(grouped)=={g['id'] for g in goals}
    recipes={r['id'] for r in catalog['recipes']}
    for goal in goals:
        assert goal['outcome'] and goal['bring'] and goal['decision']
        assert set(goal['recipe_ids'])<=recipes


def test_initial_recipe_plans_are_small_disjoint_and_explicitly_unexecuted():
    catalog=build_catalog(ROOT)
    for recipe in catalog['recipes']:
        plan=recipe['plan'];available={s['id'] for s in recipe['steps']}
        assert plan['minimum'] and set(plan['minimum'])<=available
        assert set(plan['instead'])<=available-set(plan['minimum'])
        assert len(plan['minimum'])==len(set(plan['minimum']))
        assert plan['inputs'] and plan['note'] and recipe['when_not']
        assert plan['first_try']['action'] and plan['first_try']['success']
        assert plan['first_try']['execution']=='proposed_not_executed'
    assert 'sin enviar datos a terceros' not in next(r for r in catalog['recipes'] if r['id']=='workspace-privado-local-soberano')['goal']


def test_presets_use_distinct_public_identities():
    catalog=build_catalog(ROOT)
    repos={r['id']:r for r in catalog['repos']}
    for preset in catalog['discovery']['compare_presets']:
        assert 2<=len(preset['repos'])<=3
        assert len(preset['repos'])==len(set(preset['repos']))
        assert all(rid in repos for rid in preset['repos'])


def test_shared_selection_conflicts_search_and_recipe_parts_in_browser_logic():
    module=ROOT/'src/repo_intelligence/web/assets/decisions.js'
    script=r'''
const assert=require('node:assert/strict');
const d=require(process.argv[1]);
const a={id:'a',name:'Skills',gh:'owner-one/skills',goals:['learn'],alt_refs:[{id:'b'}]};
const b={id:'b',name:'Skills',gh:'owner-two/skills',goals:['learn'],combine_refs:[{id:'c'}]};
const c={id:'c',name:'C',goals:['build']},e={id:'e',name:'E'};
const byId=Object.fromEntries([a,b,c,e].map(x=>[x.id,x]));
assert.deepEqual(d.ids('a,unknown,a,b,c,e',byId),['a','b','c']);
assert.deepEqual(d.ids({bad:true},byId),[]);
const shared=new URL('https://example.org/'+d.href(['a','b'],byId));
assert.deepEqual(d.ids(new URLSearchParams(shared.hash.split('?')[1]).get('ids'),byId),['a','b']);
assert.equal(d.relationship(a,b),'alternative');
assert.equal(d.relationship(b,c),'complement');
assert.equal(d.relationship(a,c),'undocumented');
assert.deepEqual(d.candidates([a,b,c],'owner-two',[],'learn').map(x=>x.id),['b']);
assert.deepEqual(d.candidates([a,b,c],'',[],'learn').map(x=>x.id),['a','b']);
assert.deepEqual(d.candidates([a,b,c],'skills',['a'],'learn').map(x=>x.id),['b']);
assert.equal(d.different({value:x=>x.name},[a,b]),false);
assert.equal(d.different({value:x=>x.gh},[a,b]),true);
assert.deepEqual(d.recipeParts({steps:[{id:'a'},{id:'b'},{id:'c'}],plan:{minimum:['a','a','ghost'],instead:['a','b']}}),{minimum:['a'],instead:['b'],extra:['c']});
'''
    result=subprocess.run(['node','-e',script,str(module)],capture_output=True,text=True,encoding='utf8')
    assert result.returncode==0,result.stderr


def test_generated_assets_are_versioned_together_and_helpers_load_before_app():
    from tempfile import TemporaryDirectory
    from repo_intelligence.web.build import build_site
    with TemporaryDirectory() as temp:
        out=Path(temp)
        build_site(ROOT,out)
        html=(out/'index.html').read_text(encoding='utf8')
        versions=re.findall(r'(?:src|href)="(?:app.js|search.js|decisions.js|guided.js|handbook.js|styles.css)\?v=([a-f0-9]+)"',html)
        assert len(versions)==6 and len(set(versions))==1
        assert html.index('src="decisions.js')<html.index('src="app.js')
        assert html.index('src="guided.js')<html.index('src="app.js')
        assert html.index('src="handbook.js')<html.index('src="app.js')
        assert (out/'decisions.js').exists()
