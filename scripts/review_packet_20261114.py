"""Print compact primary-source packets for individual editorial decisions."""
import argparse
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
SOURCES=ROOT/'data/reviews/679-20261114/sources'


def blocks(text):
    result=[]
    for match in re.finditer(r'```([^\n]*)\n(.*?)```',text,re.S):
        result.append(dict(number=len(result),line=text[:match.start()].count('\n')+1,language=match[1].strip(),code=match[2].strip()))
    return result


def main():
    sys.stdout.reconfigure(encoding='utf8')
    p=argparse.ArgumentParser();p.add_argument('--cat',type=int);p.add_argument('--offset',type=int,default=0);p.add_argument('--limit',type=int,default=8);p.add_argument('--id');p.add_argument('--block',type=int)
    args=p.parse_args()
    c=json.loads((ROOT/'INDICE_IA.json').read_text(encoding='utf8'));d=json.loads((ROOT/'INDICE_IA.detalle.json').read_text(encoding='utf8'))
    repos=[r for r in c['repos'] if r['cat']>0 and not r.get('alias_of') and (not args.cat or r['cat']==args.cat) and (not args.id or r['id']==args.id)]
    if not args.id:repos=repos[args.offset:args.offset+args.limit]
    for repo in repos:
        rid=repo['id'];card=d['repos'][rid];source=json.loads((SOURCES/rid/'source.json').read_text(encoding='utf8'))
        print('\n###',rid,repo['cat'],repo['sub'],repo['role'],'SOURCE',source['status'])
        if source['status']!='available':print(source);continue
        text=(SOURCES/rid/'readme.md').read_text(encoding='utf8',errors='replace');lines=text.splitlines();code=blocks(text)
        if args.block is not None:
            print(json.dumps(code[args.block],ensure_ascii=False,indent=2));continue
        print('PURPOSE',source.get('metadata',{}).get('description') or repo['one'])
        print('CURRENT',repo['one'])
        a=card['access'];print('ACCESS',','.join(k+'='+str(a.get(k)) for k in ['api','cost','claude_code','codex','local_model']))
        clean=[(i+1,re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',line)).strip()) for i,line in enumerate(lines)]
        intro=[(i,line) for i,line in clean if len(line)>65 and len(line)<600 and not line.startswith(('|','[!','![')) and 'img.shields' not in line and not re.match(r'^https?://',line)]
        for line in intro[:1]:print('INTRO',line[0],line[1][:310])
        selected=[]
        for block in code:
            if re.search(r'pip install|uv (?:add|pip|sync|tool)|uvx |pipx |npm (?:install|i |create)|npx |pnpm |yarn |docker (?:run|compose)|git clone|brew install|winget|/plugin|codex |claude ',block['code'],re.I):selected.append(block)
        if not selected:selected=code[:1]
        for block in selected[:2]:print('BLOCK',block['number'],'L'+str(block['line']),block['language'],block['code'][:450].replace('\n',' ⏎ '),(' [LONG]' if len(block['code'])>450 else ''))
        groups={"CLIENT":r'codex|antigravity|claude code',"MCP":r'MCP server|MCP-compatible|stdio|streamable.http',"LOCAL":r'ollama|llama.cpp|lm studio|local models?|local llm|offline',"COST":r'API[_ -]?KEY|subscription|pricing|billing|paid|credits|license',"NEEDS":r'prerequisit|requirements|requires '}
        for label,pattern in groups.items():
            evidence=[(i,line) for i,line in clean if re.search(pattern,line,re.I) and len(line)>20 and not line.startswith('![')]
            for line in evidence[:(3 if label=='CLIENT' else 2)]:print(label,line[0],line[1][:225])
        links=re.findall(r'\[([^\]]+)\]\(([^)]+)\)',text)
        relevant=[(label,url) for label,url in links if re.search(r'install|setup|quick.?start|getting.started|documentation|pricing',label,re.I) and not url.startswith('#')]
        print('DOCS',relevant[:4])
        print('BLOCKS',len(code),'LINES',len(lines),'SHA',source['blob_sha'])


if __name__=='__main__':main()
