"""Parse editorial fichas from Guia.md into structured fields."""
import json, re, sys
from pathlib import Path

text = Path(sys.argv[1]).read_text(encoding="utf-8")
out_path = sys.argv[2]
# cut auto appendix
text = text.split("<!-- BL_ALEXANDRIA_AUTO_APPEND_START -->")[0]
cat = 0
fichas = {}
cur = None
FIELD_RE = re.compile(r"^\*\*(Etiquetas|Qué es|Por qué destaca|Cómo funciona|Instalación|Casos|Stack|Elige si|Limitaciones|Combina con|Repo):\*\*\s*(.*)$")
for line in text.splitlines():
    m = re.match(r"^## (\d+)\. ", line)
    if m:
        cat = int(m.group(1)); cur = None; continue
    if line.startswith("## "):
        cur = None; continue
    if line.startswith("### "):
        title = line[4:].strip()
        if any(s in title for s in ("Escaneo rápido", "¿Cuál elegir", "Leyenda", "Recetas")) or re.match(r"^[^\w]*\d+\. ", title):
            cur = None; continue
        name = re.sub(r"^[^\w]+", "", title).strip()
        cur = {"title": title, "name": name, "cat": cat, "fields": {}}
        fichas[name] = cur
        continue
    if cur is None:
        continue
    m = FIELD_RE.match(line.strip())
    if m:
        cur["fields"][m.group(1)] = m.group(2).strip()
json.dump(fichas, open(out_path, "w"), ensure_ascii=False, indent=1)
print(len(fichas), "fichas")
