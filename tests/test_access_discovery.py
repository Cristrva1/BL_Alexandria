"""Checks for the practical questions the library must answer truthfully."""
import json
from pathlib import Path
import subprocess

from repo_intelligence.core.access import API_LABELS, CLIENT_LABELS, LOCAL_LABELS, COST_LABELS, HARDWARE_LABELS, access_facts, access_routes
from repo_intelligence.core.catalog import load_catalog
from repo_intelligence.menu.export import derive_install
from repo_intelligence.analysis.recommend import recommend

ROOT=Path(__file__).resolve().parents[1]


def test_local_program_and_empty_providers_do_not_imply_free_or_local_models():
    repo={"exec":"local","prov":[]}
    assert access_facts(repo)["api"] == "unconfirmed"
    assert access_facts(repo)["local_model"] == "unconfirmed"
    assert "no_api" not in access_routes(repo)


def test_installation_never_guesses_a_package_or_starts_a_service():
    command, confidence, _ = derive_install({"name":"a-repo-not-a-package","role":"library","exec":"local","stack":"Python"})
    assert "pip install" not in command
    assert confidence == "clone"
    command, _, _ = derive_install({"name":"a-directory","role":"directory","stack":"Python"})
    assert ".claude/skills" not in command
    assert "Consultar" in command


def test_documented_entry_command_survives_without_being_rewritten():
    command, confidence, _ = derive_install({"name":"different-github-name", "getting_started":{"command":"pip install actual-package", "command_status":"documented"}})
    assert command == "pip install actual-package"
    assert confidence == "ok"


def test_every_public_card_has_separate_sourced_access_facts():
    cat=load_catalog(ROOT)
    public=[r for r in cat.repos if r.get("gh") and not r.get("alias_of")]
    for repo in public:
        a=repo["access"]
        assert a["api"] in API_LABELS, repo["id"]
        assert a["local_model"] in LOCAL_LABELS
        assert a["cost"] in COST_LABELS
        assert a["hardware"] in HARDWARE_LABELS
        assert a["claude_code"] in CLIENT_LABELS and a["codex"] in CLIENT_LABELS
        assert a["sources"] and a["checked_at"] and a["source_blob_sha"]
        assert repo["getting_started"]["steps"]
        assert repo["getting_started"]["source"].startswith("https://github.com/")
        assert repo["getting_started"]["audience"] in {"ready_app","agent","reading","developer","setup"}


def test_known_routes_distinguish_hosting_model_calls_and_external_services():
    cat=load_catalog(ROOT)
    assert cat.get("videofy-minimal")["access"]["api"] == "required"
    assert cat.get("edge-tts")["access"]["local_model"] != "supported"
    assert cat.get("codex")["access"]["codex"] == "native"
    assert cat.get("t3code")["access"]["codex"] == "project_integration"
    assert cat.get("e2b")["access"]["cost"] == "usage_based"
    assert cat.get("e2b")["access"]["api"] == "not_required"


def test_taxonomy_and_goal_references_are_consistent():
    cat=load_catalog(ROOT)
    goals=cat.compact["discovery"]["goals"]
    assert len({goal["id"] for goal in goals}) == len(goals)
    for repo in cat.repos:
        category=cat.category(repo["cat"])
        assert repo["sub"] in {sub["key"] for sub in category["subs"]}, repo["id"]
    for goal in goals:
        assert 1 <= len(goal["starters"]) <= 3
        for rid in goal["starters"] + goal["guided"]:
            assert cat.get(rid), (goal["id"], rid)
    assert cat.get("qlib")["cat"] != cat.get("metabase")["cat"]


def test_recommend_respects_an_explicit_access_route(tmp_path):
    import shutil
    for filename in ["INDICE_IA.json", "INDICE_IA.detalle.json"]:
        shutil.copy(ROOT/filename,tmp_path/filename)
    result=recommend(tmp_path,"transcribir audio",max_repos=3,access_route="local_model")
    assert result["recommended_repos"]
    assert all("local_model" in access_routes(repo) for repo in result["recommended_repos"])


def test_task_recommendation_does_not_fill_slots_with_unrelated_agent_skills(tmp_path):
    import shutil
    for filename in ["INDICE_IA.json", "INDICE_IA.detalle.json"]:
        shutil.copy(ROOT/filename,tmp_path/filename)
    result=recommend(tmp_path,"Crear una presentación desde documentos usando Codex",max_repos=3,access_route="codex")
    assert [repo["id"] for repo in result["recommended_repos"]] == ["ppt-master"]


def test_browser_search_handles_tasks_accents_and_access_intersections():
    script=r'''
const fs=require('fs');
const search=require(process.argv[1]);
const catalog=JSON.parse(fs.readFileSync(0,'utf8'));
const find=q=>search.search(catalog.repos,catalog.categories,catalog.discovery.goals,new URLSearchParams(q));
const voice=find('q='+encodeURIComponent('quiero transcribir audio'));
if(!voice.some(r=>r.id==='faster-whisper'))throw Error('Spanish task did not find transcription');
const presentation=find('q='+encodeURIComponent('PRESENTACIÓN'));
if(!presentation.some(r=>r.id==='ppt-master'))throw Error('Accent/synonym search failed');
const subset=find('goal=presentaciones&route=codex');
if(!subset.length||subset.some(r=>!r.routes.includes('codex')))throw Error('Access intersection failed');
const natural=find('q='+encodeURIComponent('presentaciones con mi suscripción de Codex'));
if(!natural.some(r=>r.id==='ppt-master')||natural.some(r=>!r.routes.includes('codex')))throw Error('Natural subscription condition failed');
const local=find('q='+encodeURIComponent('documentos con modelos locales sin API'));
if(!local.length||local.some(r=>!r.routes.includes('local_model')||!r.routes.includes('no_api')))throw Error('Local/no-API condition failed');
if(find('q=zzzxnonexistenttoken').length)throw Error('Unknown term returned false matches');
const guide=(q)=>search.guided(catalog.repos,catalog.categories,catalog.discovery.goals,new URLSearchParams(q));
if(guide('').length)throw Error('Guided flow needs an explicit goal');
const starters=guide('goal=local&route=local_model');
if(starters.length!==3||starters[0].id!=='jan')throw Error('Guided local flow should prioritize a documented interface');
if(starters.some(r=>!r.routes.includes('local_model')||r.status))throw Error('Guided access filter failed');
const agent=guide('goal=presentaciones&route=codex');
if(!agent.length||agent.length>3||agent.some(r=>!r.routes.includes('codex')))throw Error('Guided agent access failed');
if(guide('goal=voz&route=codex').length)throw Error('Guided flow must not invent subscription support');
if(guide('goal=documentos').some(r=>['pdfcraft','docling'].includes(r.id)))throw Error('Preprocessing is not a document chat app');
if(guide('goal=presentaciones').some(r=>r.id==='excalidraw'))throw Error('A diagram editor is not a presentation generator');
console.log(JSON.stringify({voice:voice.length,presentation:presentation.length,subset:subset.length}));
'''
    from repo_intelligence.web.catalog import build_catalog
    result=subprocess.run(["node","-e",script,str(ROOT/"src/repo_intelligence/web/assets/search.js")],input=json.dumps(build_catalog(ROOT)),capture_output=True,text=True,encoding="utf-8")
    assert result.returncode==0,result.stderr
