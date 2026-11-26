# Alexandría para agentes · Escritura y calidad de texto

Categoría 27 «Skills de diseño, contenido y especialidades» › subcategoría `escritura`. 4 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=27&sub=escritura · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `humanizer` | Skill para revisar estilo y claridad de texto conservando su sentido; no prueba… | 1 Básico | 72 | MIT (OSI permisiva) | recomendado |
| `i-have-adhd` | Skill para que un agente presente primero la respuesta y organice su salida con… | 2 Intermedio | 67 | MIT (OSI permisiva) | sin grupo |
| `no-ai-slop` | Skill para revisar escritura y eliminar patrones repetitivos o frases poco… | 2 Intermedio | 55 | MIT (OSI permisiva) | alternativa |
| `stop-slop` | Skill con reglas para eliminar las señales de escritura IA: frases prohibidas… | 1 Básico | 40 | MIT (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Humanizer (`humanizer`)

- **Repo:** https://github.com/blader/humanizer · MIT · nivel 1 · 72/100 · recomendado en «Skills para quitar el tono de IA a los textos»
- **Qué es:** Skill de escritura de código abierto (MIT) de blader que hace que un texto escrito por IA suene a persona sin cambiar su contenido. Muy popular y activa (v4.0.0); el README lleva un patrocinio.
- **Cuándo elegirlo:** Casos: Mejorar claridad de un correo; Revisar prosa repetitiva.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Agente con skills; texto propio breve; hardware prerequisites; API de IA: no; Agente con skills; texto propio breve.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add blader/humanizer --global --agent codex` — fuente: https://github.com/blader/humanizer/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Revisa un párrafo y compara la versión propuesta con los hechos y tono del original Éxito: Puedes aceptar cambios de estilo sin alterar el contenido
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `marketingskills` [27/dominio], `postiz-app` [18/marketing]
- **Alternativas:** `no-ai-slop`, `stop-slop`
- **Riesgos y avisos:** Alternativas (elige una): no-ai-slop, stop-slop. Documenta Claude Code, Codex y otros hosts de skills; mejorar estilo no demuestra autoría humana ni garantiza pasar detectores.

### i-have-adhd (`i-have-adhd`)

- **Repo:** https://github.com/ayghri/i-have-adhd · MIT · nivel 2 · 67/100
- **Qué es:** Skill/plugin de código abierto (MIT) de ayghri que hace las respuestas de los asistentes de código más directas («apto para TDAH, sin diagnóstico necesario»). Popular y activo (v0.4.1).
- **Cuándo elegirlo:** Casos: Reducir distracciones en instrucciones; Organizar una explicación de trabajo.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente soportado; preferencia personal de presentación; hardware prerequisites; API de IA: no; Agente soportado; preferencia personal de presentación.
- **Instalación (documentada en la fuente; no ejecutada):** `claude plugin install i-have-adhd@i-have-adhd` — fuente: https://github.com/ayghri/i-have-adhd/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Activa el skill y pide explicar cómo crear una carpeta vacía para comparar la estructura de respuesta Éxito: Puedes reconocer una respuesta directa y pasos delimitados
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `gemini-cli` [20/terminal]
- **Riesgos y avisos:** INSTALL.md documenta Claude Code, Codex y Antigravity CLI; la activación y always-on difieren entre hosts; es formato de comunicación, no intervención médica.

### no-ai-slop (`no-ai-slop`)

- **Repo:** https://github.com/petergyang/no-ai-slop · MIT · nivel 2 · 55/100 · alternativa en «Skills para quitar el tono de IA a los textos»
- **Qué es:** Skill de escritura de código abierto (MIT) de Peter Yang. Activa (v1.0.6).
- **Cuándo elegirlo:** Casos: Editar una publicación; Mejorar claridad de un informe.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP); Agente compatible; texto propio; hardware prerequisites; API de IA: no; Agente compatible; texto propio.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add petergyang/no-ai-slop --skill no-ai-slop --global --yes` — fuente: https://github.com/petergyang/no-ai-slop/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Revisa un texto corto y contrasta cada cambio con el sentido y voz originales Éxito: Puedes aceptar correcciones concretas sin perder información
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `marketingskills` [27/dominio]
- **Alternativas:** `humanizer`, `stop-slop`
- **Riesgos y avisos:** Alternativas (elige una): humanizer, stop-slop. Tiene metadatos de plugins para ChatGPT y Codex y formato de skill portable; no garantiza detección o invisibilidad de escritura AI.

### Stop Slop (`stop-slop`)

- **Repo:** https://github.com/hardikpandya/stop-slop · MIT · nivel 1 · 40/100 · alternativa en «Skills para quitar el tono de IA a los textos»
- **Qué es:** Skill de código abierto (MIT) de Hardik Pandya para eliminar marcas de IA en la prosa. Sin releases y con último cambio en marzo de 2026.
- **Cuándo elegirlo:** Casos: Reducir frases vagas; Revisar un borrador antes de publicarlo.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Claude con skills o instrucciones pegadas en otro modelo; texto propio; hardware prerequisites; API de IA: no; Claude con skills o instrucciones pegadas en otro modelo; texto propio.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/hardikpandya/stop-slop/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Aplica la lista de frases a un párrafo y conserva cualquier término técnico necesario Éxito: Puedes justificar cada cambio de redacción
- **Combina con:** `claude-code` [20/terminal], `marketingskills` [27/dominio], `postiz-app` [18/marketing]
- **Alternativas:** `humanizer`, `no-ai-slop`
- **Riesgos y avisos:** Alternativas (elige una): no-ai-slop, humanizer. Sus reglas son estrictas (por ejemplo, elimina todos los adverbios) y pueden aplanar el estilo. Documenta instalación en Claude Code y uso de instrucciones en otros LLM; no acredita plugins específicos para Codex o Antigravity.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-27-escritura.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Escritura y calidad de texto», lee `docs/alexandria/categoria-27-escritura.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-27-escritura.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
