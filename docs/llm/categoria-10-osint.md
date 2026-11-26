# Alexandría para agentes · Inteligencia de fuentes abiertas y mapas

Categoría 10 «Dashboards, analítica y mapas» › subcategoría `osint`. 7 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=10&sub=osint · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `gods-eye-view` | Visualizador geoespacial en un globo 3D que reúne fuentes abiertas para… | 2 Intermedio | 68 | MIT (solo código) (OSI permisiva) | recomendado |
| `sherlock` | CLI OSINT que busca un nombre de usuario en más de 400 redes sociales y sitios… | 1 Básico | 67 | MIT (OSI permisiva) | recomendado |
| `theharvester` | Herramienta OSINT de reconocimiento que reúne correos, subdominios, IP y… | 2 Intermedio | 66 | GPL-2.0 (OSI copyleft) | sin grupo |
| `maigret` | Recopila un dossier sobre una persona a partir de un nombre de usuario… | 1 Básico | 63 | MIT (OSI permisiva) | alternativa |
| `osiris` | Panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes… | 2 Intermedio | 53 | MIT (OSI permisiva) | alternativa |
| `pythia` | Plataforma local que reúne fuentes de actualidad y genera escenarios con… | 3 Avanzado | 47 | MIT (OSI permisiva) | sin grupo |
| `recon-ng` | Framework modular de reconocimiento web OSINT con espacios de trabajo, base de… | 2 Intermedio | 44 | GPL-3.0 (OSI copyleft) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### gods-eye-view (`gods-eye-view`)

- **Repo:** https://github.com/bilawalsidhu/gods-eye-view · MIT (solo código) · nivel 2 · 68/100 · recomendado en «Paneles OSINT sobre globo 3D»
- **Qué es:** God's Eye View, visualizador geoespacial en un globo 3D que reúne datos abiertos en tiempo real, de @bilawalsidhu. Licencia MIT (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Explorar información geoespacial pública; Consultar el globo desde un agente MCP.
- **Requisitos:** nivel 2: preparación media; Node y npm; WebGL; claves opcionales para datos o voz; app local para MCP; hardware prerequisites; API de IA: opcional; Node y npm; WebGL; claves opcionales para datos o voz; app local para MCP.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/bilawalsidhu/gods-eye-view/blob/main/README.md

  ```bash
  git clone https://github.com/bilawalsidhu/gods-eye-view.git
  cd gods-eye-view
  npm ci
  npm run doctor
  npm run dev
  ```
- **Primera prueba propuesta (no ejecutada):** Abre una capa pública y contrasta un objeto del globo con su fuente y hora de actualización Éxito: Puedes identificar qué datos son reales, simulados o no disponibles
- **Combina con:** `claude-code` [20/terminal], `hermes-agent` [21/asistentes], `pythia`
- **Alternativas:** `osiris`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativa (elige una): osiris. El seguimiento de cámaras y ALPR plantea cuestiones de privacidad. MCP de Claude y Codex sí está documentado; reutilizar sesión OAuth para voz es otra función experimental y no acredita un contrato Realtime cubierto por tu plan.

### Sherlock (`sherlock`)

- **Repo:** https://github.com/sherlock-project/sherlock · MIT · nivel 1 · 67/100 · recomendado en «Búsqueda de usuarios en redes sociales»
- **Qué es:** Herramienta OSINT de código abierto (MIT) mantenida por el Sherlock Project y su comunidad. Muy popular; el README advierte de que los paquetes de terceros para ParrotOS y Ubuntu 24.04 parecen estar rotos.
- **Cuándo elegirlo:** Casos: comprobar dónde está registrado un nombre de usuario propio o de tu marca; iniciar una investigación OSINT autorizada a partir de un alias.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pipx install sherlock-project` — fuente: https://github.com/sherlock-project/sherlock/blob/master/docs/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pipx install sherlock-project` y busca un nombre de usuario propio. Éxito: La salida lista las URL de los perfiles encontrados y guarda un archivo de resultados.
- **Combina con:** `theharvester`, `claude-code` [20/terminal], `duckdb` [25/datos]
- **Alternativas:** `maigret`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Alternativas (elige una): maigret.

### theHarvester (`theharvester`)

- **Repo:** https://github.com/laramies/theHarvester · GPL-2.0 · nivel 2 · 66/100
- **Qué es:** Herramienta OSINT de código abierto (solo GPL-2.0) creada por Christian Martorella (laramies) y mantenida por la comunidad desde hace años. Activa; requiere Python 3.14 y uv.
- **Cuándo elegirlo:** Casos: inventariar la superficie expuesta de tu propio dominio; fase inicial de reconocimiento en una auditoría de seguridad autorizada.
- **Requisitos:** nivel 2: preparación sencilla, varios servicios con Docker Compose; Python, Dockerfile, docker-compose.yml, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up --build -d` — fuente: https://github.com/laramies/theHarvester/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Clona el repositorio, ejecuta `uv sync` y lanza la búsqueda de ejemplo con las fuentes pasivas crtsh y certspotter sobre un dominio propio. Éxito: La terminal informa del resultado de cada fuente y lista subdominios encontrados.
- **Combina con:** `sherlock`, `maigret`, `katana` [4/crawlers], `recon-ng`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Alternativa cercana: recon-ng (framework modular de reconocimiento).

### Maigret (`maigret`)

- **Repo:** https://github.com/soxoj/maigret · MIT · nivel 1 · 63/100 · alternativa en «Búsqueda de usuarios en redes sociales»
- **Qué es:** Herramienta OSINT de código abierto (MIT) creada por soxoj, derivada de Sherlock y ampliada. Activa; el autor advierte de que las comprobaciones de sitios se rompen con el tiempo y requieren mantenimiento.
- **Cuándo elegirlo:** Casos: auditar la huella pública de un alias propio; investigaciones OSINT autorizadas que requieren un informe consolidado.
- **Requisitos:** nivel 1: preparación sencilla; Python, Dockerfile, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install maigret` — fuente: https://github.com/soxoj/maigret/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install maigret` (Python 3.10+) y busca un alias propio con salida HTML. Éxito: Se genera un informe HTML con los perfiles encontrados y los datos extraídos.
- **Combina con:** `theharvester`, `claude-code` [20/terminal], `duckdb` [25/datos]
- **Alternativas:** `sherlock`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): sherlock. El README incluye patrocinios de proxies y servicios de pago no necesarios para la herramienta.

### osiris (`osiris`)

- **Repo:** https://github.com/simplifaisoul/osiris · MIT · nivel 2 · 53/100 · alternativa en «Paneles OSINT sobre globo 3D»
- **Qué es:** OSIRIS (Open Source Intelligence & Reconnaissance Integrated System), panel OSINT en tiempo real de @simplifaisoul. Licencia MIT. Es reciente (creado en mayo de 2026, ~12k estrellas, v5.0.0).
- **Cuándo elegirlo:** Casos: Explorar noticias por ubicación; Comparar eventos públicos en un globo.
- **Requisitos:** nivel 2: preparación media; Node y npm; conexión a fuentes públicas; claves opcionales para capas extra; hardware prerequisites; API de IA: opcional; Node y npm; conexión a fuentes públicas; claves opcionales para capas extra.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/simplifaisoul/osiris/blob/master/README.md

  ```bash
  git clone https://github.com/simplifaisoul/osiris.git
  cd osiris
  npm install
  npm run dev
  ```
- **Primera prueba propuesta (no ejecutada):** Activa una capa pública y contrasta un evento con la fuente original y su fecha Éxito: Puedes identificar origen y actualización del evento en el mapa
- **Combina con:** `pythia`, `hermes-agent` [21/asistentes], `claude-code` [20/terminal]
- **Alternativas:** `gods-eye-view`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Alternativa (elige una): gods-eye-view. El acceso a cámaras públicas plantea cuestiones de privacidad y uso responsable. La etiqueta tiempo real no garantiza latencia ni precisión de todas las fuentes; el MCP expone acciones y debe configurarse aparte.

### Pythia (`pythia`)

- **Repo:** https://github.com/jangles-byte/Pythia · MIT · nivel 3 · 47/100
- **Qué es:** PYTHIA, plataforma local de predicción geopolítica de @jangles-byte que fusiona MiroFish (motor de predicción por inteligencia de enjambre) y Osiris (panel de inteligencia global). Licencia MIT.
- **Cuándo elegirlo:** Casos: Resumir fuentes públicas con un LLM local; Comparar escenarios sobre un conjunto de eventos.
- **Requisitos:** nivel 3: preparación pesada; Ollama con modelo descargado; Python y uv; checkout Osiris; dependencias del script; hardware prerequisites; API de IA: no; Ollama con modelo descargado; Python y uv; checkout Osiris; dependencias del script.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/jangles-byte/Pythia/blob/main/README.md

  ```bash
  git clone https://github.com/jangles-byte/Pythia && cd Pythia
  cp .env.example .env          # sensible defaults — no keys needed
  ./run-all.sh                  # starts Osiris + the engine and opens the UI
  ```
- **Primera prueba propuesta (no ejecutada):** Consulta un resumen del estado observado y separa los eventos de los escenarios generados Éxito: Cada evento tiene origen y los escenarios se identifican como hipótesis
- **Combina con:** `osiris`, `mirofish` [3/experimentos], `ollama` [8/motores], `claude-code` [20/terminal], `gods-eye-view`
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Sin alternativas declaradas. Las predicciones de LLM no son análisis de inteligencia verificados. Las predicciones son resultados generados y no probabilidades verificadas; MCP stdio permite consultar el motor desde los clientes.

### Recon-ng (`recon-ng`)

- **Repo:** https://github.com/lanmaster53/recon-ng · GPL-3.0 · nivel 2 · 44/100
- **Qué es:** Framework de reconocimiento de código abierto (GPL-3.0) creado por Tim Tomes (lanmaster53). Maduro, con ritmo de cambios bajo (último push en octubre de 2026).
- **Cuándo elegirlo:** Casos: organizar un reconocimiento OSINT autorizado en espacios de trabajo reproducibles; automatizar consultas a varias fuentes con módulos y claves de API.
- **Requisitos:** nivel 2: preparación media; Python, Dockerfile, docker-compose.yml; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/lanmaster53/recon-ng/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala las dependencias del README, crea un espacio de trabajo e instala un módulo pasivo del marketplace. Éxito: El módulo se ejecuta y sus resultados aparecen en la tabla correspondiente del espacio de trabajo.
- **Combina con:** `theharvester`, `duckdb` [25/datos], `claude-code` [20/terminal]
- **Riesgos y avisos:** Uso dual con datos personales: respeta la privacidad y la base legal del tratamiento. Ritmo de mantenimiento bajo: comprueba que los módulos que necesitas siguen funcionando.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-10-osint.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Inteligencia de fuentes abiertas y mapas», lee `docs/alexandria/categoria-10-osint.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-10-osint.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
