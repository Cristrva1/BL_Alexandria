import json,glob,os,sys
W='/home/claude/work'
have={os.path.basename(p)[:-5] for p in glob.glob(W+'/out/*/*.json')}
pk=sys.argv[1]
d=json.load(open(f'{W}/plan/{pk}.json'))
od=json.load(open(W+'/plan/INDICE_IA.detalle.json'))['repos']
for r in d['repos']:
    if r['id'] in have: continue
    g=r.get('github') or {}
    e=od.get(r['id'],{})
    print(f"{r['id']}|{r['target_cat']}.{r['target_sub']}|{r.get('gh')}|{g.get('stars')}|{g.get('language')}|{g.get('license')}|arch={g.get('archived')}|{(g.get('description') or '')[:150]}" + (f"|OLD:{e.get('desc','')[:150]}" if e else ''))
