[Áreas](../areas.md) · [Inicio](../README.md)

# Programación, backend y despliegue

Elige un agente de código, comprende un proyecto y prepara su infraestructura, pruebas y seguimiento.

111 repos únicos · 5 subcategorías. [Ver en el explorador](../../docs/index.html#/area/desarrollo).

## Opciones para empezar

[Codex CLI](../fichas/codex.md), [Repomix](../fichas/repomix.md), [coolify](../fichas/coolify.md)

Son opciones para comparar. No es necesario instalar todas.

## Subcategorías

### Agentes y editores para programar

Herramientas de terminal, IDE y sesiones de desarrollo.

[Explorar 22 repos](../../docs/index.html#/explorar?area=desarrollo&topic=dev-codigo)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [Aider](../fichas/aider.md) | Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos. | API de IA opcional |
| [Android Skills](../fichas/android-skills.md) | Añade guías oficiales de Android a Claude Code, Codex o Antigravity para revisar, compilar y probar aplicaciones Android. | Sin clave propia de API de IA en la ruta básica |
| [Antigravity CLI](../fichas/antigravity-cli.md) | Agente de programación de Google para la terminal (agy), con subagentes, MCP y skills; se distribuye en binarios, sin código fuente. | Sin clave propia de API de IA en la ruta básica |
| [Claude Code](../fichas/claude-code.md) | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. | API de IA opcional |
| [Cline](../fichas/cline.md) | Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. | API de IA opcional |
| [Codex CLI](../fichas/codex.md) | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. | API de IA opcional |
| [DeepSeek Harness (DSH)](../fichas/deepseek-harness.md) | Harness de agentes de DeepSeek en vista previa, con arquitectura de plugins, Web UI local y proveedores de modelos configurables. | Depende de la ruta elegida |
| [Gemini CLI](../fichas/gemini-cli.md) | CLI de Google orientado actualmente a Code Assist empresarial; el README remite el acceso individual a Antigravity CLI. | API de IA opcional |
| [goose](../fichas/goose.md) | Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM. | API de IA opcional |
| [Kilo Code](../fichas/kilocode.md) | Agente de código abierto para VS Code, JetBrains y la terminal, con más de 500 modelos, modos de trabajo y marketplace de agentes, skills y MCP. | API de IA necesaria |
| [MiMo-Code](../fichas/mimo-code.md) | Asistente de código de Xiaomi MiMo para la terminal con herramientas de archivos, comandos, Git y memoria persistente. | API de IA opcional |
| [mini-swe-agent](../fichas/mini-swe-agent.md) | Agente de ingeniería de software mínimo (unas 100 líneas) del equipo de SWE-bench y SWE-agent: solo usa bash y rinde alto en SWE-bench. | API de IA opcional |
| [Open Interpreter](../fichas/open-interpreter.md) | Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con modelos locales o baratos. | Depende de la ruta elegida |
| [Open SWE](../fichas/open-swe.md) | Robin, fábrica de cambios sobre Deep Agents que despliega con Managed Deep Agents y entrega propuestas revisables. | API de IA necesaria |
| [OpenCode](../fichas/opencode.md) | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. | API de IA opcional |
| [opencode-manager](../fichas/opencode-manager.md) | Interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil. | Depende de la ruta elegida |
| [OpenCursor](../fichas/opencursor.md) | Extensión abierta de VS Code con chat de agente, búsqueda semántica, herramientas y conexión a varios modelos. | API de IA opcional |
| [OpenHands](../fichas/openhands.md) | Agent Canvas: centro de sesiones autoalojado para OpenHands, Claude Code, Codex y agentes ACP. | API de IA opcional |
| [openidea](../fichas/openidea.md) | Entorno de desarrollo con editor, depurador, Git y herramientas para trabajar con código en distintos lenguajes. | Sin clave propia de API de IA en la ruta básica |
| [Qwen Code](../fichas/qwen-code.md) | Agente de código de terminal del equipo Qwen, multiprotocolo (OpenAI, Anthropic, Gemini, Qwen o modelos locales), con skills, subagentes y MCP. | API de IA opcional |
| [T3 Code](../fichas/t3code.md) | Interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina. | API de IA opcional |
| [Zed](../fichas/zed.md) | Editor de código de alto rendimiento y multijugador, de los creadores de Atom y Tree-sitter, con IA integrada y agentes externos por ACP. | API de IA opcional |

### Comprender y revisar código

Índices y análisis para orientarte dentro de repositorios.

[Explorar 27 repos](../../docs/index.html#/explorar?area=desarrollo&topic=dev-comprender)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [APScheduler](../fichas/apscheduler.md) | Programa funciones Python para un horario, un intervalo o una fecha concreta dentro de una aplicación propia. | Sin clave propia de API de IA en la ruta básica |
| [ast-grep](../fichas/ast-grep.md) | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. | Sin clave propia de API de IA en la ruta básica |
| [Biome](../fichas/biome.md) | Formateador y linter en un solo binario para JavaScript, TypeScript, JSX, JSON, CSS, GraphQL y más, usable por CLI y LSP. | Sin clave propia de API de IA en la ruta básica |
| [codebase-memory-mcp](../fichas/codebase-memory-mcp.md) | Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para agentes. | API de IA opcional |
| [codegraph](../fichas/codegraph.md) | CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada archivo. | API de IA opcional |
| [floorplan](../fichas/floorplan.md) | Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto. | Sin clave propia de API de IA en la ruta básica |
| [fzf](../fichas/fzf.md) | Buscador difuso de línea de comandos y kit de interfaces de terminal para seleccionar archivos, historial o cualquier lista de forma interactiva. | Sin clave propia de API de IA en la ruta básica |
| [GitHub CLI](../fichas/cli.md) | CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. | Sin clave propia de API de IA en la ruta básica |
| [Gitleaks](../fichas/gitleaks.md) | Detector de secretos (contraseñas, claves de API, tokens) en repositorios git, archivos y stdin, usable como hook o acción de CI. | Sin clave propia de API de IA en la ruta básica |
| [GitNexus](../fichas/gitnexus.md) | Explora flujos de ejecución y previsualiza renombrados semánticos con el índice de GitNexus. El visor web se conecta al servidor del CLI. | Sin clave propia de API de IA en la ruta básica |
| [graphify](../fichas/graphify.md) | CLI y skill que convierten código y documentos en un grafo consultable; el código se analiza localmente con AST y la extracción semántica tiene rutas separadas. | API de IA opcional |
| [Hishel](../fichas/hishel.md) | Añade caché a peticiones HTTP de Python con políticas de expiración y adaptadores de almacenamiento reutilizables. | Sin clave propia de API de IA en la ruta básica |
| [lazygit](../fichas/lazygit.md) | Interfaz de terminal sencilla para git: preparar fragmentos o líneas, rebase interactivo, cherry-pick y gestión de ramas con atajos. | Sin clave propia de API de IA en la ruta básica |
| [npkill](../fichas/npkill.md) | Muestra cuánto espacio ocupan carpetas generadas por herramientas de desarrollo y permite revisarlas antes de eliminar residuos. | Sin clave propia de API de IA en la ruta básica |
| [Open Code Review](../fichas/open-code-review.md) | Revisa cambios de código con reglas y un informe guiado, usando su propio proveedor de IA o el asistente de programación que ya tienes. | API de IA opcional |
| [openai-python](../fichas/openai-python.md) | SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API. | API de IA necesaria |
| [Pake](../fichas/pake.md) | Convierte una página web o una carpeta con tu web estática en una app de escritorio ligera para macOS, Windows o Linux con un solo comando. | Sin clave propia de API de IA en la ruta básica |
| [pre-commit](../fichas/pre-commit.md) | Framework para gestionar y ejecutar hooks de git multilenguaje antes de cada commit: linters, formateadores y escáneres declarados en YAML. | Sin clave propia de API de IA en la ruta básica |
| [PyBreaker](../fichas/pybreaker.md) | Protege una integración Python con un interruptor que pausa llamadas tras varios fallos y después permite comprobar si volvió el servicio. | Sin clave propia de API de IA en la ruta básica |
| [Repomix](../fichas/repomix.md) | Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. | Sin clave propia de API de IA en la ruta básica |
| [Requests Cache](../fichas/requests-cache.md) | Guarda respuestas de solicitudes Python para reutilizarlas cuando sean válidas y reducir viajes repetidos a un servicio HTTP. | Sin clave propia de API de IA en la ruta básica |
| [ripgrep](../fichas/ripgrep.md) | Búsqueda recursiva de texto por expresiones regulares muy rápida que respeta .gitignore y omite archivos ocultos y binarios. | Sin clave propia de API de IA en la ruta básica |
| [Ruff](../fichas/ruff.md) | Linter y formateador de Python extremadamente rápido escrito en Rust, compatible con Flake8, isort y Black, con más de 800 reglas. | Sin clave propia de API de IA en la ruta básica |
| [SonarQube Community Build](../fichas/sonarqube.md) | Plataforma de inspección continua de calidad y seguridad del código: análisis estático de bugs, vulnerabilidades y mantenibilidad en muchos lenguajes. | Sin clave propia de API de IA en la ruta básica |
| [SWE-bench](../fichas/swe-bench.md) | Benchmark para evaluar si los modelos resuelven issues reales de GitHub. | API de IA opcional |
| [tree-sitter](../fichas/tree-sitter.md) | Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código. | Sin clave propia de API de IA en la ruta básica |
| [TruffleHog](../fichas/trufflehog.md) | Busca, clasifica, verifica y analiza credenciales filtradas en git, chats, wikis, logs, almacenes de objetos y sistemas de archivos. | Sin clave propia de API de IA en la ruta básica |

### Backend, alojamiento y despliegue

Infraestructura, servicios y herramientas de operación.

[Explorar 32 repos](../../docs/index.html#/explorar?area=desarrollo&topic=dev-infra)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [Agent Protocol](../fichas/agent-protocol.md) | Especificación de LangChain para exponer cualquier agente con una API estándar de ejecuciones, hilos y estado. | Sin clave propia de API de IA en la ruta básica |
| [Agent Substrate](../fichas/agent-substrate.md) | Aloja tareas con estado en Kubernetes y permite probar cómo se suspenden y reanudan dentro de entornos separados. | Sin clave propia de API de IA en la ruta básica |
| [agent-desktop](../fichas/agent-desktop.md) | CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y operar aplicaciones de escritorio. | Sin clave propia de API de IA en la ruta básica |
| [Appwrite](../fichas/appwrite.md) | Plataforma de backend abierta orientada a agentes y desarrolladores: autenticación, bases de datos, almacenamiento, funciones, mensajería, tiempo real y hosting, con MCP. | Sin clave propia de API de IA en la ruta básica |
| [Caddy](../fichas/caddy.md) | Servidor web y proxy inverso extensible con HTTPS automático por defecto, configurable con Caddyfile o JSON y API. | Sin clave propia de API de IA en la ruta básica |
| [CasaOS](../fichas/casaos.md) | Entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos. | Sin clave propia de API de IA en la ruta básica |
| [claude-task-master](../fichas/claude-task-master.md) | Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP. | API de IA opcional |
| [Composio](../fichas/composio.md) | Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps reales. | Sin clave propia de API de IA en la ruta básica |
| [coolify](../fichas/coolify.md) | Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios. | Sin clave propia de API de IA en la ruta básica |
| [Dokploy](../fichas/dokploy.md) | Plataforma como servicio autoalojada, alternativa a Vercel, Netlify y Heroku, para desplegar aplicaciones y bases de datos con Docker y Traefik. | Sin clave propia de API de IA en la ruta básica |
| [E2B](../fichas/e2b.md) | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. | Sin clave propia de API de IA en la ruta básica |
| [free-for-dev](../fichas/free-for-dev.md) | Directorio de servicios de infraestructura y desarrollo que ofrecen planes o niveles gratuitos. | Sin clave propia de API de IA en la ruta básica |
| [FreeDomain](../fichas/freedomain.md) | Recursos de registro de dominios y aprendizaje práctico de DNS publicados por DigitalPlat. | Sin clave propia de API de IA en la ruta básica |
| [frp](../fichas/frp.md) | Proxy inverso rápido para exponer servidores locales detrás de NAT o cortafuegos a internet, con TCP, UDP, HTTP, HTTPS y modo P2P. | Sin clave propia de API de IA en la ruta básica |
| [Gemini Computer Use (preview)](../fichas/computer-use-preview.md) | Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web. | API de IA necesaria |
| [Headscale](../fichas/headscale.md) | Implementación abierta y autoalojada del servidor de control de Tailscale para crear tu propia red privada WireGuard con los clientes oficiales. | Sin clave propia de API de IA en la ruta básica |
| [Kiri](../fichas/kiri.md) | Ejecuta contenedores de desarrollo y permite verlos desde una aplicación de escritorio que crea su propio contexto de Docker. | Sin clave propia de API de IA en la ruta básica |
| [LibreTranslate](../fichas/libretranslate.md) | Traduce texto con una interfaz web y una API que puedes alojar en tu equipo usando modelos de traducción de Argos. | Sin clave propia de API de IA en la ruta básica |
| [MasterDnsVPN](../fichas/masterdnsvpn.md) | Implementación en Go de un túnel que transporta tráfico TCP mediante consultas y respuestas DNS. | Sin clave propia de API de IA en la ruta básica |
| [NemoClaw](../fichas/nemoclaw.md) | Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes. | Depende de la ruta elegida |
| [NetBird](../fichas/netbird.md) | Red privada superpuesta basada en WireGuard con SSO, MFA y control de acceso granular, autoalojable o en la nube. | Sin clave propia de API de IA en la ruta básica |
| [nodeterm](../fichas/nodeterm.md) | Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con organización por proyecto. | API de IA opcional |
| [Pangolin Community Edition](../fichas/pangolin.md) | Controla qué personas pueden entrar a aplicaciones propias mediante un proxy y reglas de acceso administradas por tu equipo. | Sin clave propia de API de IA en la ruta básica |
| [Portainer CE](../fichas/portainer.md) | Interfaz web ligera para gestionar contenedores en Docker, Swarm, Podman, Kubernetes y ACI (Community Edition). | Sin clave propia de API de IA en la ruta básica |
| [sandbox](../fichas/sandbox.md) | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. | Sin clave propia de API de IA en la ruta básica |
| [Screen Relay](../fichas/screen-relay.md) | Muestra en el navegador un escritorio de prueba para ver una aplicación gráfica sin usar tu escritorio personal. | Sin clave propia de API de IA en la ruta básica |
| [shepherd](../fichas/shepherd.md) | Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus recorridos. | API de IA opcional |
| [supabase](../fichas/supabase.md) | Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones. | Sin clave propia de API de IA en la ruta básica |
| [Tailcat](../fichas/tailcat.md) | Conecta dos equipos propios para el intercambio temporal de datos mediante un enlace cifrado entre los extremos. | Sin clave propia de API de IA en la ruta básica |
| [Traefik Proxy](../fichas/traefik.md) | Proxy inverso y balanceador de carga dinámico para contenedores y microservicios que se configura automáticamente desde Docker, Kubernetes y otros. | Sin clave propia de API de IA en la ruta básica |
| [Uptime Kuma](../fichas/uptime-kuma.md) | Monitor de disponibilidad autoalojado y fácil de usar: comprueba webs y servicios, envía alertas a más de 90 canales y publica páginas de estado. | Sin clave propia de API de IA en la ruta básica |
| [WireGuard Easy](../fichas/wg-easy.md) | La forma más sencilla de ejecutar WireGuard VPN con interfaz web para gestionar clientes, códigos QR, estadísticas y 2FA. | Sin clave propia de API de IA en la ruta básica |

### Evaluación, trazas y observabilidad

Medir resultados y revisar lo que hace una aplicación de IA.

[Explorar 14 repos](../../docs/index.html#/explorar?area=desarrollo&topic=dev-evaluar)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [ccusage](../fichas/ccusage.md) | Resume los tokens y estima el coste de tus sesiones de asistentes a partir de los registros locales de sus terminales. | Sin clave propia de API de IA en la ruta básica |
| [Claude-Code-Usage-Monitor](../fichas/claude-code-usage-monitor.md) | Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a partir de la información disponible. | Sin clave propia de API de IA en la ruta básica |
| [DeepEval](../fichas/deepeval.md) | Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. | API de IA opcional |
| [Helicone](../fichas/helicone.md) | Pasarela de IA y plataforma de observabilidad de LLM abierta: registra peticiones, costes y latencias, gestiona prompts y enruta a más de 100 modelos. | Sin clave propia de API de IA en la ruta básica |
| [langfuse](../fichas/langfuse.md) | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. | API de IA opcional |
| [LM Evaluation Harness](../fichas/lm-eval-harness.md) | Arnés estándar de EleutherAI para evaluar modelos de lenguaje en cientos de benchmarks académicos con backends Hugging Face, vLLM, SGLang o APIs. | API de IA opcional |
| [loguru](../fichas/loguru.md) | Librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa. | Sin clave propia de API de IA en la ruta básica |
| [MLflow](../fichas/mlflow.md) | Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro. | API de IA opcional |
| [NeMo Guardrails](../fichas/guardrails.md) | Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales con LLM. | Depende de la ruta elegida |
| [OpenLLMetry](../fichas/openllmetry.md) | Instrumentación abierta basada en OpenTelemetry para aplicaciones de LLM: traza llamadas a modelos, bases vectoriales y frameworks hacia tu backend de observabilidad. | Sin clave propia de API de IA en la ruta básica |
| [Opik](../fichas/opik.md) | Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes. | API de IA opcional |
| [Phoenix](../fichas/phoenix.md) | Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry. | API de IA opcional |
| [promptfoo](../fichas/promptfoo.md) | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. | API de IA opcional |
| [Ragas](../fichas/ragas.md) | Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. | Depende de la ruta elegida |

### Contexto, consumo y enrutamiento

Reducir contexto innecesario y organizar el acceso a modelos.

[Explorar 16 repos](../../docs/index.html#/explorar?area=desarrollo&topic=dev-contexto)

| Repositorio | Para qué sirve | API de IA |
|---|---|---|
| [BentoML](../fichas/bentoml.md) | Framework Python para convertir modelos y pipelines de IA en APIs de producción, con empaquetado en imágenes Docker y despliegue reproducible. | Sin clave propia de API de IA en la ruta básica |
| [claude-code-router](../fichas/claude-code-router.md) | Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local. | Depende de la ruta elegida |
| [GPTCache](../fichas/gptcache.md) | Reutiliza respuestas de consultas parecidas a un modelo mediante una caché semántica con reglas de comparación configurables. | API de IA opcional |
| [GPUStack](../fichas/gpustack.md) | Gestor de clústeres de GPU para servir modelos de IA: configura vLLM, SGLang o TensorRT-LLM, expone APIs compatibles con OpenAI y aprovisiona instancias GPU. | Sin clave propia de API de IA en la ruta básica |
| [headroom](../fichas/headroom.md) | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. | API de IA opcional |
| [litellm](../fichas/litellm.md) | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. | API de IA opcional |
| [LLMLingua](../fichas/llmlingua.md) | Acorta texto de entrada para modelos de lenguaje y permite medir cuánto contexto conservas antes de enviar el prompt. | Sin clave propia de API de IA en la ruta básica |
| [OmniRoute](../fichas/omniroute.md) | Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acceso. | API de IA opcional |
| [Portkey AI Gateway](../fichas/portkey-gateway.md) | Centraliza llamadas a distintos proveedores de modelos mediante una pasarela con reglas de ruta, presupuestos y registro de solicitudes. | API de IA necesaria |
| [Ray](../fichas/ray.md) | Motor de cómputo distribuido para IA: escala Python de un portátil a un clúster, con bibliotecas para datos, entrenamiento, ajuste, RL y serving. | Sin clave propia de API de IA en la ruta básica |
| [rtk](../fichas/rtk.md) | Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código. | API de IA opcional |
| [SGLang](../fichas/sglang.md) | Framework de servicio de alto rendimiento para LLM y modelos multimodales. | Sin clave propia de API de IA en la ruta básica |
| [TensorRT-LLM](../fichas/tensorrt-llm.md) | Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de lenguaje con kernels y runtimes especializados. | Sin clave propia de API de IA en la ruta básica |
| [TOON](../fichas/toon-format.md) | Convierte listas de objetos JSON a un texto con encabezado y filas para experimentar con entradas más compactas para modelos. | Sin clave propia de API de IA en la ruta básica |
| [vLLM](../fichas/vllm.md) | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. | Sin clave propia de API de IA en la ruta básica |
| [Xinference](../fichas/xinference.md) | Plataforma abierta de inferencia para modelos de lenguaje, visión, embeddings, reranking, imagen, audio y vídeo, con API compatible con OpenAI y varios motores. | Sin clave propia de API de IA en la ruta básica |

La revisión de documentación no equivale a una instalación probada. Consulta cada ficha para acceso, coste, equipo y pasos de arranque.
