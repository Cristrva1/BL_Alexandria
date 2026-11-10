"""Expand compact hand-written batches (batches/*.py, list FICHAS) into out/manual/<id>.json."""
import json, runpy, sys
from pathlib import Path
W = Path('/home/claude/work')
K = {'r': 'role', 'e': 'exec', 's': 'setup', 'm': 'mcp', 'p': 'prov', 't': 'tags', 'n': 'name', 'o': 'one', 'd': 'desc',
     'w': 'why', 'h': 'how', 'i': 'install', 'c': 'cases', 'st': 'stack', 'md': 'models', 'ch': 'choose_if',
     'av': 'avoid_if', 'l': 'limits', 'cw': 'combines_with', 'al': 'alternatives', 'pk': 'pick', 'nt': 'notes'}
n = 0
for f in sorted((W / 'batches').glob('*.py')) if len(sys.argv) < 2 else [Path(a) for a in sys.argv[1:]]:
    for x in runpy.run_path(str(f))['FICHAS']:
        out = {'id': x['id']}
        for k, v in x.items():
            if k != 'id':
                out[K.get(k, k)] = v
        out.setdefault('mcp', False); out.setdefault('prov', []); out.setdefault('pick', False)
        out.setdefault('limits', ''); out.setdefault('alternatives', [])
        if isinstance(out.get('cases'), str):
            out['cases'] = [c.strip() for c in out['cases'].split('|')]
        json.dump(out, open(W / 'out/manual' / f"{x['id']}.json", 'w'), ensure_ascii=False, indent=1); n += 1
print('manual', n)
