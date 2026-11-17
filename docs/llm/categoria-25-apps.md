# Alexandría para agentes · Apps de datos en Python

Categoría 25 «Procesar datos y trabajar con notebooks» › subcategoría `apps`. 6 repos. Generado el 2026-11-16 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=25&sub=apps · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `streamlit` | Framework para levantar apps internas y prototipos de datos desde Python con… | 2 Intermedio | 76 | Apache-2.0 (OSI permisiva) | recomendado |
| `gradio` | Librería Python para crear y compartir apps web de modelos de ML en minutos. | 2 Intermedio | 71 | Apache-2.0 (OSI permisiva) | alternativa |
| `reflex` | Framework para crear aplicaciones web completas (frontend y backend) solo con… | 2 Intermedio | 71 | Apache-2.0 (OSI permisiva) | alternativa |
| `dash` | Framework para construir aplicaciones analíticas interactivas en Python… | 2 Intermedio | 69 | MIT (OSI permisiva) | sin grupo |
| `nicegui` | Framework Python para interfaces web en el navegador con botones, gráficos… | 2 Intermedio | 68 | MIT (OSI permisiva) | alternativa |
| `panel` | Framework de HoloViz para dashboards y apps de datos en Python que funcionan… | 2 Intermedio | 55 | BSD-3-Clause (OSI permisiva) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### streamlit (`streamlit`)

- **Repo:** https://github.com/streamlit/streamlit · Apache-2.0 · nivel 2 · 76/100 · recomendado en «Apps web de datos en Python»
- **Qué es:** Streamlit, framework de apps de datos en Python, propiedad de Snowflake. Licencia Apache-2.0. Es muy maduro (~46k estrellas, 1.67.0) y ahora se presenta como «agent-native».
- **Cuándo elegirlo:** Casos: Preparar un dashboard de ventas ficticias; Explorar un simulador de demanda.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; script pequeño; datos ficticios; hardware prerequisites; API de IA: opcional; Python; script pequeño; datos ficticios.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install streamlit` — fuente: https://github.com/streamlit/streamlit/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una app con un control y una tabla de ejemplo y comprueba que la interacción actualiza la vista Éxito: Puedes identificar script, estado y resultado
- **Combina con:** `dash`, `polars` [25/datos], `duckdb` [25/datos], `awesome-llm-apps` [19/guias], `pygwalker` [25/datos]
- **Alternativas:** `gradio`, `reflex`, `nicegui`, `panel`
- **Riesgos y avisos:** Alternativas (elige una): gradio. Streamlit skills instala instrucciones para Claude Code y agentes que leen .agents; no convierte la suscripción del agente en backend de cualquier app creada.

### Gradio (`gradio`)

- **Repo:** https://github.com/gradio-app/gradio · Apache-2.0 · nivel 2 · 71/100 · alternativa en «Apps web de datos en Python»
- **Qué es:** Gradio, paquete Python para crear demos y apps web de modelos de ML, APIs o cualquier función, mantenido por Hugging Face. Licencia Apache-2.0. Es muy maduro (~44k estrellas, gradio@6.32.0).
- **Cuándo elegirlo:** Casos: Crear una demo de un modelo; Preparar una herramienta interna de texto.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python 3.10+; función o modelo de prueba; hardware prerequisites; API de IA: opcional; Python 3.10+; función o modelo de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install --upgrade gradio` — fuente: https://github.com/gradio-app/gradio/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea una interfaz para una función simple de texto y pruébala localmente antes de compartir un enlace Éxito: Puedes ver la relación entre entrada, función y salida
- **Combina con:** `transformers` [24/entrenamiento], `llama-factory` [24/entrenamiento], `ollama` [8/motores], `rembg` [11/edicion], `f5-tts` [29/tts]
- **Alternativas:** `streamlit`, `reflex`, `nicegui`, `panel`
- **Riesgos y avisos:** Alternativas (elige una): streamlit. Incluye skills para agentes compatibles con .agents y ruta Claude; una URL de compartir expone la app y no sustituye autenticación o alojamiento de producción.

### Reflex (`reflex`)

- **Repo:** https://github.com/reflex-dev/reflex · Apache-2.0 · nivel 2 · 71/100 · alternativa en «Apps web de datos en Python»
- **Qué es:** Framework de código abierto (Apache-2.0) de Reflex Inc. para aplicaciones web full-stack en Python puro. La empresa ofrece además servicios comerciales: AI Builder, alojamiento gestionado y una edición Enterprise.
- **Cuándo elegirlo:** Casos: construir un panel interno o una herramienta con formularios y tablas sin escribir JavaScript; prototipar una app de IA con estado, como un generador de imágenes.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `uv add reflex` — fuente: https://github.com/reflex-dev/reflex/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Crea un proyecto con `uv init`, ejecuta `uv add reflex`, `uv run reflex init` y `uv run reflex run`. Éxito: La app de ejemplo se abre en http://localhost:3000 y se recarga al editar el código.
- **Combina con:** `claude-code` [20/terminal], `pandas` [25/datos], `coolify` [22/infraestructura]
- **Alternativas:** `streamlit`, `gradio`, `nicegui`, `panel`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Es alternativa de Streamlit, Gradio, NiceGUI y Panel: Reflex apunta a apps completas con varias páginas y estado; Streamlit y Gradio a prototipos y demos….

### dash (`dash`)

- **Repo:** https://github.com/plotly/dash · MIT · nivel 2 · 69/100
- **Qué es:** Dash, framework de Plotly para construir apps analíticas web en Python (también R y Julia), sobre Plotly.js, React y Flask. Licencia MIT. Es maduro (~24k estrellas, v4.5.0) y tiene versión comercial (Dash Enterprise).
- **Cuándo elegirlo:** Casos: Crear un tablero interactivo; Comparar escenarios con controles.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; entorno de desarrollo; datos de muestra; hardware prerequisites; API de IA: no; Python; entorno de desarrollo; datos de muestra.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://dash.plotly.com/getting-started
- **Primera prueba propuesta (no ejecutada):** Sigue la app inicial y conecta un selector a un gráfico pequeño Éxito: Puedes comprobar qué callback cambia la figura
- **Combina con:** `streamlit`, `echarts` [10/graficos], `duckdb` [25/datos]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Es un framework Python; el README mezcla ejemplos OSS y funciones Enterprise que no vienen todas con el paquete básico.

### NiceGUI (`nicegui`)

- **Repo:** https://github.com/zauberzeug/nicegui · MIT · nivel 2 · 68/100 · alternativa en «Apps web de datos en Python»
- **Qué es:** Framework de interfaz de código abierto (MIT) creado por Zauberzeug, una empresa alemana de robótica. Activo, con paquetes en PyPI, Docker y conda-forge.
- **Cuándo elegirlo:** Casos: crear un panel de control para un robot o una casa domótica; hacer una pequeña herramienta web para ajustar parámetros de un algoritmo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, docker-compose.yml, package.json, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `python3 -m pip install nicegui` — fuente: https://github.com/zauberzeug/nicegui/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `python3 -m pip install nicegui`, escribe un script con `ui.label` y `ui.button` y ejecútalo con `ui.run()`. Éxito: La interfaz se abre en el navegador (puerto 8080) y se recarga al guardar.
- **Combina con:** `leaflet` [10/geoespacial], `echarts` [10/graficos], `three.js` [26/animacion], `pandas` [25/datos]
- **Alternativas:** `streamlit`, `gradio`, `reflex`, `panel`
- **Riesgos y avisos:** Alternativa de Streamlit, Gradio, Panel y Reflex; destaca para control de hardware y robótica por su modelo de eventos.

### Panel (`panel`)

- **Repo:** https://github.com/holoviz/panel · BSD-3-Clause · nivel 2 · 55/100 · alternativa en «Apps web de datos en Python»
- **Qué es:** Framework de código abierto (BSD-3-Clause) del ecosistema HoloViz, respaldado por Anaconda y otros patrocinadores. Activo y maduro.
- **Cuándo elegirlo:** Casos: convertir un análisis de notebook en un dashboard interactivo para el equipo; crear una plataforma interna con varias páginas, tablas editables y autenticación.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install panel` — fuente: https://github.com/holoviz/panel/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install panel`, crea `app.py` con un widget enlazado a un gráfico y ejecútalo con `panel serve app.py --dev`. Éxito: El dashboard se abre en el navegador y responde a los controles.
- **Combina con:** `jupyterlab` [25/datos], `marimo` [25/datos], `claude-code` [20/terminal], `deck.gl` [10/geoespacial], `echarts` [10/graficos]
- **Alternativas:** `streamlit`, `gradio`, `reflex`, `nicegui`
- **Riesgos y avisos:** Panel publica una comparación con Streamlit en su documentación; ambos están agrupados como alternativas.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-25-apps.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Apps de datos en Python», lee `docs/alexandria/categoria-25-apps.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-25-apps.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
