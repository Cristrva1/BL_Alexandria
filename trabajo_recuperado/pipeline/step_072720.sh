cd /home/claude/work && cat > plan/renamed.json <<'EOF'
[["graphify","Graphify-Labs/graphify"],["supertonic","supertone-oss-archive/supertonic"],["antigravity-awesome-skills","sickn33/agentic-awesome-skills"],["notebooklm-mcp-cli","jacob-bd/gemini-notebook-mcp-cli"],["omnivoice-studio","debpalash/VoiceStudio"],["nemo","NVIDIA-NeMo/Speech"],["odysseus","odysseus-dev/odysseus"]]
EOF
timeout 300 python3 fetch_stars.py plan/renamed.json research/existing_meta.json 2>&1 | tail -2
python3 - <<'EOF'
import json
sp='/home/claude/work/'
pairs = dict(tuple(p) for p in json.load(open(sp+'existing_repos.json')))
for rid, full in json.load(open(sp+'plan/renamed.json')):
    pairs[rid] = full
meta = {k.lower(): v for k, v in json.load(open(sp+'research/existing_meta.json')).items()}
gh = {}
missing = []
for rid, full in pairs.items():
    m = meta.get(full.lower())
    if m:
        gh[rid] = m['full_name']
    else:
        missing.append((rid, full))
print('resolved', len(gh), 'missing', missing)
json.dump(gh, open(sp+'plan/existing_gh.json','w'), indent=0)
for rid in ['graphify','supertonic','antigravity-awesome-skills','notebooklm-mcp-cli','omnivoice-studio','nemo','odysseus']:
    m = meta[gh[rid].lower()]
    print(rid, m['full_name'], m['stars'], m['archived'], (m['description'] or '')[:90])
EOF