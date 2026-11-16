"""Generate task-first wayfinding and access guides from the canonical library."""
from collections import Counter
from pathlib import Path

from repo_intelligence.core.access import API_LABELS, ROUTE_LABELS, access_facts, access_routes
from repo_intelligence.core.catalog import Catalog, md_cell, slug
from repo_intelligence.core.reading import GUIDES
from repo_intelligence.guides.areas import render_area_guides


def render_navigation(root: Path, catalog: Catalog) -> None:
    human=root/'human';human.mkdir(parents=True,exist_ok=True)
    public=[r for r in catalog.repos if int(r.get('cat') or 0)>0 and not r.get('alias_of')]
    areas=render_area_guides(root,catalog)
    readme=['# Biblioteca de Alexandría', '', 'Encuentra qué usar entre cientos de repositorios de IA y automatización. Entiende qué hace cada uno, cómo empezar y si usa una suscripción, una API o un modelo local.', '', '<!-- BL:STATS -->', f'{len(public)} repositorios', '<!-- /BL:STATS -->', '', '## ¿Qué estás buscando?', '', '| Necesito… | Empieza aquí |', '|---|---|', '| Resolver una tarea sin conocer los nombres de los repos | [Rutas por objetivo](human/rutas.md) |', '| Aprovechar mi acceso a Claude Code o Codex | [Formas de uso](human/formas-de-uso.md) |', '| Saber si necesito pagar una API o puedo usar un modelo local | [Acceso y costes](human/acceso.md) |', '| Comparar e instalar una herramienta concreta | [Guía de arranque](human/instalar.md) |', '| Explorar todo por tema | [Mapa de categorías](human/README.md#explora-por-tema) |', '| Ver las incorporaciones recientes | [Novedades de la biblioteca](human/novedades.md) |', '', '## Usa el explorador', '', 'El explorador reúne búsqueda por tarea, filtros de acceso, fichas completas y comparación de hasta tres opciones. Incluye las guías y las recetas en la misma navegación.', '', 'Descarga este repositorio y abre `docs/index.html` en tu navegador. Funciona sin un servidor. También puedes levantarlo desde la carpeta del proyecto:', '', '```powershell', 'uv run repo-intelligence web serve', '```', '', '## Lee una ficha antes de instalar', '', '1. Qué resultado produce y cuándo conviene elegirlo.', '2. API de IA, acceso desde Claude Code o Codex y modelos locales documentados.', '3. Coste por ruta, servicios externos y requisitos de equipo.', '4. Pasos de arranque y comandos respaldados por la documentación.', '5. Alternativas, complementos y fecha y fuentes de revisión.', '', 'Las estrellas miden popularidad. El código abierto no incluye automáticamente servicios, modelos o licencias sin coste. Una interfaz local no demuestra que el modelo también lo sea.', '', '## Para construir algo completo', '', 'Las [recetas](human/playbooks/README.md) ordenan pocas piezas por función: WhatsApp, investigación, RAG, video, presentaciones y otros flujos. La [guía completa](Guia.md) y el [catálogo](Catalogo.md) quedan como referencia de consulta.', '', '## Para agentes y colaboradores', '', '- [AGENTS.md](AGENTS.md): protocolo de selección y fuentes canónicas.', '- [Menú portable](menu_portable/REPO_MENU.md): copia el índice a otro proyecto.', '- [Mantenimiento editorial](human/mantenimiento.md): cómo incorporar, verificar y regenerar.', '', 'No es necesario descargar los proyectos catalogados para consultar la biblioteca.']
    readme[4:4]=['**[Abrir Alexandría en línea](https://cristrva1.github.io/BL_Alexandria/)** — consulta la biblioteca sin descargar ni instalar nada.', '']
    if (root/'data'/'handbook.json').exists():
        i=next(i for i,line in enumerate(readme) if line.startswith('| Explorar todo por tema'))
        readme[i:i]=[
            '| Configurar o mejorar un agente, modelo local o automatización del teléfono | [Configurar IA](https://cristrva1.github.io/BL_Alexandria/#/configurar) |',
            '| Copiar una plantilla o saber dónde ejecutar un comando | [Prompts y comandos](https://cristrva1.github.io/BL_Alexandria/#/prompts) |',
            '| Elegir alojamiento, datos, contenedores o acceso remoto | [Servicios y despliegue](https://cristrva1.github.io/BL_Alexandria/#/servicios) |',
        ]
    if (root/'data'/'techniques.json').exists():
        i=next(i for i,line in enumerate(readme) if line.startswith('| Explorar todo por tema'))
        readme[i:i]=['| Trabajar mejor con agentes: técnicas, ideas y recomendaciones | [Técnicas e ideas](https://cristrva1.github.io/BL_Alexandria/#/tecnicas) · [versión Markdown](human/TECNICAS.md) |']
    review=catalog.compact.get('discovery',{}).get('editorial_review',{})
    if review.get('reviewed')==len(public):
        report=review.get('report','reports/review-679-2026-11-14.json')
        readme[6:6]=[f'Las **{len(public)} fichas tienen revisión documental individual**: categoría, ejemplos prácticos, primeros pasos, costes y compatibilidad con Claude Code, Codex, Antigravity y modelos locales. Consulta el [registro de revisión]({report}) y el [método editorial](curation/review-679-2026-11-14/README.md). Los ejemplos son propuestas; las instalaciones no se ejecutaron.', '']
    readme=[line.replace('Claude Code o Codex','Claude Code, Codex o Antigravity').replace('5. Alternativas, complementos y fecha y fuentes de revisión.','5. Primera prueba propuesta, resultado observable, alternativas y fuentes fechadas.') for line in readme]
    start=next(i for i,line in enumerate(readme) if line.startswith('Descarga este repositorio'))
    readme[start:start+1]=['1. En esta página de GitHub pulsa **Code → Download ZIP**.', '2. Extrae el ZIP en una carpeta de tu equipo.', '3. Abre la carpeta `docs` y haz doble clic en `index.html`.', '4. Entra en **Guíame**, describe tu proyecto, experiencia, equipo y acceso a IA y revisa hasta tres opciones.', '', 'No necesitas Python ni descargar los proyectos del catálogo para consultar el explorador. Si ya trabajas con el entorno de desarrollo del proyecto, también puedes levantarlo desde la terminal:']
    readme.insert(readme.index('## ¿Qué estás buscando?'), '[Primera vez: lee cómo elegir](human/elegir.md) · [Diccionario breve](human/vocabulario.md)')
    if areas:
        readme=[line.replace('[Mapa de categorías](human/README.md#explora-por-tema)','[Categorías y subcategorías](human/areas.md)') for line in readme]
        i=readme.index('## Usa el explorador')
        readme[i:i]=['## Explora por área de trabajo', '', 'Empieza por [Frontend y páginas web](human/areas/frontend.md), [Ciberseguridad](human/areas/ciberseguridad.md), [Producción audiovisual](human/areas/audiovisual.md) o [Trading y finanzas](human/areas/trading.md). Consulta las demás áreas y sus subcategorías en [el mapa práctico](human/areas.md).', '', 'Para preparar tu agente: [Configuración de Claude Code](human/areas/configurar-claude-code.md) · [Configuración de Codex](human/areas/configurar-codex.md) · [Configuración de Antigravity](human/areas/configurar-antigravity.md).', '']
    start=readme.index('1. En esta página de GitHub pulsa **Code → Download ZIP**.')
    readme[start:start]=['Si prefieres guardar una copia para consultar en tu equipo:', '']
    # Binarias Labs logo: web/build.py copies it to docs/marca when the explorer is built.
    readme[0:0]=['<p align="center"><a href="https://cristrva1.github.io/BL_Alexandria/"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/marca/binarias-labs-dark.png"><img src="docs/marca/binarias-labs.png" alt="Binarias Labs" width="246" height="62"></picture></a></p>', '']
    i=readme.index('**[Abrir Alexandría en línea](https://cristrva1.github.io/BL_Alexandria/)** — consulta la biblioteca sin descargar ni instalar nada.')
    readme[i+1:i+1]=['', 'Un proyecto de **Binarias Labs**: tecnología que integra posibilidades.']
    (root/'README.md').write_text('\n'.join(readme)+'\n',encoding='utf8')
    for guide in GUIDES:
        lines=['[Inicio](README.md) · [Rutas por objetivo](rutas.md) · [Explorador](../docs/index.html)', '', '# '+guide['title'], '', guide['intro'], '']
        for section in guide['sections']:lines+=['## '+section['title'],'',section['text'],'']
        if guide.get('sources'):
            lines+=['## Fuentes y fecha','',f'Documentación consultada el {catalog.meta.get("access_checked") or "fecha por confirmar"}. Las condiciones de los proveedores pueden cambiar.','']
            lines += [f'- [{s["title"]}]({s["url"]})' for s in guide['sources']]
        (human/(guide['id']+'.md')).write_text('\n'.join(lines).rstrip()+'\n',encoding='utf8')
    lines=['[Inicio](README.md) · [Cómo elegir](elegir.md) · [Acceso y costes](acceso.md)', '', '# ¿Qué quieres conseguir?', '', 'Empieza por un resultado. Los repos de entrada son opciones para comparar, no una lista que debas instalar completa.', '']
    for goal in catalog.compact.get('discovery',{}).get('goals',[]):
        lines+=['## '+goal['title'],'',goal['description'],'', '| Punto de partida | Qué hace | Acceso básico |','|---|---|---|']
        if goal.get('outcome'):
            lines[-2:-2]=['**Resultado buscado:** '+goal['outcome'],'','**Prepara:** '+goal['bring'],'','**Decide primero:** '+goal['decision'],'']
        for rid in goal['starters']:
            r=catalog.get(rid)
            if r:lines.append(f'| [{md_cell(r["name"])}](fichas/{slug(rid)}.md) | {md_cell(r["one"])} | {API_LABELS[access_facts(r)["api"]]} |')
        lines+=['',f'[Ver la ruta en el explorador](../docs/index.html#/rutas?goal={goal["id"]})','']
    (human/'rutas.md').write_text('\n'.join(lines).rstrip()+'\n',encoding='utf8')
    counts=Counter(route for repo in public for route in access_routes(repo))
    lines=['[Inicio](README.md) · [Acceso y costes](acceso.md)', '', '# Buscar por forma de uso', '', 'Estas rutas se pueden combinar con un objetivo o categoría. Revisa la ficha: cada etiqueta describe una ruta concreta y no incluye automáticamente los costes de servicios externos.', '', '| Ruta | Repos | Abrir |','|---|---:|---|']
    for route,title in ROUTE_LABELS.items():lines.append(f'| {title} | {counts[route]} | [Explorar](../docs/index.html#/explorar?route={route}) |')
    lines+=['', '## Requisitos por confirmar','', 'Una fuente revisada no equivale a una prueba de ejecución. Los perfiles distinguen software sin LLM, acceso por agente, proveedores elegibles y cuestiones no documentadas.','', '| Repo | Pregunta pendiente |','|---|---|']
    for repo in public:
        a=access_facts(repo)
        if a['review']=='pending':lines.append(f'| [{repo["name"]}](fichas/{slug(repo["id"])}.md) | {md_cell(a["api_note"])} |')
    (human/'formas-de-uso.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
    lines=['[Inicio](README.md)', '', '# Mantener Alexandria', '', '## Incorporar un repo', '', '1. Revisa el README original y la documentación de instalación, autenticación y precios que enlaza.', '2. Añade o corrige la entrada en los dos índices canónicos. Conserva un id estable aunque cambie el propietario en GitHub.', '3. Escribe qué resultado produce, cuándo usarlo y cuál es su alternativa. Ubícalo en una categoría y subcategoría existentes antes de crear otra.', '4. Registra acceso, coste, modelos locales y clientes por separado. Usa por confirmar cuando no exista evidencia suficiente.', '5. Guarda la fuente, fecha y procedencia del comando. Un nombre de repo no basta para deducir un paquete.', '6. Regenera las guías y comprueba las referencias antes de publicar.', '', '## Consultar fuentes', '', '```powershell', 'uv run python scripts/audit_sources.py --id <id>', 'uv run repo-intelligence guide build', 'uv run repo-intelligence menu export', 'uv run repo-intelligence web build', 'uv run pytest', '```', '', 'El script de auditoría guarda material para revisar; no convierte coincidencias de palabras en compatibilidad o precios verificados. Los scripts de curaduría e importación fechados son migraciones históricas: no repetirlos sin adaptar sus categorías y decisiones. El enriquecedor propone borradores heurísticos; revisar categoría y subcategoría contra el mapa actual antes de incorporarlos.', '', '## Fechas diferentes', '', '- Añadido a Alexandria: primera aparición del id en su historial de Git.', '- Revisión de acceso: consulta de fuentes sobre modelos, cuentas e instalación.', '- Actividad del proyecto: fecha comunicada por su fuente, cuando se haya verificado.', '', 'No confundir una fecha de revisión editorial con actividad reciente del autor. No marcar todos los repos no descargados como novedades.']
    if (root/'data'/'handbook.json').exists():
        lines += ['', '## Mantener las guías de configuración y servicios', '',
                  'El contenido de Configurar IA, Servicios y despliegue, Prompts y comandos vive en `data/handbook.json`. Complementa el inventario de repos: no se añade un servicio o concepto al recuento de proyectos por aparecer en este manual.', '',
                  'Revisa la fuente del proyecto, la fecha, la ruta de acceso y el contexto de cada comando. Conserva los límites cuando falte evidencia y distingue la prueba propuesta de una instalación ejecutada. Las plantillas originales indican los datos que necesita aportar la persona.', '',
                  '`guide build` genera también `human/MANUAL_IA.md` y el sitio de Pages. `web build` actualiza la copia web. El cargador comprueba fuentes, comandos y referencias antes de publicar.']
    if (root/'data'/'techniques.json').exists():
        lines += ['', '## Mantener técnicas e ideas', '',
                  'Las técnicas, reglas y sitios útiles viven en `data/techniques.json`. Escribe resúmenes y pasos propios, enlaza fuentes públicas (repositorio o documentación oficial antes que una publicación social) y copia los comandos tal como aparecen en la fuente, con lugar de ejecución y efecto. Marca como no verificadas las cifras de terceros.', '',
                  '`guide build` genera `human/TECNICAS.md`. El cargador rechaza enlaces privados o de Google Docs, áreas inexistentes, identificadores repetidos y comandos sin fuente.']
    if (root/'data'/'retired.json').exists():
        lines += ['', '## Retirar repos obsoletos', '',
                  'Retira un repo solo con evidencia: archivado en GitHub, aviso de abandono de sus autores, sustituto oficial o años sin cambios en la rama principal. Comprueba la fecha del último commit, no la del último push. Presenta la lista a la persona responsable antes de borrar.', '',
                  'Al retirar, quita la ficha de `INDICE_IA.json` e `INDICE_IA.detalle.json`, limpia sus apariciones en `alt`, `combines_with`, áreas, objetivos y recetas, y regístrala en `data/retired.json` con motivo, evidencia, último commit y sustitutos del catálogo. El detector de stars no vuelve a proponer los repos de esa lista. El registro histórico de la revisión de 679 fichas no se modifica.']
    (human/'mantenimiento.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
