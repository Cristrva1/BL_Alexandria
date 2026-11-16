"""`repo-intelligence add`: altas por lote con gh api simulado, ligero y combinaciones."""
from __future__ import annotations

import base64
import json
import shutil
from pathlib import Path

import pytest
from typer.testing import CliRunner

from repo_intelligence.analysis.combina_policy import classify, combo_map
from repo_intelligence.cli import app
from repo_intelligence.curate import add as add_mod

ROOT = Path(__file__).resolve().parents[1]
README = "# Demo\n\nInstala con `pip install demo-tool` y ejecuta `demo scan`.\n"


def _meta(full: str, gid: int, **extra) -> dict:
    owner, name = full.split("/")
    meta = {"id": gid, "full_name": full, "name": name, "html_url": f"https://github.com/{full}", "private": False, "archived": False,
            "stargazers_count": 4321, "license": {"spdx_id": "MIT"}, "pushed_at": "2026-11-10T00:00:00Z", "topics": ["security"],
            "homepage": f"https://{name}.example", "default_branch": "main", "language": "Go", "description": "A demo tool",
            "owner": {"login": owner, "type": "Organization"}}
    meta.update(extra)
    return meta


def fake_gh(metas: dict[str, dict]):
    calls: list[str] = []

    def gh(path: str) -> dict:
        calls.append(path)
        parts = path.split("/")
        full = "/".join(parts[1:3])
        meta = metas.get(full.lower())
        if meta is None:
            raise add_mod.AddError(f"gh api {path}: Not Found")
        if len(parts) == 3:
            return meta
        if parts[3] == "readme":
            return {"html_url": f"{meta['html_url']}/blob/main/README.md", "sha": "abc123",
                    "content": base64.b64encode(README.encode()).decode()}
        if parts[3] == "git":
            return {"sha": "tree123", "tree": [{"path": "go.mod", "type": "blob"}, {"path": "Dockerfile", "type": "blob"}]}
        if parts[3] == "releases":
            return {"tag_name": "v1.2.3", "published_at": "2026-11-01T00:00:00Z"}
        raise add_mod.AddError("ruta no simulada")

    gh.calls = calls  # type: ignore[attr-defined]
    return gh


@pytest.fixture()
def project(tmp_path: Path) -> Path:
    for name in ("INDICE_IA.json", "INDICE_IA.detalle.json"):
        shutil.copy(ROOT / name, tmp_path / name)
    (tmp_path / "data").mkdir()
    shutil.copy(ROOT / "data/retired.json", tmp_path / "data/retired.json")
    shutil.copytree(ROOT / "curation/descripciones-4s", tmp_path / "curation/descripciones-4s")
    (tmp_path / "scripts").mkdir()
    shutil.copy(ROOT / "scripts/document_curation_20261114.py", tmp_path / "scripts/document_curation_20261114.py")
    return tmp_path


def _spec(rid: str, full: str, **extra) -> dict:
    spec = {"gh": full, "id": rid, "name": rid.title(), "cat": 16, "sub": "defensa", "kind": "app",
            "one": "Herramienta de demostración para comprobar el alta automática de un repo de seguridad en el catálogo.",
            "how": "CLI en Go que analiza un objetivo de laboratorio y genera un informe.",
            "examples": ["auditar un servidor de laboratorio propio", "comparar dos configuraciones antes de publicarlas"],
            "try": ["Instala con `pip install demo-tool` y ejecuta un análisis sobre una VM propia.", "Obtienes un informe con hallazgos."],
            "tags": ["security"], "goals": [], "cmd": "pip install demo-tool",
            "que_es": "Herramienta de ejemplo para las pruebas.", "que_hace": "Analiza un objetivo de laboratorio.",
            "como_lo_hace": "Se instala con pip y se ejecuta en la terminal.", "fuentes": [f"https://github.com/{full}"],
            "combina_con": [{"id": "wazuh", "motivo": "Enviar hallazgos al SIEM.", "orden_instalacion": "Wazuh primero."},
                            {"id": "lynis", "motivo": "Completar la auditoría del host.", "orden_instalacion": "Lynis después."},
                            {"id": "crowdsec", "motivo": "Bloquear lo detectado.", "orden_instalacion": "CrowdSec al final."}]}
    spec.update(extra)
    return spec


def _load(root: Path):
    compact = json.loads((root / "INDICE_IA.json").read_text(encoding="utf8"))
    detail = json.loads((root / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]
    return compact, detail


def test_full_batch_writes_entries_four_sections_and_reciprocity(project: Path):
    gh = fake_gh({"acme/demo": _meta("acme/demo", 990001)})
    result = add_mod.run_add(project, {"lote": "prueba", "fecha": "2026-11-16", "repos": [_spec("demo", "acme/demo")]}, gh=gh)
    assert [a["id"] for a in result.added] == ["demo"] and not result.skipped
    compact, detail = _load(project)
    repo = next(r for r in compact["repos"] if r["id"] == "demo")
    assert repo["github_id"] == 990001 and repo["stars"] == 4321 and repo["license"] == "MIT" and "nivel" not in repo
    d = detail["demo"]
    assert d["que_es"] and d["combines_with"] == ["wazuh", "lynis", "crowdsec"]
    assert d["descripcion_github"]["latest_release"] == "v1.2.3 (2026-11-01)"
    assert d["getting_started"]["command"] == "pip install demo-tool"
    assert "alcance autorizado" in d["limits"]
    # al menos un destino no hub/saturado recibe la recíproca (p. ej. lynis tras las altas de ciber)
    assert result.reciprocal, result.reciprocal
    dest = next(iter(result.reciprocal))
    assert "demo" in result.reciprocal[dest]
    back = next(c for c in detail[dest]["combina_con"] if c["id"] == "demo")
    assert back["reciproca_de"] == "demo" and back["motivo"].startswith("Combinación recíproca")
    four = [json.loads(p.read_text(encoding="utf8")) for p in (project / "curation/descripciones-4s").glob("*.json")]
    assert any("demo" in {c["id"] for c in (doc["repos"].get(dest) or {}).get("combina_con", [])} for doc in four)
    assert (project / "curation/descripciones-4s/48-altas-prueba.json").exists()
    assert (project / "curation/altas/prueba.json").exists() and (project / "reports/altas/prueba.json").exists()
    assert not classify(combo_map(detail), exempt=add_mod.ligero_ids(compact))["violation"]
    cat = next(c for c in compact["categories"] if c["num"] == 16)
    assert cat["count"] == sum(r["cat"] == 16 and not r.get("alias_of") for r in compact["repos"])


def test_rejects_archived_duplicates_and_retired(project: Path):
    compact, _ = _load(project)
    nmap = next(r for r in compact["repos"] if r["id"] == "nmap")
    retired = json.loads((project / "data/retired.json").read_text(encoding="utf8"))["repos"][0]
    metas = {"acme/old": _meta("acme/old", 990002, archived=True),
             nmap["gh"].lower(): _meta(nmap["gh"], nmap["github_id"]),
             "other/nmap-copy": _meta("other/nmap-copy", nmap["github_id"]),
             retired["gh"].lower(): _meta(retired["gh"], retired["github_id"])}
    batch = {"lote": "rechazos", "repos": [_spec("old", "acme/old"), _spec("nmap2", nmap["gh"]),
                                         _spec("nmapcopy", "other/nmap-copy"), _spec("ret", retired["gh"])]}
    result = add_mod.run_add(project, batch, gh=fake_gh(metas), simulate=True)
    reasons = {s["gh"]: s["motivo"] for s in result.skipped}
    assert "archivado" in reasons["acme/old"]
    assert "ya está en el catálogo como «nmap»" in reasons[nmap["gh"]]
    assert "ya está en el catálogo como «nmap»" in reasons["other/nmap-copy"]
    assert "--force" in reasons[retired["gh"]] and not result.added
    forced = add_mod.run_add(project, {"lote": "f", "repos": [_spec("ret", retired["gh"])]}, gh=fake_gh(metas), force=True, simulate=True)
    assert [a["id"] for a in forced.added] == ["ret"] and any("retirado" in w for w in forced.warnings)


def test_id_collision_and_invalid_spec_stop_the_batch(project: Path):
    gh = fake_gh({"acme/demo": _meta("acme/demo", 990003)})
    clash = add_mod.run_add(project, {"lote": "x", "repos": [_spec("wazuh", "acme/demo")]}, gh=gh, simulate=True)
    assert "el id «wazuh» ya lo usa" in clash.skipped[0]["motivo"]
    with pytest.raises(add_mod.AddError, match="60-175"):
        add_mod.run_add(project, {"lote": "x", "repos": [_spec("demo", "acme/demo", one="Corta")]}, gh=gh, simulate=True)
    with pytest.raises(add_mod.AddError, match="combina_con debe tener 3-6"):
        add_mod.run_add(project, {"lote": "x", "repos": [_spec("demo", "acme/demo", combina_con=[])]}, gh=gh, simulate=True)
    with pytest.raises(add_mod.AddError, match="no existe en la categoría"):
        add_mod.run_add(project, {"lote": "x", "repos": [_spec("demo", "acme/demo", sub="inexistente")]}, gh=gh, simulate=True)
    before = (project / "INDICE_IA.json").read_text(encoding="utf8")
    assert before == (ROOT / "INDICE_IA.json").read_text(encoding="utf8")  # nada escrito


def test_ligero_allows_zero_combos_but_validates_ids(project: Path):
    gh = fake_gh({"acme/lite": _meta("acme/lite", 990004), "acme/lite2": _meta("acme/lite2", 990005)})
    result = add_mod.run_add(project, {"lote": "ligero", "repos": [_spec("lite", "acme/lite", combina_con=[])]}, gh=gh, ligero=True)
    assert result.added[0]["nivel"] == "ligero"
    compact, detail = _load(project)
    assert next(r for r in compact["repos"] if r["id"] == "lite")["nivel"] == "ligero" and detail["lite"]["combina_con"] == []
    with pytest.raises(add_mod.AddError, match="no-existe"):
        add_mod.run_add(project, {"lote": "l2", "repos": [_spec("lite2", "acme/lite2", ligero=True,
                                                               combina_con=[{"id": "no-existe", "motivo": "x"}])]}, gh=gh)
    # un ligero que enlaza a otro repo no le obliga a corresponder
    add_mod.run_add(project, {"lote": "l3", "repos": [_spec("lite2", "acme/lite2", ligero=True,
                                                           combina_con=[{"id": "lynis", "motivo": "Auditar el host."}])]}, gh=gh)
    compact, detail = _load(project)
    assert "lite2" not in {c["id"] for c in detail["lynis"]["combina_con"]}
    groups = classify(combo_map(detail), exempt=add_mod.ligero_ids(compact))
    assert ("lite2", "lynis") in groups["exempt"] and not groups["violation"]


def test_alt_groups_new_subcategories_and_skipped_partner(project: Path):
    metas = {"acme/one": _meta("acme/one", 990006), "acme/two": _meta("acme/two", 990007), "acme/gone": _meta("acme/gone", 990008, archived=True)}
    one = _spec("one", "acme/one", sub="nueva-sub", combina_con=[{"id": "gone", "motivo": "x"}], ligero=True)
    two = _spec("two", "acme/two", sub="nueva-sub")
    batch = {"lote": "alt", "subcategorias_nuevas": [{"cat": 16, "key": "nueva-sub", "title": "Subcategoría de prueba"}],
             "alt_groups": [["one", "two", "gone"]], "repos": [one, two, _spec("gone", "acme/gone")]}
    result = add_mod.run_add(project, batch, gh=fake_gh(metas))
    assert result.new_subs == ["16/nueva-sub"] and {a["id"] for a in result.added} == {"one", "two"}
    assert any("omitidos" in w for w in result.warnings)
    compact, detail = _load(project)
    repos = {r["id"]: r for r in compact["repos"]}
    assert repos["one"]["alt"] == ["two"] and repos["two"]["alt"] == ["one"] and detail["one"]["alternatives"] == ["two"]
    assert "nueva-sub" in {s["key"] for c in compact["categories"] if c["num"] == 16 for s in c["subs"]}


def test_single_add_scaffolds_pending_draft(project: Path):
    meta = _meta("acme/draft", 990009)
    spec = add_mod.default_spec("acme/draft", meta, cat=16, sub="defensa")
    spec["ligero"] = True
    result = add_mod.run_add(project, {"lote": "borrador", "repos": [spec]}, gh=fake_gh({"acme/draft": meta}), simulate=True)
    assert result.added[0]["borrador"] and spec["one"].startswith(add_mod.PENDING)


def test_suggest_and_apply_combos_respect_alts_and_cap(project: Path):
    compact, detail = _load(project)
    picks = add_mod.suggest_combos("hashcat", compact, detail)
    ids = [p["id"] for p in picks]
    assert ids and len(ids) <= 6 and "hashcat" not in ids
    assert not set(ids) & set(next(r for r in compact["repos"] if r["id"] == "hashcat")["alt"])
    assert not set(ids) & {c["id"] for c in detail["hashcat"]["combina_con"]}
    out = add_mod.apply_suggested(project, "hashcat", picks)
    compact, detail = _load(project)
    assert len(detail["hashcat"]["combina_con"]) <= 6 and out["añadidas"]
    assert not classify(combo_map(detail), exempt=add_mod.ligero_ids(compact))["violation"]


def test_cli_suggestions_for_existing_repo_do_not_write(monkeypatch):
    monkeypatch.chdir(ROOT)
    before = (ROOT / "INDICE_IA.detalle.json").read_bytes()
    result = CliRunner().invoke(app, ["add", "wazuh", "--sugerir-combos"])
    assert result.exit_code == 0, result.output
    assert "Combinaciones sugeridas para wazuh" in result.output
    assert (ROOT / "INDICE_IA.detalle.json").read_bytes() == before
    refused = CliRunner().invoke(app, ["add", "nmap/nmap"])
    assert refused.exit_code != 0


def test_cli_batch_simulation_with_mocked_gh(monkeypatch, project: Path):
    lote = project / "lote.json"
    lote.write_text(json.dumps({"lote": "cli", "repos": [_spec("demo", "acme/demo")]}), encoding="utf8")
    monkeypatch.chdir(project)
    gh = fake_gh({"acme/demo": _meta("acme/demo", 990010)})
    monkeypatch.setattr(add_mod, "gh_api", gh)
    monkeypatch.setattr(add_mod.run_add, "__kwdefaults__", {**add_mod.run_add.__kwdefaults__, "gh": gh})
    from repo_intelligence.quality import metrics as metrics_mod

    def fake_collect(root, targets, **_kw):
        return {t["id"]: {"id": t["id"], "fecha": "2026-11-16", "estrellas": 4321, "estrellas_anio": 900.0, "edad_dias": 1800,
                          "commits_90d": 40, "releases_365d": 6, "primera_respuesta_dias": 1.0, "ratio_cerradas": 0.9,
                          "cuota_principal": 0.5, "semver_mayor": 1, "licencia_spdx": "MIT", "propietario": "acme",
                          "propietario_tipo": "Organization", "lenguaje": "Go", "scorecard": None} for t in targets}

    monkeypatch.setattr(metrics_mod, "collect", fake_collect)
    result = CliRunner().invoke(app, ["add", "--desde", str(lote), "--simular"])
    assert result.exit_code == 0, result.output
    assert "demo" in result.output and "simulación" in result.output
    assert "Calidad al alta" in result.output and "/100" in result.output


def test_catalog_has_no_pending_drafts():
    compact = json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]
    assert not [r["id"] for r in compact["repos"] if r.get("borrador")]
    for rid, d in detail.items():
        for f in ("que_es", "que_hace", "como_lo_hace", "desc"):
            assert add_mod.PENDING + ":" not in (d.get(f) or ""), (rid, f)
