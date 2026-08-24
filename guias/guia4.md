
---

## 8. Workspaces de IA Local & Notebooks

Entornos privados todo-en-uno y herramientas tipo NotebookLM.

### 🔍 Escaneo rápido

| Repo | Qué es | Ejec. | Setup | Elige si… |
|---|---|---|---|---|
| [ECC](#-ecc) | Sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendimiento de forma segura. | 🏠 | 🔴 | Ejecutas agentes con acceso real a tu máquina y necesitas contención. |
| [odysseus](#-odysseus) | Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado. | 🏠 | 🔴 | Quieres operación privada todo-en-uno y aceptas operar la infra. |
| [open-notebook](#-open-notebook) | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. | 🏠 | 🟡 | Quieres NotebookLM privado y sin cuotas. |
| [notebooklm-py](#-notebooklm-py) | API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código. | ☁️ | 🟢 | Automatizas el NotebookLM real y aceptas el riesgo de API no oficial. |
| [notebooklm-mcp-cli](#-notebooklm-mcp-cli) | CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP. | ☁️ | 🟢 | Integras NotebookLM con tu asistente MCP. |

### ⚖️ ¿Cuál elegir? — Local privado vs. NotebookLM

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **odysseus** | Asistente administrativo integral (correo, calendario, docs) | Chat+docs+correo+calendario local en una sola UI | Solo necesitas RAG sobre documentos |
| **open-notebook** | Conocimiento privado tipo NotebookLM sin nube | 100% local vía Ollama, sin cuotas ni envío de datos | Quieres el NotebookLM real de Google |
| **notebooklm-py / notebooklm-mcp-cli** | Automatizar el NotebookLM real de Google a escala | Sube y sintetiza fuentes en la nube desde código/MCP | Tu política de datos prohíbe salir de local |

### 🌌 ECC
**Etiquetas:** Ejecución 🏠 local-first · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendimiento de forma segura. Actúa como capa intermedia entre el modelo y tu sistema, de modo que las acciones del agente pasan por un escudo antes de tocar el filesystem o la shell.
**Por qué destaca:** aporta una capa de seguridad de ejecución poco común en arneses de agentes, orientada a equipos que dan acceso real a su máquina a herramientas como Claude Code o Cursor. Su core en Rust y el soporte multi-agente lo diferencian de los runtimes puramente en Python.
**Cómo funciona:** intercepta y valida las acciones del agente (comandos bash, ficheros, red) mediante un core en Rust con hooks y memoria persistente, y solo las deja proseguir si cumplen la política definida.
**Instalación:** `git clone` del repo y compilación del core en Rust más dependencias en TS/Python/Go. Requiere toolchain de Rust y permisos para instalar hooks a nivel de sistema.
**Casos:** que Claude ejecute comandos bash sin poner en riesgo el sistema · memoria persistente y hooks entre sesiones · sandbox de agentes con auditoría de cada acción.
**Stack:** Rust (core), TypeScript, Python, Go — **Modelo/API:** Claude Code, Cursor, Zed, Codex, Gemini, Copilot.
**Elige si:** ejecutas agentes con acceso real a tu máquina y necesitas contención — **Evita si:** solo haces prompts de chat sin ejecución de código.
**Combina con:** [OpenHands](#-openhands) · [sandbox](#-sandbox) · [hermes-agent](#-hermes-agent)
**Repo:** [GitHub](https://github.com/affaan-m/ECC)

### ⛺ odysseus
**Etiquetas:** Ejecución 🏠 local-first · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado. Sustituye la dispersión entre varios SaaS por un único panel que tú controlas.
**Por qué destaca:** ofrece una alternativa local y soberana a las suites tipo Copilot/Workspace AI, juntando en un solo lugar lo que normalmente reparten varios servicios cerrados. Su enfoque todo-en-uno sobre stack open-source lo hace atractivo para perfiles técnicos que priorizan privacidad.
**Cómo funciona:** un backend Python orquesta los agentes sobre una base PostgreSQL y una UI React, conectando con modelos locales vía Ollama/Llama.cpp o con APIs comerciales para razonar sobre tus datos.
**Instalación:** `docker compose` para levantar backend, base de datos y frontend, o despliegue manual con Python y Node. Requiere PostgreSQL y un endpoint de modelo (Ollama local o API key comercial).
**Casos:** asistente administrativo privado que redacta correos y agenda desde tus documentos · research sobre tu propia base de conocimiento · sustituto self-host de Copilot personal.
**Stack:** Python, React, PostgreSQL — **Modelo/API:** Ollama/Llama.cpp o APIs comerciales (agnóstico vía configuración).
**Elige si:** quieres operación privada todo-en-uno y aceptas operar la infra — **Evita si:** prefieres SaaS gestionado sin mantenimiento.
**Combina con:** [open-notebook](#-open-notebook) · [ECC](#-ecc) · [mem0](#-mem0) · receta [Workspace privado](#-4-workspace-privado-local-soberano)
**Repo:** [GitHub](https://github.com/pewdiepie-archdaemon/odysseus)

### 📓 open-notebook
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. Resuelve el envío de documentos sensibles a la nube que implica el NotebookLM oficial.
**Por qué destaca:** cubre la demanda de un NotebookLM sin envío de datos a la nube y es uno de los proyectos de referencia en la comunidad open-source para este caso. Su autor (lfnovo) lo mantiene activo con soporte para modelos locales y comerciales.
**Cómo funciona:** un backend FastAPI indexa las fuentes y las consulta vía RAG contra modelos servidos por Ollama, con una UI React/Next.js para notebooks y generación de audio.
**Instalación:** `docker` (imagen oficial) o `pip` más Ollama para los modelos locales. Requiere Ollama instalado y al menos un modelo descargado (p. ej. Llama 3) para el modo 100% local.
**Casos:** subir un manual y generar un audio explicativo · chats de consulta sobre tus PDFs privados · síntesis temática de varias fuentes sin cuotas.
**Stack:** Python (FastAPI), React/Next.js — **Modelo/API:** Llama 3/Gemma 2 vía Ollama o APIs comerciales.
**Elige si:** quieres NotebookLM privado y sin cuotas — **Evita si:** prefieres el NotebookLM real automatizado ([notebooklm-py](#-notebooklm-py)).
**Combina con:** [odysseus](#-odysseus) · [markitdown](#-markitdown)
**Repo:** [GitHub](https://github.com/lfnovo/open-notebook)

### 🎙️ notebooklm-py
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código. Cubre el vacío de automatización que la interfaz web oficial no ofrece.
**Por qué destaca:** abre el NotebookLM real a la automatización, algo que la interfaz web oficial no permite, útil para procesar fuentes a escala. Se instala como un paquete pip y expone una API síncrona clara.
**Cómo funciona:** envuelve los endpoints internos de NotebookLM en una librería Python que sube fuentes y dispara síntesis usando tu sesión/credenciales de Google (no hay API pública oficial).
**Instalación:** `pip install` de la librería más configuración de credenciales de Google (cookies de sesión o auth no oficial).
**Casos:** subir 20 PDFs y pedir una síntesis temática · automatizar generación de notas de audio en lote · volcar fuentes a un notebook desde un pipeline.
**Stack:** Python — **Modelo/API:** NotebookLM/Google (Gemini Pro/Ultra).
**Limitaciones:** usa endpoints internos no oficiales de Google; puede romper ante cambios de la web y depende de credenciales de sesión válidas.
**Elige si:** automatizas el NotebookLM real y aceptas el riesgo de API no oficial — **Evita si:** quieres todo local ([open-notebook](#-open-notebook)).
**Combina con:** [notebooklm-mcp-cli](#-notebooklm-mcp-cli)
**Repo:** [GitHub](https://github.com/teng-lin/notebooklm-py)

### 🎚️ notebooklm-mcp-cli
**Etiquetas:** Ejecución ☁️ API/cloud · MCP 🔌 · Rol 🧩 motor/runtime · Setup 🟢 fácil
**Qué es:** CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP. Convierte NotebookLM en una herramienta invocable por asistentes.
**Por qué destaca:** expone NotebookLM como herramienta MCP, permitiendo que asistentes como Claude lo usen como un servicio más dentro de sus flujos. Cubre el mismo caso que la API Python pero pensado para integración con agentes.
**Cómo funciona:** levanta un servidor MCP en Python que traduce las llamadas del cliente a operaciones de NotebookLM (crear, actualizar y consultar notebooks) usando tus credenciales de Google.
**Instalación:** `pip install` o `git clone` y registro del servidor MCP en tu cliente (Claude Desktop, etc.). Requiere credenciales de Google válidas.
**Casos:** crear/actualizar notebooks en la nube desde MCP · flujos repetibles de audio desde un asistente · volcar fuentes desde otro agente.
**Stack:** Python, MCP — **Modelo/API:** NotebookLM/Google.
**Limitaciones:** depende de credenciales de Google y de endpoints internos no oficiales; puede romper ante cambios de NotebookLM.
**Elige si:** integras NotebookLM con tu asistente MCP — **Evita si:** prefieres la API directa en scripts ([notebooklm-py](#-notebooklm-py)).
**Combina con:** [notebooklm-py](#-notebooklm-py) · [awesome-mcp-servers](#-awesome-mcp-servers)
**Repo:** [GitHub](https://github.com/jacob-bd/notebooklm-mcp-cli)

---

## 9. Diseño, UI & Frontend

Diseño asistido, librerías de componentes, animación y 3D.

### 🔍 Escaneo rápido

| Repo | Qué es | Rol | Setup | Elige si… |
|---|---|---|---|---|
| [open-design](#-open-design) | Editor/workspace de diseño colaborativo asistido por IA que genera, maqueta y anima interfaces a partir de instrucciones en lenguaje natural; alternativa libre a Claude Design Artifacts. | 🖥️ | 🟡 | Generas UI desde texto y quieres edición visual. |
| [penpot](#-penpot) | Plataforma open-source de diseño y prototipado colaborativo, pensada para equipos de producto y diseño que quieren soberanía sobre sus archivos. | 🖥️ | 🔴 | Quieres diseño abierto y soberano, self-host. |
| [plasmic](#-plasmic) | Builder visual para apps y sitios conectado a tu propia base de código, que permite diseñar y publicar sin perder el control del código real. | 🖥️ | 🟡 | Quieres editar visual sobre tu código React. |
| [design.md](#-designmd) | Especificación de formato para describir una identidad visual a agentes de código (tokens YAML + prosa), de modo que el agente herede un sistema de diseño coherente entre sesiones. | 🎨 | 🟢 | Quieres consistencia de marca con IA y usas agentes para UI. |
| [impeccable](#-impeccable) | Guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" de UI por IA) que empuja al agente hacia frontends con criterio. | 🎨 | 🟢 | Quieres frontends que no parezcan generados por IA. |
| [tailwindcss](#-tailwindcss) | Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado. | 📚 | 🟢 | Quieres estilar rápido y consistente. |
| [magicui](#-magicui) | Librería de componentes UI visualmente atractivos (animaciones, efectos, secciones) para montar interfaces modernas con buen acabado desde el inicio. | 📚 | 🟢 | Priorizas estética y velocidad. |
| [heroui](#-heroui) | Librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, dashboards y landings consistentes. | 📚 | 🟢 | Quieres calidad + accesibilidad listas. |
| [ui](#-ui-shadcn) | Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada. | 📚 | 🟢 | Quieres control total del código de UI. |
| [normalize.css](#-normalizecss) | Hoja de estilos que normaliza los defaults entre navegadores para partir de una base de rendering uniforme. | 📚 | 🟢 | Quieres base CSS uniforme y ligera. |
| [GSAP](#-gsap) | Librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincronizados sobre cualquier propiedad del DOM. | 📚 | 🟡 | Necesitas animación avanzada y control fino de timelines. |
| [motion](#-motion) | Librería de animación declarativa para React/JS (antes Framer Motion) que añade transiciones y microinteracciones con muy poco código. | 📚 | 🟢 | Animas componentes React con API declarativa. |
| [three.js](#-threejs) | Motor 3D (WebGL) para renderizar gráficos y escenas interactivas directamente en el navegador. | 📚 | 🟡 | Renderizas 3D en web y quieres control a bajo nivel. |
| [react-three-fiber](#-react-three-fiber) | Renderer de React para three.js que expresa escenas 3D como componentes declarativos y reactivos. | 📚 | 🟡 | Haces 3D en React y quieres reactividad. |
| [swr](#-swr) | Librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano. | 📚 | 🟢 | Manejas datos remotos en React y quieres caché simple. |

### ⚖️ ¿Cuál elegir? — Diseño asistido vs. builder

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **open-design** | Generar/animar UI desde instrucciones en lenguaje natural | Bidireccional, multimodelo (AMR) y editable | Quieres editar sobre tu código existente |
| **plasmic** | Editar visualmente sobre tu propio código React/Next | Conecta con componentes y datos de tu repo | Generas desde texto sin codebase previo |
| **penpot** | Diseño/prototipo colaborativo open-source | SVG nativo, self-host real, alternativa a Figma | Necesitas generación por IA integrada |
| **design.md / impeccable** | Guiar a un agente de código a diseñar con criterio | Sistema/reglas persistentes anti-slop visual | No usas agentes para generar UI |

### ⚖️ ¿Cuál elegir? — Librerías de componentes

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **ui (shadcn)** | Control total del código de UI | Copy-paste, sin capa pesada ni lock-in | Quieres componentes "llave en mano" con actualizaciones automáticas |
| **heroui** | Accesibilidad y producción lista | React Aria + Tailwind + integración MCP | No usas React/Tailwind |
| **magicui** | Estética y velocidad de acabado | Componentes vistosos (animaciones, efectos) listos | Necesitas accesibilidad estricta |
| **tailwindcss** | Base de estilos de casi todo lo anterior | Utility-first universal, bundle optimizado | Prefieres CSS-in-JS o estilos scoped |

### 🎨 open-design
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** editor/workspace de diseño colaborativo asistido por IA que genera, maqueta y anima interfaces a partir de instrucciones en lenguaje natural; alternativa libre a Claude Design Artifacts. Resuelve el ir y venir entre prompt, preview y código exportable.
**Por qué destaca:** combina generación por IA con edición visual real y enruta varios modelos en una sola herramienta, algo poco común en editores abiertos. Su arquitectura Tauri (Rust) le da un binario nativo ligero frente a apps puramente web.
**Cómo funciona:** app de escritorio en React + Tauri (Rust) que traduce prompts a UI editable y la sincroniza de vuelta, con un enrutador AMR que reparte peticiones entre modelos según la tarea.
**Instalación:** clonar el repo y compilar la app Tauri, o usar los binarios de release según plataforma. Requiere claves API de al menos un proveedor (OpenAI/Anthropic/Google/DeepSeek).
**Casos:** describir una pantalla y ver cómo la IA la maqueta y anima · importar sistemas de diseño (Figma, Tailwind) y iterarlos por voz.
**Stack:** TypeScript/React, Tauri (Rust) — **Modelo/API:** GPT-4o, Claude, Gemini, DeepSeek vía AMR.
**Elige si:** generas UI desde texto y quieres edición visual — **Evita si:** prefieres editar visualmente sobre tu código existente ([plasmic](#-plasmic)).
**Combina con:** [tailwindcss](#-tailwindcss) · [heroui](#-heroui) · receta [Web app moderna](#-7-web-app-moderna-con-ia)
**Repo:** [GitHub](https://github.com/nexu-io/open-design)

### ✏️ penpot
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🔴 pesado
**Qué es:** plataforma open-source de diseño y prototipado colaborativo, pensada para equipos de producto y diseño que quieren soberanía sobre sus archivos. Es la alternativa abierta a Figma más conocida.
**Por qué destaca:** es la alternativa abierta a Figma más madura y adoptada, con estándares web (SVG nativo) y self-host real. Su licencia MPL y el respaldo de la Fundación Penpot le dan viabilidad a largo plazo.
**Cómo funciona:** suite web basada en SVG y CSS que corre sobre varios servicios desplegados con Docker (frontend, backend, bases de datos), con colaboración en tiempo real multiusuario.
**Instalación:** `docker compose` con los manifiestos oficiales (o plan cloud gestionado). Requiere varios contenedores y recursos no triviales, de ahí el setup 🔴.
**Casos:** diseñar landings, componentes y sistemas de marca · colaboración self-host con control de los archivos · prototipado interactivo para equipos.
**Stack:** stack web self-host, Docker (Clojure/ClojureScript) — **Modelo/API:** no nativa.
**Elige si:** quieres diseño abierto y soberano, self-host — **Evita si:** necesitas generación por IA ([open-design](#-open-design)) o no quieres operar Docker.
**Combina con:** [design.md](#-designmd) · [plasmic](#-plasmic)
**Repo:** [GitHub](https://github.com/penpot/penpot)

### 🧱 plasmic
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** builder visual para apps y sitios conectado a tu propia base de código, que permite diseñar y publicar sin perder el control del código real. Cubre el hueco entre no-code y desarrollo a medida.
**Por qué destaca:** une edición visual tipo no-code con tus componentes y datos existentes, reduciendo el salto entre diseñador y desarrollador. Soporta Next.js, Gatsby y otros frameworks React con un SDK que carga los diseños en runtime.
**Cómo funciona:** editor visual web que genera/consume componentes React/Next.js de tu repo y los sirve vía SDK (`@plasmicapp/loader-*`) o código generado, manteniendo sincronía con tu codebase.
**Instalación:** `npm i @plasmicapp/loader-nextjs` (o el loader del framework) y conectar el proyecto a tu app. Requiere un proyecto React/Next existente.
**Casos:** construir landings/experiencias sobre un stack existente · edición visual de componentes propios por perfiles no técnicos · headless CMS visual.
**Stack:** Node.js, React/Next.js — **Modelo/API:** no específica.
**Elige si:** quieres editar visual sobre tu código React — **Evita si:** generas desde texto sin codebase previo ([open-design](#-open-design)).
**Combina con:** [tailwindcss](#-tailwindcss) · [ui](#-ui-shadcn)
**Repo:** [GitHub](https://github.com/plasmicapp/plasmic)

### 📐 design.md
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** especificación de formato para describir una identidad visual a agentes de código (tokens YAML + prosa), de modo que el agente herede un sistema de diseño coherente entre sesiones. Resuelve la inconsistencia de marca cuando varias personas o agentes tocan la UI.
**Por qué destaca:** propuesta de Google Labs que aporta no solo los valores sino el "por qué" y cómo aplicarlos, algo que un simple archivo de tokens no transmite. Al ser un formato declarativo, funciona con cualquier agente que lea Markdown.
**Cómo funciona:** archivo Markdown/YAML que el agente lee como contexto persistente, combinando tokens de diseño (color, tipografía, espaciado) con guías en prosa sobre cuándo usarlos.
**Instalación:** crear un `design.md` en el repo siguiendo el formato (sin dependencias). Solo necesitas un agente de código que lo cargue como contexto.
**Casos:** dar al agente un sistema de diseño persistente · mantener coherencia de marca entre varios contribuyentes · onboarding rápido de estilo para nuevos agentes.
**Stack:** Markdown/YAML — **Modelo/API:** agentes de código (Claude Code, Cursor, etc.).
**Elige si:** quieres consistencia de marca con IA y usas agentes para UI — **Evita si:** no usas agentes para generar código de UI.
**Combina con:** [impeccable](#-impeccable) · [skills_emil](#-skills_emil)
**Repo:** [GitHub](https://github.com/google-labs-code/design.md)

### 💎 impeccable
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" de UI por IA) que empuja al agente hacia frontends con criterio. Ataca el patrón repetitivo de interfaces que "huelen" a IA.
**Por qué destaca:** ataca de forma deliberada el "AI slop" visual con reglas deterministas, un enfoque diferenciado frente a prompts genéricos de diseño. Su autor (pbakaus, ex Google) le da peso en la comunidad de diseño para agentes.
**Cómo funciona:** se instala como skill que añade comandos y detectores; itera la UI en el navegador y señala patrones delatores (Inter omnipresente, gradientes morados, sombras genéricas, etc.).
**Instalación:** `npx impeccable` (skill para Claude Code y compatibles). Requiere Node y un agente compatible con skills.
**Casos:** evitar Inter+gradientes morados en todo · iterar diseño en vivo en el navegador · auditar una UI generada antes de entregarla.
**Stack:** Node (`npx impeccable`) — **Modelo/API:** Claude Code y compatibles.
**Elige si:** quieres frontends que no parezcan generados por IA — **Evita si:** no generas UI con agentes.
**Combina con:** [taste-skill](#-taste-skill) · [ui-ux-pro-max-skill](#-ui-ux-pro-max-skill) · [design.md](#-designmd)
**Repo:** [GitHub](https://github.com/pbakaus/impeccable)

### 🌬️ tailwindcss
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado. Elimina el contexto de estilos disperso entre hojas y componentes.
**Por qué destaca:** se ha vuelto el estándar de facto del estilado web moderno y la base sobre la que se montan casi todas las librerías de componentes actuales (shadcn, heroui, magicui). Su motor v4 con engine nativo en Rust aceleró el build.
**Cómo funciona:** motor que escanea tus archivos de plantilla y genera solo el CSS de las utilidades usadas (purge automático), optimizando el bundle final a lo mínimo.
**Instalación:** `npm i tailwindcss` y configurar el plugin de PostCSS/CLI, o vía CDN para pruebas rápidas. Requiere un build step para producción.
**Casos:** estilar landings y apps sin escribir CSS a mano · base de estilos de casi cualquier lib de componentes actual · design system consistente por composición.
**Stack:** Node.js, CSS — **Modelo/API:** N/A.
**Elige si:** quieres estilar rápido y consistente — **Evita si:** prefieres CSS-in-JS o estilos scoped por componente.
**Combina con:** [heroui](#-heroui) · [ui](#-ui-shadcn) · [magicui](#-magicui)
**Repo:** [GitHub](https://github.com/tailwindlabs/tailwindcss)

### ✨ magicui
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de componentes UI visualmente atractivos (animaciones, efectos, secciones) para montar interfaces modernas con buen acabado desde el inicio. Apunta al impacto visual más que a la accesibilidad estricta.
**Por qué destaca:** prioriza el impacto visual con piezas vistosas listas para usar, popular en landings y portfolios que buscan diferenciarse rápido. Es compatible con el registro de shadcn, así que se integra en el mismo flujo.
**Cómo funciona:** componentes React/Next.js sobre Tailwind y motion que se copian o instalan vía CLI compatible con shadcn (`npx shadcn add`).
**Instalación:** `npx shadcn add` apuntando al registro de Magic UI, o copiar el componente directamente. Requiere Tailwind y motion instalados.
**Casos:** landing o dashboard con buen acabado desde el inicio · prototipado vistoso para demos · secciones hero con animaciones de impacto.
**Stack:** Node.js, React/Next.js — **Modelo/API:** N/A.
**Elige si:** priorizas estética y velocidad — **Evita si:** necesitas accesibilidad estricta ([heroui](#-heroui)).
**Combina con:** [tailwindcss](#-tailwindcss) · [motion](#-motion)
**Repo:** [GitHub](https://github.com/magicuidesign/magicui)

### 🦸 heroui
**Etiquetas:** Ejecución 🏠 local-first · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, dashboards y landings consistentes. Resuelve la accesibilidad seria sin renunciar a un estilado moderno.
**Por qué destaca:** combina accesibilidad seria (React Aria de Adobe), integración MCP para asistentes y soporte de Next.js/React 19, una mezcla poco habitual en kits de UI. Su instalación por módulos evita inflar el bundle.
**Cómo funciona:** componentes React construidos sobre React Aria (comportamiento/accesibilidad) y estilados con Tailwind, instalables por módulos y con un plugin de Tailwind para los tokens del tema.
**Instalación:** `npm i @heroui/react` y configurar el plugin de Tailwind. Requiere React 18+ y Tailwind.
**Casos:** dashboards, SaaS o landings accesibles y consistentes · base de UI con accesibilidad out-of-the-box · integración con asistentes vía MCP.
**Stack:** Node.js, React, Tailwind — **Modelo/API:** tooling MCP/asistentes.
**Elige si:** quieres calidad + accesibilidad listas — **Evita si:** quieres control copy-paste del código ([ui](#-ui-shadcn)).
**Combina con:** [tailwindcss](#-tailwindcss) · [swr](#-swr)
**Repo:** [GitHub](https://github.com/heroui-inc/heroui)

### 🧱 ui (shadcn)
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada. El código fuente pasa a ser tuyo y lo editas a voluntad.
**Por qué destaca:** popularizó el modelo "el código es tuyo": sin capa pesada ni lock-in, se ha vuelto la base de incontables design systems. Su combinación de Radix UI (accesibilidad) + Tailwind (estilos) es el patrón de facto en React moderno.
**Cómo funciona:** CLI que copia el código fuente de cada componente (Radix + Tailwind) directamente a tu proyecto, para que lo edites y versiones como parte de tu codebase.
**Instalación:** `npx shadcn@latest init` y luego `npx shadcn add <componente>`. Requiere React + Tailwind configurados.
**Casos:** pantallas administrativas o landings sobre tu stack · base de un design system propio versionado · punto de partida que personalizas sin límites.
**Stack:** Node.js, React, Tailwind, Radix UI — **Modelo/API:** N/A.
**Elige si:** quieres ser dueño del código de UI — **Evita si:** prefieres una lib "llave en mano" con updates automáticos ([heroui](#-heroui)).
**Combina con:** [tailwindcss](#-tailwindcss) · [plasmic](#-plasmic)
**Repo:** [GitHub](https://github.com/shadcn-ui/ui)

### 🧯 normalize.css
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** hoja de estilos que normaliza los defaults entre navegadores para partir de una base de rendering uniforme. Resuelve las inconsistencias de margen, tipografía y formularios entre Chrome, Firefox y Safari.
**Por qué destaca:** clásico ampliamente usado que, en lugar de borrar estilos (como un reset agresivo), preserva los defaults útiles y corrige solo las inconsistencias. Lleva años como referencia cross-browser.
**Cómo funciona:** un único CSS que ajusta elementos donde los navegadores difieren (márgenes, alturas de línea, renderizado de fuentes), sin imponer una estética propia.
**Instalación:** `npm i normalize.css` e importarlo al inicio de tu CSS, o enlazar por CDN. No requiere build step.
**Casos:** base consistente antes de aplicar tu estilado · igualar rendering cross-browser en proyectos legacy · complemento de un reset propio.
**Stack:** CSS — **Modelo/API:** N/A.
**Elige si:** quieres base CSS uniforme y ligera — **Evita si:** ya usas el preflight de Tailwind, que cubre lo mismo.
**Combina con:** [tailwindcss](#-tailwindcss)
**Repo:** [GitHub](https://github.com/necolas/normalize.css)

### 🎞️ GSAP
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincronizados sobre cualquier propiedad del DOM. Es la herramienta de referencia del motion web profesional.
**Por qué destaca:** referencia veterana del motion web profesional, con rendimiento y precisión difíciles de igualar para animación detallada. Su ecosistema de plugins (ScrollTrigger, Flip, DrawSVG) cubre casos que otras librerías no alcanzan.
**Cómo funciona:** motor JavaScript que anima propiedades de cualquier objeto/DOM mediante tweens y timelines encadenables, con plugins como ScrollTrigger para animaciones ligadas al scroll.
**Instalación:** `npm i gsap` o vía CDN. Algunos plugins premium requieren membresía del Club GreenSock; los core son libres.
**Casos:** animaciones avanzadas y timelines sincronizados · efectos scroll y transiciones complejas · microinteracciones de alta precisión fuera de React.
**Stack:** JavaScript — **Modelo/API:** N/A.
**Elige si:** necesitas animación avanzada y control fino de timelines — **Evita si:** te basta animar componentes React con API declarativa ([motion](#-motion)).
**Combina con:** [three.js](#-threejs) · [motion](#-motion)
**Repo:** [GitHub](https://github.com/greensock/GSAP)

### 🌀 motion
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de animación declarativa para React/JS (antes Framer Motion) que añade transiciones y microinteracciones con muy poco código. Hizo accesible la animación en el ecosistema React.
**Por qué destaca:** su API declarativa hizo accesible la animación en React y es de las más adoptadas del ecosistema. La versión actual (`motion`) unifica React y vanilla bajo el mismo paquete.
**Cómo funciona:** componentes `motion.*` y hooks que interpolan props de estado y manejan entradas/salidas, gestos y layout animations automáticamente sin manipular el DOM a mano.
**Instalación:** `npm i motion` (o `framer-motion` para la versión legacy). Requiere React para los bindings `motion.*`.
**Casos:** animar entradas/salidas de componentes · microinteracciones y gestos fáciles · animaciones de layout cuando reordenas listas.
**Stack:** JavaScript/React — **Modelo/API:** N/A.
**Elige si:** animas componentes React con API declarativa — **Evita si:** necesitas timelines complejos no ligados a React ([GSAP](#-gsap)).
**Combina con:** [magicui](#-magicui) · [react-three-fiber](#-react-three-fiber)
**Repo:** [GitHub](https://github.com/motiondivision/motion)

### 🔺 three.js
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** motor 3D (WebGL) para renderizar gráficos y escenas interactivas directamente en el navegador. Abstrae la complejidad de WebGL en escenas, cámaras, luces y mallas.
**Por qué destaca:** es el estándar del 3D web, con un ecosistema enorme de ejemplos, loaders y helpers alrededor. Su longevidad (desde 2010) y la comunidad activa lo hacen la base de casi todo 3D web.
**Cómo funciona:** abstrae WebGL en un grafo de escena (escenas, cámaras, luces, mallas) y gestiona el bucle de render por ti, con materiales y geometrías listas para usar.
**Instalación:** `npm i three` o vía CDN/módulo ES. Para algo más que una demo necesitas familiaridad con conceptos de gráficos 3D.
**Casos:** escenas 3D y visualizaciones inmersivas · experiencias web interactivas · base para frameworks como react-three-fiber.
**Stack:** JavaScript/WebGL — **Modelo/API:** N/A.
**Elige si:** renderizas 3D en web y quieres control a bajo nivel — **Evita si:** trabajas solo 2D o prefieres la ergonomía de React ([react-three-fiber](#-react-three-fiber)).
**Combina con:** [react-three-fiber](#-react-three-fiber) · [GSAP](#-gsap)
**Repo:** [GitHub](https://github.com/mrdoob/three.js)

### 🔻 react-three-fiber
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** renderer de React para three.js que expresa escenas 3D como componentes declarativos y reactivos. Lleva la mentalidad componible de React al 3D sin abandonar three.js por debajo.
**Por qué destaca:** lleva la mentalidad declarativa y componible de React al 3D, integrándose con el resto del ecosistema (estado, hooks, drei). Su ecosistema (`@react-three/drei`, `@react-three/postprocessing`) cubre la mayoría de necesidades comunes.
**Cómo funciona:** reconciliador custom que traduce el árbol JSX a objetos de three.js y los actualiza con los cambios de estado de React, gestionando el bucle de render automáticamente.
**Instalación:** `npm i three @react-three/fiber` (y normalmente `@react-three/drei` para helpers). Requiere React + three.js.
**Casos:** escenas 3D dentro de apps React · integrar 3D con estado y hooks del ecosistema React · visualizaciones reactivas a datos.
**Stack:** JavaScript/React — **Modelo/API:** N/A.
**Elige si:** haces 3D en React y quieres reactividad — **Evita si:** no usas React o necesitas control a bajo nivel ([three.js](#-threejs) directo).
**Combina con:** [three.js](#-threejs) · [motion](#-motion)
**Repo:** [GitHub](https://github.com/pmndrs/react-three-fiber)

### 🔄 swr
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano. Cubre el caso de consumir APIs en frontend sin manejar caché a mano.
**Por qué destaca:** creada por Vercel, ofrece una DX muy pulida para consumir APIs y es referencia junto a React Query. Su peso mínimo y la revalidación en foco/intervalo cubren la mayoría de apps sin configuración.
**Cómo funciona:** hook `useSWR(key, fetcher)` que cachea por clave, revalida al recuperar foco o en intervalo, y deduplica peticiones simultáneas al mismo key.
**Instalación:** `npm i swr`. Solo necesita un fetcher (una función async) por clave; funciona con cualquier API REST/GraphQL.
**Casos:** consumir APIs en frontend con caché y revalidación · datos en tiempo casi real sin WebSocket · mutaciones optimistas con `useSWRMutation`.
**Stack:** JavaScript/React — **Modelo/API:** N/A.
**Elige si:** manejas datos remotos en React y quieres caché simple — **Evita si:** prefieres React Query con su modelo de caché global más rico.
**Combina con:** [heroui](#-heroui) · receta [Web app moderna](#-7-web-app-moderna-con-ia)
**Repo:** [GitHub](https://github.com/vercel/swr)

---

## 10. Analítica & Visualización

Product analytics, dashboards y librerías de gráficos.

### 🔍 Escaneo rápido

| Repo | Qué es | Rol | Setup | Elige si… |
|---|---|---|---|---|
| [posthog](#-posthog) | Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite. | ⚙️ | 🔴 | Quieres entender el uso real y el comportamiento de usuarios. |
| [metabase](#-metabase) | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir. | ⚙️ | 🟡 | Quieres BI accesible para perfiles no técnicos. |
| [dash](#-dash) | Framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos. | 📚 | 🟡 | Quieres dashboards productivos en Python con control del frontend. |
| [echarts](#-echarts) | Librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos. | 📚 | 🟡 | Necesitas gráficos ricos y variados embebidos. |
| [uPlot](#-uplot) | Librería ultraligera para gráficos de series temporales capaz de pintar cientos de miles de puntos sin penalizar el rendimiento. | 📚 | 🟢 | Priorizas velocidad y peso del bundle. |
| [streamlit](#-streamlit) | Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni. | 📚 | 🟢 | Quieres una UI de datos al vuelo y prototipos rápidos. |
| [awesome-dataviz](#-awesome-dataviz) | Directorio curado de herramientas, librerías y recursos de visualización de datos recopilados por la comunidad. | 📂 | 🟢 | Buscas opciones de visualización y aún no has elegido. |

### ⚖️ ¿Cuál elegir? — Plataforma vs. librería

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **posthog** | Analítica de producto/eventos y comportamiento | Funnels, session replay, feature flags, autohospedable | Solo necesitas BI sobre una BD estática |
| **metabase** | BI/reporting para negocio, sin código | Dashboards visuales sobre cualquier BD soportada | Necesitas analítica de eventos por usuario |
| **dash / streamlit** | Apps de datos a medida en Python | Control total del frontend de datos | Prefieres gráficos embebidos en una web JS |
| **echarts / uPlot** | Gráficos embebidos en tu web | echarts=potente y variado · uPlot=ligero/rápido | Quieres una plataforma completa de analítica |

### 📈 posthog
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite. Cubre todo el ciclo de medición de producto sin integrar varias herramientas.
**Por qué destaca:** referente open source de analítica de producto, autohospedable y muy adoptado por equipos que quieren evitar el lock-in de herramientas SaaS. Su licencia MIT y la amplitud de funciones (replay, flags, A/B tests) lo hacen competitivo frente a Amplitude/Mixpanel.
**Cómo funciona:** instrumentas eventos con su SDK (JS/Python/etc.) que se ingieren en su backend, y exploras todo desde su panel web con funnels, grabaciones de sesión y experimentos.
**Instalación:** `docker compose` para self-host, o SDK vía `npm i posthog-js` / `pip install posthog` apuntando al cloud. El self-host requiere ClickHouse y recursos no triviales.
**Casos:** medir conversiones antes/después de cambios · funnels y session replay para diagnosticar fricción · feature flags y A/B tests controlados.
**Stack:** Python/Node, ClickHouse, self-host o cloud — **Modelo/API:** complementa apps instrumentadas con agentes.
**Elige si:** quieres entender el uso real y el comportamiento de usuarios — **Evita si:** solo necesitas BI sobre una BD estática ([metabase](#-metabase)).
**Combina con:** [metabase](#-metabase) · receta [Marketing de agencia](#-6-marketing-de-agencia)
**Repo:** [GitHub](https://github.com/PostHog/posthog)

### 📊 metabase
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. Apunta a perfiles no técnicos que necesitan reporting propio.
**Por qué destaca:** de las plataformas BI open source más populares por su facilidad de uso y su editor visual de consultas accesible para perfiles no técnicos. Su despliegue como JAR o contenedor lo hace muy portable.
**Cómo funciona:** se conecta a tu BD (Postgres, MySQL, BigQuery, etc.), define preguntas mediante un constructor visual o SQL nativo, y las agrupa en dashboards interactivos servidos por web.
**Instalación:** `docker run metabase/metabase`, o JAR ejecutable con Java. Requiere una BD de aplicación (H2 por defecto, recomendado Postgres/MySQL para producción).
**Casos:** tableros de marketing/ventas sin escribir SQL · reporting de negocio sobre tu BD existente · exploración ad-hoc por perfiles no técnicos.
**Stack:** Java/Clojure, BD, web — **Modelo/API:** N/A.
**Elige si:** quieres BI accesible para perfiles no técnicos — **Evita si:** necesitas analítica de eventos por usuario ([posthog](#-posthog)).
**Combina con:** [posthog](#-posthog) · [echarts](#-echarts)
**Repo:** [GitHub](https://github.com/metabase/metabase)

### 🧮 dash
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos. Cubre el caso de dashboards productivos en Python sin salir del lenguaje.
**Por qué destaca:** estándar de facto para dashboards productivos en Python, respaldado por Plotly y muy usado en entornos científicos y empresariales. Su modelo de callbacks sobre Flask da control fino del frontend sin JS.
**Cómo funciona:** declaras el layout y callbacks en Python sobre un servidor Flask, y renderiza gráficos interactivos con Plotly.js en el navegador, respondiendo a los inputs del usuario.
**Instalación:** `pip install dash`. Requiere Python y, para producción, un servidor WSGI (gunicorn/uwsgi).
**Casos:** dashboard interno de campañas/telemetría · paneles con Plotly y controles reactivos · apps de datos productivas en Python.
**Stack:** Python, Plotly, Flask, web — **Modelo/API:** consume resultados de pipelines IA.
**Elige si:** quieres dashboards productivos en Python con control del frontend — **Evita si:** prefieres prototipos ultrarrápidos ([streamlit](#-streamlit)).
**Combina con:** [streamlit](#-streamlit) · [echarts](#-echarts)
**Repo:** [GitHub](https://github.com/plotly/dash)

### 📉 echarts
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos. Cubre casi cualquier tipo de chart en el navegador.
**Por qué destaca:** una de las librerías de charts más completas y populares del ecosistema web, con renderizado de alto rendimiento sobre Canvas/SVG y comunidad muy activa. Su origen en Baidu y su paso a la ASF le dan madurez.
**Cómo funciona:** configuras un objeto de opciones en JavaScript que la librería pinta sobre Canvas o SVG, con soporte de mapas, series complejas, animaciones y renderizado incremental para datasets grandes.
**Instalación:** `npm i echarts` o vía CDN. Para tipos especiales (mapas) puede necesitar datos geográficos aparte.
**Casos:** gráficos interactivos, mapas y series complejas · reporting embebido en apps web · visualizaciones de alto volumen de datos.
**Stack:** JavaScript/TypeScript — **Modelo/API:** N/A.
**Elige si:** necesitas gráficos ricos y variados embebidos — **Evita si:** solo series temporales simples y priorizas peso ([uPlot](#-uplot)).
**Combina con:** [metabase](#-metabase) · [heroui](#-heroui)
**Repo:** [GitHub](https://github.com/apache/echarts)

### 📈 uPlot
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería ultraligera para gráficos de series temporales capaz de pintar cientos de miles de puntos sin penalizar el rendimiento. Apuesta por hacer una sola cosa (líneas/áreas temporales) mejor que ninguna.
**Por qué destaca:** célebre por su tamaño minúsculo (pocos KB) y velocidad de renderizado, ideal cuando el peso del bundle y los FPS importan. Su autor (leeoniya) la mantiene con foco obsesivo en rendimiento.
**Cómo funciona:** dibuja líneas y áreas directamente sobre Canvas con una API minimalista en JavaScript optimizada para datasets enormes, sin dependencias y sin virtual DOM.
**Instalación:** `npm i uplot` o vía CDN. Sin dependencias; se integra en cualquier stack web.
**Casos:** dashboards con muchísimos puntos · charts rápidos en frontend embebido · monitorización en tiempo real donde el peso importa.
**Stack:** JavaScript — **Modelo/API:** N/A.
**Elige si:** priorizas velocidad y peso del bundle — **Evita si:** necesitas tipos de gráfico variados ([echarts](#-echarts)).
**Combina con:** [swr](#-swr) · receta [Web app moderna](#-7-web-app-moderna-con-ia)
**Repo:** [GitHub](https://github.com/leeoniya/uPlot)

### 📊 streamlit
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. Convierte un script de datos en una app web interactiva casi al instante.
**Por qué destaca:** muy popular en la comunidad de data science e IA por convertir un script en una app web interactiva casi al instante. Su modelo de rerun top-to-bottom simplifica la iteración frente a callbacks manuales.
**Cómo funciona:** ejecuta tu script de arriba abajo en cada interacción y mapea widgets y gráficos a una UI web reactiva servida automáticamente, con caché para evitar recálculos costosos.
**Instalación:** `pip install streamlit` y `streamlit run app.py`. Requiere Python; no necesita frontend aparte.
**Casos:** prototipo para consultar datos/resultados de un modelo · demos de datos y modelos para stakeholders · dashboards internos rápidos.
**Stack:** Python — **Modelo/API:** frontend ideal para LLMs/pipelines.
**Elige si:** quieres una UI de datos al vuelo y prototipos rápidos — **Evita si:** necesitas una app productiva con control fino del frontend ([dash](#-dash)).
**Combina con:** [dash](#-dash) · [data-science-ipython-notebooks](#-data-science-ipython-notebooks)
**Repo:** [GitHub](https://github.com/streamlit/streamlit)

### 🗂️ awesome-dataviz
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** directorio curado de herramientas, librerías y recursos de visualización de datos recopilados por la comunidad. Punto de partida para descubrir opciones de dataviz sin búsquedas dispersas.
**Por qué destaca:** punto de partida cómodo de la serie "awesome" para descubrir y comparar opciones de dataviz sin búsquedas dispersas. Su organización por categorías (lenguaje, tipo de chart, plataforma) facilita el filtrado.
**Cómo funciona:** es una lista en Markdown alojada en GitHub, organizada por categorías con enlaces a cada herramienta y recurso, mantenida por contribuciones de la comunidad.
**Instalación:** no requiere instalación; se consulta en GitHub.
**Casos:** elegir una librería de charts por lenguaje/plataforma · descubrir recursos y ejemplos de dataviz · comparar alternativas antes de decidir.
**Stack:** Markdown — **Modelo/API:** N/A.
**Elige si:** buscas opciones de visualización y aún no has elegido — **Evita si:** ya elegiste tu librería y solo necesitas usarla.
**Combina con:** [echarts](#-echarts) · [awesome-bigdata](#-awesome-bigdata)
**Repo:** [GitHub](https://github.com/javierluraschi/awesome-dataviz)

---

## 11. Generación de Imagen & Visión

Motores de difusión, control/condicionamiento, restauración y rostros.

### 🔍 Escaneo rápido

| Repo | Qué es | Ejec. | Setup | Elige si… |
|---|---|---|---|---|
| [ComfyUI](#-comfyui) | Motor local modular para crear pipelines visuales de generación con IA mediante un grafo de nodos, donde cada paso (carga de modelo, sampling, postproceso) es un bloque conectable y reutilizable. | 🏠 | 🔴 | Quieres control total y pipelines reproducibles. |
| [stable-diffusion-webui](#-stable-diffusion-webui) | Interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador. | 🏠 | 🔴 | Quieres extensiones y comunidad amplia. |
| [Fooocus](#-fooocus) | Herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, ocultando parámetros técnicos tras presets inteligentes. | 🏠 | 🟡 | Quieres resultados ya, sin curva. |
| [InvokeAI](#-invokeai) | Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpainting, gestión de modelos y workflows encadenables. | 🏠 | 🔴 | Trabajas creatividad profesional y quieres una app estable con canvas. |
| [diffusers](#-diffusers) | Librería de Hugging Face para construir y ejecutar pipelines de modelos de difusión (imagen, video, audio) desde código, con APIs estandarizadas para schedulers, componentes y modelos. | 🏠 | 🔴 | Programas generación y quieres control total por código. |
| [ControlNet](#-controlnet) | Método y familia de modelos que condicionan la generación text-to-image con señales externas (poses, bordes Canny, profundidad, mapas de segmentación), fijando la estructura del resultado. | 🏠 | 🔴 | Necesitas control estructural fino de la composición. |
| [sd-webui-controlnet](#-sd-webui-controlnet) | Extensión que integra ControlNet en Stable Diffusion WebUI (AUTOMATIC1111), con preprocesadores para poses, bordes, profundidad y más. | 🏠 | 🔴 | Ya usas SD WebUI y quieres ControlNet sin cambiar de entorno. |
| [ComfyUI_IPAdapter_plus](#-comfyui_ipadapter_plus) | Conjunto de nodos para ComfyUI que implementa IPAdapter, permitiendo condicionar la generación con una o varias imágenes de referencia para transferir estilo o identidad. | 🏠 | 🔴 | Trabajas en ComfyUI y necesitas consistencia visual por referencia. |
| [GFPGAN](#-gfpgan) | Algoritmo de restauración facial de Tencent ARC que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados. | 🏠 | 🟡 | Restauras rostros borrosos o fundidos. |
| [Real-ESRGAN](#-real-esrgan) | Herramienta de superresolución y restauración para imágenes reales que reescala (2×/4×) y limpia material de baja calidad sin rehacerlo desde cero. | 🏠 | 🟡 | Reescalas imágenes o video a más resolución. |
| [LivePortrait](#-liveportrait) | Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen (humanos, pero también mascotas). | 🏠 | 🔴 | Animas retratos a partir de una foto. |
| [Deep-Live-Cam](#-deep-live-cam) | Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. | 🏠 | 🔴 | Necesitas swap en vivo legítimo con consentimiento. |
| [face_recognition](#-face_recognition) | Librería de Python con API de alto nivel para detección y reconocimiento facial: localizar caras, compararlas e identificarlas por similitud. | 🏠 | 🟡 | Necesitas reconocimiento facial básico y rápido de implementar. |
| [Open-Generative-AI](#-open-generative-ai) | Plataforma alternativa libre a servicios premium de video/imagen que agrupa más de 200 modelos generativos accesibles desde terminal o integrados con agentes. | 🔀 | 🟡 | Quieres un hub de generación multi-modal sin atarte a un SaaS. |
| [fluxer](#-fluxer) | Plataforma generativa emergente con foco en audio y video mejorados, ofrecida como cliente Canary web/desktop; su API y self-host aún están en finalización. | 🔀 | 🟡 | Quieres probar algo nuevo y seguir su evolución. |

### ⚖️ ¿Cuál elegir? — Motor de generación de imagen

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **ComfyUI** | Pipelines complejos, repetibles y exportables | Control por nodos, muy potente y modular | Quieres simplicidad inmediata sin curva |
| **stable-diffusion-webui** | Ecosistema y extensiones variadas | Comunidad enorme, plugins de todo tipo | Prefieres un flujo moderno y limpio |
| **Fooocus** | Resultados rápidos sin tuning | Mínima fricción técnica, presets inteligentes | Necesitas control fino del pipeline |
| **InvokeAI** | Trabajo creativo profesional | Flujo pulido y unificado (canvas, layers) | Solo quieres una prueba puntual |
| **diffusers** | Generación desde código Python | Estándar reutilizable de Hugging Face | Quieres una UI lista sin programar |

### ⚖️ ¿Cuál elegir? — Control y restauración

| Repo | Foco | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **ControlNet / sd-webui-controlnet** | Control estructural (pose/bordes) | Composición precisa condicionada | Solo necesitas generación libre |
| **ComfyUI_IPAdapter_plus** | Referencia de estilo/identidad | Consistencia visual sin reentrenar | No usas ComfyUI |
| **GFPGAN** | Restaurar rostros | Recupera caras degradadas | La imagen no tiene rostros |
| **Real-ESRGAN** | Upscaling general | Reescala con detalle | Solo necesitas comprimir, no ampliar |

### 🧠 ComfyUI
**Etiquetas:** Ejecución 🏠 local-first · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** motor local modular para crear pipelines visuales de generación con IA mediante un grafo de nodos, donde cada paso (carga de modelo, sampling, postproceso) es un bloque conectable y reutilizable. Resuelve la composición de flujos de difusión complejos que una UI fija no permite.
**Por qué destaca:** es la referencia para flujos de difusión avanzados y reproducibles, con una comunidad enorme y un ecosistema de nodos/extensiones muy activo. Su autor (comfyanonymous) lo mantiene con foco en rendimiento y compatibilidad con los modelos más recientes (SDXL, Flux).
**Cómo funciona:** ejecuta modelos de difusión (Stable Diffusion, SDXL, Flux) sobre PyTorch+GPU, encadenando nodos en un grafo visual servido desde una interfaz web local que expone cada paso como bloque configurable.
**Instalación:** `git clone` del repo y arranque con `python main.py` (o paquete portable en Windows); requiere descargar checkpoints aparte y una GPU con VRAM decente (8 GB+ recomendado).
**Casos:** pipeline para generar/transformar/exportar imágenes de campaña · composición fina y repetible · flujos con ControlNet/IPAdapter encadenados.
**Stack:** Python, GPU, PyTorch, modelos locales — **Modelo/API:** local-first (difusión).
**Limitaciones:** requiere GPU con VRAM suficiente; los checkpoints pesan varios GB y la curva del grafo de nodos es empinada para nuevos.
**Elige si:** quieres control total y pipelines reproducibles — **Evita si:** buscas simplicidad inmediata ([Fooocus](#-fooocus)).
**Combina con:** [ComfyUI_IPAdapter_plus](#-comfyui_ipadapter_plus) · [Real-ESRGAN](#-real-esrgan) · receta [Pipeline de Reels](#-2-pipeline-de-reels--video-corto)
**Repo:** [GitHub](https://github.com/comfyanonymous/ComfyUI)

### 🖼️ stable-diffusion-webui
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🔴 pesado
**Qué es:** interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador. Es la UI que popularizó la difusión local.
**Por qué destaca:** fue la UI que popularizó SD y mantiene una de las comunidades y catálogos de plugins más grandes del ecosistema. Su madurez y la cantidad de extensiones (ControlNet, ADetailer, ReActor) la hacen muy versátil.
**Cómo funciona:** levanta un servidor Gradio que orquesta modelos de difusión sobre PyTorch+GPU, con pestañas y scripts para cada modo de generación y un sistema de extensiones instalables desde la propia UI.
**Instalación:** `git clone` y ejecutar `webui-user.bat` (Windows) o `webui.sh` (Linux/Mac); el script crea el entorno e instala dependencias automáticamente. Requiere GPU con VRAM decente y checkpoints descargados aparte.
**Casos:** probar estilos rápido desde una UI · usar el enorme ecosistema de extensiones · inpainting y img2img sin montar pipeline.
**Stack:** Python, GPU, PyTorch, Gradio, modelos locales — **Modelo/API:** local-first (difusión).
**Limitaciones:** requiere GPU con VRAM suficiente; la base de código es veterana y el flujo es menos limpio que alternativas modernas como InvokeAI.
**Elige si:** quieres extensiones y comunidad amplia — **Evita si:** prefieres un flujo moderno y limpio ([InvokeAI](#-invokeai)).
**Combina con:** [sd-webui-controlnet](#-sd-webui-controlnet)
**Repo:** [GitHub](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

### 🎨 Fooocus
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, ocultando parámetros técnicos tras presets inteligentes. Es la opción más sencilla para empezar con difusión local.
**Por qué destaca:** es la opción más sencilla para empezar con difusión local, muy valorada por quienes quieren calidad sin aprender ajustes finos. Su autor (lllyasviel, el mismo de ControlNet) le da credibilidad técnica.
**Cómo funciona:** corre modelos de difusión SDXL sobre PyTorch+GPU optimizando prompts y sampling de forma automática, con una UI web ligera que expone solo lo esencial (estilo, número de imágenes, prompt).
**Instalación:** descargar el paquete portable (un clic, descomprimir y ejecutar `run.bat` en Windows) o `git clone` con su script de arranque. Requiere GPU con VRAM moderada (6 GB+ recomendado).
**Casos:** artes de campaña sin montar pipeline · iteración rápida diaria con calidad SDXL · generación para perfiles no técnicos.
**Stack:** Python, GPU, PyTorch, modelos SDXL locales — **Modelo/API:** local-first (difusión).
**Limitaciones:** requiere GPU; ofrece poco control fino frente a ComfyUI y su ecosistema de extensiones es reducido.
**Elige si:** quieres resultados ya, sin curva — **Evita si:** necesitas control fino del pipeline ([ComfyUI](#-comfyui)).
**Combina con:** [Real-ESRGAN](#-real-esrgan)
**Repo:** [GitHub](https://github.com/lllyasviel/Fooocus)
