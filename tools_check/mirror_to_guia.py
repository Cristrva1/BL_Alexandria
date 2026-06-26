#!/usr/bin/env python3
"""Reconstruye Guia.md a partir de los 5 guias/*.md enriquecidos.

Guia.md = [header único hasta antes de '### Leyenda de badges']
        + [cuerpo compartido = guia1(from '### Leyenda').rstrip() + '\\n\\n' + guia2-5.strip()]
        + [auto-appendix desde '<!-- BL_ALEXANDRIA_AUTO_APPEND_START -->' hasta el final]

Uso: python tools_check/mirror_to_guia.py [--check]
  --check: solo verifica que el cuerpo compartido coincide, no escribe.
"""
from __future__ import annotations
import sys, io, pathlib

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
GUIDE_DIR = ROOT / "guias"
GUIA_MD = ROOT / "Guia.md"

MARKER = "### Leyenda de badges"
APPEND_START = "<!-- BL_ALEXANDRIA_AUTO_APPEND_START -->"
APPEND_END = "<!-- BL_ALEXANDRIA_AUTO_APPEND_END -->"


def main() -> int:
    check_only = "--check" in sys.argv

    g1 = (GUIDE_DIR / "guia1.md").read_text(encoding="utf-8")
    g2 = (GUIDE_DIR / "guia2.md").read_text(encoding="utf-8")
    g3 = (GUIDE_DIR / "guia3.md").read_text(encoding="utf-8")
    g4 = (GUIDE_DIR / "guia4.md").read_text(encoding="utf-8")
    g5 = (GUIDE_DIR / "guia5.md").read_text(encoding="utf-8")
    G = GUIA_MD.read_text(encoding="utf-8")

    # Header único de Guia.md (antes del cuerpo compartido)
    idx_marker_G = G.index(MARKER)
    header = G[:idx_marker_G]

    # Auto-appendix de Guia.md (desde APPEND_START hasta el final)
    if APPEND_START in G:
        idx_append_G = G.index(APPEND_START)
        appendix = G[idx_append_G:]
    else:
        appendix = ""

    # Cuerpo compartido reconstruido desde los guias enriquecidos
    g1_body = g1[g1.index(MARKER):]
    body = (
        g1_body.rstrip() + "\n\n"
        + g2.strip() + "\n\n"
        + g3.strip() + "\n\n"
        + g4.strip() + "\n\n"
        + g5.rstrip()
    )

    # Nuevo Guia.md
    new_G = header + body
    if appendix:
        new_G = new_G + "\n\n" + appendix

    if check_only:
        # Comparar cuerpo compartido actual vs reconstruido
        idx_append_curr = G.index(APPEND_START) if APPEND_START in G else len(G)
        current_body = G[idx_marker_G:idx_append_curr].rstrip()
        if current_body == body:
            print("OK: cuerpo compartido de Guia.md ya coincide con guias/*.md")
            return 0
        else:
            print(f"DIFERENCIA: cuerpo actual {len(current_body)} vs reconstruido {len(body)}")
            # find first divergence
            for i in range(min(len(current_body), len(body))):
                if current_body[i] != body[i]:
                    s = max(0, i - 50)
                    print(f"  firstDiv @ {i}")
                    print(f"  current: {current_body[s:i+50]!r}")
                    print(f"  new:     {body[s:i+50]!r}")
                    break
            return 1

    # Escribir
    GUIA_MD.write_text(new_G, encoding="utf-8")
    print(f"Guia.md reconstruido: {len(new_G)} bytes (era {len(G)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
