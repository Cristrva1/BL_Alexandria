#!/usr/bin/env python3
"""Verificación de integridad de las guías (guias/*.md).

Revisa:
  (a) Nº de fichas por archivo y total (esperado 156).
  (b) Anclas internas `(#-...)` que no tengan un `###` correspondiente.
  (c) Fichas a las que les falte algún campo obligatorio.
  (d) Filas de tabla con nº de columnas distinto a su cabecera.

Uso:  python tools_check/check_guias.py [directorio_guias]
"""
from __future__ import annotations
import re, sys, io, pathlib

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

GUIDE_DIR = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "guias")
EXPECTED_TOTAL = 156

REQUIRED_FIELDS = [
    "Qué es", "Por qué destaca", "Cómo funciona", "Instalación",
    "Casos", "Stack", "Elige si", "Combina con", "Repo",
]

# Ancla GitHub: minúsculas, sin emoji, espacios→'-', signos eliminados.
def slugify(title: str) -> str:
    t = re.sub(r"^###\s+", "", title).strip()
    t = re.sub(r"[^\w\s-]", "", t, flags=re.UNICODE)  # quita emojis/signos
    t = t.lower().strip()
    t = re.sub(r"\s", "-", t)  # cada espacio → un guion (sin colapsar, convención de la guía)
    return "#-" + t.lstrip("-")

def main() -> int:
    files = sorted(GUIDE_DIR.glob("*.md"))
    if not files:
        print(f"ERROR: no se encontraron .md en {GUIDE_DIR}")
        return 1

    # 1) Recoger todos los encabezados ### y generar anclas
    all_anchors: set[str] = set()
    for f in files:
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.startswith("### "):
                all_anchors.add(slugify(line))

    problems = 0
    total_fichas = 0

    for f in files:
        text = f.read_text(encoding="utf-8")
        lines = text.splitlines()

        # (a) Conteo de fichas
        fichas = sum(1 for l in lines if l.startswith("**Repo:**"))
        total_fichas += fichas

        # (b) Anclas rotas
        for m in re.finditer(r"\]\((#-[^)]+)\)", text):
            anchor = m.group(1)
            if anchor not in all_anchors:
                print(f"ANCLA ROTA en {f.name}: {anchor}")
                problems += 1

        # (c) Campos faltantes por ficha
        # Una ficha empieza en '### ' (no Escaneo/¿Cuál) y termina en la siguiente '### ' o '## '
        ficha_starts = [
            i for i, l in enumerate(lines)
            if l.startswith("### ")
            and "Escaneo rápido" not in l
            and "¿Cuál elegir" not in l
            and "Leyenda de badges" not in l
        ]
        for idx, start in enumerate(ficha_starts):
            end = ficha_starts[idx + 1] if idx + 1 < len(ficha_starts) else len(lines)
            block = "\n".join(lines[start:end])
            if "**Repo:**" not in block:
                continue  # no es ficha de repo
            missing = [fld for fld in REQUIRED_FIELDS if f"**{fld}**" not in block and f"**{fld}:**" not in block]
            if missing:
                title = lines[start].replace("### ", "").strip()
                print(f"CAMPO FALTANTE en {f.name} [{title}]: {', '.join(missing)}")
                problems += 1

        # (d) Filas de tabla con nº de columnas distinto a cabecera
        in_table = False
        header_cols = 0
        for l in lines:
            stripped = l.strip()
            if stripped.startswith("|") and stripped.endswith("|"):
                cells = [c for c in stripped.split("|")][1:-1]  # quita vacíos de bordes
                if not in_table:
                    header_cols = len(cells)
                    in_table = True
                elif re.match(r"^\|[\s|:-]+\|$", stripped):
                    continue  # separador
                else:
                    if len(cells) != header_cols and header_cols > 0:
                        print(f"FILA DESCUADRADA en {f.name}: {len(cells)} cols vs cabecera {header_cols} — {stripped[:80]}")
                        problems += 1
            else:
                in_table = False

    print(f"\nTOTAL fichas: {total_fichas} (esperado {EXPECTED_TOTAL})")
    print(f"PROBLEMAS: {problems}")
    return 0 if problems == 0 and total_fichas == EXPECTED_TOTAL else 1

if __name__ == "__main__":
    sys.exit(main())
