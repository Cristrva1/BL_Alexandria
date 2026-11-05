# Brief de redacción — BL_Alexandria (biblioteca curada de repos de IA)

Contexto: BL_Alexandria es una biblioteca en **español** que ayuda a personas y agentes de IA a
elegir repositorios de IA/automatización para un proyecto. Cada repo tiene una ficha que se
muestra en catálogos, páginas por categoría, un explorador web y un menú para agentes.
Hoy muchas fichas tienen textos en inglés copiados del README, frases rotas o categorías
equivocadas. Tu trabajo: dejar cada repo de tu paquete con una ficha **precisa, clara y en
español natural**.

Fecha de referencia: 2026-11-05. Los datos de GitHub del paquete (`github`) son reales y de hoy:
úsalos como ancla de verdad. Si el texto editorial previo contradice a GitHub, gana GitHub.

## Fuentes que debes usar

1. `github` del paquete: descripción oficial, topics, licencia, lenguaje, actividad, archivado.
2. `editorial` (si existe): prosa en español ya escrita a mano. Consérvala si es correcta;
   recórtala, corrígela o reescríbela si es imprecisa.
3. `current`: datos viejos del índice. Úsalos solo como pista: muchos `one`/`desc` son basura
   (anuncios de sponsors, avisos de cripto, listas de enlaces, texto en chino/inglés).
4. **README real**: para repos `is_new: true`, y para cualquier repo donde dudes (instalación,
   qué hace exactamente), consulta el README con WebFetch:
   `https://raw.githubusercontent.com/<owner>/<repo>/HEAD/README.md` (si falla, prueba
   `https://github.com/<owner>/<repo>`). No inventes funciones ni comandos.

## Salida

Escribe **un archivo JSON por repo** en el directorio de salida de tu paquete:
`<OUT_DIR>/<id>.json` (el id exacto que te dan; no lo cambies). Escríbelos a medida que avanzas
(no al final), así el trabajo no se pierde. Formato (todas las claves obligatorias salvo
indicación):

```json
{
  "id": "open-webui",
  "name": "Open WebUI",
  "role": "app",
  "exec": "local",
  "setup": "easy",
  "mcp": true,
  "prov": ["openai", "local"],
  "tags": ["local", "chatbot", "rag", "python", "docker"],
  "one": "Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas.",
  "desc": "2-3 frases: qué es, qué problema resuelve y para quién.",
  "why": "1-2 frases: por qué destaca frente a alternativas (enfoque, adopción, calidad).",
  "how": "1-2 frases: cómo funciona por dentro (arquitectura, mecanismo clave).",
  "install": "Comando real y corto, p. ej. `docker run -d -p 3000:8080 ghcr.io/open-webui/open-webui:main` o `pip install open-webui`.",
  "cases": ["Caso concreto 1", "Caso concreto 2", "Caso concreto 3"],
  "stack": "Python, Svelte, Docker",
  "models": "Qué LLM/API usa en ejecución, p. ej. 'Agnóstico: Ollama o cualquier API compatible con OpenAI.' o 'No usa LLM.'",
  "choose_if": "Condición clara para elegirlo (p. ej. 'necesitas un ChatGPT privado para tu equipo con modelos locales').",
  "avoid_if": "Condición para no elegirlo, mencionando la alternativa si aplica (p. ej. 'solo quieres una app de escritorio individual; mira `jan`').",
  "limits": "1 frase con la limitación real más importante, o \"\" si no hay nada relevante.",
  "combines_with": ["ollama", "litellm"],
  "alternatives": ["lobehub", "librechat"],
  "pick": true,
  "notes": "Opcional: dudas o avisos para el integrador (renombrado, archivado, etc.)."
}
```

## Reglas de estilo (obligatorias)

- Español neutro, tuteo, frases cortas y concretas. Nada de hype: prohibido "potente",
  "revolucionario", "increíble", "mágico", "el mejor", "game changer". Sin emojis.
- Términos técnicos en inglés solo cuando son el nombre usual (RAG, prompt, webhook, self-host,
  embeddings, fine-tuning, MCP, CLI, SDK). No traduzcas nombres de producto.
- **`one`** (lo más importante: se lee en tablas): una sola frase de 60-130 caracteres que
  empiece por un sustantivo que diga QUÉ es ("Plataforma…", "Librería…", "CLI…", "Servidor MCP…",
  "Agente de código…", "Colección de skills…") y termine con punto. Debe decir el valor
  distintivo, no genéricos. Mal: "Herramienta potente para IA." Bien: "Motor de workflows visual
  con 400+ integraciones y nodos de IA, auto-hospedable con Docker."
- **`desc`**: 2-3 frases, máx. ~420 caracteres. No repitas literalmente `one`.
- **`why`**, **`how`**: 1-2 frases cada uno, máx. ~280 caracteres. No cites números de estrellas
  (ya los mostramos aparte).
- **`install`**: el método oficial más directo del README (pip/uv/npm/npx/docker/brew/curl, o
  descarga de releases para apps). Comandos entre backticks. Si hay paso imprescindible (p. ej.
  descargar un modelo, variable de entorno), añádelo en pocas palabras. Para skills/plugins de
  Claude Code: el comando de marketplace/plugin si existe o `git clone` a la carpeta de skills.
  Para catálogos/cursos: "No se instala: abre el repo y copia lo que necesites."
- **`cases`**: exactamente 3 frases cortas (≤ 70 caracteres cada una), concretas.
- **`choose_if`/`avoid_if`**: una frase cada uno, sin punto final, empezando en minúscula
  ("necesitas…", "buscas…", "ya usas…", "tu equipo…"). Para mencionar otro repo usa su id entre
  backticks (`firecrawl`). **Nunca** uses enlaces markdown `[x](y)` en ningún campo.
- **`limits`**: honesto (licencia restrictiva, archivado, requiere GPU, ToS, etc.) o "".
- **`stack`**: lenguajes/tecnologías principales separados por comas (3-6 elementos).
- **`name`**: nombre visible con su capitalización oficial (`LangGraph`, `llama.cpp`, `n8n`).

## Clasificación (campos cortos)

- `role`: `platform` (producto completo con UI y backend que despliegas) · `runtime`
  (motor/framework que ejecuta lógica: frameworks de agentes, motores de inferencia, agentes de
  código) · `library` (lo importas desde tu código) · `skill` (instrucciones, skills, prompts o
  plugins para un agente) · `directory` (lista curada, catálogo, curso o cookbook) · `app`
  (aplicación de escritorio, CLI o web para usuario final).
- `exec`: `local` (corre en tu máquina sin servicio externo obligatorio) · `cloud` (depende de
  una API o servicio remoto) · `hybrid` (funciona de ambas formas).
- `setup`: `easy` (un comando o paquete) · `medium` (configurar servicios, credenciales o varias
  piezas) · `heavy` (GPU, infraestructura multi-servicio o compilación).
- `mcp`: true solo si expone o consume Model Context Protocol de forma nativa/documentada.
- `prov`: proveedores LLM que usa en ejecución, de este vocabulario: `openai`, `anthropic`,
  `google`, `local` (Ollama/llama.cpp/modelos locales), `mcp`. `[]` si no usa LLM o no aplica.
- `tags`: 3-6 en total. 2-4 funcionales de este vocabulario: whatsapp, automation, agents,
  coding-agent, mcp, scraping, browser, research, search, llmops, memory, rag, vector-db,
  inference, local, ui, design, dataviz, analytics, image, vision, audio, tts, stt, video, docs,
  ocr, pdf, slides, code, training, data, notebooks, email, notifications, crm, chatbot, skills,
  prompts, learning, security, evaluation, observability. Más 1-2 técnicos: python, typescript,
  javascript, go, rust, java, ruby, php, cpp, docker, postgres, react.
- `combines_with`: 2-4 ids que se usan JUNTO a este repo (complementos, no sustitutos). Solo ids
  que existan en `ALL_IDS.json` (puede ser de cualquier categoría; prefiere repos conocidos).
- `alternatives`: 0-3 ids que cumplen LA MISMA función (sustitutos; elegir uno excluye al otro).
  Solo ids de `ALL_IDS.json`. No pongas complementos aquí.
- `pick`: `true` para el repo que recomendarías por defecto en su subcategoría (máx. 1-2 por
  subcategoría dentro de tu paquete). Si no, `false`.

## Casos especiales

- Repos **archivados** (`github.archived: true`): dilo en `limits` y sugiere alternativa en
  `avoid_if`. Repos con `status: "missing"`: el repo ya no existe en GitHub; escribe la ficha
  con lo que haya y pon en `limits` "El repositorio original ya no está disponible en GitHub;
  usa tu clon local o la alternativa `x`."
- Repos **renombrados/movidos** (el `gh` difiere del nombre viejo): usa el nombre nuevo y
  menciónalo en `notes`.
- `alias_of` presente: es un duplicado local; ficha mínima que remita al principal.
- Si un repo te parece mal ubicado en su categoría/subcategoría, NO lo muevas: escribe la ficha
  igual y explica en `notes` dónde lo pondrías.

## Calidad

Antes de escribir cada archivo verifica: ¿`one` dice qué es y para qué sirve en una frase?
¿El comando de instalación es real? ¿Todo está en español? ¿`combines_with`/`alternatives` usan
ids válidos? ¿No hay enlaces markdown? Escribe JSON válido (UTF-8, comillas dobles).

Al terminar, responde con un resumen breve: cuántos archivos escribiste, ids con dudas y
cualquier hallazgo importante (repos archivados, renombrados, descripciones previas erróneas).
