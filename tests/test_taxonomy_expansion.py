"""Protect navigation and identities when broad rooms are split by task."""
from pathlib import Path

from repo_intelligence.core.catalog import load_catalog
from repo_intelligence.web.catalog import build_catalog

ROOT = Path(__file__).resolve().parents[1]


def test_every_public_entry_has_one_consistent_room_in_all_catalog_layers():
    catalog = load_catalog(ROOT)
    web = build_catalog(ROOT)
    public = {r["id"]: r for r in catalog.repos if r["cat"] > 0 and not r.get("alias_of")}
    assert set(public) == {r["id"] for r in web["repos"]}
    rooms = [c for c in web["categories"] if c["num"] > 0]
    assert len({c["num"] for c in rooms}) == 32
    assert sum(c["count"] for c in rooms) == len(public)
    for room in rooms:
        assert room["question"] and room["description"] and room["starters"]
        assert room["count"] == catalog.category(room["num"])["count"]
    for rid, repo in public.items():
        detail = catalog.detail["repos"][rid]
        assert (repo["cat"], repo["sub"]) == (detail["cat"], detail["sub"])


def test_task_boundaries_separate_different_jobs_and_preserve_historical_category_paths():
    catalog = load_catalog(ROOT)
    for group in [("n8n","evolution-api","odoo"),("codex","langgraph","gpt-researcher"),
                  ("whisper","ffmpeg","remotion"),("comfyui","ultralytics"),
                  ("docling","ppt-master"),("mem0","langfuse"),
                  ("duckdb","unsloth","repomix")]:
        assert len({catalog.get(rid)["cat"] for rid in group}) == len(group), group
    assert catalog.get("rnnoise")["cat"] == catalog.get("whisper")["cat"]
    assert catalog.category_file(1) == "01-automatizaci-n-mensajer-a-crm.md"
    assert catalog.category_file(12) == "12-audio-voz-video.md"
    assert catalog.get("codex")["doc"] == "human/fichas/codex.md"


def test_goals_cover_their_current_members_and_keep_valid_references():
    catalog = load_catalog(ROOT)
    for goal in catalog.compact["discovery"]["goals"]:
        members = [r for r in catalog.repos if goal["id"] in r.get("goals",[]) or r["id"] in goal["starters"]+goal["guided"]]
        assert set(goal["categories"]) == {r["cat"] for r in members}


def test_resolved_names_keep_official_hosts_and_independent_access_requirements():
    catalog = load_catalog(ROOT)
    creative, security, kimi = [catalog.get(rid) for rid in ["creative-architect","cybersecurity-skills","kimi-k2-7-code"]]
    assert creative["gh"] == "Hainrixz/creative-architect"
    assert creative["access"]["claude_code"] == "host"
    assert creative["access"]["codex"] == "not_documented"
    assert security["gh"] == "mukul975/Anthropic-Cybersecurity-Skills"
    assert security["access"]["codex"] == "host"
    assert "no un producto oficial de Anthropic" in security["limits"]
    assert not kimi.get("gh") and not kimi.get("github_id")
    assert kimi["repo_url"] == "https://huggingface.co/moonshotai/Kimi-K2.7-Code"
    assert kimi["sources"]["model_revision"] in kimi["getting_started"]["source"]
    assert kimi["access"]["local_model"] == "supported"
    assert kimi["setup"] == "heavy" and 'infraestructura' in kimi['access']['hardware_note']
    for repo in [creative,security,kimi]:
        assert repo["access"]["source_blob_sha"] == repo["sources"]["readme_blob_sha"]
