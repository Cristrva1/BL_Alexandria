import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validar_biblioteca_drive", ROOT / "scripts/validar_biblioteca_drive.py")
vb = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = vb
spec.loader.exec_module(vb)

SUB = "01_IA_y_Desarrollo/01_Agentes/01_Harness.md"


def ficha(fid="X-2121401671418863948", fuente="https://x.com/autor/status/2121401671418863948", **over):
    meta = {
        "id": fid, "responsable": "grok", "plataforma": "X", "formato": "publicación", "autor": "@autor",
        "publicado": "2026-11-14", "capturado": "2026-11-15", "tipo": "Guía o tutorial", "prioridad": "media",
        "fuente": fuente, "fuentes_extra": "", "repos": "", "enlaces": "", "contenido": "completo",
        "riesgo": "", "compartido_por": "", "legado": "",
    }
    meta.update(over)
    body = meta.pop("_body", "Resumen de la ficha.")
    block = "\n".join(f"{k}: {meta[k]}".rstrip() for k in vb.KEYS)
    return f"## {fid} · Título\n\n```ficha\n{block}\n```\n\n{body}\n\n---\n"


def library(tmp_path, fichas, runs=None):
    tmp_path.mkdir(parents=True, exist_ok=True)
    (tmp_path / "00_LEEME_PROTOCOLO.md").write_text("# Protocolo\n", encoding="utf-8")
    (tmp_path / "00_INDICE.md").write_text("# Índice\n", encoding="utf-8")
    sub = tmp_path / SUB
    sub.parent.mkdir(parents=True)
    sub.write_text("# Harness — Agentes\n\n" + "\n".join(fichas), encoding="utf-8")
    for agent in ("grok", "muse"):
        (tmp_path / "90_Corridas" / agent).mkdir(parents=True)
    for name, text in (runs or {}).items():
        (tmp_path / "90_Corridas" / name).write_text(text, encoding="utf-8")
    return tmp_path


def test_ids_from_urls():
    assert vb.id_from_url("https://x.com/a/status/123456789") == "X-123456789"
    assert vb.id_from_url("https://www.instagram.com/reel/DfLoqUWOuvy/?id=1") == "IG-DfLoqUWOuvy"
    assert vb.id_from_url("https://www.facebook.com/reel/1234567890") == "FB-1234567890"
    assert vb.id_from_url("https://example.com/x") is None
    assert vb.message_id("Instagram", "2026-11-06", "Título").startswith("MSG-IG-20261106-")


def test_valid_library_passes(tmp_path):
    rep = vb.validate(library(tmp_path, [ficha()]))
    assert rep.errors == []
    assert rep.stats["fichas"] == 1


def test_detects_id_mismatch_duplicates_and_bad_values(tmp_path):
    fichas = [
        ficha(),
        ficha(),
        ficha(fid="X-999999", responsable="codex", tipo="Cosa", riesgo="malware"),
    ]
    errors = "\n".join(vb.validate(library(tmp_path, fichas)).errors)
    assert "ID repetido" in errors
    assert "no corresponde a la fuente" in errors
    assert "responsable='codex'" in errors
    assert "tipo='Cosa'" in errors
    assert "riesgo 'malware'" in errors


def test_new_ficha_needs_capture_date_and_fenced_metadata(tmp_path):
    broken = "## X-123456 · Sin bloque\n\nTexto suelto.\n"
    errors = "\n".join(vb.validate(library(tmp_path, [ficha(capturado=""), broken])).errors)
    assert "falta 'capturado'" in errors
    assert "falta el bloque ```ficha" in errors


def test_warnings_for_undeclared_repos_status_and_private_terms(tmp_path):
    body = ("Usa https://github.com/owner/tool. Ya integrado en BL_Alexandria. Sirve para ProyectoX.\n\n"
            "**Notas privadas:**\n- ProyectoX lo usa.")
    rep = vb.validate(library(tmp_path, [ficha(_body=body)]), private_terms=["ProyectoX"])
    warnings = "\n".join(rep.warnings)
    assert "owner/tool" in warnings
    assert "estados de Alexandría" in warnings
    assert "ProyectoX" in warnings
    rep2 = vb.validate(library(tmp_path / "b", [ficha(_body="Autor: fandeproyectox.")]), private_terms=["ProyectoX"])
    assert not any("términos privados" in w for w in rep2.warnings)


def test_runs_are_checked_and_listed_for_review(tmp_path):
    ok_run = ("estado: terminada\n# Corrida grok 2026-11-28\n\n| id | decision | archivo | nota |\n|---|---|---|---|\n"
              f"| X-2121401671418863948 | nueva | {SUB} | |\n| X-2125000000000000003 | pendiente_contenido | | DM |\n")
    bad_run = ("estado: terminada\n| id | decision | archivo | nota |\n|---|---|---|---|\n"
               "| X-2125000000000000009 | nueva | 01_IA_y_Desarrollo/01_Agentes/99_No.md | |\n"
               "| X-2125000000000000010 | inventada | | |\n")
    root = library(tmp_path, [ficha()], {"grok/2026-11-28.md": ok_run, "muse/2026-11-28.md": bad_run})
    rep = vb.validate(root, since="2026-11-28")
    errors = "\n".join(rep.errors)
    assert "no existe" in errors
    assert "decisión 'inventada'" in errors
    assert [r["id"] for r in rep.to_review] == ["X-2121401671418863948"]


def test_cli_exit_code(tmp_path):
    root = library(tmp_path, [ficha(), ficha()])
    assert vb.main([str(root)]) == 1
