# Alexandría para agentes · Ahorro de contexto y tokens

Categoría 23 «Operar, evaluar y medir modelos de IA» › subcategoría `tokens`. 2 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=23&sub=tokens · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `rtk` | Proxy de terminal que compacta salidas de comandos para reducir el contexto que… | 1 Básico | 69 | Apache-2.0 (OSI permisiva) | recomendado |
| `headroom` | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo… | 2 Intermedio | 60 | Apache-2.0 (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### rtk (`rtk`)

- **Repo:** https://github.com/rtk-ai/rtk · Apache-2.0 · nivel 1 · 69/100 · recomendado en «Compactar contexto y tokens»
- **Qué es:** RTK (Rust Token Killer), filtro de salidas de terminal para agentes de programación, de rtk-ai. El binario por defecto combina Apache-2.0 y BUSL-1.1, y la edición `rtk-oss` es solo Apache-2.0.
- **Cuándo elegirlo:** Casos: Reducir salida repetitiva de comandos; Estudiar consumo de contexto por tarea.
- **Requisitos:** nivel 1: preparación sencilla; Binario para tu sistema; agente y proyecto de prueba; configuración por agente; hardware prerequisites; API de IA: opcional; Binario para tu sistema; agente y proyecto de prueba; configuración por agente.
- **Instalación (documentada en la fuente; no ejecutada):** `winget install rtk-ai.rtk` — fuente: https://github.com/rtk-ai/rtk/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Prueba un comando RTK y compara su salida con la versión sin comprimir antes de activar hooks Éxito: Puedes comprobar datos omitidos y contadores de ahorro
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `gemini-cli` [20/terminal], `claude-code-usage-monitor` [23/observabilidad], `mimo-code` [20/terminal]
- **Alternativas:** `headroom`
- **Riesgos y avisos:** BSL (source-available): no es OSI; revisa usos comerciales y la fecha de cambio de licencia. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): headroom. Si quieres solo código Apache-2.0, instala `rtk-oss`. Claude y Codex tienen hooks documentados; Antigravity usa un archivo de reglas y no la misma automatización; las cifras de ahorro dependen de la tarea.

### headroom (`headroom`)

- **Repo:** https://github.com/headroomlabs-ai/headroom · Apache-2.0 · nivel 2 · 60/100 · alternativa en «Compactar contexto y tokens»
- **Qué es:** Headroom, capa de compresión de contexto para agentes y LLM de Headroom Labs (paquete `headroom-ai` en PyPI y npm). Licencia Apache-2.0. Es muy activo (~80k estrellas, v0.44.0).
- **Cuándo elegirlo:** Casos: Reducir salidas extensas de herramientas; Comparar una sesión con y sin compresión.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python compatible; contenido de prueba; agente o cliente MCP si lo conectas; hardware prerequisites; API de IA: opcional; Python compatible; contenido de prueba; agente o cliente MCP si lo conectas.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install headroom-ai` — fuente: https://github.com/headroomlabs-ai/headroom/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Comprime una salida JSON pequeña y compara el resultado con el original antes de envolver un agente Éxito: Puedes identificar qué se conservó y recuperar el original cuando corresponda
- **Combina con:** `claude-code` [20/terminal], `litellm` [23/serving], `context-engineering` [19/guias], `codegraph` [7/codigo], `claude-code-usage-monitor` [23/observabilidad], `mimo-code` [20/terminal]
- **Alternativas:** `rtk`
- **Riesgos y avisos:** Alternativas (elige una): rtk. El número de estrellas crece de forma inusual para un proyecto tan joven; los ahorros son mediciones del propio proyecto. Documenta wrap para Claude y Codex y MCP para cualquier cliente compatible; los ahorros de benchmarks no garantizan iguales respuestas en toda tarea.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-23-tokens.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Ahorro de contexto y tokens», lee `docs/alexandria/categoria-23-tokens.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-23-tokens.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
