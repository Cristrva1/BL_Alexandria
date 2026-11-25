# Alexandría para agentes · Workspaces privados y segundos cerebros

Categoría 8 «Chats, modelos locales y espacios privados» › subcategoría `workspaces`. 6 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=8&sub=workspaces · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `anything-llm` | App todo en uno para chatear con tus documentos y usar agentes con modelos… | 1 Básico | 78 | MIT (OSI permisiva) | recomendado |
| `odysseus` | Workspace auto-hospedado que unifica chats, research, documentos, correo… | 3 Avanzado | 73 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `private-gpt` | Capa de API completa para apps de IA privadas sobre modelos locales: RAG… | 2 Intermedio | 67 | Apache-2.0 (OSI permisiva) | alternativa |
| `hermes-desktop` | App de escritorio que envuelve al agente Hermes en una interfaz nativa. | 1 Básico | 54 | MIT (OSI permisiva) | sin grupo |
| `khoj` | Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con… | 2 Intermedio | 48 | AGPL-3.0 (OSI copyleft) | alternativa |
| `claude-second-brain` | Organiza una bóveda de Obsidian para que Claude Code consulte y mantenga notas… | 2 Intermedio | — | MIT | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### AnythingLLM (`anything-llm`)

- **Repo:** https://github.com/Mintplex-Labs/anything-llm · MIT · nivel 1 · 78/100 · recomendado en «Workspaces privados con documentos y chat»
- **Qué es:** Aplicación de IA «todo en uno» de código abierto (MIT) de Mintplex Labs, con versión de escritorio (Mac, Windows, Linux), Docker multiusuario, instancia alojada y app Android. Madura y activa (v1.19.0).
- **Cuándo elegirlo:** Casos: Consultar documentación propia; Separar bases de conocimiento por proyecto.
- **Requisitos:** nivel 1: preparación sencilla; App de escritorio o Docker; LLM y embeddings; documento de prueba; hardware prerequisites; API de IA: opcional; App de escritorio o Docker; LLM y embeddings; documento de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un workspace con un PDF corto y consulta un dato presente en él Éxito: Puedes abrir el fragmento que apoya la respuesta
- **Combina con:** `ollama` [8/motores], `qdrant` [6/vectores], `litellm` [23/serving], `localai` [8/motores], `chroma` [6/vectores], `milvus` [6/vectores]
- **Alternativas:** `private-gpt`, `khoj`, `open-webui`, `onyx`
- **Riesgos y avisos:** Alternativas (elige una): open-webui, khoj, private-gpt, onyx. Desktop, Docker y móvil tienen capacidades y licencias que debes comprobar; elige también embeddings locales para una ruta privada completa.

### odysseus (`odysseus`)

- **Repo:** https://github.com/odysseus-dev/odysseus · AGPL-3.0 · nivel 3 · 73/100
- **Qué es:** Espacio de trabajo de IA autoalojado de código abierto (AGPL-3.0) de odysseus-dev que reúne chat, agentes, investigación, documentos, correo, notas, calendario y flujos con modelos locales.
- **Cuándo elegirlo:** Casos: Organizar notas y tareas con IA; Comparar respuestas de modelos desde un workspace.
- **Requisitos:** nivel 3: preparación pesada, varios servicios con Docker Compose; Docker; configuración .env; proveedor o modelos locales; hardware prerequisites; API de IA: depends; Docker; configuración .env; proveedor o modelos locales.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/odysseus-dev/odysseus/blob/dev/README.md

  ```bash
  git clone https://github.com/odysseus-dev/odysseus.git
  cd odysseus
  cp .env.example .env
  docker compose up -d --build
  ```
- **Primera prueba propuesta (no ejecutada):** Abre un chat con un texto ficticio y prueba el editor de documentos sin conectar correo real Éxito: Puedes distinguir conversación, documento y herramientas habilitadas
- **Combina con:** `ollama` [8/motores], `vllm` [23/serving], `playwright-mcp` [5/servidores]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Mantén `AUTH_ENABLED=true` y `LOCALHOST_BYPASS=false` en cualquier despliegue en red. ChromaDB y SearXNG ya vienen en su Compose. Local/API describe el modelo elegido; conservar la app en tu servidor no impide enviar datos a un proveedor remoto.

### PrivateGPT (`private-gpt`)

- **Repo:** https://github.com/zylon-ai/private-gpt · Apache-2.0 · nivel 2 · 67/100 · alternativa en «Workspaces privados con documentos y chat»
- **Qué es:** Capa de API de código abierto (Apache 2.0) de Zylon que convierte modelos locales en aplicaciones de IA para producción; es la base de la plataforma on-premise Zylon. Versión 1.0.1 publicada en 2026.
- **Cuándo elegirlo:** Casos: Construir una API privada sobre documentos; Usar un modelo local como backend de programación.
- **Requisitos:** nivel 2: preparación media; Servidor LLM compatible OpenAI; Python 3.11 o distribución adecuada; documentos de prueba; hardware prerequisites; API de IA: depends; Servidor LLM compatible OpenAI; Python 3.11 o distribución adecuada; documentos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install private-gpt` — fuente: https://github.com/zylon-ai/private-gpt/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta el servidor local y consulta un documento breve con la API de RAG Éxito: Puedes seguir la consulta y comprobar el fragmento recuperado
- **Combina con:** `ollama` [8/motores], `vllm` [23/serving], `llama-cpp` [8/motores]
- **Alternativas:** `anything-llm`, `khoj`
- **Riesgos y avisos:** Alternativa (elige una): anything-llm. La combinación antigua con qdrant se retiró porque el README actual no la menciona. La guía documenta backend local para Claude Code; no confirma por eso integración de todas las funciones de Codex o Antigravity.

### Hermes Desktop (`hermes-desktop`)

- **Repo:** https://github.com/fathah/hermes-desktop · MIT · nivel 1 · 54/100
- **Qué es:** Aplicación de escritorio nativa mantenida por la comunidad (Hermes One, de fathah) para instalar, configurar y usar Hermes Agent de Nous Research. Licencia MIT; en desarrollo activo (v0.7.8), con funciones que pueden cambiar.
- **Cuándo elegirlo:** Casos: Usar Hermes desde una interfaz de escritorio; Consultar una instancia remota de Hermes.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador oficial del proyecto; backend Hermes local o remoto; proveedor o endpoint local; hardware prerequisites; API de IA: depends; Instalador oficial del proyecto; backend Hermes local o remoto; proveedor o endpoint local.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install hermes-desktop` — fuente: https://github.com/fathah/hermes-desktop/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Configura un backend de prueba y confirma la dirección antes de iniciar un chat Éxito: La interfaz muestra el backend y devuelve una respuesta del proveedor elegido
- **Combina con:** `hermes-agent` [21/asistentes], `ollama` [8/motores], `mem0` [6/memoria], `vllm` [23/serving]
- **Riesgos y avisos:** El README sugiere conceder temporalmente sudo sin contraseña en WSL para instalar; revierte el cambio al terminar. Proyecto en desarrollo activo; no hace falta aplicar el ejemplo de sudoers del README para explicar o elegir la ruta de instalación.

### Khoj (`khoj`)

- **Repo:** https://github.com/khoj-ai/khoj · AGPL-3.0 · nivel 2 · 48/100 · alternativa en «Workspaces privados con documentos y chat»
- **Qué es:** Aplicación de IA personal («segundo cerebro») de código abierto (AGPL-3.0) y autoalojable de Khoj, que escala de un uso individual en el dispositivo a IA empresarial.
- **Cuándo elegirlo:** Casos: Consultar notas desde Obsidian; Crear un asistente de investigación personal.
- **Requisitos:** nivel 2: preparación media; Ruta self-host o cuenta Cloud; modelo; notas de prueba; hardware prerequisites; API de IA: depends; Ruta self-host o cuenta Cloud; modelo; notas de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `python -m pip install 'khoj[local]'` — fuente: https://github.com/khoj-ai/khoj/blob/master/documentation/docs/get-started/setup.mdx
- **Primera prueba propuesta (no ejecutada):** Añade dos notas y pregunta por un dato que solo aparece en una Éxito: La respuesta permite revisar la nota utilizada
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `markitdown` [13/conversion]
- **Alternativas:** `anything-llm`, `private-gpt`, `surfsense`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): anything-llm, surfsense. Tiene plugin oficial para Obsidian. El README admite LLM locales y remotos; no mezcles la instalación de Khoj con su proyecto relacionado Pipali.

### Claude Second Brain (`claude-second-brain`)

- **Repo:** https://github.com/jessepinkman9900/claude-second-brain · MIT · nivel 2 · —/100
- **Qué es:** Organiza una bóveda de Obsidian para que Claude Code consulte y mantenga notas con instrucciones y búsqueda local.
- **Cuándo elegirlo:** Casos: Probar una wiki personal con notas ficticias.; Buscar referencias locales a un tema en una bóveda de demostración.
- **Requisitos:** nivel 2: preparación media, se instala dentro de un agente (skill, plugin o MCP), requiere programar con él; JavaScript, package.json; API de IA: no; Claude Code, Obsidian y una bóveda nueva; consulta la guía para qmd y dependencias..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/jessepinkman9900/claude-second-brain/blob/599f55ad50afceb9eae4f31746aa37274087d239/README.md
- **Primera prueba propuesta (no ejecutada):** Prepara una bóveda desechable con tres notas y siembra una consulta a partir del ejemplo. Éxito: El asistente encuentra la nota relevante y muestra qué documento utilizó.
- **Riesgos y avisos:** El inicio instala dependencias y crea archivos. Búsqueda local no significa que el contexto enviado a Claude sea local.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-8-workspaces.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Workspaces privados y segundos cerebros», lee `docs/alexandria/categoria-8-workspaces.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-8-workspaces.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
