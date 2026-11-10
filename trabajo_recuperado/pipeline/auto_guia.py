"""Build fichas for existing repos from the hand-written prose in Guia.md (guia_fichas.json)."""
import json, re
from pathlib import Path
W = Path('/home/claude/work')
g = json.load(open(W/'research/guia_fichas.json')); gm = json.load(open(W/'research/guia_map.json'))
gm['ui'] = 'ui (shadcn)'
oc = {r['id']: r for r in json.load(open(W/'plan/INDICE_IA.json'))['repos']}
od = json.load(open(W/'plan/INDICE_IA.detalle.json'))['repos']
ids = {l.split('\t')[0] for l in open(W/'plan/existing_target.tsv') if l.strip()} | {l.split('\t')[0] for l in open(W/'plan/new_repos.tsv') if l.strip()}
done = {p.stem for p in W.glob('out/p*/*.json')} | {p.stem for p in W.glob('out/manual/*.json')}
VOC = set('whatsapp automation agents coding-agent mcp scraping browser research search llmops memory rag vector-db inference local ui design dataviz analytics image vision audio tts stt video docs ocr pdf slides code training data notebooks email notifications crm chatbot skills prompts learning security evaluation observability python typescript javascript go rust java ruby php cpp docker postgres react'.split())
LINK = re.compile(r'\[([^\]]+)\]\(#-([^)]+)\)')
def cap(s): s = s.strip(); return s[:1].upper() + s[1:]
def sent(s):
    s = cap(re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', s)).strip()
    return s if not s or s[-1] in '.!?' else s + '.'
n = 0
for rid, key in gm.items():
    if rid not in ids or rid in done: continue
    f = g[key]['fields']; c = oc.get(rid, {}); d = od.get(rid, {})
    que = sent(f.get('Qué es', ''))
    parts = re.split(r'(?<=[.!?])\s+', que)
    one, rest = parts[0], ' '.join(parts[1:])
    et = f.get('Etiquetas', '')
    stack, models = (f.get('Stack', '') + ' — **Modelo/API:** ').split(' — **Modelo/API:** ')[:2]
    elige = f.get('Elige si', '').split(' — **Evita si:** ')
    combos = [m.group(2) for m in LINK.finditer(f.get('Combina con', '')) if m.group(2) in ids]
    tags = [t for t in c.get('tags', []) if t in VOC][:6]
    out = {
        'id': rid, 'name': c.get('name', rid), 'role': c.get('role'), 'exec': c.get('exec'), 'setup': c.get('setup'),
        'mcp': ('🔌' in et) or c.get('mcp', False), 'prov': c.get('prov', []), 'tags': tags,
        'one': one, 'desc': rest or (que + ' ' + re.split(r'(?<=[.!?])\s+', sent(f.get('Por qué destaca', '')))[0]).strip(),
        'why': sent(f.get('Por qué destaca', '')), 'how': sent(f.get('Cómo funciona', '')),
        'install': sent(f.get('Instalación', '')),
        'cases': [cap(x).rstrip('.') for x in f.get('Casos', '').split(' · ') if x.strip()][:3],
        'stack': stack.strip().rstrip('.'), 'models': sent(models.strip()) if models.strip() else '',
        'choose_if': elige[0].strip().rstrip('.') or d.get('choose_if', ''),
        'avoid_if': (elige[1].strip().rstrip('.') if len(elige) > 1 else d.get('avoid_if', '')),
        'limits': sent(f.get('Limitaciones', '')),
        'combines_with': combos or d.get('combines_with', []), 'alternatives': c.get('alt', []), 'pick': False,
    }
    json.dump(out, open(W/f'out/auto/{rid}.json', 'w'), ensure_ascii=False, indent=1); n += 1
print('auto', n)
