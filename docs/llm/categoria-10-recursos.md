# Alexandría para agentes · Recursos y casos de uso

Categoría 10 «Dashboards, analítica y mapas» › subcategoría `recursos`. 2 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=10&sub=recursos · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `awesome-dataviz` | Directorio curado de herramientas, librerías y recursos de visualización de… | 1 Básico | 58 | CC-BY-4.0 (OSI permisiva) | sin grupo |
| `data-analyst-roadmap` | Hoja de ruta para aprender análisis de datos, con tecnologías, capacidades y… | 1 Básico | 38 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### awesome-dataviz (`awesome-dataviz`)

- **Repo:** https://github.com/hal9ai/awesome-dataviz · CC-BY-4.0 · nivel 1 · 58/100
- **Qué es:** Awesome Dataviz, lista curada de frameworks, librerías y software de visualización open source, creada por @fasouto y mantenida con patrocinio de Hal9. Licencia CC BY 4.0 (GitHub muestra NOASSERTION). Tiene ~4.5k estrellas.
- **Cuándo elegirlo:** Casos: Encontrar una biblioteca de mapas; Comparar gráficos para React y JavaScript.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; tipo de gráfico y framework objetivo; hardware prerequisites; API de IA: no; Navegador; tipo de gráfico y framework objetivo.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/hal9ai/awesome-dataviz/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Selecciona dos bibliotecas de un mismo tipo y compara licencia, accesibilidad y formato de datos Éxito: Tienes candidatos con documentación original y requisitos identificados
- **Combina con:** `echarts` [10/graficos], `d3` [10/graficos], `awesome-bigdata` [25/datos]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. El directorio reúne opciones; no se instala completo ni verifica automáticamente la calidad de cada enlace.

### data-analyst-roadmap (`data-analyst-roadmap`)

- **Repo:** https://github.com/mtahiraslan/data-analyst-roadmap · MIT · nivel 1 · 38/100
- **Qué es:** Hoja de ruta para aprender análisis de datos, de @mtahiraslan. Licencia MIT. Es pequeña (~1k estrellas) y su último cambio es de octubre de 2025.
- **Cuándo elegirlo:** Casos: Organizar un plan inicial de estudio; Identificar conocimientos para un primer proyecto.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; tiempo de estudio; una tabla pequeña de práctica; hardware prerequisites; API de IA: no; Navegador; tiempo de estudio; una tabla pequeña de práctica.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/mtahiraslan/data-analyst-roadmap/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Elige SQL o una hoja de cálculo y resuelve una pregunta con una tabla ficticia Éxito: Puedes explicar dato de entrada, cálculo y resultado
- **Combina con:** `duckdb` [25/datos], `marimo` [25/datos], `metabase` [10/bi]
- **Riesgos y avisos:** Sin alternativas declaradas. Recurso introductorio, sin mantenimiento reciente. Es una ruta basada en experiencia del autor, no una garantía de empleo ni un programa que debas completar entero.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-10-recursos.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Recursos y casos de uso», lee `docs/alexandria/categoria-10-recursos.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-10-recursos.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
