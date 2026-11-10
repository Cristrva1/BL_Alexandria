cat > /home/claude/work/parse_guia.py <<'EOF'
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
EOF
python3 /home/claude/work/parse_guia.py Guia.md /home/claude/work/research/guia_fichas.json
python3 - <<'EOF'
import json, re
sp = '/home/claude/work/'
f = json.load(open(sp+'research/guia_fichas.json'))
c = json.load(open('INDICE_IA.json'))['repos']
def norm(s): return re.sub(r'[^a-z0-9]', '', s.lower())
by = {norm(k): k for k in f}
matched, unmatched, catdiff = {}, [], []
for r in c:
    cands = [norm(r['id']), norm(r['name'])]
    k = next((by[x] for x in cands if x in by), None)
    if k:
        matched[r['id']] = k
        if f[k]['cat'] != r['cat']:
            catdiff.append((r['id'], r['cat'], f[k]['cat']))
    else:
        unmatched.append((r['id'], r['cat']))
print('matched', len(matched), 'unmatched', len(unmatched))
print('UNMATCHED:', unmatched)
print('CAT DIFF (id, compact, guia):', len(catdiff))
for x in catdiff: print('  ', x)
fields = {}
for k, v in f.items():
    for fk in v['fields']: fields[fk] = fields.get(fk, 0) + 1
print(fields)
used = set(matched.values())
print('guia fichas not in compact:', [k for k in f if k not in used])
json.dump(matched, open(sp+'research/guia_map.json','w'), indent=0)
EOF