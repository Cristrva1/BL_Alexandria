"""Compile individual editorial decisions; never label an inferred row reviewed."""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from copy import deepcopy
import json
from pathlib import Path
import re
import sys

from review_packet_20261114 import blocks

ROOT = Path(__file__).resolve().parents[1]
CURATION = ROOT / 'curation/review-679-2026-11-14'
SOURCES = ROOT / 'data/reviews/679-20261114/sources'
DATE = '2026-11-15'
API = dict(N='not_required', O='optional', R='required', D='depends', **{'?':'unconfirmed'})
COST = dict(F='no_model_fee', H='host_plan', U='usage_based', C='choice', **{'?':'unconfirmed'})
CLIENT = {'-':'not_documented','H':'host','M':'connector','P':'project_integration','N':'native','R':'reference','D':'depends','?':'unconfirmed'}
LOCAL = {'-':'not_applicable','L':'supported','D':'not_documented','?':'unconfirmed'}


def read(path):
    return json.loads(path.read_text(encoding='utf8'))


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=1)+'\n', encoding='utf8')


def overlays(pattern):
    result = {}
    for path in sorted(CURATION.glob(pattern)):
        for rid, value in read(path).items():
            if rid in result:
                if isinstance(value, list):
                    result[rid] = list(dict.fromkeys(result[rid]+value))
                else:
                    result[rid].update(value)
            else:
                result[rid] = value
    return result


def command(spec, text):
    """Only select commands literally present in the reviewed source."""
    if spec in {'read', 'readme'} or spec.startswith('docs:'):
        return '', ''
    if spec.startswith('c:'):
        literal = spec[2:]
        if not any(line.strip().removeprefix('$ ').strip() == literal for line in text.splitlines()):
            raise ValueError(f'Command is not a whole source line: {literal}')
        return literal, 'shell'
    source_blocks = blocks(text)
    selected, languages = [], []
    for part in spec.split('+'):
        match = re.fullmatch(r'b(\d+)(?::(\d+)-(\d+))?', part)
        if not match:
            raise ValueError(f'Invalid block selection: {part}')
        block = source_blocks[int(match[1])]
        code = block['code']
        if match[2] is not None:
            lines = code.splitlines()
            start, end = int(match[2]), int(match[3])
            if not 0 <= start <= end < len(lines):
                raise ValueError(f'Invalid source range: {part}')
            code = '\n'.join(lines[start:end+1])
        selected.append(code)
        languages.append(block['language'])
    # Shell prompts in source snippets are presentation, not executable syntax.
    code = '\n\n'.join(selected)
    code = '\n'.join(re.sub(r'^(?:> |\$ )', '', line) for line in code.splitlines())
    return code, ', '.join(dict.fromkeys(languages))


def compile_reviews():
    compact, detail = read(ROOT/'INDICE_IA.json'), read(ROOT/'INDICE_IA.detalle.json')
    public = {r['id']:r for r in compact['repos'] if r['cat']>0 and not r.get('alias_of')}
    rows, compiled, errors = {}, {}, []
    extras, corrections = overlays('extra*source*.json'), overlays('corrections*.json')
    for path in sorted(CURATION.glob('reviews*.psv')):
        with path.open(encoding='utf8', newline='') as handle:
            for line, row in enumerate(csv.DictReader(handle, delimiter='|'), 2):
                rid = row.get('id')
                try:
                    if rid not in public or rid in rows:
                        raise ValueError('Unknown or duplicate repository')
                    if None in row or any(not str(v).strip() for v in row.values()):
                        raise ValueError('Missing or extra fields')
                    rows[rid] = row
                    source = read(SOURCES/rid/'source.json')
                    if source['status'] != 'available' or not source.get('blob_sha'):
                        raise ValueError('No verified source')
                    if source.get('metadata',{}).get('private'):
                        raise ValueError('Private source cannot enter public review')
                    if public[rid].get('github_id') and public[rid]['github_id'] != source['metadata']['id']:
                        raise ValueError('GitHub identity changed')
                    text = (SOURCES/rid/'readme.md').read_text(encoding='utf8')
                    install_command, language = command(row['install'], text)
                    values = [v.strip() for v in row['access'].split(',')]
                    api,cost,claude,codex,antigravity,local = values
                    access = dict(api=API[api], cost=COST[cost], claude_code=CLIENT[claude], codex=CLIENT[codex], antigravity=CLIENT[antigravity], local_model=LOCAL[local])
                    category = (public[rid]['cat'], public[rid]['sub']) if row['category']=='=' else (int(row['category'].split(':')[0]), row['category'].split(':')[1])
                    compiled[rid] = dict(row=row, source=source, command=install_command, language=language, access=access, category=category, extra_sources=extras.get(rid,[]), corrections=corrections.get(rid,{}))
                except (ValueError, KeyError, IndexError, OSError) as error:
                    errors.append(f'{path.name}:{line} {rid}: {error}')
    return compact, detail, public, compiled, errors


def apply(compact, detail, public, compiled):
    from repo_intelligence.core.access import access_routes, SUPPORTED_CLIENT
    from repo_intelligence.core.taxonomy import build_areas
    ready_apps=set(read(CURATION/'installation-profiles.json')['ready_apps'])
    if ready_apps-set(public):raise ValueError('Unknown ready-app identity')
    topics = {t['id']:t for a in compact['discovery']['areas'] for t in a['topics']}
    for num,key,title in [(18,'reservas','Reservas y programación de citas'),(17,'comunidades','Comunidades,chat y llamadas'),(26,'simulacion','Física y simulación')]:
        category = next(c for c in compact['categories'] if c['num']==num)
        if not any(s['key']==key for s in category['subs']):
            category['subs'].append(dict(key=key,title=title))
    def topic(aid,tid,title,description,selectors=None):
        if tid not in topics:
            value = dict(id=tid,title=title,description=description,selectors=selectors or [],repos=[],reference_repos=[],keywords=[])
            next(a for a in compact['discovery']['areas'] if a['id']==aid)['topics'].append(value)
            topics[tid]=value
        return topics[tid]
    topic('automatizacion','negocio-reservas','Reservas y citas','Organizar disponibilidad y reserva de horarios.',[dict(cat=18,subs=['reservas'])])
    topics['negocio-whatsapp'].update(title='WhatsApp y pasarelas de mensajería',description='Distinguir conexiones oficiales,pasarelas y bibliotecas de WhatsApp.',selectors=[dict(cat=17,subs=['whatsapp'])])
    topic('automatizacion','negocio-chatbots','Constructores de conversaciones','Diseñar flujos conversacionales y conectar canales.',[dict(cat=17,subs=['chatbots'])])
    topic('automatizacion','negocio-comunidades','Comunidades,chat y llamadas','Organizar espacios compartidos de comunicación.',[dict(cat=17,subs=['comunidades'])])
    topic('audiovisual','av-simulacion','Física y simulación','Simular cuerpos,colisiones y sistemas físicos.',[dict(cat=26,subs=['simulacion'])])
    for prefix in ['claude','codex','antigravity']:
        aid = 'configurar-claude-code' if prefix=='claude' else 'configurar-'+prefix
        topic(aid,prefix+'-mcp','MCP y herramientas conectadas','Conectar herramientas por MCP; cada servidor conserva sus permisos y costes.')
        topic(aid,prefix+'-integraciones','Integraciones,proveedores y paneles','Adaptadores del proyecto para modelos,sesiones o servicios; revisa qué función usa realmente el plan.')
    for rid, item in compiled.items():
        row, source = item['row'], item['source']
        repo, card = public[rid], detail['repos'][rid]
        before = deepcopy(card.get('access',{}))
        previous_review = card.get('editorial_review',{})
        old_category = previous_review.get('previous_category',[repo['cat'],repo['sub']])
        repo.update(item['corrections']); card.update(item['corrections'])
        repo.update(cat=item['category'][0], sub=item['category'][1])
        card.update(cat=repo['cat'], sub=repo['sub'])
        access = card.setdefault('access',{})
        access.update(item['access'])
        access.update(review='documented', checked_at=DATE, source_blob_sha=source['blob_sha'], sources=list(dict.fromkeys([source['url'], *item['extra_sources']])), scope='La ficha distingue programa, modelo, agente y servicios externos. Compatibilidad documental; no se instaló ni probó el proyecto en los clientes.', cost_note=row['cost_note'], api_note=row['cost_note'], subscription_note=row['review_note'], local_note=row['review_note'],hardware='prerequisites',hardware_note=row['needs'].replace(';','; '))
        access.pop('other_access',None)
        access['mode'] = 'reference' if row['install']=='read' else 'agent_extension' if repo['role']=='skill' else 'software'
        card['cases'] = [row['example_1'], row['example_2']]
        # Replace legacy inferred prose; the new text comes from the individual ledger.
        card['desc'] = item['corrections'].get('desc') or repo['one']
        card['why'] = 'Usos propuestos: '+row['example_1']+'; '+row['example_2']+'.'
        card['how'] = row['review_note']
        card['stack'] = row['needs'].replace(';','; ')
        card['models'] = row['cost_note']
        card['choose_if'] = 'Tu objetivo encaja con estos ejemplos: '+row['example_1']+'; '+row['example_2']
        card['avoid_if'] = 'Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo'
        card['limits'] = row['review_note']
        card['first_step'] = row['first_action']
        card['first_try'] = dict(action=row['first_action'], success=row['success'], execution='proposed_not_executed')
        card['practical_examples'] = [dict(scenario=row[key], status='illustrative') for key in ('example_1','example_2')]
        guide_url = row['install'][5:] if row['install'].startswith('docs:') else source['url']
        prereqs = row['needs'].split(';')
        steps = (['Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.', 'Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.', 'Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.'] if item['command'] else ['Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.', 'Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.']) if row['install']!='read' else [row['first_action']+'.','Comprueba: '+row['success']+'.']
        if row['install']!='read' and (access['api']!='not_required' or access['local_model']=='supported' or repo['role']=='skill'):
            steps.append('Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.')
        audience='reading' if row['install']=='read' else 'agent' if repo['role']=='skill' else 'ready_app' if rid in ready_apps else 'developer' if repo['role']=='library' else 'setup'
        card['getting_started'] = dict(kind='reference' if row['install']=='read' else 'source', audience=audience, entry_url='', prerequisites=prereqs, steps=steps, command=item['command'], command_language=item['language'], command_status='documented' if item['command'] else 'reference' if row['install']=='read' else 'readme', source=guide_url, note='Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.', checked_at=DATE)
        card['install'] = ' '.join(steps)+' Guía original: '+guide_url
        card['editorial_review'] = dict(status='source_reviewed', checked_at=DATE, source=source['url'], source_blob_sha=source['blob_sha'], previous_source_blob_sha=previous_review.get('previous_source_blob_sha',before.get('source_blob_sha','')), previous_category=old_category,category_verdict='confirmed' if row['category']=='=' else 'corrected', note=row['review_note'], checks=['identity','category','examples','installation_source','api_costs','claude_code','codex','antigravity','local_model'], installation_tested=False)
        metadata=source.get('metadata',{})
        if 'archived' in metadata:
            repo['source_archived']=card['source_archived']=metadata['archived']
            if repo.get('status')!='unverified':
                if metadata['archived']:repo['status']='archived'
                elif repo.get('status')=='archived':repo.pop('status')
        if isinstance(metadata.get('license'),dict):
            card['license']=metadata['license'].get('spdx_id') or card.get('license','')
        repo['routes'] = access_routes(card)
        if 'connector' in [access[k] for k in ('claude_code','codex','antigravity')]:
            repo['mcp'] = card['mcp'] = True
        for tid in [t.removeprefix('+') for t in row['topics'].split(';')] if row['topics']!='=' else []:
            topics[tid]['repos'] = sorted(set(topics[tid].get('repos',[])) | {rid})
        for client,prefix in [('claude_code','claude'),('codex','codex'),('antigravity','antigravity')]:
            value=access[client]
            tid=prefix+'-mcp' if value=='connector' else prefix+'-skills' if value=='host' else prefix+'-integraciones' if value=='project_integration' else None
            if tid:topics[tid]['repos']=sorted(set(topics[tid]['repos'])|{rid})
    # Botpress is now an SDK/integration hub, not a substitute for the Rasa server.
    for repo in compact['repos']:
        if repo['id']=='botpress':repo['alt']=[]
        else:repo['alt']=[rid for rid in repo.get('alt',[]) if rid!='botpress']
        if repo['id'] in detail['repos']:
            detail['repos'][repo['id']]['alternatives']=repo.get('alt',[])
    for area in compact['discovery']['areas']:
        client=area.get('client')
        if not client:continue
        evidence_ids=set()
        for entry in area['topics']:
            ids=set(entry.get('repos',[]))|set(entry.get('reference_repos',[]))
            def is_reference(rid):
                return compiled[rid]['access'][client]=='reference' or detail['repos'][rid]['access']['mode']=='reference'
            entry['repos']=sorted(rid for rid in ids if compiled[rid]['access'][client] in SUPPORTED_CLIENT and not is_reference(rid))
            entry['reference_repos']=sorted(rid for rid in ids if is_reference(rid) and compiled[rid]['access'][client] in SUPPORTED_CLIENT|{'reference'})
            evidence_ids.update(entry['repos']+entry['reference_repos'])
        area['evidence']=[dict(repo_id=rid,source=compiled[rid]['source']['url'],readme_blob_sha=compiled[rid]['source']['blob_sha'],checked_at=DATE,usage='reference' if is_reference(rid) else 'documented_integration') for rid in sorted(evidence_ids)]
        area['starters']=[rid for rid in area['starters'] if rid in evidence_ids]
    counts = Counter(r['cat'] for r in compact['repos'] if not r.get('alias_of'))
    for cat in compact['categories']:
        cat['count'] = counts[cat['num']]
    compact['discovery']['reviewed_at'] = DATE
    compact.setdefault('meta',{}).update(updated=DATE,access_checked=DATE)
    for goal in compact['discovery']['goals']:
        goal['categories']=sorted({r['cat'] for r in public.values() if goal['id'] in r.get('goals',[]) or r['id'] in goal['starters']+goal['guided']})
    compact['discovery']['editorial_review']=dict(total=len(public),reviewed=len(compiled),date=DATE,report='reports/review-679-2026-11-14.json',scope='Documentación individual; ejemplos propuestos; sin pruebas de instalación de terceros.')
    for recipe in compact['recipes']:
        if recipe['id']=='pipeline-de-reels-video-corto':
            recipe['repos']=['kokoro' if rid=='chatterbox' else rid for rid in recipe['repos']]
            for step in recipe['steps']:
                if step['id']=='chatterbox':step.update(id='kokoro',role='Genera una voz en off con una voz e idioma compatibles')
            recipe['flow']=[['kokoro' if value=='chatterbox' else value for value in edge] for edge in recipe['flow']]
            recipe['how']='Flujo propuesto: WhisperX prepara subtítulos; Kokoro sintetiza narración; ComfyUI genera visuales; Remotion compone y FFmpeg exporta. Comprueba los datos,la duración y la licencia de cada recurso. MoneyPrinterTurbo es otra aplicación con su configuración y costes propios.'
            recipe['when_not']='Si solo necesitas cortar un video existente,no necesitas generar voces o imágenes. Kokoro,ComfyUI y los demás modelos tienen requisitos de equipo distintos; si eliges servicios remotos,revisa sus tarifas. Chatterbox queda como archivo de investigación y no como voz inicial recomendada.'
    build_areas(compact,[{**r,'access':detail['repos'][r['id']]['access']} for r in public.values()])
    save(ROOT/'INDICE_IA.json', compact); save(ROOT/'INDICE_IA.detalle.json', detail)


def main():
    sys.stdout.reconfigure(encoding='utf8')
    parser = argparse.ArgumentParser(); parser.add_argument('--apply',action='store_true'); args=parser.parse_args()
    compact,detail,public,compiled,errors = compile_reviews()
    pending = sorted(set(public)-compiled.keys())
    if errors:
        print('\n'.join(errors)); raise SystemExit(1)
    report = dict(date=DATE,total=len(public),individually_reviewed=len(compiled),pending=pending,corrected_categories=sum(item['row']['category']!='=' for item in compiled.values()),method='Individual primary-source editorial review; examples proposed; no third-party installation executed.',repositories={rid:dict(category=item['category'],category_verdict='confirmed' if item['row']['category']=='=' else 'corrected',access=item['access'],source=item['source']['url'],source_blob_sha=item['source']['blob_sha'],installation_selection=item['row']['install'],installation_tested=False,cost_note=item['row']['cost_note'],note=item['row']['review_note']) for rid,item in sorted(compiled.items())})
    save(ROOT/'reports/review-679-2026-11-14.json',report)
    print(f'{len(compiled)}/{len(public)} individually reviewed; {len(pending)} pending; commands validated against snapshots.')
    if args.apply:
        if pending:
            raise SystemExit('Refusing to apply an incomplete review as a complete catalogue revision.')
        apply(compact,detail,public,compiled)


if __name__=='__main__':
    main()
