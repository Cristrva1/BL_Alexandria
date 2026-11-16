"""Retiros decididos por el propietario el 2026-11-16 (20 candidatos + ecosistema n8n)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RETIRED_NOW = {
    "openclaude", "codex-chatgpt-web", "fugu", "company-pixel-office", "pixel-hedge-fund", "pixelfund-ai",
    "palmier-pro", "open-generative-ai", "dsh-qa", "dsh-android", "dsh-ios", "dsh-game-studio", "treg",
    "deepwiki-open", "pandas-ai", "face-recognition", "ruview", "music-megathread", "camofox-browser", "hypit",
    "n8n", "n8n-mcp", "n8n-skills",
}
KEPT = {"annas-mcp", "deep-live-cam", "facefusion", "browser-harness", "browser-use", "dsh-noema"}


def test_retired_repos_are_in_the_ledger_and_purged():
    ledger = {r["id"]: r for r in json.loads((ROOT / "data" / "retired.json").read_text())["repos"]}
    assert RETIRED_NOW <= set(ledger)
    assert ledger["n8n"]["reason"] == "editorial"
    assert "n8n-io" in ledger["n8n"]["evidence"]
    index = json.loads((ROOT / "INDICE_IA.json").read_text())
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text())
    ids = {r["id"] for r in index["repos"]}
    assert KEPT <= ids
    gone = RETIRED_NOW | {"n8n-io"}
    assert not ids & gone
    assert not set(detail["repos"]) & gone
    for rid, entry in detail["repos"].items():
        assert not {c["id"] for c in entry.get("combina_con") or []} & gone, rid
        assert not set(entry.get("combines_with") or []) & gone, rid
        assert not set(entry.get("alternatives") or []) & gone, rid
    for repo in index["repos"]:
        assert not set(repo.get("alt") or []) & gone, repo["id"]
    for recipe in index["recipes"]:
        assert not set(recipe["repos"]) & gone, recipe["id"]
    for rid in gone:
        assert not (ROOT / "human" / "fichas" / f"{rid}.md").exists(), rid
