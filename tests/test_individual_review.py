"""Protect documentary evidence, uncertainty and category boundaries in the 679 review."""
import csv
import json
from pathlib import Path

from repo_intelligence.core.access import access_routes
from repo_intelligence.core.catalog import load_catalog
from repo_intelligence.web.catalog import build_catalog

ROOT=Path(__file__).resolve().parents[1]
CURATION=ROOT/'curation/review-679-2026-11-14'


def test_every_public_identity_has_one_individual_decision_and_current_evidence():
    rows=[]
    for path in CURATION.glob('reviews*.psv'):
        with path.open(encoding='utf8',newline='') as handle:
            rows.extend(csv.DictReader(handle,delimiter='|'))
    catalog=build_catalog(ROOT)
    report=json.loads((ROOT/'reports/review-679-2026-11-14.json').read_text(encoding='utf8'))
    assert len(rows)==len({r['id'] for r in rows})==679
    assert {r['id'] for r in rows}=={r['id'] for r in catalog['repos']}==set(report['repositories'])
    assert report['individually_reviewed']==report['total']==679 and not report['pending']
    ledger={r['id']:r for r in rows}
    for repo in catalog['repos']:
        record=report['repositories'][repo['id']]
        review=repo['editorial_review']
        assert review['status']=='source_reviewed' and review['installation_tested'] is False
        assert repo['access']['source_blob_sha']==review['source_blob_sha']==record['source_blob_sha']
        assert record['source'] in repo['access']['sources']
        assert len(review['checks'])==9
        assert len(repo['practical_examples'])==2
        assert repo['first_try']['action']==ledger[repo['id']]['first_action']
        assert repo['first_try']['execution']=='proposed_not_executed'
        assert repo['first_try']['success']==ledger[repo['id']]['success']
        selected=ledger[repo['id']]['install']
        if selected.startswith('docs:'):
            assert repo['getting_started']['source']==selected[5:]
        if selected in {'read','readme'} or selected.startswith('docs:'):
            assert not repo['getting_started']['command']
        assert all(example['status']=='illustrative' for example in repo['practical_examples'])


def test_meaningful_classification_and_identity_corrections():
    cat=load_catalog(ROOT)
    for rid,expected in {'cal.diy':(18,'reservas'),'fluxer':(17,'comunidades'),'warp':(26,'simulacion'),'planck-js':(26,'simulacion'),'skillspector':(16,'skills'),'moviepy':(30,'motores'),'nextcloud-server':(15,'archivos')}.items():
        repo=cat.get(rid)
        assert (repo['cat'],repo['sub'])==expected
        assert repo['editorial_review']['category_verdict']=='corrected'
    assert cat.get('llmfit')['role']=='app'
    assert 'hardware' in cat.get('llmfit')['desc'].lower() or 'equipo' in cat.get('llmfit')['desc'].lower()
    assert cat.get('botpress')['role']=='library' and not cat.get('botpress')['alternatives']
    assert cat.get('muse-spark')['status']=='unverified'
    assert cat.get('muse-spark')['access']['api']=='unconfirmed'
    assert not cat.get('muse-spark')['getting_started']['command']


def test_references_and_unknown_costs_do_not_become_supported_plan_routes():
    cat=load_catalog(ROOT)
    prompt=cat.get('prompt-master')
    assert prompt['access']['codex']==prompt['access']['antigravity']=='reference'
    assert 'codex' not in access_routes(prompt) and 'antigravity' not in access_routes(prompt)
    assert 'review' in access_routes(cat.get('edge-tts'))
    assert cat.get('edge-tts')['access']['local_model']!='supported'
    assert cat.get('video-use')['access']['api']=='required'
    assert cat.get('claude-agent-sdk-python')['access']['claude_code']=='project_integration'
    assert 'no_api' not in access_routes({'access':{'api':'required','local_model':'supported','cost':'choice'}})
    assert 'no_api' in access_routes({'access':{'api':'not_required','cost':'host_plan'}})


def test_antigravity_is_available_in_exports_without_promoting_sdk_mentions():
    catalog=build_catalog(ROOT)
    assert 'antigravity' in catalog['labels']['route']
    repos={r['id']:r for r in catalog['repos']}
    assert 'antigravity' in repos['camofox-browser']['routes']
    assert 'antigravity' not in repos['openai-python']['routes']
    topics={t['id']:t for a in catalog['discovery']['areas'] for t in a['topics']}
    assert 'camofox-browser' in topics['antigravity-mcp']['repo_ids']
    assert 'fluxer' not in topics['negocio-whatsapp']['repo_ids']
    assert 'fluxer' in topics['negocio-comunidades']['repo_ids']
