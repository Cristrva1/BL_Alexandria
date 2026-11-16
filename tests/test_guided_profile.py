"""Personalized guidance must change choices without inventing access or hardware support."""
import json
from pathlib import Path
import subprocess

from repo_intelligence.web.catalog import build_catalog

ROOT=Path(__file__).resolve().parents[1]
MODULE=ROOT/'src/repo_intelligence/web/assets/guided.js'


def run_js(script,catalog=None):
    result=subprocess.run(['node','-e',script,str(MODULE)],input=json.dumps(catalog or {}),capture_output=True,text=True,encoding='utf8')
    assert result.returncode==0,result.stderr


def test_goal_detection_has_manual_override_and_handles_ambiguity():
    run_js(r'''
const assert=require('node:assert/strict'),g=require(process.argv[1]);
const c=JSON.parse(require('node:fs').readFileSync(0,'utf8'));
const goals=c.discovery.goals;
assert.equal(g.inferGoal('Quiero crear una presentación a partir de un PDF',goals).goal.id,'presentaciones');
assert.equal(g.inferGoal('Quiero transcribir una entrevista y obtener subtítulos',goals).goal.id,'voz');
assert.equal(g.inferGoal('Quiero generar imágenes con IA local',goals).goal.id,'imagenes');
assert.equal(g.inferGoal('Quiero crear una presentación',goals,'diagramas').goal.id,'diagramas');
assert.equal(g.inferGoal('Crear diagramas y una presentación',goals).kind,'ambiguous');
assert.equal(g.inferGoal('Un proyecto completamente nuevo para mis ideas',goals).kind,'unrecognized');
''',build_catalog(ROOT))


FIXTURE=r'''
const assert=require('node:assert/strict'),g=require(process.argv[1]);
const item=(id,extra={})=>({id,name:id,lead:'Herramienta para la tarea',setup:'medium',role:'app',status:'',
  getting_started:{audience:'setup',source:'https://example.org/docs',prerequisites:['datos de prueba']},
  access:{api:'not_required',local_model:'not_applicable',cost:'no_model_fee',mode:'software'},
  first_try:{action:'Ejecutar una prueba pequeña',success:'Un resultado verificable'},...extra});
const catalog=repos=>({repos,discovery:{goals:[{id:'task',title:'Tarea',keywords:[],starters:repos.map(x=>x.id),guided:repos.map(x=>x.id)}]}});
const choose=(repos,profile={})=>g.recommend(catalog(repos),{project:'Quiero resolver esta tarea',goal:'task',...profile});
'''


def test_experience_changes_the_order_between_application_and_code():
    run_js(FIXTURE+r'''
const library=item('code',{role:'library',getting_started:{audience:'developer'}});
const app=item('app',{getting_started:{audience:'ready_app'}});
assert.equal(choose([library,app],{experience:'beginner'}).picks[0].item.id,'app');
assert.equal(choose([library,app],{experience:'developer'}).picks[0].item.id,'code');
assert.ok(choose([library,app]).picks.length<=3);
''')


def test_resources_conservatively_change_a_local_beginner_start():
    run_js(FIXTURE+r'''
const heavy=item('heavy',{setup:'heavy',access:{api:'optional',local_model:'supported',cost:'choice'}});
const low=choose([heavy],{experience:'beginner',mode:'local',ram:'small',gpu:'no'});
assert.equal(low.picks.length,0);assert.equal(low.excluded.preparation,1);
const capable=choose([heavy],{experience:'beginner',mode:'local',ram:'large',gpu:'yes'});
assert.equal(capable.picks.length,1);
assert.ok(capable.picks[0].warnings.some(w=>w.includes('no confirman')));
''')


def test_a_web_chat_does_not_become_a_coding_subscription():
    run_js(FIXTURE+r'''
const skill=item('skill',{access:{api:'not_required',local_model:'not_applicable',cost:'host_plan',mode:'agent_extension',codex:'host',claude_code:'host'}});
assert.equal(choose([skill],{clients:['web'],mode:'existing'}).picks.length,0);
assert.equal(choose([skill],{clients:['codex'],mode:'existing'}).picks.length,1);
assert.deepEqual(choose([skill],{clients:['codex','claude'],mode:'existing'}).picks[0].matched,['codex','claude']);
''')


def test_local_components_cannot_remove_required_apis_or_promote_references():
    run_js(FIXTURE+r'''
const partial=item('partial',{access:{api:'required',local_model:'supported',cost:'usage_based',codex:'project_integration'}});
const reference=item('reference',{access:{api:'not_required',local_model:'not_applicable',cost:'host_plan',mode:'agent_extension',codex:'reference'}});
for(const mode of ['local','no_api','existing'])assert.equal(choose([partial,reference],{mode,clients:['codex']}).picks.length,0);
assert.equal(choose([partial],{mode:'api'}).picks.length,1);
''')


def test_browser_only_needs_an_explicit_web_route_not_a_cloud_label():
    run_js(FIXTURE+r'''
const hosted=item('browser',{getting_started:{audience:'ready_app',browser_url:'https://example.org/app'}});
const api=item('cloud-api',{exec:'cloud'});
const result=choose([hosted,api],{os:'browser',experience:'beginner'});
assert.deepEqual(result.picks.map(p=>p.item.id),['browser']);
assert.equal(result.excluded.device,1);
assert.equal(g.startSteps(result.picks[0],result.profile)[0].href,'https://example.org/app');
''')


def test_real_catalog_recommendations_keep_identity_sources_and_three_clear_steps():
    run_js(r'''
const assert=require('node:assert/strict'),g=require(process.argv[1]);
const c=JSON.parse(require('node:fs').readFileSync(0,'utf8'));
const p={project:'Quiero crear una presentación desde un PDF',experience:'beginner',os:'windows',ram:'medium',gpu:'no',clients:['codex'],mode:'existing'};
const result=g.recommend(c,p);
assert.ok(result.picks.length>0 && result.picks.length<=3);
assert.ok(result.picks.every(x=>x.matched.includes('codex') && x.item.access.api!=='required'));
for(const pick of result.picks){
  const steps=g.startSteps(pick,p);assert.equal(steps.length,3);
  assert.ok(steps[0].text.includes('Windows'));assert.ok(steps[0].href.startsWith('https://'));
  assert.equal(steps[2].text,pick.item.first_try.action);
}
const browser=g.recommend(c,{project:'Quiero dibujar un diagrama de mi proceso',goal:'diagramas',experience:'beginner',os:'browser'});
assert.ok(browser.picks.length>0 && browser.picks.length<=3);
assert.ok(browser.picks.every(p=>p.item.getting_started.browser_url));
assert.ok(!browser.picks.some(p=>p.item.id==='mermaid'));
const tldraw=browser.picks.find(p=>p.item.id==='tldraw');
assert.ok(tldraw);
assert.equal(g.startSteps(tldraw,browser.profile)[2].text,tldraw.item.getting_started.browser_first_try.action);
assert.ok(!/proyecto de prueba/.test(g.startSteps(tldraw,browser.profile)[2].text));
assert.ok(g.firstTry(tldraw).success.includes('sin crear un proyecto de código'));
const restricted=g.recommend(c,{project:'Quiero generar imágenes con IA local',goal:'imagenes',experience:'beginner',mode:'local',ram:'small',gpu:'no'});
assert.ok(!restricted.picks.some(p=>p.item.id==='rembg'));
const lowCpu=g.recommend(c,{project:'Quiero generar imágenes con IA local',experience:'beginner',mode:'local',os:'windows',ram:'small',gpu:'no'});
assert.ok(!lowCpu.picks.some(p=>p.item.id==='comfyui'));
assert.ok(lowCpu.excluded.preparation>0);
const cpu=g.recommend(c,{project:'Quiero generar imágenes con IA local',experience:'intermediate',mode:'local',os:'windows',ram:'large',gpu:'no'});
assert.ok(cpu.picks.find(p=>p.item.id==='comfyui').warnings.some(text=>text.includes('pesada')));
''',build_catalog(ROOT))


def test_normalization_limits_text_and_does_not_invent_answers():
    run_js(r'''
const assert=require('node:assert/strict'),g=require(process.argv[1]);
const p=g.normalize({project:'x'.repeat(2000),experience:'expert!',os:'ios?',ram:'9999',clients:['web','web','fake'],mode:'free-forever'});
assert.equal(p.project.length,800);assert.equal(p.experience,'unknown');assert.equal(p.os,'unknown');
assert.equal(p.ram,'unknown');assert.equal(p.mode,'any');assert.deepEqual(p.clients,['web']);
''')


def test_documented_browser_routes_keep_primary_provenance():
    catalog=build_catalog(ROOT)
    web=[r for r in catalog['repos'] if r['getting_started'].get('browser_url')]
    assert {'excalidraw','tldraw','penpot'}<={r['id'] for r in web}
    for repo in web:
        start=repo['getting_started']
        assert start['browser_url'].startswith('https://')
        assert start['browser_source'] in repo['access']['sources']
        assert start['browser_checked_at']
