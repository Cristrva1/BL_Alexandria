"""Comandos de instalación literales y licencias confirmadas leyendo LICENSE (revisión 2026-11-16)."""
import json
from pathlib import Path

from repo_intelligence.menu.export import derive_install
from repo_intelligence.web.catalog import build_catalog

ROOT = Path(__file__).resolve().parents[1]
COMPACT = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
DETAIL = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]


def _reviewed(result):
    return {rid: x for rid, x in DETAIL.items() if (x.get("revision_instalacion") or {}).get("resultado") == result}


def test_documented_commands_have_source_and_status():
    for rid, x in _reviewed("documentado").items():
        gs, rev = x["getting_started"], x["revision_instalacion"]
        assert gs["command_status"] == "documented", rid
        assert gs["command"].strip(), rid
        assert gs["source"].startswith("https://") and gs["source"] == rev["fuente"], rid
        assert "no ejecutado" in gs["note"] and gs["checked_at"] == rev["fecha"], rid
        assert f"`{gs['command']}`" in x["install"], rid
        assert "no se seleccionó uno verificable" not in " ".join(gs.get("steps") or []), rid
        for bad in ("{plugin-name}", "vX.Y.Z", "git@github.com"):
            assert bad not in gs["command"], rid


def test_repos_without_command_point_to_official_readme():
    for rid, x in _reviewed("sin_comando").items():
        gs = x["getting_started"]
        assert gs["command_status"] != "documented" and not gs.get("command"), rid
        assert "ver README oficial" in gs["note"], rid
        assert x["install"].startswith("Ver README oficial"), rid


def test_menu_uses_documented_command():
    for rid, x in list(_reviewed("documentado").items())[:20]:
        command, _, _ = derive_install({**x, "repo": x.get("repo_url") or ""})
        assert command == x["getting_started"]["command"], rid


def test_verified_licences_replace_noassertion_and_reach_web():
    compact = {r["id"]: r for r in COMPACT["repos"]}
    verified = {rid: x["licencia_verificada"] for rid, x in DETAIL.items() if x.get("licencia_verificada")}
    if not verified:
        return
    web = {r["id"]: r for r in build_catalog(ROOT)["repos"]}
    for rid, lv in verified.items():
        assert lv["texto"] and lv["fecha"] and lv["github"] == "NOASSERTION", rid
        assert lv.get("fuente", "").startswith("https://"), rid
        effective = compact.get(rid, {}).get("license") or DETAIL[rid].get("license")
        assert str(effective).upper() != "NOASSERTION", rid
        assert web[rid]["licencia_verificada"] == lv, rid
        ficha = (ROOT / "human" / "fichas" / f"{rid}.md").read_text(encoding="utf8")
        assert "**Licencia revisada el" in ficha, rid


def test_web_app_shows_reviewed_licence():
    app = (ROOT / "src/repo_intelligence/web/assets/app.js").read_text(encoding="utf8")
    assert "item.licencia_verificada" in app and "Licencia revisada el" in app
    for out in ("web", "docs"):
        assert "Licencia revisada el" in (ROOT / out / "app.js").read_text(encoding="utf8")
