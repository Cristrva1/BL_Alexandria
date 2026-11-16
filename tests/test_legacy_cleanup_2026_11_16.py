"""Legacy guides, plans and n8n infrastructure removed (2026-11-16)."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GONE = ["guias/guia1.md", "guias/guia3.md", "Plan.a.md", "PLAN_ENRIQUECER_GUIAS.md",
        "docs/superpowers/specs/2026-08-23-bl-alexandria-mapa-completo.md", "infra/n8n/docker-compose.yml",
        "tools_check/mirror_to_guia.py"]


def test_legacy_files_are_gone_and_unreferenced():
    for rel in GONE:
        assert not (ROOT / rel).exists(), rel
    for rel in ["README.md", "AGENTS.md", "Guia.md", "scripts/expand_guia_scan_tables.py", "INDICE_IA.detalle.json"]:
        text = (ROOT / rel).read_text(encoding="utf8")
        for needle in ["guia1.md", "guia3.md", "Plan.a.md", "PLAN_ENRIQUECER_GUIAS", "mirror_to_guia", "infra/n8n"]:
            assert needle not in text, (rel, needle)


def test_remaining_legacy_guides_have_no_broken_anchors():
    result = subprocess.run([sys.executable, "tools_check/check_guias.py"], cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout[-2000:]
