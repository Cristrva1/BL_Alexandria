python3 -c "
import json, re
d = json.load(open('INDICE_IA.detalle.json'))['repos']
missing = []
out = []
for rid, r in d.items():
    url = (r.get('repo') or '').strip()
    m = re.search(r'github\.com[/:]([^/\s]+)/([^/\s#?]+)', url)
    if m:
        owner, name = m.group(1), m.group(2)
        name = re.sub(r'\.git$', '', name)
        out.append((rid, f'{owner}/{name}'))
    else:
        missing.append((rid, url))
print(len(out), 'with github url')
print('missing:', missing)
json.dump(out, open('/home/claude/work/existing_repos.json','w'), indent=0)
" ; mkdir -p /home/claude/work