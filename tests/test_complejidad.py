"""Nivel de complejidad 1-4: señales, correcciones manuales y presentación."""
import json
from pathlib import Path

import yaml

from repo_intelligence.quality import complexity as C
from repo_intelligence.web.catalog import build_catalog

ROOT = Path(__file__).resolve().parents[1]


def _entry(**kw):
    base = {"id": "x", "cat": 1, "sub": "s", "role": "app", "setup": "easy"}
    base.update(kw)
    return base


def _detail(audience="setup", hardware="ordinary", note="", api="optional", command="", mode="software"):
    return {"getting_started": {"audience": audience, "command": command, "prerequisites": []},
            "access": {"hardware": hardware, "hardware_note": note, "api": api, "mode": mode}}


def test_signals():
    assert C.compute(_entry(role="directory"), _detail())[0] == 1
    assert C.compute(_entry(setup="heavy"), _detail(audience="ready_app"))[0] == 2
    assert C.compute(_entry(setup="easy", role="library"), _detail(audience="developer"))[0] == 2
    assert C.compute(_entry(setup="medium"), _detail(hardware="gpu"))[0] == 3
    assert C.compute(_entry(setup="medium"), _detail(note="GPU según tarea"))[0] == 2  # GPU opcional
    assert C.compute(_entry(setup="easy"), _detail(command="helm install x"))[0] == 3
    assert C.compute(_entry(setup="easy"), _detail(command="docker compose up -d"))[0] == 2
    assert C.compute(_entry(setup="easy"), _detail(api="required"))[0] == 2
    assert C.compute(_entry(cat=16, sub="explotacion-c2", setup="heavy"), _detail())[0] == 4
    assert C.compute(_entry(cat=16, sub="reversing", setup="easy"), _detail())[0] == 3
    level, why = C.compute(_entry(setup="medium"), _detail(hardware="gpu"))
    assert "necesita GPU" in why


def test_manual_override_wins_and_keeps_auto():
    res = C.resolve("x", _entry(setup="heavy"), _detail(), {"x": {"nivel": 1, "motivo": "instalador"}})
    assert res["nivel"] == 1 and res["origen"] == "manual" and res["auto"] == 3 and res["motivos"] == ["instalador"]


def test_catalog_levels_overrides_and_rendering():
    compact = {r["id"]: r for r in json.loads((ROOT / "INDICE_IA.json").read_text(encoding="utf8"))["repos"]}
    detail = json.loads((ROOT / "INDICE_IA.detalle.json").read_text(encoding="utf8"))["repos"]
    overrides = yaml.safe_load((ROOT / "curation" / "complejidad.yaml").read_text(encoding="utf8"))["correcciones"]
    public = [r for r in compact.values() if not r.get("alias_of") and int(r.get("cat") or 0) > 0]
    for r in public:
        assert r["complejidad"] in (1, 2, 3, 4), r["id"]
        cx = detail[r["id"]]["complejidad_detalle"]
        assert cx["nivel"] == r["complejidad"] and cx["nombre"] == C.NAMES[cx["nivel"]] and cx["motivos"]
    for rid, o in overrides.items():
        assert rid in compact, rid
        assert compact[rid]["complejidad"] == o["nivel"] and detail[rid]["complejidad_detalle"]["origen"] == "manual"
    assert compact["handbrake"]["complejidad"] == 1
    levels = {n: sum(1 for r in public if r["complejidad"] == n) for n in (1, 2, 3, 4)}
    assert all(levels.values())
    ficha = (ROOT / "human" / "fichas" / "handbrake.md").read_text(encoding="utf8")
    assert "**Nivel:** 1 Básico" in ficha
    web = {r["id"]: r for r in build_catalog(ROOT)["repos"]}
    assert web["handbrake"]["complejidad"]["nivel"] == 1
    js = (ROOT / "src" / "repo_intelligence" / "web" / "assets" / "app.js").read_text(encoding="utf8")
    search = (ROOT / "src" / "repo_intelligence" / "web" / "assets" / "search.js").read_text(encoding="utf8")
    assert "Nivel de complejidad" in js and 'params.get("complejidad")' in search
