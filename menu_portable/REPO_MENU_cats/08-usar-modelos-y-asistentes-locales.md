# 8. Usar modelos y asistentes locales — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `airllm`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=motores,engine,jupyter-notebook

**Qué es:** Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes.
**Stack:** Jupyter Notebook
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/lyogavin/airllm

**Instalación** [+]: `pip install airllm`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `anything-llm`
role=app · exec=local · setup=easy · mcp=True · prov=openai,anthropic,local · tags=rag,agents,local,javascript

**Qué es:** Organiza documentos en espacios de trabajo, crea RAG sin configurar nada y añade agentes con herramientas. Escritorio o Docker multiusuario.
**Stack:** JavaScript, Node.js, React
**Acceso y costes:**
- API de IA: API de IA opcional. Puedes elegir la ruta local documentada o configurar un proveedor remoto; la ruta remota puede requerir API key o acceso propio.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. La inferencia local consume recursos de tu equipo. Los proveedores remotos y servicios del cliente tienen sus propios planes y tarifas.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/Mintplex-Labs/anything-llm

**Instalación** [?]: `Seguir la instalación original: https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres RAG privado sin programar
**Evita si:** necesitas un pipeline de RAG a medida; mira `llama-index`
**Combina con:** `ollama`
**Alternativas (elige una):** `open-webui`, `khoj`, `private-gpt`, `onyx`

## `chatbox`
role=app · exec=hybrid · setup=easy · mcp=False · prov=— · tags=chats,assistant,chatbot,chatgpt,claude,claude-code,copilot,deepseek

**Qué es:** Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz común. Configura conexiones de modelos y conserva conversaciones en una aplicación multiplataforma.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: API de IA opcional. Puedes elegir la ruta local documentada o configurar un proveedor remoto; la ruta remota puede requerir API key o acceso propio.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. La inferencia local consume recursos de tu equipo. Los proveedores remotos y servicios del cliente tienen sus propios planes y tarifas.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/chatboxai/chatbox

**Instalación** [?]: `Seguir la instalación original: https://github.com/chatboxai/chatbox/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un cliente de escritorio que conecte varios modelos
**Evita si:** no quieres mantener modelos o un entorno de ejecución propio
**Alternativas (elige una):** `jan`

## `cherry-studio`
role=app · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic,google,local · tags=chatbot,agents,typescript

**Qué es:** Chatea con decenas de proveedores y modelos locales, usa asistentes predefinidos, MCP y base de conocimiento desde una sola app.
**Stack:** TypeScript, Electron, React
**Acceso y costes:**
- API de IA: API de IA opcional. Puedes elegir la ruta local documentada o configurar un proveedor remoto; la ruta remota puede requerir API key o acceso propio.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. La inferencia local consume recursos de tu equipo. Los proveedores remotos y servicios del cliente tienen sus propios planes y tarifas.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/CherryHQ/cherry-studio

**Instalación** [?]: `Seguir la instalación original: https://github.com/CherryHQ/cherry-studio/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres una app de escritorio multi-proveedor completa
**Evita si:** solo quieres modelos locales simples; mira `jan`
**Combina con:** `ollama`
**Alternativas (elige una):** `jan`, `lobehub`

## `exo`
role=runtime · exec=local · setup=medium · mcp=False · prov=local · tags=inference,local,python

**Qué es:** Une Macs, PCs o teléfonos en un clúster que comparte la carga de un modelo que no cabría en uno solo.
**Stack:** Python, MLX
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/exo-explore/exo

**Instalación** [?]: `Seguir la instalación original: https://github.com/exo-explore/exo/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tienes varios equipos y quieres correr un modelo grande
**Evita si:** un solo equipo te basta; mira `ollama`
**Combina con:** `open-webui`

## `freetoken`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=motores,engine,python

**Qué es:** Herramientas para servir modelos de IA en hardware local mediante las rutas de inferencia y aceleración del proyecto.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/FlashML-org/FreeToken

**Instalación** [?]: `Seguir la instalación original: https://github.com/FlashML-org/FreeToken/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Herramientas para servir modelos de IA en hardware local mediante las rutas de inferencia y aceleración del proyecto.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `hermes-desktop`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=agents,ui,typescript

**Qué es:** Para quien quiere usar Hermes Agent como aplicación y no solo desde la terminal.
**Stack:** TypeScript, Electron
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/fathah/hermes-desktop

**Instalación** [?]: `Seguir la instalación original: https://github.com/fathah/hermes-desktop/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** usas Hermes Agent y prefieres una app de escritorio
**Evita si:** no usas Hermes
**Combina con:** `hermes-agent`

## `jan`
role=app · exec=local · setup=easy · mcp=False · prov=local,openai · tags=chatbot,local,rust

**Qué es:** Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. Comprueba el modelo y backend activo: el modo local necesita recursos de tu equipo y la ruta remota conserva sus propios requisitos de acceso.
**Stack:** Rust, TypeScript, Tauri
**Acceso y costes:**
- API de IA: API de IA opcional. Puedes elegir la ruta local documentada o configurar un proveedor remoto; la ruta remota puede requerir API key o acceso propio.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. La inferencia local consume recursos de tu equipo. Los proveedores remotos y servicios del cliente tienen sus propios planes y tarifas.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/janhq/jan

**Instalación** [?]: `Seguir la instalación original: https://github.com/janhq/jan/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un ChatGPT local en tu escritorio
**Evita si:** necesitas multiusuario; mira `open-webui`
**Combina con:** `ollama`
**Alternativas (elige una):** `cherry-studio`, `textgen`, `chatbox`

## `khoj`
role=app · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,local · tags=research,rag,agents,python

**Qué es:** Busca en tus documentos y en internet, crea agentes personalizados, programa resúmenes y hace investigación profunda. Accesible desde web, Obsidian, Emacs o WhatsApp.
**Stack:** Python, Django, Next.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/khoj-ai/khoj

**Instalación** [?]: `Seguir la instalación original: https://github.com/khoj-ai/khoj/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un asistente sobre tus notas personales
**Evita si:** necesitas una plataforma de equipo; mira `anything-llm`
**Combina con:** `ollama`
**Alternativas (elige una):** `anything-llm`, `surfsense`

## `librechat`
role=app · exec=hybrid · setup=medium · mcp=True · prov=openai,anthropic,google,local · tags=chatbot,agents,typescript,docker

**Qué es:** Une OpenAI, Anthropic, Google, Azure, OpenRouter y modelos locales con agentes, artifacts, búsqueda y control de usuarios.
**Stack:** TypeScript, React, Node.js, MongoDB
**Acceso y costes:**
- API de IA: API de IA opcional. Puedes elegir la ruta local documentada o configurar un proveedor remoto; la ruta remota puede requerir API key o acceso propio.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. La inferencia local consume recursos de tu equipo. Los proveedores remotos y servicios del cliente tienen sus propios planes y tarifas.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/LibreChat-AI/LibreChat

**Instalación** [?]: `Seguir la instalación original: https://github.com/LibreChat-AI/LibreChat/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres todos los proveedores en un chat con SSO
**Evita si:** usas sobre todo modelos locales; mira `open-webui`
**Combina con:** `litellm`, `ollama`
**Alternativas (elige una):** `open-webui`, `lobehub`

## `llama-cpp`
role=runtime · exec=local · setup=medium · mcp=False · prov=local · tags=inference,local,cpp

**Qué es:** Base de Ollama, LM Studio y muchas apps. Incluye un servidor compatible con OpenAI y herramientas para cuantizar modelos GGUF.
**Stack:** C++, C, CUDA, Metal
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/ggml-org/llama.cpp

**Instalación** [?]: `Seguir la instalación original: https://github.com/ggml-org/llama.cpp/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres el máximo control y rendimiento local
**Evita si:** prefieres simplicidad; mira `ollama`
**Combina con:** `open-webui`
**Alternativas (elige una):** `ollama`, `llamafile`, `localai`

## `llamafile`
role=runtime · exec=local · setup=easy · mcp=False · prov=local · tags=inference,local,cpp

**Qué es:** Empaqueta modelo y motor en un ejecutable que funciona en Windows, macOS y Linux sin instalar nada. Proyecto de Mozilla.
**Stack:** C++, Cosmopolitan
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/mozilla-ai/llamafile

**Instalación** [?]: `Seguir la instalación original: https://github.com/mozilla-ai/llamafile/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres repartir un modelo que funcione con doble clic
**Evita si:** vas a cambiar de modelos a menudo; mira `ollama`
**Alternativas (elige una):** `ollama`, `llama-cpp`

## `llmfit`
role=library · exec=hybrid · setup=easy · mcp=False · prov=— · tags=inference,local,rust

**Qué es:** Resuelve la elección subjetiva de modelo: la conviertes en un flujo objetivo y reproducible con métricas.
**Stack:** Go/Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/AlexsJones/llmfit

**Instalación** [+]: `uv tool install -U llmfit`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas elegir modelo con datos y reproducibilidad
**Evita si:** ya tienes el modelo decidido o tu caso no justifica un harness de evaluación
**Combina con:** `litellm`, `langfuse`

## `lobehub`
role=app · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic,google,local · tags=chatbot,agents,typescript

**Qué es:** Antes LobeChat: chat elegante con agentes, plugins, base de conocimiento y despliegue en un clic. Ahora añade agentes que trabajan en tus chats de equipo.
**Stack:** TypeScript, Next.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/lobehub/lobehub

**Instalación** [?]: `Seguir la instalación original: https://github.com/lobehub/lobehub/blob/canary/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un chat bonito y extensible con agentes
**Evita si:** necesitas el máximo control empresarial; mira `librechat`
**Combina con:** `ollama`
**Alternativas (elige una):** `open-webui`, `librechat`, `cherry-studio`

## `localai`
role=runtime · exec=local · setup=medium · mcp=False · prov=local · tags=inference,local,go,docker

**Qué es:** Sustituye la API de OpenAI por una propia que corre modelos abiertos de muchos tipos. Útil para apps que ya hablan con OpenAI.
**Stack:** Go, C++, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/mudler/LocalAI

**Instalación** [?]: `Seguir la instalación original: https://github.com/mudler/LocalAI/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres una API tipo OpenAI local para varias modalidades
**Evita si:** solo necesitas chat local simple; mira `ollama`
**Combina con:** `anything-llm`
**Alternativas (elige una):** `ollama`, `llama-cpp`

## `magnitude`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=motores,engine,rust

**Qué es:** Motor de inferencia local que adapta su ejecución al hardware y ofrece conexiones para agentes y aplicaciones.
**Stack:** Rust, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/magnitudedev/magnitude

**Instalación** [?]: `Seguir la instalación original: https://github.com/magnitudedev/magnitude/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Motor de inferencia local que adapta su ejecución al hardware y ofrece conexiones para agentes y aplicaciones.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `muse-spark`
role=app · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=workspaces,download-muse-ai,download-muse-spark,muse,muse-ai,muse-spark,muse-spark-1-1,muse-spark-1-2

**Qué es:** Proyecto de terceros que se presenta como un estudio de IA de escritorio; su afiliación y funciones no están verificadas. El README describe un cliente multimodal y distribuciones binarias; el alcance real no se comprobó ejecutándolo.
**Stack:** Python
**Acceso y costes:**
- API de IA: API: por confirmar. No se da por verificada la autenticación o el coste real de esta integración de terceros.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Ejecución con modelos locales por confirmar. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Coste por confirmar. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/muse-spark-app/muse-spark

**Instalación** [?]: `Seguir la instalación original: https://github.com/muse-spark-app/muse-spark/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** solo deseas revisar su procedencia y código antes de evaluar el proyecto
**Evita si:** no quieres mantener modelos o un entorno de ejecución propio

## `nextcloud-server`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=workspaces,cloud,collaboration,decentralized,design,distributed,enterprise,federation

**Qué es:** Servidor de Nextcloud para almacenar y compartir archivos, contactos y calendarios en infraestructura propia. Opera una nube personal con usuarios, almacenamiento y aplicaciones integrables.
**Stack:** PHP, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/nextcloud/server

**Instalación** [?]: `Seguir la instalación original: https://github.com/nextcloud/server/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas una plataforma autoalojada para documentos y colaboración
**Evita si:** no quieres mantener modelos o un entorno de ejecución propio

## `notebooklm-mcp-cli`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=— · tags=mcp,notebooks,python

**Qué es:** Convierte NotebookLM en una herramienta invocable por asistentes.
**Stack:** Python, MCP
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta documentada usa un servicio en línea mediante sesión o acceso propio; no implica ejecución local del modelo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Conecta un cliente MCP con una sesión de NotebookLM. El acceso y los límites los determina Google, además del agente que invoque las herramientas.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/jacob-bd/gemini-notebook-mcp-cli

**Instalación** [?]: `Seguir la instalación original: https://github.com/jacob-bd/gemini-notebook-mcp-cli/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** integras NotebookLM con tu asistente MCP
**Evita si:** prefieres la API directa en scripts (notebooklm-py)
**Combina con:** `notebooklm-py`, `awesome-mcp-servers`

## `notebooklm-py`
role=library · exec=cloud · setup=easy · mcp=False · prov=— · tags=notebooks,research,python

**Qué es:** Cubre el vacío de automatización que la interfaz web oficial no ofrece.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta documentada usa un servicio en línea mediante sesión o acceso propio; no implica ejecución local del modelo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Cliente no oficial que reutiliza una sesión de Google/NotebookLM. No es un modelo local ni una API oficial incluida por Claude o Codex.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/teng-lin/notebooklm-py

**Instalación** [?]: `Seguir la instalación original: https://github.com/teng-lin/notebooklm-py/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** automatizas el NotebookLM real y aceptas el riesgo de API no oficial
**Evita si:** quieres todo local (open-notebook)
**Combina con:** `notebooklm-mcp-cli`

## `odysseus`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=agents,local,python,docker

**Qué es:** Sustituye la dispersión entre varios SaaS por un único panel que tú controlas.
**Stack:** Python, React, PostgreSQL
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/odysseus-dev/odysseus

**Instalación** [?]: `Seguir la instalación original: https://github.com/odysseus-dev/odysseus/blob/dev/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres operación privada todo-en-uno y aceptas operar la infra
**Evita si:** prefieres SaaS gestionado sin mantenimiento
**Combina con:** `open-notebook`, `ecc`, `mem0`

## `ollama`
role=runtime · exec=local · setup=easy · mcp=False · prov=local · tags=inference,local,go

**Qué es:** Un comando para bajar y ejecutar modelos como Qwen, Gemma, DeepSeek o gpt-oss. Casi todas las apps de IA local lo soportan.
**Stack:** Go, C++
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/ollama/ollama

**Instalación** [?]: `Seguir la instalación original: https://github.com/ollama/ollama/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres modelos locales funcionando en minutos
**Evita si:** necesitas servir a muchos usuarios con GPU; mira `vllm`
**Combina con:** `open-webui`, `n8n`, `anything-llm`
**Alternativas (elige una):** `llama-cpp`, `localai`, `llamafile`

## `open-notebook`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=notebooks,research,typescript,docker

**Qué es:** Resuelve el envío de documentos sensibles a la nube que implica el NotebookLM oficial.
**Stack:** Python (FastAPI), React/Next.js
**Acceso y costes:**
- API de IA: API de IA opcional. Puedes elegir la ruta local documentada o configurar un proveedor remoto; la ruta remota puede requerir API key o acceso propio.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. La inferencia local consume recursos de tu equipo. Los proveedores remotos y servicios del cliente tienen sus propios planes y tarifas.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/lfnovo/open-notebook

**Instalación** [?]: `Seguir la instalación original: https://github.com/lfnovo/open-notebook/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres NotebookLM privado y sin cuotas
**Evita si:** prefieres el NotebookLM real automatizado (notebooklm-py)
**Combina con:** `odysseus`, `markitdown`
**Alternativas (elige una):** `deeptutor`, `surfsense`

## `open-webui`
role=app · exec=local · setup=easy · mcp=True · prov=openai,local · tags=chatbot,local,rag,docker

**Qué es:** Da a tu equipo un chat privado con usuarios, documentos, búsqueda web, herramientas y modelos locales o en la nube.
**Stack:** Python, Svelte, Docker
**Acceso y costes:**
- API de IA: API de IA opcional. Puedes elegir la ruta local documentada o configurar un proveedor remoto; la ruta remota puede requerir API key o acceso propio.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. La inferencia local consume recursos de tu equipo. Los proveedores remotos y servicios del cliente tienen sus propios planes y tarifas.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/open-webui/open-webui

**Instalación** [+]: `pip install open-webui`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas un ChatGPT privado para tu equipo
**Evita si:** solo quieres una app de escritorio individual; mira `jan`
**Combina con:** `ollama`, `searxng`, `litellm`
**Alternativas (elige una):** `librechat`, `lobehub`, `anything-llm`, `textgen`

## `private-gpt`
role=platform · exec=local · setup=medium · mcp=False · prov=local,openai · tags=rag,local,python

**Qué es:** Ofrece una API lista para construir apps de IA sin que los datos salgan de tu entorno. Funciona con cualquier motor compatible con OpenAI.
**Stack:** Python, FastAPI
**Acceso y costes:**
- API de IA: API de IA opcional. Puedes elegir la ruta local documentada o configurar un proveedor remoto; la ruta remota puede requerir API key o acceso propio.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. La inferencia local consume recursos de tu equipo. Los proveedores remotos y servicios del cliente tienen sus propios planes y tarifas.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/zylon-ai/private-gpt

**Instalación** [?]: `Seguir la instalación original: https://github.com/zylon-ai/private-gpt/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** construyes un producto de IA que no puede enviar datos fuera
**Evita si:** quieres una app lista para usuarios finales; mira `anything-llm`
**Combina con:** `ollama`, `qdrant`
**Alternativas (elige una):** `anything-llm`

## `surfsense`
role=app · exec=hybrid · setup=medium · mcp=False · prov=openai,local · tags=research,rag,notebooks,python

**Qué es:** Conecta tus fuentes (archivos, Slack, Notion, GitHub, web) y conversa con ellas con citas, genera podcasts y reportes. Puede funcionar sin conexión.
**Stack:** Python, FastAPI, Next.js, PostgreSQL
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/MODSetter/SurfSense

**Instalación** [?]: `Seguir la instalación original: https://github.com/MODSetter/SurfSense/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un NotebookLM propio y con más fuentes
**Evita si:** solo quieres el NotebookLM de Google por código; mira `notebooklm-py`
**Combina con:** `ollama`
**Alternativas (elige una):** `open-notebook`, `khoj`

## `textgen`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=chatbot,local,inference,python

**Qué es:** La clásica "oobabooga": carga modelos en muchos formatos y backends, con chat, modo notebook y entrenamiento LoRA.
**Stack:** Python, Gradio
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/oobabooga/textgen

**Instalación** [?]: `Seguir la instalación original: https://github.com/oobabooga/textgen/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres experimentar con muchos backends locales
**Evita si:** quieres algo sencillo; mira `jan` u `ollama`
**Alternativas (elige una):** `jan`, `open-webui`

## `transformers.js`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=motores,browser,javascript,transformers,webml

**Qué es:** Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y audio en JavaScript. Carga modelos compatibles y realiza inferencia en el navegador o en entornos JavaScript sin un servidor de modelos propio.
**Stack:** JavaScript, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/huggingface/transformers.js

**Instalación** [+]: `npm i @huggingface/transformers`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres ejecutar un modelo compatible dentro del navegador
**Evita si:** no quieres mantener modelos o un entorno de ejecución propio
**Combina con:** `swr`
