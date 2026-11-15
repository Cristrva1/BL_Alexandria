"""Curated learning resources, separate from the repository inventory."""
from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse


PROMPT_TOPICS = {'empezar', 'programar', 'mejorar', 'disenar', 'lanzar', 'contenido', 'negocio', 'aprender', 'diagnosticar', 'movil', 'operar'}


def _https(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == 'https' and bool(parsed.netloc)


def load_handbook(root: Path, repo_ids: set[str] | None = None) -> dict:
    path = Path(root) / 'data' / 'handbook.json'
    if not path.exists():
        return {'groups': [], 'resources': [], 'prompts': [], 'paths': [], 'updated_at': ''}
    data = json.loads(path.read_text(encoding='utf-8'))
    groups = {g['id']: g for g in data['groups']}
    resources = {r['id']: r for r in data['resources']}
    all_entries = data['resources'] + data['prompts'] + data['paths']
    ids = [r['id'] for r in all_entries]
    if len(ids) != len(set(ids)) or any(not re.fullmatch(r'[a-z0-9-]+', id) for id in ids):
        raise ValueError('Handbook identifiers must be unique, lower-case slugs')
    if len(groups) != len(data['groups']) or any(g['section'] not in {'configurar', 'servicios'} for g in groups.values()):
        raise ValueError('Invalid handbook groups')
    for resource in data['resources']:
        if resource['group'] not in groups:
            raise ValueError(f"Unknown group: {resource['id']}")
        for key in ('name', 'kind', 'summary', 'verify', 'access', 'cost'):
            if not resource.get(key, '').strip():
                raise ValueError(f"Missing {key}: {resource['id']}")
        for key in ('prepare', 'steps', 'improve', 'limits', 'sources'):
            if not resource.get(key):
                raise ValueError(f"Missing {key}: {resource['id']}")
        if any(not _https(s['url']) or not s.get('checked_at') for s in resource['sources']):
            raise ValueError(f"Invalid source: {resource['id']}")
        if any(not _https(c['source']) or not all(c.get(k) for k in ('title', 'text', 'where', 'effect')) for c in resource['commands']):
            raise ValueError(f"Invalid command: {resource['id']}")
        if repo_ids is not None and set(resource['repo_ids']) - repo_ids:
            raise ValueError(f"Unknown curated repository: {resource['id']}")
    for prompt in data['prompts']:
        if not all(prompt.get(k) for k in ('title', 'topic', 'when', 'inputs', 'body', 'expect', 'authorship')):
            raise ValueError(f"Incomplete prompt: {prompt['id']}")
        if prompt['topic'] not in PROMPT_TOPICS or prompt.get('level', 'inicial') not in {'inicial', 'intermedio', 'avanzado'}:
            raise ValueError(f"Invalid prompt topic or level: {prompt['id']}")
        inspired = prompt.get('inspired_by')
        if inspired and (not _https(inspired.get('url', '')) or 'docs.google.com' in inspired['url']):
            raise ValueError(f"Invalid prompt inspiration source: {prompt['id']}")
    for route in data['paths']:
        if route['section'] not in {'configurar', 'servicios'} or not route['steps']:
            raise ValueError(f"Invalid learning path: {route['id']}")
        if any(step['resource'] not in resources or not step['text'] for step in route['steps']):
            raise ValueError(f"Unknown learning path resource: {route['id']}")
    return data


def render_handbook(root: Path) -> Path:
    """Generate the GitHub-readable companion from the same content as the site."""
    data = load_handbook(root)
    lines = ['# Configurar IA, prompts y servicios', '',
             'Generado desde `data/handbook.json`. Guías de orientación documental; no acreditan instalación ni rendimiento. Las plantillas son originales de Alexandría.', '',
             f"Revisión: {data['updated_at']}. Los precios, planes y versiones pueden cambiar.", '',
             '## Índice', '']
    for group in data['groups']:
        lines += [f"### {group['title']}", '']
        lines += [f"- [{r['name']}](#{r['id']})" for r in data['resources'] if r['group'] == group['id']]
        lines.append('')
    for route in data['paths']:
        lines += [f"## {route['title']}", '', route['goal'], '']
        for i, step in enumerate(route['steps'], 1):
            name = next(r['name'] for r in data['resources'] if r['id'] == step['resource'])
            lines.append(f"{i}. [{name}](#{step['resource']}): {step['text']}")
        lines += ['', f"**Comprueba:** {route['verify']}", '', route['limit'], '']
    for resource in data['resources']:
        lines += [f'<a id="{resource["id"]}"></a>', '', f"## {resource['name']}", '',
                  f"**Tipo:** {resource['kind']}", '', resource['summary'], '',
                  '### Antes de empezar', '']
        lines += ['- ' + text for text in resource['prepare']]
        lines += ['', '### Primera prueba', '']
        lines += [f'{i}. {text}' for i, text in enumerate(resource['steps'], 1)]
        lines += ['', f"**Qué comprobar:** {resource['verify']}", '',
                  f"**Cuenta y compatibilidad:** {resource['access']}", '', f"**Costes:** {resource['cost']}", '',
                  '### Mejoras después de la primera prueba', '']
        lines += ['- ' + text for text in resource['improve']]
        lines += ['', '### Límites', ''] + ['- ' + text for text in resource['limits']]
        for command in resource['commands']:
            lines += ['', f"### Comando: {command['title']}", '', f"Dónde: {command['where']}", '',
                      '```text', command['text'], '```', '', command['effect'], '', f"[Fuente del comando]({command['source']})"]
        if resource['repo_ids']:
            lines += ['', 'Fichas del catálogo: ' + ' · '.join(f'[{id}](fichas/{id}.md)' for id in resource['repo_ids'])]
        lines += ['', '### Fuentes', '']
        lines += [f"- [{source['title']}]({source['url']}) · {source['checked_at']}" for source in resource['sources']]
        lines.append('')
    lines += ['## Prompts', '', 'Sustituye los campos entre corchetes. Revisa la respuesta antes de ejecutar acciones.', '']
    for prompt in data['prompts']:
        lines += [f"### {prompt['title']}", '', prompt['when'], '', '```text', prompt['body'], '```', '',
                  f"**Resultado esperado:** {prompt['expect']}", '']
        if prompt.get('inspired_by'):
            lines += [f"Idea de partida: [{prompt['inspired_by']['title']}]({prompt['inspired_by']['url']}). Texto reescrito por Alexandría.", '']
    output = Path(root) / 'human' / 'MANUAL_IA.md'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('\n'.join(lines), encoding='utf-8')
    return output
