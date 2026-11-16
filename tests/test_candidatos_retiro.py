"""Informe de candidatos a retiro: tres condiciones, evidencia por repo y sin tocar data/retired.json."""
import json
import shutil
from pathlib import Path

import pytest
from typer.testing import CliRunner

from repo_intelligence.cli import app
from repo_intelligence.quality import retirement

ROOT = Path(__file__).resolve().parents[1]


def _repo(rid, cat=5, sub="x", **kw):
    return {"id": rid, "name": rid.title(), "gh": f"acme/{rid}", "cat": cat, "sub": sub, **kw}


def _axes():
    return {k: 1.0 for k in ("adopcion", "mantenimiento", "licencia", "madurez", "respaldo", "encaje", "seguridad")}


@pytest.fixture()
def project(tmp_path):
    repos = [_repo("viejo"), _repo("lider"), _repo("unico"), _repo("solo"), _repo("activo"), _repo("archivado"), _repo("bueno"),
             _repo("sinmetricas"), _repo("retirado"), _repo("codeberg", repository_host="codeberg.org")]
    (tmp_path / "INDICE_IA.json").write_text(json.dumps({"repos": repos}), encoding="utf8")
    scores = {"viejo": 30, "lider": 40, "unico": 35, "solo": 20, "activo": 30, "archivado": 44.9, "bueno": 60, "retirado": 10}
    commits = {"viejo": 0, "lider": 0, "unico": 0, "solo": 0, "activo": 12, "archivado": 50, "bueno": 0, "retirado": 0}
    (tmp_path / "data/metricas/cache").mkdir(parents=True)
    (tmp_path / "data/metricas/puntuaciones.json").write_text(json.dumps({"repos": {
        k: {"puntuacion": v, "ejes": _axes(), "licencia": {"clase": "osi_permisiva"}} for k, v in scores.items()}}), encoding="utf8")
    for rid, n in commits.items():
        (tmp_path / f"data/metricas/cache/{rid}.json").write_text(json.dumps({
            "id": rid, "commits_365d": n, "commits_90d": 0, "ultimo_push": "2025-01-01", "archivado": rid == "archivado",
            "estrellas": 100}), encoding="utf8")
    ranking = [{"id": r, "posicion": i + 1, "puntuacion": scores[r], "papel": "recomendado" if r == "lider" else "alternativa",
                "cuando": "Si buscas esto", "cuando_origen": "plantilla", "caso_unico": r == "unico"}
               for i, r in enumerate(["lider", "viejo", "unico", "activo", "archivado", "bueno"])]
    (tmp_path / "data/grupos.json").write_text(json.dumps({"grupos": [{"id": "g", "titulo": "Grupo de prueba", "ranking": ranking,
                                                                       "miembros": [r["id"] for r in ranking], "recomendado": "lider"}]}),
                                                encoding="utf8")
    (tmp_path / "data/retired.json").write_text(json.dumps({"repos": [{"id": "retirado"}]}), encoding="utf8")
    return tmp_path


def test_only_repos_meeting_all_three_conditions(project):
    data = retirement.evaluate(project, today="2026-11-16")
    assert [e["id"] for e in data["candidatos"]] == ["viejo", "archivado"]
    near = {e["id"]: retirement._fails(e) for e in data["cerca"]}
    assert near == {"lider": "caso único", "unico": "caso único", "solo": "caso único", "activo": "con commits en 365 días",
                    "bueno": "puntuación ≥ umbral"}
    assert {x["id"]: x["motivo"] for x in data["sin_datos"]} == {"sinmetricas": "sin métricas en caché", "codeberg": "alojado en codeberg.org"}
    viejo = data["candidatos"][0]
    assert viejo["grupo"]["recomendado"] == "lider" and viejo["grupo"]["puntuacion_recomendado"] == 40
    assert all(viejo["condiciones"].values())


def test_threshold_is_configurable(project):
    assert [e["id"] for e in retirement.evaluate(project, threshold=25, today="2026-11-16")["candidatos"]] == []


def test_cli_writes_report_and_leaves_retired_untouched(project, monkeypatch):
    before = (project / "data/retired.json").read_bytes()
    result = CliRunner().invoke(app, ["candidatos-retiro", "--root", str(project), "--fecha", "2026-11-16"])
    assert result.exit_code == 0, result.output
    md = (project / "reports/candidatos-retiro-2026-11-16.md").read_text(encoding="utf8")
    js = json.loads((project / "reports/candidatos-retiro-2026-11-16.json").read_text(encoding="utf8"))
    assert "pendiente de revisión" in md
    assert "## Candidatos (2)" in md and "`viejo`" in md and "Evidencia por repo" in md and "alternativa" in md.lower()
    assert len(js["candidatos"]) == 2 and js["nota"].startswith("Propuesta")
    assert (project / "data/retired.json").read_bytes() == before


def test_published_report_matches_current_data():
    reports = sorted((ROOT / "reports").glob("candidatos-retiro-*.json"))
    assert reports, "falta el informe de candidatos a retiro"
    data = json.loads(reports[-1].read_text(encoding="utf8"))
    retired = {r.get("id") for r in json.loads((ROOT / "data/retired.json").read_text(encoding="utf8"))["repos"]}
    for e in data["candidatos"]:
        assert (e["id"] in retired) == (e.get("estado") == "retirado"), e["id"]
        assert e["puntuacion"] < data["umbral"] and (e["commits_365d"] == 0 or e["archivado"]) and e["grupo"]["papel"] != "recomendado"


def test_retired_candidate_keeps_its_row_with_state(project):
    retirement.write_report(project, retirement.evaluate(project, today="2026-11-16"))
    ledger = json.loads((project / "data/retired.json").read_text(encoding="utf8"))
    ledger["repos"].append({"id": "viejo", "retired_at": "2026-11-16", "reason": "inactivo"})
    (project / "data/retired.json").write_text(json.dumps(ledger), encoding="utf8")
    data = retirement.evaluate(project, today="2026-11-16")
    state = {e["id"]: e["estado"] for e in data["candidatos"]}
    assert state == {"viejo": "retirado", "archivado": "pendiente de revisión"}
    assert "Retirados tras la revisión: viejo" in data["nota"]
    assert "retirado el 2026-11-16 (inactivo)" in retirement.render_md(data)
