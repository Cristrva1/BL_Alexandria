"""Build INDICE_IA.json + INDICE_IA.detalle.json (schema 1.2) from agent outputs.

Usage: python merge.py [--write]
Without --write it only validates and prints a report.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

SP = Path('/home/claude/work')
ROOT = Path('/home/claude/bl_alexandria')
WRITE = '--write' in sys.argv

old_c = json.load(open(SP / 'plan/INDICE_IA.json', encoding='utf-8'))
old_d = json.load(open(SP / 'plan/INDICE_IA.detalle.json', encoding='utf-8'))
old_compact = {r['id']: r for r in old_c['repos']}
old_detail = old_d['repos']
cats = json.load(open(SP / 'plan/categories.json', encoding='utf-8'))
cat_by = {c['num']: c for c in cats}
recipes = json.load(open(SP / 'plan/recipes.json', encoding='utf-8'))
guia = json.load(open(SP / 'research/guia_fichas.json', encoding='utf-8'))
gmap = json.load(open(SP / 'research/guia_map.json', encoding='utf-8'))
gmap['ui'] = 'ui (shadcn)'
meta = {}
for f in ['existing_meta.json', 'new_meta.json']:
    for k, v in json.load(open(SP / 'research' / f, encoding='utf-8')).items():
        meta[k.lower()] = v
existing_gh = json.load(open(SP / 'plan/existing_gh.json', encoding='utf-8'))

targets = {}
for line in open(SP / 'plan/existing_target.tsv', encoding='utf-8'):
    if line.strip():
        rid, cat, sub = line.rstrip('\n').split('\t')
        targets[rid] = {'cat': int(cat), 'sub': sub, 'gh': existing_gh.get(rid), 'new': False}
for line in open(SP / 'plan/new_repos.tsv', encoding='utf-8'):
    if line.strip():
        rid, full, cat, sub = line.rstrip('\n').split('\t')
        targets[rid] = {'cat': int(cat), 'sub': sub, 'gh': full, 'new': True}

outs = {}
bad_json = []
for p in sorted((SP / 'out').glob('p*/*.json')):
    try:
        data = json.load(open(p, encoding='utf-8'))
    except Exception as exc:  # noqa: BLE001
        bad_json.append((str(p), str(exc)))
        continue
    rid = data.get('id') or p.stem
    outs[rid] = data

ROLES = {'platform', 'runtime', 'library', 'skill', 'directory', 'app'}
EXECS = {'local', 'cloud', 'hybrid'}
SETUPS = {'easy', 'medium', 'heavy'}
PROVS = {'openai', 'anthropic', 'google', 'local', 'mcp'}
SUB_EMOJI = {
    (1, 'motores'): '🔁', (1, 'n8n'): '🔁', (1, 'whatsapp'): '💬', (1, 'chatbots'): '🤖', (1, 'crm'): '👥', (1, 'marketing'): '📣', (1, 'internas'): '🧱',
    (2, 'catalogos'): '🗂️', (2, 'metodologia'): '🧭', (2, 'escritura'): '✍️', (2, 'dominio'): '📈', (2, 'prompts'): '💡', (2, 'guias'): '🎓',
    (3, 'coding'): '👨‍💻', (3, 'py'): '🐍', (3, 'ts'): '🟦', (3, 'visual'): '🧩', (3, 'asistentes'): '🦾', (3, 'research'): '🔎', (3, 'infra'): '🛠️', (3, 'experimentos'): '🧪',
    (4, 'crawlers'): '🕷️', (4, 'llm'): '🧠', (4, 'navegador'): '🌐', (4, 'busqueda'): '🔍', (4, 'social'): '📱',
    (5, 'sdk'): '🧰', (5, 'servidores'): '🔌', (5, 'directorios'): '📚',
    (6, 'memoria'): '🧠', (6, 'rag'): '📎', (6, 'vectores'): '🧮', (6, 'serving'): '🚀', (6, 'tokens'): '🗜️', (6, 'observabilidad'): '📡',
    (7, 'codigo'): '🧬', (7, 'calidad'): '🛡️', (7, 'entrenamiento'): '🏋️', (7, 'aprender'): '📘', (7, 'modelos'): '🧠', (7, 'herramientas'): '🧰', (7, 'datos'): '🗃️',
    (8, 'motores'): '🦙', (8, 'chats'): '💬', (8, 'workspaces'): '🏠', (8, 'notebooklm'): '📓',
    (9, 'componentes'): '🧱', (9, 'estilos'): '🎨', (9, 'animacion'): '✨', (9, 'diseno'): '✏️', (9, 'ia-ui'): '🪄', (9, 'skills'): '🎯',
    (10, 'producto'): '📈', (10, 'bi'): '📊', (10, 'graficos'): '📉', (10, 'apps'): '🧪', (10, 'recursos'): '📚',
    (11, 'interfaces'): '🖼️', (11, 'modelos'): '🌀', (11, 'edicion'): '🩹', (11, 'rostros'): '🙂', (11, 'vision'): '👁️', (11, 'suites'): '🎛️',
    (12, 'stt'): '🎙️', (12, 'tts'): '🗣️', (12, 'voz-agentes'): '📞', (12, 'edicion'): '✂️', (12, 'programatico'): '🎞️', (12, 'generativo'): '🎬', (12, 'musica'): '🎵',
    (13, 'conversion'): '🔄', (13, 'ocr'): '🔠', (13, 'pdf'): '📑', (13, 'slides'): '🖥️', (13, 'diagramas'): '🗺️',
    (0, 'hub'): '🧰',
}
LINK_RE = re.compile(r'\[([^\]]+)\]\((?:#|https?://|\.)[^)]*\)')
issues = defaultdict(list)


def slug(value):
    return re.sub(r'[^a-zA-Z0-9]+', '-', value.lower()).strip('-') or 'item'


def clean(text):
    text = (text or '').strip()
    text = LINK_RE.sub(r'\1', text)
    return re.sub(r'\s+', ' ', text)


def clause(text):
    text = clean(text).rstrip('.').strip()
    if text.lower().startswith('quieres '):
        pass
    return text


def sentence(text):
    text = clean(text)
    if text and text[-1] not in '.!?…':
        text += '.'
    return text


def guia_emoji(rid):
    key = gmap.get(rid)
    if not key:
        return ''
    title = guia[key]['title']
    m = re.match(r'^(\W+?)\s', title)
    return m.group(1).strip() if m else ''


def fallback_one(rid, od, oc, gh_meta):
    ed = guia.get(gmap.get(rid, ''), {}).get('fields', {}) if rid in gmap else {}
    text = ed.get('Qué es') or od.get('desc') or (gh_meta or {}).get('description') or oc.get('one') or ''
    first = re.split(r'(?<=[.!?])\s', clean(text))[0]
    return sentence(first[:1].upper() + first[1:])


ids = list(targets)
valid = set(ids)
compact_rows, detail_rows = {}, {}
for rid in ids:
    t = targets[rid]
    o = outs.get(rid)
    oc = old_compact.get(rid, {})
    od = old_detail.get(rid, {})
    gh_meta = meta.get((t['gh'] or '').lower())
    if o is None:
        issues['missing_output'].append(rid)
        o = {}
    name = clean(o.get('name')) or oc.get('name') or rid
    role = o.get('role') if o.get('role') in ROLES else oc.get('role', 'library')
    exec_ = o.get('exec') if o.get('exec') in EXECS else oc.get('exec', 'local')
    setup = o.get('setup') if o.get('setup') in SETUPS else oc.get('setup', 'medium')
    if o and o.get('role') not in ROLES:
        issues['bad_role'].append((rid, o.get('role')))
    prov = [p for p in (o.get('prov') or []) if p in PROVS]
    tags = []
    for tag in (o.get('tags') or oc.get('tags') or []):
        tag = str(tag).lower().strip()
        if tag and tag not in tags:
            tags.append(tag)
    tags = tags[:7]
    one = sentence(o.get('one')) if o.get('one') else fallback_one(rid, od, oc, gh_meta)
    if len(one) > 175:
        issues['long_one'].append((rid, len(one)))
    alts = []
    for a in (o.get('alternatives') or []):
        if a in valid and a != rid and a not in alts:
            alts.append(a)
        elif a not in valid:
            issues['bad_alt_id'].append((rid, a))
    combos = []
    for c in (o.get('combines_with') or od.get('combines_with') or []):
        if c in valid and c != rid and c not in combos and c not in alts:
            combos.append(c)
        elif c not in valid:
            issues['bad_combo_id'].append((rid, c))
    status = ''
    if gh_meta and gh_meta.get('archived'):
        status = 'archived'
    if rid in ('arcads-claude-code', 'wan2gp'):
        status = 'missing'
    if rid in ('tools', 'guia'):
        status = 'local'
    if rid == 'n8n-io':
        status = 'alias'
    lic = (gh_meta or {}).get('license')
    lic = {'NOASSERTION': 'Otra (ver repo)', None: ''}.get(lic, lic)
    pushed = ((gh_meta or {}).get('pushed_at') or '')[:10]
    full = (gh_meta or {}).get('full_name') or t['gh']
    repo_url = f'https://github.com/{full}' if full else (od.get('repo') or '')
    if rid in ('arcads-claude-code', 'wan2gp'):
        repo_url = (od.get('repo') or '').removesuffix('.git')
    emoji = guia_emoji(rid) or SUB_EMOJI.get((t['cat'], t['sub']), '')
    entry = {
        'id': rid, 'name': name, 'emoji': emoji, 'cat': t['cat'], 'sub': t['sub'],
        'role': role, 'exec': exec_, 'setup': setup, 'mcp': bool(o.get('mcp', oc.get('mcp', False))),
        'prov': prov, 'tags': tags,
        'stars': (gh_meta or {}).get('stars'), 'gh': full if gh_meta else None,
        'lib': not t['new'], 'pick': bool(o.get('pick')),
    }
    if status:
        entry['status'] = status
    if rid == 'n8n-io':
        entry['alias_of'] = 'n8n'
        entry['pick'] = False
    entry['one'] = one
    entry['alt'] = alts
    entry['doc'] = f'human/fichas/{slug(rid)}.md'
    compact_rows[rid] = entry

    cases = [clean(c).rstrip('.') for c in (o.get('cases') or []) if clean(c)][:4]
    det = {
        'name': name, 'cat': t['cat'], 'sub': t['sub'],
        'desc': clean(o.get('desc')) or clean(od.get('desc')),
        'why': clean(o.get('why')),
        'how': clean(o.get('how')),
        'install': clean(o.get('install')),
        'cases': cases,
        'stack': clean(o.get('stack')) or clean(od.get('stack')),
        'models': clean(o.get('models')),
        'choose_if': clause(o.get('choose_if')) or clause(od.get('choose_if')),
        'avoid_if': clause(o.get('avoid_if')) or clause(od.get('avoid_if')),
        'limits': clean(o.get('limits')),
        'combines_with': combos,
        'alternatives': alts,
        'repo': repo_url,
        'homepage': (gh_meta or {}).get('homepage') or '',
        'license': lic or '',
        'lang': (gh_meta or {}).get('language') or '',
        'updated': pushed,
        'doc': entry['doc'],
    }
    for k in ('desc', 'install', 'choose_if', 'avoid_if'):
        if not det[k]:
            issues[f'empty_{k}'].append(rid)
    if o.get('notes'):
        issues['notes'].append((rid, o['notes']))
    detail_rows[rid] = det

# symmetric alternatives (cap 5)
for rid, entry in compact_rows.items():
    for a in list(entry['alt']):
        other = compact_rows[a]
        if rid not in other['alt'] and len(other['alt']) < 5 and not other.get('alias_of') and not entry.get('alias_of'):
            other['alt'].append(rid)
            if rid in detail_rows[a]['combines_with']:
                detail_rows[a]['combines_with'].remove(rid)
for rid in compact_rows:
    detail_rows[rid]['alternatives'] = compact_rows[rid]['alt']

# picks: at least one, at most two per (cat, sub)
groups = defaultdict(list)
for rid, entry in compact_rows.items():
    if entry['cat'] > 0 and not entry.get('alias_of'):
        groups[(entry['cat'], entry['sub'])].append(entry)
for key, members in groups.items():
    ok = [m for m in members if m.get('status') not in ('archived', 'missing')]
    picks = [m for m in ok if m['pick']]
    for m in members:
        if m.get('status') in ('archived', 'missing'):
            m['pick'] = False
    if not picks and ok:
        best = max(ok, key=lambda m: m['stars'] or 0)
        best['pick'] = True
        issues['auto_pick'].append(f"{key}: {best['id']}")
    elif len(picks) > 2:
        keep = sorted(picks, key=lambda m: -(m['stars'] or 0))[:2]
        for m in picks:
            if m not in keep:
                m['pick'] = False
        issues['trimmed_picks'].append(f"{key}: kept {[m['id'] for m in keep]}")

# order: cat, sub order, pick, stars
sub_order = {(c['num'], s['key']): i for c in cats for i, s in enumerate(c['subs'])}
ordered = sorted(compact_rows.values(), key=lambda e: (e['cat'] if e['cat'] > 0 else 99, sub_order.get((e['cat'], e['sub']), 99), 0 if e['pick'] else 1, -(e['stars'] or 0), e['name'].lower()))

counts = Counter(e['cat'] for e in ordered if not e.get('alias_of'))
categories = []
for c in cats:
    categories.append({
        'num': c['num'], 'emoji': c['emoji'], 'title': c['title'], 'desc': c['desc'],
        'file': f"human/categorias/{c['num']:02d}-{slug(c['title'])}.md" if c['num'] > 0 else '',
        'count': counts.get(c['num'], 0), 'subs': c['subs'],
    })

recipes_out = []
for rc in recipes:
    for step in rc['steps']:
        if step['id'] not in valid:
            issues['bad_recipe_id'].append((rc['id'], step['id']))
    recipes_out.append({'id': rc['id'], 'emoji': rc['emoji'], 'title': rc['title'], 'goal': rc['goal'],
                        'repos': [s['id'] for s in rc['steps']], 'steps': rc['steps'], 'flow': rc['flow'],
                        'how': rc['how'], 'when_not': rc['when_not']})

total = sum(1 for e in ordered if not e.get('alias_of'))
public = sum(1 for e in ordered if not e.get('alias_of') and e['cat'] > 0)
model_guidance = {
    'key_distinction': 'Separa el AGENTE/IDE con el que CONSTRUYES (Claude Code, Codex, Antigravity, Gemini CLI, OpenCode) del LLM que tu APP llama EN EJECUCIÓN (campo prov). La mayoría de repos runtime son agnósticos al agente de código.',
    'rule_of_thumb': "Filtra por herramienta solo en repos role=skill/directory; el resto se elige por función.",
    'tools': {
        'claude-code': {'label': 'Claude Code', 'best_fit_repos': ['claude-code', 'anthropic-skills', 'claude-plugins-official', 'superpowers', 'awesome-claude-code', 'awesome-claude-skills', 'claude-mem', 'n8n-skills', 'geo-seo-claude', 'agency-agents'], 'note': 'Skills en .claude/skills y plugins con /plugin marketplace.'},
        'codex': {'label': 'Codex', 'best_fit_repos': ['codex', 'agent-skills', 'antigravity-awesome-skills', 'awesome-agent-skills', 'spec-kit', 'marketingskills', 'taste-skill'], 'note': 'Lee AGENTS.md y skills portables (formato Agent Skills).'},
        'antigravity': {'label': 'Antigravity', 'best_fit_repos': ['antigravity-awesome-skills', 'awesome-agent-skills', 'prompt-master', 'stitch-skills'], 'note': ''},
        'gemini-cli': {'label': 'Gemini CLI', 'best_fit_repos': ['gemini-cli', 'awesome-agent-skills', 'antigravity-awesome-skills', 'stitch-skills'], 'note': ''},
        'opencode': {'label': 'OpenCode', 'best_fit_repos': ['opencode', 'awesome-agent-skills', 'antigravity-awesome-skills', 'prompt-master'], 'note': ''},
        'grok': {'label': 'Grok', 'best_fit_repos': [], 'note': 'Sin repos específicos: úsalo como proveedor LLM en runtime (los repos agnósticos lo aceptan vía API compatible con OpenAI).'},
        'deepseek': {'label': 'DeepSeek', 'best_fit_repos': ['deepseek-coder'], 'note': 'Es el modelo; el resto es agnóstico vía proveedor compatible con OpenAI.'},
    },
}
for tool in model_guidance['tools'].values():
    for rid in tool['best_fit_repos']:
        if rid not in valid:
            issues['bad_tool_repo'].append(rid)

start_here = [
    {'want': 'Un bot de WhatsApp que atienda, venda y pase a humano', 'recipe': 'bot-de-whatsapp-con-ia', 'repos': ['evolution-api', 'n8n', 'chatwoot']},
    {'want': 'Un ChatGPT privado con modelos en mi máquina', 'recipe': 'chatgpt-privado-local', 'repos': ['ollama', 'open-webui', 'jan']},
    {'want': 'Preguntarle a mis documentos (RAG)', 'recipe': 'rag-sobre-documentos', 'repos': ['docling', 'llama-index', 'qdrant']},
    {'want': 'Programar más rápido con un agente de código', 'recipe': 'agente-de-codigo-potenciado', 'repos': ['claude-code', 'codex', 'opencode', 'superpowers']},
    {'want': 'Un agente que investigue en la web y cite fuentes', 'recipe': 'agente-de-research-profundo', 'repos': ['gpt-researcher', 'firecrawl', 'searxng']},
    {'want': 'Automatizar procesos entre mis apps', 'cat': 1, 'sub': 'motores', 'repos': ['n8n', 'activepieces', 'windmill']},
    {'want': 'Crear o conectar herramientas por MCP', 'recipe': 'construir-una-appservidor-mcp', 'repos': ['fastmcp', 'playwright-mcp', 'github-mcp-server']},
    {'want': 'Un agente de voz para web o teléfono', 'recipe': 'agente-de-voz', 'repos': ['pipecat', 'livekit-agents', 'kokoro']},
    {'want': 'Videos cortos con voz y subtítulos', 'recipe': 'pipeline-de-reels-video-corto', 'repos': ['whisperx', 'remotion', 'moneyprinterturbo']},
    {'want': 'Generar o editar imágenes con IA', 'cat': 11, 'repos': ['comfyui', 'flux', 'rembg']},
    {'want': 'Una web app moderna con IA integrada', 'recipe': 'web-app-moderna-con-ia', 'repos': ['ui', 'tailwindcss', 'vercel-ai']},
    {'want': 'Dashboards y analítica de producto', 'recipe': 'analitica-con-ia', 'repos': ['posthog', 'superset', 'metabase']},
    {'want': 'Convertir PDFs y documentos para IA', 'cat': 13, 'sub': 'conversion', 'repos': ['markitdown', 'docling', 'mineru']},
    {'want': 'Entrenar o afinar un modelo', 'cat': 7, 'sub': 'entrenamiento', 'repos': ['unsloth', 'llama-factory', 'transformers']},
]
for item in start_here:
    for rid in item['repos']:
        if rid not in valid:
            issues['bad_start_repo'].append(rid)

compact_out = {
    '$schema_version': '1.2',
    'meta': {
        'title': f'Índice IA — {public} repos curados de IA y Automatización',
        'purpose': 'Que una persona o un agente elija repos útiles con bajo gasto de tokens. Empieza por AGENTS.md.',
        'how_to_use': [
            '1. Lee solo este JSON. Filtra por cat/sub/tags/role/exec/setup/prov y la frase one.',
            "2. 'pick': true marca el imprescindible de cada subcategoría; 'stars' indica popularidad en GitHub.",
            "3. Desempata con 'alt' (sustitutos: elige uno y descarta los demás).",
            "4. Para productos end-to-end parte de 'recipes'.",
            "5. Considera la herramienta del usuario con 'model_guidance'.",
            "6. Solo para finalistas: abre INDICE_IA.detalle.json por id (instalación, elige/evita, combina) o la ficha 'doc'.",
        ],
        'tiers': {'scan': 'INDICE_IA.json (este)', 'detail': 'INDICE_IA.detalle.json', 'human': 'human/categorias/NN-*.md y human/fichas/<id>.md'},
        'fields': {
            'cat/sub': 'categoría (número) y subcategoría (clave de categories[].subs)',
            'role': 'platform/runtime/library/skill/directory/app',
            'exec': 'local/cloud/hybrid', 'setup': 'easy/medium/heavy', 'mcp': 'expone/consume MCP',
            'prov': 'openai/anthropic/google/local/mcp; []=no usa LLM o no aplica',
            'stars': 'estrellas de GitHub en meta.stars_checked', 'gh': 'owner/repo en GitHub',
            'lib': 'true si ya está clonado en tu biblioteca local (../Repositorios_Prueba)',
            'pick': 'imprescindible de su subcategoría', 'status': 'archived/missing/local/alias (solo si aplica)',
            'alt': 'sustitutos (elige uno)', 'one': 'qué es, en una frase',
        },
        'stars_checked': '2026-11-05',
        'repo_url': 'https://github.com/Cristrva1/BL_Alexandria',
        'start_here': start_here,
    },
    'legend': old_c.get('legend', {}),
    'model_guidance': model_guidance,
    'categories': categories,
    'recipes': recipes_out,
    'detail_file': 'INDICE_IA.detalle.json',
    'repos': ordered,
}
detail_out = {
    '$schema_version': '1.2',
    'note': 'Detalle por id. Compañero de INDICE_IA.json. Campos: desc, why, how, install, cases, stack, models, choose_if, avoid_if, limits, combines_with, alternatives, repo, homepage, license, lang, updated, doc.',
    'repos': {e['id']: detail_rows[e['id']] for e in ordered},
}

print('outputs:', len(outs), 'targets:', len(targets), 'bad json:', bad_json)
for k, v in issues.items():
    if k == 'notes':
        continue
    print(f'{k}: {len(v)}', v[:12])
print('notes:', len(issues['notes']))
print('counts:', sorted(counts.items()))
print('picks:', sum(1 for e in ordered if e['pick']), 'archived:', sum(1 for e in ordered if e.get('status') == 'archived'))
if WRITE:
    (ROOT / 'INDICE_IA.json').write_text(json.dumps(compact_out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (ROOT / 'INDICE_IA.detalle.json').write_text(json.dumps(detail_out, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (SP / 'notes.json').write_text(json.dumps(issues['notes'], ensure_ascii=False, indent=1), encoding='utf-8')
    print('WROTE indices')
