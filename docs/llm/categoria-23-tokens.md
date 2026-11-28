# Alexandría para agentes · Ahorro de contexto y tokens

Categoría 23 «Operar, evaluar y medir modelos de IA» › subcategoría `tokens`. 5 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
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
| `toon-format` | Convierte listas de objetos JSON a un texto con encabezado y filas para… | 2 Intermedio | 72 | MIT (OSI permisiva) | sin grupo |
| `rtk` | Proxy de terminal que compacta salidas de comandos para reducir el contexto que… | 1 Básico | 69 | Apache-2.0 (OSI permisiva) | recomendado |
| `headroom` | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo… | 2 Intermedio | 61 | Apache-2.0 (OSI permisiva) | alternativa |
| `gptcache` | Reutiliza respuestas de consultas parecidas a un modelo mediante una caché… | 2 Intermedio | 58 | MIT (OSI permisiva) | sin grupo |
| `llmlingua` | Acorta texto de entrada para modelos de lenguaje y permite medir cuánto… | 2 Intermedio | 48 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### TOON (`toon-format`)

- **Repo:** https://github.com/toon-format/toon · MIT · nivel 2 · 72/100
- **Qué es:** TOON es un formato de texto y una biblioteca JavaScript de referencia para codificar datos JSON.
- **Cuándo elegirlo:** Casos: Representar un inventario ficticio de productos con los mismos tres campos en cada fila.; Preparar una tabla de registros con idéntica estructura para comparar el tamaño con JSON compacto.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; TypeScript, package.json; API de IA: no; Node.js con npm y un proyecto con módulos ES.; Dos registros JSON ficticios con los mismos campos..
- **Instalación (documentada en la fuente; no ejecutada):** `npm install @toon-format/toon` — fuente: https://github.com/toon-format/toon/blob/92d7fc6d8af920afc99d1b6533cfc976c472fe7d/README.md
- **Primera prueba propuesta (no ejecutada):** Usa encode con dos registros ficticios que compartan campos, siguiendo el ejemplo del README de la versión 4.4.0. Éxito: La salida conserva ambos registros y enumera los campos en el encabezado. Revisa los valores y compárala con el JSON…

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

- **Repo:** https://github.com/headroomlabs-ai/headroom · Apache-2.0 · nivel 2 · 61/100 · alternativa en «Compactar contexto y tokens»
- **Qué es:** Headroom, capa de compresión de contexto para agentes y LLM de Headroom Labs (paquete `headroom-ai` en PyPI y npm). Licencia Apache-2.0. Es muy activo (~80k estrellas, v0.44.0).
- **Cuándo elegirlo:** Casos: Reducir salidas extensas de herramientas; Comparar una sesión con y sin compresión.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python compatible; contenido de prueba; agente o cliente MCP si lo conectas; hardware prerequisites; API de IA: opcional; Python compatible; contenido de prueba; agente o cliente MCP si lo conectas.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install headroom-ai` — fuente: https://github.com/headroomlabs-ai/headroom/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Comprime una salida JSON pequeña y compara el resultado con el original antes de envolver un agente Éxito: Puedes identificar qué se conservó y recuperar el original cuando corresponda
- **Combina con:** `claude-code` [20/terminal], `litellm` [23/serving], `context-engineering` [19/guias], `codegraph` [7/codigo], `claude-code-usage-monitor` [23/observabilidad], `mimo-code` [20/terminal]
- **Alternativas:** `rtk`
- **Riesgos y avisos:** Alternativas (elige una): rtk. El número de estrellas crece de forma inusual para un proyecto tan joven; los ahorros son mediciones del propio proyecto. Documenta wrap para Claude y Codex y MCP para cualquier cliente compatible; los ahorros de benchmarks no garantizan iguales respuestas en toda tarea.

### GPTCache (`gptcache`)

- **Repo:** https://github.com/zilliztech/GPTCache · MIT · nivel 2 · 58/100
- **Qué es:** Reutiliza respuestas de consultas parecidas a un modelo mediante una caché semántica con reglas de comparación configurables.
- **Cuándo elegirlo:** Casos: Evitar recalcular preguntas repetidas en un prototipo.; Comparar falsos aciertos de caché con dos preguntas casi iguales.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, Makefile, requirements.txt, setup.py; API de IA: opcional; Python y un componente de embeddings y almacenamiento compatible; entorno de prueba con consultas ficticias..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://gptcache.readthedocs.io
- **Primera prueba propuesta (no ejecutada):** Configura el ejemplo en un entorno aislado y manda dos consultas de ejemplo similares. Éxito: Puedes observar cuándo se reutiliza una respuesta y cuándo se vuelve a calcular.
- **Riesgos y avisos:** Los ejemplos con OpenAI requieren su clave. No compartas entradas y respuestas privadas entre usuarios de distintas cuentas.

### LLMLingua (`llmlingua`)

- **Repo:** https://github.com/microsoft/LLMLingua · MIT · nivel 2 · 48/100
- **Qué es:** Acorta texto de entrada para modelos de lenguaje y permite medir cuánto contexto conservas antes de enviar el prompt.
- **Cuándo elegirlo:** Casos: Comparar un prompt largo con su versión comprimida.; Medir tokens ahorrados y revisar si mantuvo una restricción importante.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, Makefile, pyproject.toml, setup.py; hardware model_dependent; API de IA: no; Python, PyTorch y un modelo de compresión compatible con el hardware..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://llmlingua.com/
- **Primera prueba propuesta (no ejecutada):** Comprime un texto público breve con un modelo local pequeño del proyecto. Éxito: Obtienes dos textos y puedes comparar tamaño, instrucciones conservadas y pérdidas.
- **Riesgos y avisos:** Menos tokens no garantiza la misma calidad; si después llamas a un LLM remoto, su tarifa es independiente.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-23-tokens.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Ahorro de contexto y tokens», lee `docs/alexandria/categoria-23-tokens.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-23-tokens.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
