"""Grupos de alternativas aprobados por el propietario el 2026-11-16: simétricos y sin combinaciones internas."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROUPS = [["codegraph", "gitnexus", "serena", "codebase-memory-mcp", "graphify"], ["omniroute", "claude-code-router", "litellm"], ["osiris", "gods-eye-view"], ["crewai", "langgraph", "agno"], ["qdrant", "pgvector", "milvus"], ["shannon", "strix"], ["mimo-code", "opencode"], ["t3code", "opencode-manager"], ["paperclip", "multica"], ["local-deep-research", "gpt-researcher"], ["coolify", "casaos"], ["moneyprinterturbo", "short-video-factory"], ["claude-task-master", "spec-kit"], ["dograh", "pipecat", "livekit-agents"], ["pytorch", "tensorflow"], ["archify", "diagram-design"], ["openmontage", "remotion-superpowers"], ["browser-harness", "browser-use"]]


def test_alt_groups_are_symmetric_and_have_no_internal_combinations():
    index = {r["id"]: r for r in json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf-8"))["repos"]}
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf-8"))["repos"]
    for group in GROUPS:
        for rid in group:
            others = set(group) - {rid}
            assert others <= set(index[rid]["alt"]), rid
            combos = {c["id"] for c in detail[rid].get("combina_con") or []}
            assert not combos & others, rid
            assert len(combos) >= 3, rid
