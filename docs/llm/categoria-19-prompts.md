# Alexandría para agentes · Prompts y prompt engineering

Categoría 19 «Aprender IA y escribir mejores prompts» › subcategoría `prompts`. 7 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=19&sub=prompts · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `prompts-chat` | La colección comunitaria de prompts más grande (antes Awesome ChatGPT Prompts)… | 1 Básico | 69 | MIT (código) + CC0-1.0 (prompts) (OSI permisiva) | recomendado |
| `fabric` | CLI con cientos de patrones de prompts para resumir, extraer y transformar… | 1 Básico | 63 | MIT (OSI permisiva) | alternativa |
| `system-prompts-and-models-of-ai-tools` | Colección de prompts y configuraciones atribuidos a herramientas de IA para… | 1 Básico | 58 | GPL-3.0 (OSI copyleft) | sin grupo |
| `prompt-engineering-guide` | Guía de referencia de DAIR.AI sobre prompts, ingeniería de contexto, RAG y… | 1 Básico | 56 | MIT (OSI permisiva) | sin grupo |
| `prompt-master` | Skill de Claude que ayuda a formular encargos para distintas herramientas de… | 1 Básico | 51 | MIT (OSI permisiva) | sin grupo |
| `chatgpt-system-prompt` | Colección de prompts de GPT y recursos sobre instrucciones de sistema y… | 1 Básico | 50 | MIT (OSI permisiva) | sin grupo |
| `chatgpt-dan` | Archivo de prompts históricos de roleplay y jailbreak atribuidos a versiones… | 1 Básico | 30 | — (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### prompts.chat (`prompts-chat`)

- **Repo:** https://github.com/f/prompts.chat · MIT (código) + CC0-1.0 (prompts) · nivel 1 · 69/100 · recomendado en «Colecciones de prompts»
- **Qué es:** La biblioteca de prompts open source más grande, mantenida por Fatih Kadir Akın (f), antes conocida como 'Awesome ChatGPT Prompts' (diciembre de 2022).
- **Cuándo elegirlo:** Casos: Encontrar una plantilla para estudiar; Compartir una biblioteca interna de prompts.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador para explorar; Node y cliente MCP si conectas la biblioteca; hardware prerequisites; API de IA: no; Navegador para explorar; Node y cliente MCP si conectas la biblioteca.
- **Instalación (documentada en la fuente; no ejecutada):** `/plugin marketplace add f/prompts.chat` — fuente: https://github.com/f/prompts.chat/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Busca un prompt de resumen y adapta sus variables a una nota propia antes de probarlo en tu asistente Éxito: Puedes identificar tarea, datos de entrada y formato esperado
- **Combina con:** `claude-code` [20/terminal], `promptfoo` [23/observabilidad], `open-webui` [8/chats]
- **Alternativas:** `fabric`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): fabric. Documenta plugin para Claude Code y MCP remoto o local estándar para clientes compatibles; las herramientas de escritura necesitan permisos propios.

### Fabric (`fabric`)

- **Repo:** https://github.com/danielmiessler/Fabric · MIT · nivel 1 · 63/100 · alternativa en «Colecciones de prompts»
- **Qué es:** Framework open source (MIT) de Daniel Miessler para aumentar capacidades humanas con IA, organizado en torno a 'patterns' (prompts reutilizables por tarea). Es muy activo (v1.4.576, publicaciones casi diarias) y maduro.
- **Cuándo elegirlo:** Casos: Extraer acciones de una reunión; Convertir notas en un esquema de artículo.
- **Requisitos:** nivel 1: preparación sencilla; Go o instalador para tu sistema; proveedor o CLI autenticado; texto breve propio; hardware prerequisites; API de IA: opcional; Go o instalador para tu sistema; proveedor o CLI autenticado; texto breve propio.
- **Instalación (documentada en la fuente; no ejecutada):** `go install github.com/danielmiessler/fabric/cmd/fabric@latest` — fuente: https://github.com/danielmiessler/Fabric/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Configura un proveedor y aplica un patrón de resumen a una nota breve que ya conozcas Éxito: Obtienes un resumen que puedes contrastar con la nota original
- **Combina con:** `ollama` [8/motores], `yt-dlp` [4/social], `open-webui` [8/chats]
- **Alternativas:** `prompts-chat`
- **Riesgos y avisos:** Alternativas (elige una): prompts-chat. Ojo: el uso de OAuth de suscripción vía backend privado puede contravenir los términos del proveedor [DATO NO…. Las rutas de suscripción son adaptadores del proyecto; Codex usa un backend privado y no garantiza continuidad ni cobertura de todo plan.

### system-prompts-and-models-of-ai-tools (`system-prompts-and-models-of-ai-tools`)

- **Repo:** https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools · GPL-3.0 · nivel 1 · 58/100
- **Qué es:** Colección (GPL-3.0) de @x1xhlol con system prompts, definiciones de herramientas y modelos atribuidos a herramientas de IA comerciales como Cursor, Devin, v0, Lovable o Windsurf. Es muy popular (~145k estrellas).
- **Cuándo elegirlo:** Casos: Estudiar instrucciones de herramientas de código; Preparar una plantilla propia de sistema.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; interés en diseño de instrucciones; hardware prerequisites; API de IA: no; Navegador; interés en diseño de instrucciones.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Compara dos estructuras atribuidas a asistentes y anota sus diferencias sin introducirlas como configuración oficial Éxito: Puedes distinguir patrones de diseño de afirmaciones no verificadas de procedencia
- **Combina con:** `chatgpt-system-prompt`, `promptfoo` [23/observabilidad], `claude-code` [20/terminal], `chatgpt-dan`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Contenido de procedencia no verificada. Las atribuciones son del recopilador; listar Claude Code o Codex no equivale a un plugin compatible ni autentica su configuración interna.

### Prompt Engineering Guide (`prompt-engineering-guide`)

- **Repo:** https://github.com/dair-ai/Prompt-Engineering-Guide · MIT · nivel 1 · 56/100
- **Qué es:** Guía de referencia de DAIR.AI (MIT) sobre ingeniería de prompts, con versión web en promptingguide.ai. Es material educativo, no software para instalar.
- **Cuándo elegirlo:** Casos: Aprender a pedir un resumen estructurado; Comparar técnicas de prompting antes de elegir una.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; pregunta de ejemplo; hardware prerequisites; API de IA: no; Navegador; pregunta de ejemplo.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Lee la sección de ejemplos y reformula una petición de resumen indicando formato y audiencia Éxito: Puedes explicar qué información añadiste y por qué
- **Combina con:** `prompt-master`, `context-engineering` [19/guias], `promptfoo` [23/observabilidad], `chatgpt-system-prompt`, `claude-cookbooks` [19/guias]
- **Riesgos y avisos:** Es una referencia y no un programa que se instala; los resultados de un modelo no garantizan el mismo resultado en otro.

### prompt-master (`prompt-master`)

- **Repo:** https://github.com/nidhinjs/prompt-master · MIT · nivel 1 · 51/100
- **Qué es:** Skill para Claude (MIT) de nidhinjs que redacta prompts optimizados para otras herramientas de IA. Es un proyecto individual y reciente (último push en octubre de 2026), sin releases.
- **Cuándo elegirlo:** Casos: Redactar un encargo de programación; Preparar un prompt de imagen con requisitos concretos.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Claude con skills o Claude Code; descripción de una tarea; hardware prerequisites; API de IA: no; Claude con skills o Claude Code; descripción de una tarea.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/nidhinjs/prompt-master/blob/main/README.md

  ```bash
  mkdir -p ~/.claude/skills
  git clone https://github.com/nidhinjs/prompt-master.git ~/.claude/skills/prompt-master
  ```
- **Primera prueba propuesta (no ejecutada):** Pide al skill que formule preguntas para redactar un prompt de una página de reservas Éxito: El prompt especifica objetivo, contexto, restricciones y criterio de aceptación
- **Combina con:** `claude-code` [20/terminal], `prompt-engineering-guide`, `anthropic-skills` [2/catalogos]
- **Riesgos y avisos:** Sin alternativas declaradas. Combinación anterior con andrej-karpathy-skills eliminada: sin relación documentada. La instalación documentada es para Claude y Claude Code; Codex y Antigravity aparecen como destinos del prompt generado y no prueban instalación nativa en….

### chatgpt_system_prompt (`chatgpt-system-prompt`)

- **Repo:** https://github.com/LouisShark/chatgpt_system_prompt · MIT · nivel 1 · 50/100
- **Qué es:** Colección (MIT) de @LouisShark, llamada 'PromptCraft', con system prompts de ChatGPT, de otros productos de IA y de miles de GPTs personalizados. Es activa (último push en noviembre de 2026).
- **Cuándo elegirlo:** Casos: Aprender estructura de instrucciones; Diseñar límites para un asistente propio.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; ejemplo propio de instrucciones; hardware prerequisites; API de IA: no; Navegador; ejemplo propio de instrucciones.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/LouisShark/chatgpt_system_prompt/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Compara una plantilla del archivo con una instrucción de tu autoría y separa objetivo, restricciones y formato Éxito: Puedes identificar patrones sin asumir autenticidad de prompts atribuidos
- **Combina con:** `system-prompts-and-models-of-ai-tools`, `promptfoo` [23/observabilidad], `prompt-engineering-guide`, `chatgpt-dan`
- **Riesgos y avisos:** Sin alternativas declaradas. Colección comunitaria educativa; atribuciones o extracciones no son documentación oficial ni garantías sobre productos actuales.

### ChatGPT_DAN (`chatgpt-dan`)

- **Repo:** https://github.com/0xk1h0/ChatGPT_DAN · — · nivel 1 · 30/100
- **Qué es:** Archivo de prompts de 'jailbreak' (DAN y otros) para ChatGPT, mantenido por @0xk1h0. No tiene licencia declarada. Es contenido histórico: la última nota de funcionamiento del README es de julio de 2023 (DAN 12.0 con GPT-3.5), aunque el…
- **Cuándo elegirlo:** Casos: Estudiar la historia de prompts de roleplay; Reconocer intentos de manipulación de instrucciones.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; criterio de lectura histórica; hardware prerequisites; API de IA: no; Navegador; criterio de lectura histórica.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/0xk1h0/ChatGPT_DAN/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Lee el aviso de fecha y analiza cómo un prompt intenta sustituir las instrucciones del sistema sin aplicarlo a servicios ajenos Éxito: Puedes explicar por qué no constituye una configuración soportada
- **Combina con:** `promptfoo` [23/observabilidad], `system-prompts-and-models-of-ai-tools`, `chatgpt-system-prompt`
- **Riesgos y avisos:** Sin alternativas declaradas. Contenido de jailbreak sin licencia: solo para investigación defensiva. Las afirmaciones de funcionamiento se refieren a GPT-3.5 en 2023 y no prueban eficacia ni compatibilidad actual.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-19-prompts.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Prompts y prompt engineering», lee `docs/alexandria/categoria-19-prompts.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-19-prompts.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
