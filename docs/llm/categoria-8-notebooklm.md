# Alexandría para agentes · NotebookLM: alternativas y clientes

Categoría 8 «Chats, modelos locales y espacios privados» › subcategoría `notebooklm`. 4 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=8&sub=notebooklm · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `open-notebook` | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes… | 2 Intermedio | 67 | MIT (OSI permisiva) | recomendado |
| `surfsense` | Alternativa abierta y privada a NotebookLM que investiga, transforma y edita… | 2 Intermedio | 62 | Apache-2.0 (OSI permisiva) | alternativa |
| `notebooklm-py` | API Python no oficial para interactuar programáticamente con NotebookLM de… | 2 Intermedio | 59 | MIT (OSI permisiva) | sin grupo |
| `notebooklm-mcp-cli` | CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar… | 1 Básico | 51 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### open-notebook (`open-notebook`)

- **Repo:** https://github.com/lfnovo/open-notebook · MIT · nivel 2 · 67/100 · recomendado en «Alternativas a NotebookLM»
- **Qué es:** Alternativa de código abierto (MIT) a NotebookLM de Google, centrada en la privacidad y creada por Luis Novo (lfnovo). Activa (v1.15.1), con interfaz en 14 idiomas.
- **Cuándo elegirlo:** Casos: Estudiar documentos en una libreta; Generar un resumen o audio sobre material propio.
- **Requisitos:** nivel 2: preparación media; Docker; proveedores de chat, embeddings y audio según función; fuentes de prueba; hardware prerequisites; API de IA: depends; Docker; proveedores de chat, embeddings y audio según función; fuentes de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up -d` — fuente: https://github.com/lfnovo/open-notebook/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un notebook con dos fuentes y pregunta por un dato con referencia Éxito: Puedes identificar la fuente y corregir un resumen
- **Combina con:** `ollama` [8/motores], `vllm` [23/serving], `activepieces` [1/motores], `scientific-agent-skills` [27/dominio], `olmocr` [13/ocr], `vibevoice` [29/tts]
- **Alternativas:** `surfsense`, `deeptutor`
- **Riesgos y avisos:** Alternativas (elige una): deeptutor, surfsense. En redes compartidas pon una contraseña o un proxy delante. La app auto-hospedada no garantiza que todos los datos se procesen localmente: depende de cada proveedor que selecciones.

### SurfSense (`surfsense`)

- **Repo:** https://github.com/MODSetter/SurfSense · Apache-2.0 · nivel 2 · 62/100 · alternativa en «Alternativas a NotebookLM»
- **Qué es:** Aplicación de escritorio de código abierto (Apache 2.0) de MODSetter, alternativa a NotebookLM que puede funcionar sin conexión («air-gapped») para documentos que no puedes subir.
- **Cuándo elegirlo:** Casos: Revisar un contrato de prueba con comentarios; Extraer datos de un archivo Excel ficticio.
- **Requisitos:** nivel 2: preparación media; Instalador para tu sistema; modelo local o remoto; LibreOffice solo para conversiones Office; hardware prerequisites; API de IA: depends; Instalador para tu sistema; modelo local o remoto; LibreOffice solo para conversiones Office.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -fsSL https://raw.githubusercontent.com/MODSetter/SurfSense/main/docker/scripts/install.sh \| bash` — fuente: https://github.com/MODSetter/SurfSense/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Añade un documento ficticio y pide una edición que se guarde como copia Éxito: Puedes comparar original y archivo nuevo y revisar las citas
- **Combina con:** `ollama` [8/motores], `vllm` [23/serving], `playwright-mcp` [5/servidores]
- **Alternativas:** `open-notebook`, `khoj`
- **Riesgos y avisos:** Alternativas (elige una): open-notebook, khoj. El índice puede permanecer local aunque el modelo sea remoto; LibreOffice no viene incluido para las conversiones Office.

### notebooklm-py (`notebooklm-py`)

- **Repo:** https://github.com/teng-lin/notebooklm-py · MIT · nivel 2 · 59/100
- **Qué es:** API de Python no oficial y skill para agentes para Google NotebookLM, rebautizado como Gemini Notebook en julio de 2026, creada por teng-lin. MIT y muy activa (v0.8.6); usa APIs no documentadas de Google que pueden cambiar sin aviso y no…
- **Cuándo elegirlo:** Casos: Automatizar consultas documentales; Exportar mapas o resúmenes propios.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python y uv o pipx; sesión Google; Chromium para login; notebook de prueba; hardware prerequisites; API de IA: no; Python y uv o pipx; sesión Google; Chromium para login; notebook de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `uv tool install "notebooklm-py[browser]"` — fuente: https://github.com/teng-lin/notebooklm-py/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un notebook con una fuente propia breve y pregunta por un dato verificable Éxito: La consulta y las referencias aparecen en el mismo notebook de Google
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `obsidian-second-brain` [15/notas]
- **Riesgos y avisos:** Se retiró la combinación con notebooklm-mcp-cli: ambos son clientes no oficiales de la misma API y se solapan; elige uno. API no oficial con endpoints que pueden cambiar; los archivos descargados quedan locales pero la generación ocurre en Google.

### notebooklm-mcp-cli (`notebooklm-mcp-cli`)

- **Repo:** https://github.com/jacob-bd/gemini-notebook-mcp-cli · MIT · nivel 1 · 51/100
- **Qué es:** CLI y servidor MCP no oficiales para Gemini Notebook (antes Google NotebookLM), de jacob-bd. MIT y muy activo (v0.16.5); el repositorio se renombró a `gemini-notebook-mcp-cli`.
- **Cuándo elegirlo:** Casos: Administrar fuentes desde un agente; Exportar contenido generado por NotebookLM.
- **Requisitos:** nivel 1: preparación sencilla; Python; cuenta Google; cliente MCP; sesión del navegador; hardware prerequisites; API de IA: no; Python; cuenta Google; cliente MCP; sesión del navegador.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install notebooklm-mcp-cli` — fuente: https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta el asistente de setup, conecta un cliente y consulta una fuente ficticia en un notebook de prueba Éxito: Puedes contrastar la respuesta y comprobar el estado de autenticación
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `gemini-cli` [20/terminal]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Activa el almacenamiento protegido en equipos personales. Se retiraron las combinaciones con notebooklm-py (solapamiento) y awesome-mcp-servers (es una lista…. Documenta los tres clientes; instalar CLI o MCP no vuelve local la generación ni evita los cupos de NotebookLM.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-8-notebooklm.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «NotebookLM: alternativas y clientes», lee `docs/alexandria/categoria-8-notebooklm.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-8-notebooklm.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
