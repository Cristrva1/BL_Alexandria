# 8. Chats, modelos locales y espacios privados — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `airllm`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=motores,engine,jupyter-notebook

**Qué es:** Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes.
**Stack:** Python; GPU o backend compatible; disco y memoria para capas y pesos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa una API de pago; ahorrar VRAM puede exigir mucho disco, RAM y tiempo; los pesos tienen licencia propia
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Que quepa en poca VRAM no significa que un modelo grande sea interactivo en tu equipo
- Coste: Sin pago a un modelo en la ruta básica. No usa una API de pago; ahorrar VRAM puede exigir mucho disco, RAM y tiempo; los pesos tienen licencia propia
- Equipo: Preparación según la ruta elegida. Python; GPU o backend compatible; disco y memoria para capas y pesos
**Repo:** https://github.com/lyogavin/airllm

**Instalación** [+]:

```
pip install airllm
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar inferencia por carga de capas; Probar un modelo que supera la VRAM disponible
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga un modelo de prueba admitido y mide el tiempo de generación además de la VRAM
**Qué comprobar:** Obtienes texto y una medida real de latencia y almacenamiento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `llmfit`, `transformers`, `peft`

## `anything-llm`
role=app · exec=local · setup=easy · mcp=True · prov=openai,anthropic,local · tags=rag,agents,local,javascript

**Qué es:** App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube.
**Stack:** App de escritorio o Docker; LLM y embeddings; documento de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Puede usar motor local y proveedores remotos; los modelos, servicios y alojamiento tienen costes separados
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Desktop, Docker y móvil tienen capacidades y licencias que debes comprobar; elige también embeddings locales para una ruta privada completa
- Coste: El coste depende del proveedor o la ruta. Puede usar motor local y proveedores remotos; los modelos, servicios y alojamiento tienen costes separados
- Equipo: Preparación según la ruta elegida. App de escritorio o Docker; LLM y embeddings; documento de prueba
**Repo:** https://github.com/Mintplex-Labs/anything-llm

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar documentación propia; Separar bases de conocimiento por proyecto
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un workspace con un PDF corto y consulta un dato presente en él
**Qué comprobar:** Puedes abrir el fragmento que apoya la respuesta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `qdrant`, `litellm`, `localai`, `chroma`, `milvus`
**Alternativas (elige una):** `open-webui`, `khoj`, `private-gpt`, `onyx`

## `chatbox`
role=app · exec=hybrid · setup=easy · mcp=False · prov=— · tags=chats,assistant,chatbot,chatgpt,claude,claude-code,copilot,deepseek

**Qué es:** Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz común.
**Stack:** Instalador Community para tu sistema; proveedor o instancia Ollama
**Acceso y costes:**
- API de IA: API de IA opcional. Community usa GPLv3; planes comerciales y proveedores tienen condiciones propias; Ollama local requiere recursos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. No confundas la edición comunitaria con los servicios comerciales ni un proveedor Claude con Claude Code
- Coste: El coste depende del proveedor o la ruta. Community usa GPLv3; planes comerciales y proveedores tienen condiciones propias; Ollama local requiere recursos
- Equipo: Preparación según la ruta elegida. Instalador Community para tu sistema; proveedor o instancia Ollama
**Repo:** https://github.com/chatboxai/chatbox

**Instalación** [+]:

```
git clone https://github.com/chatboxai/chatbox.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Conversar con varios proveedores; Probar un modelo local desde escritorio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta un proveedor y guarda una conversación con una nota ficticia
**Qué comprobar:** Puedes identificar el modelo y recuperar el chat
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `litellm`, `localai`
**Alternativas (elige una):** `jan`, `nextchat`, `lobehub`

## `cherry-studio`
role=app · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic,google,local · tags=chatbot,agents,typescript

**Qué es:** App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad.
**Stack:** Instalador para Windows, macOS o Linux; proveedor o Ollama/LM Studio
**Acceso y costes:**
- API de IA: API de IA opcional. Los proveedores y funciones remotas pueden cobrar; el código es AGPL y ofrece alternativa de licencia comercial
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es una app multiproveedor; escoger Anthropic u OpenAI no la convierte en sesión de Claude Code o Codex
- Coste: El coste depende del proveedor o la ruta. Los proveedores y funciones remotas pueden cobrar; el código es AGPL y ofrece alternativa de licencia comercial
- Equipo: Preparación según la ruta elegida. Instalador para Windows, macOS o Linux; proveedor o Ollama/LM Studio
**Repo:** https://github.com/CherryHQ/cherry-studio

**Instalación** [?]:

```
Seguir la instalación original: https://cherryai.com/docs/en/getting-started/quick-start/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar respuestas de varios modelos; Organizar una base documental de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Configura un modelo y prueba una pregunta sobre una nota ficticia en un espacio de trabajo
**Qué comprobar:** Puedes comprobar el proveedor y la respuesta usada en la conversación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `litellm`, `playwright-mcp`
**Alternativas (elige una):** `jan`, `lobehub`

## `exo`
role=runtime · exec=local · setup=medium · mcp=False · prov=local · tags=inference,local,python

**Qué es:** Ejecuta modelos grandes repartiéndolos entre varios equipos de tu casa u oficina.
**Stack:** Para app: Apple Silicon y macOS 15.1+; equipos en la misma red y versión; modelo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere API remota; varios equipos, red y almacenamiento son recursos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La app macOS y la ejecución desde fuentes tienen requisitos distintos; Windows no está confirmado en la ruta revisada
- Coste: Sin pago a un modelo en la ruta básica. No requiere API remota; varios equipos, red y almacenamiento son recursos propios
- Equipo: Preparación según la ruta elegida. Para app: Apple Silicon y macOS 15.1+; equipos en la misma red y versión; modelo
**Repo:** https://github.com/exo-explore/exo

**Instalación** [+]:

```
brew install --cask exo
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Compartir memoria entre equipos compatibles; Experimentar con inferencia distribuida local
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Empieza en un Mac y añade un segundo equipo compatible antes de repartir un modelo
**Qué comprobar:** El panel muestra los dispositivos y la distribución de trabajo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `open-webui`, `librechat`, `litellm`, `mlx-lm`

## `freetoken`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=motores,engine,python

**Qué es:** Herramientas para servir modelos de IA en hardware local mediante las rutas de inferencia y aceleración del proyecto.
**Stack:** Python y uv; acelerador compatible; pesos y espacio según modelo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige API remota; pesos, memoria, disco y aceleradores son recursos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Las afirmaciones sobre modelos enormes y velocidad pertenecen al autor y no demuestran que funcionen en cualquier PC
- Coste: Sin pago a un modelo en la ruta básica. No exige API remota; pesos, memoria, disco y aceleradores son recursos propios
- Equipo: Preparación según la ruta elegida. Python y uv; acelerador compatible; pesos y espacio según modelo
**Repo:** https://github.com/FlashML-org/FreeToken

**Instalación** [+]:

```
uv pip install "freetoken[accel]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Experimentar con inferencia de modelos MoE; Evaluar un backend de aceleración local
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sigue el quickstart con el modelo más pequeño compatible y mide memoria y latencia
**Qué comprobar:** Puedes generar una salida y registrar el consumo real de tu equipo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `open-webui`, `litellm`, `codex`

## `hermes-desktop`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=agents,ui,typescript

**Qué es:** App de escritorio que envuelve al agente Hermes en una interfaz nativa.
**Stack:** Instalador oficial del proyecto; backend Hermes local o remoto; proveedor o endpoint local
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La interfaz no incluye créditos; el backend, modelo y servicios externos se presupuestan según ruta
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Proyecto en desarrollo activo; no hace falta aplicar el ejemplo de sudoers del README para explicar o elegir la ruta de instalación
- Coste: El coste depende del proveedor o la ruta. La interfaz no incluye créditos; el backend, modelo y servicios externos se presupuestan según ruta
- Equipo: Preparación según la ruta elegida. Instalador oficial del proyecto; backend Hermes local o remoto; proveedor o endpoint local
**Repo:** https://github.com/fathah/hermes-desktop

**Instalación** [+]:

```
npm install hermes-desktop
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Usar Hermes desde una interfaz de escritorio; Consultar una instancia remota de Hermes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Configura un backend de prueba y confirma la dirección antes de iniciar un chat
**Qué comprobar:** La interfaz muestra el backend y devuelve una respuesta del proveedor elegido
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `hermes-agent`, `ollama`, `mem0`, `vllm`

## `jan`
role=app · exec=local · setup=easy · mcp=False · prov=local,openai · tags=chatbot,local,rust

**Qué es:** Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz.
**Stack:** Instalador de escritorio oficial; RAM y disco; modelo compatible
**Acceso y costes:**
- API de IA: API de IA opcional. El modo local usa tu equipo; los proveedores remotos tienen sus tarifas; modelos tienen licencias propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Para comenzar usa la distribución de escritorio; make dev y yarn son rutas para desarrollar el código de Jan
- Coste: El coste depende del proveedor o la ruta. El modo local usa tu equipo; los proveedores remotos tienen sus tarifas; modelos tienen licencias propias
- Equipo: Preparación según la ruta elegida. Instalador de escritorio oficial; RAM y disco; modelo compatible
**Repo:** https://github.com/janhq/jan

**Instalación** [+]:

```
git clone https://github.com/janhq/jan
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Conversar con un modelo privado; Comparar un modelo local con una API
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Desde la app descarga un modelo pequeño y prueba una conversación local
**Qué comprobar:** Ves el modelo cargado y puedes repetir la consulta sin proveedor remoto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `llmfit`, `ollama`, `playwright-mcp`
**Alternativas (elige una):** `cherry-studio`, `textgen`, `chatbox`

## `khoj`
role=app · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,local · tags=research,rag,agents,python

**Qué es:** Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones.
**Stack:** Ruta self-host o cuenta Cloud; modelo; notas de prueba
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Self-hosting usa tu infraestructura y modelo local o API; Cloud y Enterprise tienen planes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El README admite LLM locales y remotos; no mezcles la instalación de Khoj con su proyecto relacionado Pipali
- Coste: El coste depende del proveedor o la ruta. Self-hosting usa tu infraestructura y modelo local o API; Cloud y Enterprise tienen planes propios
- Equipo: Preparación según la ruta elegida. Ruta self-host o cuenta Cloud; modelo; notas de prueba
**Repo:** https://github.com/khoj-ai/khoj

**Instalación** [+]:

```
python -m pip install 'khoj[local]'
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar notas desde Obsidian; Crear un asistente de investigación personal
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade dos notas y pregunta por un dato que solo aparece en una
**Qué comprobar:** La respuesta permite revisar la nota utilizada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `litellm`, `markitdown`
**Alternativas (elige una):** `anything-llm`, `surfsense`

## `koboldcpp`
role=runtime · exec=local · setup=easy · mcp=False · prov=— · tags=inference,cpp,local,app

**Qué es:** Ejecutable único basado en llama.cpp para correr modelos GGUF en local con interfaz web KoboldAI Lite y APIs compatibles con OpenAI y Ollama.
**Stack:** C++, CMakeLists.txt, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/LostRuins/koboldcpp

**Instalación** [+]:

```
git clone https://github.com/LostRuins/koboldcpp.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: chatear o escribir historias con un modelo local sin instalar dependencias; dar a otras apps una API local compatible con OpenAI u Ollama
**Evita si:** no quieres preparar modelos, dependencias y hardware propios
**Primera prueba propuesta:** Descarga el ejecutable de la release para tu sistema, elige un modelo GGUF pequeño y arráncalo.
**Qué comprobar:** La interfaz web local responde y el endpoint compatible con OpenAI devuelve texto.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `sillytavern`, `open-webui`, `kokoro`
**Alternativas (elige una):** `llamafile`

## `librechat`
role=app · exec=hybrid · setup=medium · mcp=True · prov=openai,anthropic,google,local · tags=chatbot,agents,typescript,docker

**Qué es:** Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada.
**Stack:** Ruta de despliegue elegida; base de datos; proveedor u Ollama
**Acceso y costes:**
- API de IA: API de IA opcional. La interfaz abierta no incluye crédito de modelos; almacenamiento, herramientas y proveedores tienen costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Sus agentes y MCP funcionan dentro de LibreChat; no acreditan usar una suscripción de otro editor para ejecutarlo
- Coste: El coste depende del proveedor o la ruta. La interfaz abierta no incluye crédito de modelos; almacenamiento, herramientas y proveedores tienen costes propios
- Equipo: Preparación según la ruta elegida. Ruta de despliegue elegida; base de datos; proveedor u Ollama
**Repo:** https://github.com/LibreChat-AI/LibreChat

**Instalación** [?]:

```
Seguir la instalación original: https://www.librechat.ai/docs
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Unificar proveedores en una interfaz; Crear asistentes con herramientas y archivos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta un proveedor y prueba un agente sin herramientas antes de añadir archivos
**Qué comprobar:** Puedes identificar el modelo y revisar la conversación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `litellm`, `ollama`, `langfuse`, `llama-cpp`, `pgvector`, `exo`
**Alternativas (elige una):** `open-webui`, `lobehub`

## `llama-cpp`
role=runtime · exec=local · setup=medium · mcp=False · prov=local · tags=inference,local,cpp

**Qué es:** Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo.
**Stack:** Binario o compilación para tu sistema; modelo GGUF; memoria suficiente
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige API remota; cómputo, memoria, disco y licencia de los pesos se revisan por separado
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. No todos los modelos o backends ofrecen las mismas funciones de herramientas y visión
- Coste: Sin pago a un modelo en la ruta básica. No exige API remota; cómputo, memoria, disco y licencia de los pesos se revisan por separado
- Equipo: Preparación según la ruta elegida. Binario o compilación para tu sistema; modelo GGUF; memoria suficiente
**Repo:** https://github.com/ggml-org/llama.cpp

**Instalación** [+]:

```
curl -LsSf https://llama.app/install.sh | sh
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Servir un modelo en CPU; Comparar cuantizaciones de un mismo modelo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta un GGUF pequeño y observa memoria y velocidad de respuesta
**Qué comprobar:** Puedes generar texto y reconocer qué backend y modelo se utilizan
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `open-webui`, `llmfit`, `librechat`, `litellm`
**Alternativas (elige una):** `ollama`, `llamafile`, `localai`

## `llamafile`
role=runtime · exec=local · setup=easy · mcp=False · prov=local · tags=inference,local,cpp

**Qué es:** Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo.
**Stack:** Ejecutable oficial del modelo; RAM y disco; instrucciones de tu sistema
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige API remota; el ejecutable contiene pesos con su propia licencia y consume recursos locales
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El README separa permisos de ejecución Unix y pasos por sistema; no asumas que cualquier archivo grande funciona igual en Windows
- Coste: Sin pago a un modelo en la ruta básica. No exige API remota; el ejecutable contiene pesos con su propia licencia y consume recursos locales
- Equipo: Preparación según la ruta elegida. Ejecutable oficial del modelo; RAM y disco; instrucciones de tu sistema
**Repo:** https://github.com/mozilla-ai/llamafile

**Instalación** [+]:

```
git clone https://github.com/mozilla-ai/llamafile.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Distribuir una demo local de un LLM; Probar inferencia sin montar un servidor complejo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Descarga el ejemplo pequeño y pregunta algo desde su interfaz local
**Qué comprobar:** El ejecutable carga el modelo y devuelve texto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `open-webui`, `anything-llm`, `librechat`
**Alternativas (elige una):** `ollama`, `llama-cpp`, `koboldcpp`

## `llmfit`
role=app · exec=hybrid · setup=easy · mcp=False · prov=— · tags=inference,local,rust

**Qué es:** Inspecciona el hardware y recomienda modelos según memoria, aceleradores y estimaciones de velocidad. Ayuda a elegir antes de descargar; no evalúa la calidad del modelo en una tarea de negocio.
**Stack:** Binario para tu sistema; acceso a datos de hardware
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La estimación no necesita llamar a un LLM; descargar o ejecutar modelos añade recursos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Estima ajuste al hardware y velocidad; no mide por sí mismo la calidad del modelo en tu tarea
- Coste: Sin pago a un modelo en la ruta básica. La estimación no necesita llamar a un LLM; descargar o ejecutar modelos añade recursos
- Equipo: Preparación según la ruta elegida. Binario para tu sistema; acceso a datos de hardware
**Repo:** https://github.com/AlexsJones/llmfit

**Instalación** [+]:

```
winget install --exact --id AlexsJones.llmfit
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Elegir un modelo antes de descargarlo; Comparar requisitos de dos cuantizaciones
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta el inspector y compara RAM y VRAM detectadas con tu equipo
**Qué comprobar:** Las recomendaciones explican qué modelos y cuantizaciones podrían caber
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `llama-cpp`, `vllm`, `airllm`, `jan`, `textgen`

## `lobehub`
role=app · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic,google,local · tags=chatbot,agents,typescript

**Qué es:** Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible.
**Stack:** Docker y Compose; modelo; servicios de la ruta elegida
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El workspace, servicios alojados y modelos tienen condiciones separadas; admite proveedores locales
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Las skills portables y conectar un agente externo son funciones distintas; la página de integración consultada aún está en migración documental
- Coste: El coste depende del proveedor o la ruta. El workspace, servicios alojados y modelos tienen condiciones separadas; admite proveedores locales
- Equipo: Preparación según la ruta elegida. Docker y Compose; modelo; servicios de la ruta elegida
**Repo:** https://github.com/lobehub/lobehub

**Instalación** [+]:

```
mkdir lobehub && cd lobehub
bash <(curl -fsSL https://lobe.li/setup.sh) -l en
docker compose up -d
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar agentes para tareas de equipo; Conectar un agente de código a un espacio de trabajo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un asistente de prueba y distingue su modelo del agente externo que puedas conectar
**Qué comprobar:** Puedes identificar qué proveedor atiende cada conversación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `litellm`, `playwright-mcp`
**Alternativas (elige una):** `open-webui`, `librechat`, `cherry-studio`, `nextchat`, `chatbox`

## `localai`
role=runtime · exec=local · setup=medium · mcp=False · prov=local · tags=inference,local,go,docker

**Qué es:** Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria.
**Stack:** Docker; modelo y backend apropiados al equipo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La ejecución local no necesita un proveedor de pago; modelos y hardware tienen requisitos y licencias propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. No necesitar GPU no garantiza buen rendimiento en cualquier modelo; compatibilidad de API no confirma integración completa con cada agente
- Coste: Sin pago a un modelo en la ruta básica. La ejecución local no necesita un proveedor de pago; modelos y hardware tienen requisitos y licencias propios
- Equipo: Preparación según la ruta elegida. Docker; modelo y backend apropiados al equipo
**Repo:** https://github.com/mudler/LocalAI

**Instalación** [+]:

```
docker run -ti --name local-ai -p 8080:8080 localai/localai:latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Ofrecer una API local a una aplicación; Probar texto o voz con distintos backends
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Arranca el servidor, instala un modelo pequeño y prueba una petición de texto
**Qué comprobar:** El endpoint responde con el modelo elegido
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `anything-llm`, `open-webui`, `librechat`, `chatbox`, `nextchat`
**Alternativas (elige una):** `ollama`, `llama-cpp`

## `magnitude`
role=runtime · exec=local · setup=heavy · mcp=False · prov=local · tags=motores,engine,rust

**Qué es:** Motor de inferencia local que adapta su ejecución al hardware y ofrece conexiones para agentes y aplicaciones.
**Stack:** Sistema y acelerador compatibles; pesos; espacio de caché para optimización
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige proveedor API para el modo local; entrenamiento de kernels, pesos y hardware consumen recursos
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El README documenta conexión a Claude Code y Codex; su cifra de velocidad es un benchmark del autor, no una garantía universal
- Coste: Sin pago a un modelo en la ruta básica. No exige proveedor API para el modo local; entrenamiento de kernels, pesos y hardware consumen recursos
- Equipo: Preparación según la ruta elegida. Sistema y acelerador compatibles; pesos; espacio de caché para optimización
**Repo:** https://github.com/magnitudedev/magnitude

**Instalación** [+]:

```
curl -fsSL https://magnitude.dev/install.sh | sh
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Servir un modelo local a Codex; Comparar backends de inferencia en tu equipo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prueba un modelo pequeño y registra la latencia antes y después del ajuste de kernels
**Qué comprobar:** Puedes comparar rendimiento en la misma máquina y con el mismo modelo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `hermes-agent`, `codex`, `opencode`

## `mlc-llm`
role=runtime · exec=local · setup=heavy · mcp=False · prov=— · tags=inference,python,local,model

**Qué es:** Motor universal de despliegue de LLM con compilación de ML: ejecuta modelos en GPU de escritorio, móviles y navegador con API compatible con OpenAI.
**Stack:** Python, CMakeLists.txt, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/mlc-ai/mlc-llm

**Instalación** [+]:

```
git clone --recursive https://github.com/mlc-ai/mlc-llm.git && cd mlc-llm/
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: ejecutar un LLM en un móvil o en el navegador sin servidor; servir un modelo en GPU AMD, Intel o Apple con una API compatible con OpenAI
**Evita si:** no quieres preparar modelos, dependencias y hardware propios
**Primera prueba propuesta:** Sigue el quick start para instalar el paquete de tu plataforma y chatear con un modelo precompilado.
**Qué comprobar:** El modelo responde en local y el servidor REST devuelve respuestas al endpoint de chat.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `transformers`, `open-webui`, `litellm`

## `mlx-lm`
role=runtime · exec=local · setup=easy · mcp=False · prov=— · tags=inference,python,local,training

**Qué es:** Paquete de Apple para generar texto y afinar LLM en Apple Silicon con MLX: miles de modelos del Hub, cuantización, LoRA y servidor HTTP.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/ml-explore/mlx-lm

**Instalación** [+]:

```
pip install mlx-lm
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: ejecutar un LLM local optimizado en un Mac con chip Apple; afinar un modelo con LoRA en un Mac sin GPU NVIDIA
**Evita si:** no quieres preparar modelos, dependencias y hardware propios
**Primera prueba propuesta:** Instala con `pip install mlx-lm` en un Mac con Apple Silicon y genera texto con un modelo cuantizado del Hub.
**Qué comprobar:** El modelo se descarga, genera la respuesta y la CLI informa de tokens por segundo.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `exo`, `open-webui`, `litellm`

## `nextchat`
role=app · exec=hybrid · setup=easy · mcp=True · prov=— · tags=chatbot,typescript,app,mcp

**Qué es:** Cliente de chat de IA ligero y multiplataforma (web, escritorio y móvil) para Claude, GPT, Gemini, DeepSeek y modelos autoalojados, con soporte MCP.
**Stack:** TypeScript, Dockerfile, docker-compose.yml, package.json
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Consumo de APIs o servicios. Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/ChatGPTNextWeb/NextChat

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/ChatGPTNextWeb/NextChat/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: desplegar un chat privado con tu propia clave para un equipo pequeño; usar un modelo autoalojado compatible con OpenAI desde una interfaz web ligera
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Despliega NextChat con Docker o Vercel usando tu clave de API y abre un chat.
**Qué comprobar:** El chat responde con el modelo configurado y el historial queda en el navegador.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `localai`, `litellm`, `fastmcp`
**Alternativas (elige una):** `lobehub`, `chatbox`

## `notebooklm-mcp-cli`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=— · tags=mcp,notebooks,python

**Qué es:** CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP.
**Stack:** Python; cuenta Google; cliente MCP; sesión del navegador
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige clave LLM propia; cuenta y límites de Google, servicios y agente anfitrión tienen condiciones separadas
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. Documenta los tres clientes; instalar CLI o MCP no vuelve local la generación ni evita los cupos de NotebookLM
- Coste: El coste depende del proveedor o la ruta. No exige clave LLM propia; cuenta y límites de Google, servicios y agente anfitrión tienen condiciones separadas
- Equipo: Preparación según la ruta elegida. Python; cuenta Google; cliente MCP; sesión del navegador
**Repo:** https://github.com/jacob-bd/gemini-notebook-mcp-cli

**Instalación** [+]:

```
pip install notebooklm-mcp-cli
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Administrar fuentes desde un agente; Exportar contenido generado por NotebookLM
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta el asistente de setup, conecta un cliente y consulta una fuente ficticia en un notebook de prueba
**Qué comprobar:** Puedes contrastar la respuesta y comprobar el estado de autenticación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `gemini-cli`

## `notebooklm-py`
role=library · exec=cloud · setup=easy · mcp=True · prov=— · tags=notebooks,research,python

**Qué es:** API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código.
**Stack:** Python y uv o pipx; sesión Google; Chromium para login; notebook de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa tu cuenta y cupos de NotebookLM, no una API local de modelo; el agente y los planes Google tienen límites separados
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. API no oficial con endpoints que pueden cambiar; los archivos descargados quedan locales pero la generación ocurre en Google
- Coste: El coste depende del proveedor o la ruta. Usa tu cuenta y cupos de NotebookLM, no una API local de modelo; el agente y los planes Google tienen límites separados
- Equipo: Preparación según la ruta elegida. Python y uv o pipx; sesión Google; Chromium para login; notebook de prueba
**Repo:** https://github.com/teng-lin/notebooklm-py

**Instalación** [+]:

```
uv tool install "notebooklm-py[browser]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar consultas documentales; Exportar mapas o resúmenes propios
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un notebook con una fuente propia breve y pregunta por un dato verificable
**Qué comprobar:** La consulta y las referencias aparecen en el mismo notebook de Google
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `obsidian-second-brain`

## `odysseus`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=agents,local,python,docker

**Qué es:** Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado.
**Stack:** Docker; configuración .env; proveedor o modelos locales
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Admite modelos locales o API; correo, búsqueda y otros servicios mantienen sus credenciales y costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Local/API describe el modelo elegido; conservar la app en tu servidor no impide enviar datos a un proveedor remoto
- Coste: El coste depende del proveedor o la ruta. Admite modelos locales o API; correo, búsqueda y otros servicios mantienen sus credenciales y costes
- Equipo: Preparación según la ruta elegida. Docker; configuración .env; proveedor o modelos locales
**Repo:** https://github.com/odysseus-dev/odysseus

**Instalación** [+]:

```
git clone https://github.com/odysseus-dev/odysseus.git
cd odysseus
cp .env.example .env
docker compose up -d --build
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Organizar notas y tareas con IA; Comparar respuestas de modelos desde un workspace
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un chat con un texto ficticio y prueba el editor de documentos sin conectar correo real
**Qué comprobar:** Puedes distinguir conversación, documento y herramientas habilitadas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `vllm`, `playwright-mcp`

## `ollama`
role=runtime · exec=local · setup=easy · mcp=False · prov=local · tags=inference,local,go

**Qué es:** La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI.
**Stack:** Instalador oficial para tu sistema; RAM y disco adecuados al modelo
**Acceso y costes:**
- API de IA: API de IA opcional. Los modelos locales usan tu hardware; modelos Cloud y búsqueda web tienen autenticación y condiciones propias
- Claude Code: Integración documentada por el proyecto
- Codex: Integración documentada por el proyecto
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Las guías del autor documentan Claude Code y Codex CLI con backend Ollama; esto cambia el modelo y no aporta modelos Anthropic/OpenAI mediante su suscripción
- Coste: El coste depende del proveedor o la ruta. Los modelos locales usan tu hardware; modelos Cloud y búsqueda web tienen autenticación y condiciones propias
- Equipo: Preparación según la ruta elegida. Instalador oficial para tu sistema; RAM y disco adecuados al modelo
**Repo:** https://github.com/ollama/ollama

**Instalación** [+]:

```
pip install ollama
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un LLM local; Conectar un modelo local a Codex CLI
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Descarga un modelo pequeño y formula una pregunta antes de conectarlo a un agente
**Qué comprobar:** Puedes identificar el modelo ejecutado y ver la respuesta en tu equipo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `open-webui`, `litellm`, `crawl4ai`, `claude-code`
**Alternativas (elige una):** `llama-cpp`, `localai`, `llamafile`

## `open-notebook`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=notebooks,research,typescript,docker

**Qué es:** Aplicación auto-hospedada para reunir fuentes, consultar documentos y producir resúmenes o audio. Permite elegir proveedores de chat, embeddings y audio locales o remotos; la privacidad del procesamiento depende de esa configuración.
**Stack:** Docker; proveedores de chat, embeddings y audio según función; fuentes de prueba
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Admite Ollama y otros servidores locales, además de APIs de pago; audio y embeddings se configuran aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La app auto-hospedada no garantiza que todos los datos se procesen localmente: depende de cada proveedor que selecciones
- Coste: El coste depende del proveedor o la ruta. Admite Ollama y otros servidores locales, además de APIs de pago; audio y embeddings se configuran aparte
- Equipo: Preparación según la ruta elegida. Docker; proveedores de chat, embeddings y audio según función; fuentes de prueba
**Repo:** https://github.com/lfnovo/open-notebook

**Instalación** [+]:

```
docker compose up -d
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar documentos en una libreta; Generar un resumen o audio sobre material propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un notebook con dos fuentes y pregunta por un dato con referencia
**Qué comprobar:** Puedes identificar la fuente y corregir un resumen
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `vllm`, `activepieces`, `scientific-agent-skills`, `olmocr`, `vibevoice`
**Alternativas (elige una):** `deeptutor`, `surfsense`

## `open-webui`
role=app · exec=local · setup=easy · mcp=True · prov=openai,local · tags=chatbot,local,rag,docker

**Qué es:** Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas.
**Stack:** Docker; Ollama accesible o proveedor remoto; volumen persistente
**Acceso y costes:**
- API de IA: API de IA opcional. Los modelos remotos consumen API; Ollama local necesita hardware; la licencia exige conservar branding salvo las excepciones aplicables
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Instalar la interfaz no instala todos los modelos; confirma que Docker puede alcanzar el servidor de inferencia
- Coste: El coste depende del proveedor o la ruta. Los modelos remotos consumen API; Ollama local necesita hardware; la licencia exige conservar branding salvo las excepciones aplicables
- Equipo: Preparación según la ruta elegida. Docker; Ollama accesible o proveedor remoto; volumen persistente
**Repo:** https://github.com/open-webui/open-webui

**Instalación** [+]:

```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Unificar chats de modelos locales; Crear una interfaz compartida para un equipo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta un modelo y conversa sobre un texto ficticio antes de cargar documentos privados
**Qué comprobar:** Puedes ver el modelo seleccionado y conservar una conversación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `litellm`, `searxng`
**Alternativas (elige una):** `librechat`, `lobehub`, `anything-llm`, `textgen`

## `private-gpt`
role=platform · exec=local · setup=medium · mcp=False · prov=local,openai · tags=rag,local,python

**Qué es:** Capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP.
**Stack:** Servidor LLM compatible OpenAI; Python 3.11 o distribución adecuada; documentos de prueba
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El servidor de inferencia y embeddings usan recursos propios o proveedores según configuración; no incluye modelos de pago
- Claude Code: Integración documentada por el proyecto
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La guía documenta backend local para Claude Code; no confirma por eso integración de todas las funciones de Codex o Antigravity
- Coste: El coste depende del proveedor o la ruta. El servidor de inferencia y embeddings usan recursos propios o proveedores según configuración; no incluye modelos de pago
- Equipo: Preparación según la ruta elegida. Servidor LLM compatible OpenAI; Python 3.11 o distribución adecuada; documentos de prueba
**Repo:** https://github.com/zylon-ai/private-gpt

**Instalación** [+]:

```
brew install private-gpt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir una API privada sobre documentos; Usar un modelo local como backend de programación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta el servidor local y consulta un documento breve con la API de RAG
**Qué comprobar:** Puedes seguir la consulta y comprobar el fragmento recuperado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `vllm`, `llama-cpp`
**Alternativas (elige una):** `anything-llm`

## `sillytavern`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=chatbot,javascript,local,app

**Qué es:** Interfaz local avanzada para chatear con LLM: une muchas APIs, personajes, rol, generación de imágenes, voz y extensiones.
**Stack:** JavaScript, Dockerfile, package.json
**Acceso y costes:**
- API de IA: API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos.
- Coste: El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan.
- Equipo: Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/SillyTavern/SillyTavern

**Instalación** [+]:

```
git clone https://github.com/SillyTavern/SillyTavern -b release
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: escribir historias o partidas de rol con personajes y memoria persistente; probar el mismo prompt contra varios modelos locales y remotos
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Instala SillyTavern con Node.js 20+, conéctalo a un backend local como KoboldCpp u Ollama y abre un chat.
**Qué comprobar:** El chat responde con el modelo conectado y la conversación se guarda en tu equipo.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `koboldcpp`, `ollama`, `comfyui`, `kokoro`, `textgen`

## `surfsense`
role=app · exec=hybrid · setup=medium · mcp=False · prov=openai,local · tags=research,rag,notebooks,python

**Qué es:** Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos.
**Stack:** Instalador para tu sistema; modelo local o remoto; LibreOffice solo para conversiones Office
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La app ofrece ruta local sin cuenta; plugins propios de búsqueda y fuentes requieren licencia; modelos remotos y generación de imágenes pueden costar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El índice puede permanecer local aunque el modelo sea remoto; LibreOffice no viene incluido para las conversiones Office
- Coste: El coste depende del proveedor o la ruta. La app ofrece ruta local sin cuenta; plugins propios de búsqueda y fuentes requieren licencia; modelos remotos y generación de imágenes pueden costar
- Equipo: Preparación según la ruta elegida. Instalador para tu sistema; modelo local o remoto; LibreOffice solo para conversiones Office
**Repo:** https://github.com/MODSetter/SurfSense

**Instalación** [+]:

```
curl -fsSL https://raw.githubusercontent.com/MODSetter/SurfSense/main/docker/scripts/install.sh \| bash
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Revisar un contrato de prueba con comentarios; Extraer datos de un archivo Excel ficticio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade un documento ficticio y pide una edición que se guarde como copia
**Qué comprobar:** Puedes comparar original y archivo nuevo y revisar las citas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `vllm`, `playwright-mcp`
**Alternativas (elige una):** `open-notebook`, `khoj`

## `textgen`
role=app · exec=local · setup=medium · mcp=False · prov=local · tags=chatbot,local,inference,python

**Qué es:** App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic.
**Stack:** Distribución portable apropiada a tu GPU o CPU; modelo GGUF
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige API de proveedor; modelos, memoria y disco son recursos y licencias propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Antes conocida por rutas text-generation-webui; usa la distribución que corresponda a tu hardware y distingue API de inferencia de token de autenticación
- Coste: Sin pago a un modelo en la ruta básica. No exige API de proveedor; modelos, memoria y disco son recursos y licencias propios
- Equipo: Preparación según la ruta elegida. Distribución portable apropiada a tu GPU o CPU; modelo GGUF
**Repo:** https://github.com/oobabooga/textgen

**Instalación** [+]:

```
docker compose up --build
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar modelos GGUF sin una API remota; Servir un endpoint local para otra app
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga un modelo pequeño en la app y revisa texto generado y consumo de memoria
**Qué comprobar:** Puedes identificar backend, modelo y memoria utilizada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `librechat`, `llmfit`, `unsloth`, `sillytavern`
**Alternativas (elige una):** `jan`, `open-webui`

## `transformers.js`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=motores,browser,javascript,transformers,webml

**Qué es:** Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y audio en JavaScript.
**Stack:** Node o navegador compatible; modelo ONNX admitido; RAM y descarga inicial
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere API remota después de disponer de modelos y assets; cada modelo conserva su licencia; distribución y hardware pueden costar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. No todos los Transformers se ejecutan sin conversión; confirma compatibilidad y backend WebGPU o WASM del modelo elegido
- Coste: Sin pago a un modelo en la ruta básica. No requiere API remota después de disponer de modelos y assets; cada modelo conserva su licencia; distribución y hardware pueden costar
- Equipo: Preparación según la ruta elegida. Node o navegador compatible; modelo ONNX admitido; RAM y descarga inicial
**Repo:** https://github.com/huggingface/transformers.js

**Instalación** [+]:

```
npm i @huggingface/transformers
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Clasificar texto en el navegador; Procesar audio o imágenes sin servidor de modelos externo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta un pipeline de clasificación de texto sobre dos frases de prueba
**Qué comprobar:** El modelo devuelve etiquetas que puedes comparar con las frases
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `qdrant`, `supabase`, `whisper`
