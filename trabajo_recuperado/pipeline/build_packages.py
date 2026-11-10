import json, re
from pathlib import Path
SP = Path('/home/claude/work')
ROOT = Path('/home/claude/bl_alexandria')
compact = {r['id']: r for r in json.load(open(ROOT/'INDICE_IA.json'))['repos']}
detail = json.load(open(ROOT/'INDICE_IA.detalle.json'))['repos']
cats = {c['num']: c for c in json.load(open(SP/'plan/categories.json'))}
gmap = json.load(open(SP/'research/guia_map.json'))
gmap['ui'] = 'ui (shadcn)'
guia = json.load(open(SP/'research/guia_fichas.json'))
meta = {}
for f in ['existing_meta.json', 'new_meta.json']:
    for k, v in json.load(open(SP/'research'/f)).items():
        meta[k.lower()] = v
existing_gh = json.load(open(SP/'plan/existing_gh.json'))
existing = [l.rstrip('\n').split('\t') for l in open(SP/'plan/existing_target.tsv') if l.strip()]
new = [l.rstrip('\n').split('\t') for l in open(SP/'plan/new_repos.tsv') if l.strip()]
old_urls = {rid: (d.get('repo') or '') for rid, d in detail.items()}

def gh_block(full):
    m = meta.get((full or '').lower())
    if not m: return None
    return {k: m.get(k) for k in ['full_name','stars','description','topics','license','language','pushed_at','archived','homepage']}

entries = {}
for rid, cat, sub in existing:
    full = existing_gh.get(rid)
    c = compact[rid]; d = detail.get(rid, {})
    e = {'id': rid, 'is_new': False, 'target_cat': int(cat), 'target_sub': sub, 'gh': full,
         'github': gh_block(full),
         'current': {k: c.get(k) for k in ['name','role','exec','setup','mcp','prov','tags','one','alt']} | {k: d.get(k) for k in ['desc','stack','choose_if','avoid_if','combines_with','alternatives']},
         'old_repo_url': old_urls.get(rid)}
    if rid in gmap:
        e['editorial'] = guia[gmap[rid]]['fields']
    if rid in ('arcads-claude-code', 'wan2gp'):
        e['status'] = 'missing'
    if rid in ('tools', 'guia'):
        e['status'] = 'local'
    if rid == 'n8n-io':
        e['alias_of'] = 'n8n'
    entries[rid] = e
for rid, full, cat, sub in new:
    entries[rid] = {'id': rid, 'is_new': True, 'target_cat': int(cat), 'target_sub': sub, 'gh': full, 'github': gh_block(full)}

# global id list
all_ids = []
for rid, e in entries.items():
    g = e.get('github') or {}
    all_ids.append({'id': rid, 'name': (e.get('current') or {}).get('name') or (g.get('full_name') or rid).split('/')[-1],
                    'cat': e['target_cat'], 'sub': e['target_sub'], 'gh': e.get('gh'),
                    'what': (g.get('description') or (e.get('current') or {}).get('one') or '')[:140]})
all_ids.sort(key=lambda x: (x['cat'], x['sub'], x['id']))
(SP/'plan/ALL_IDS.json').write_text(json.dumps(all_ids, ensure_ascii=False, indent=0), encoding='utf-8')

packages = {
 'p01': {'cats': [1]},
 'p02': {'cats': [2]},
 'p03': {'cats': [3], 'subs': ['coding','py','ts']},
 'p04': {'cats': [3, 5], 'subs3': ['visual','asistentes','research','infra','experimentos']},
 'p05': {'cats': [4, 8, 0]},
 'p06': {'cats': [6, 10]},
 'p07': {'cats': [7, 13]},
 'p08': {'cats': [9, 11]},
 'p09': {'cats': [12]},
}
summary = {}
for pid, spec in packages.items():
    sel = []
    for rid, e in entries.items():
        if e['target_cat'] not in spec['cats']: continue
        if pid == 'p03' and e['target_sub'] not in spec['subs']: continue
        if pid == 'p04' and e['target_cat'] == 3 and e['target_sub'] not in spec['subs3']: continue
        sel.append(e)
    sel.sort(key=lambda e: (spec['cats'].index(e['target_cat']), e['target_sub'], e['id']))
    pcats = [cats[n] for n in spec['cats']]
    pkg = {'package': pid, 'out_dir': str(SP/'out'/pid), 'categories': pcats, 'repos': sel}
    (SP/'plan'/f'{pid}.json').write_text(json.dumps(pkg, ensure_ascii=False, indent=1), encoding='utf-8')
    (SP/'out'/pid).mkdir(parents=True, exist_ok=True)
    summary[pid] = (len(sel), sum(1 for e in sel if e['is_new']), sum(1 for e in sel if 'editorial' in e))
print(summary, sum(v[0] for v in summary.values()))
