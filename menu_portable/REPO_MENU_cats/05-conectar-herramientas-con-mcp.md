# 5. Conectar herramientas con MCP — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `annas-mcp`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=— · tags=servidores,annas-archive,cli,mcp-server,go

**Qué es:** Servidor MCP y CLI de Go para buscar y recuperar documentos desde Anna's Archive y sus espejos.
**Stack:** Binario oficial para tu sistema; cliente MCP; clave solo para descargas
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Buscar no necesita variables; descargar por su API requiere la donación y clave descritas por el autor
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Configura la ruta absoluta del binario y del directorio de descargas; la herramienta no concede derechos sobre los documentos
- Coste: El coste depende del proveedor o la ruta. Buscar no necesita variables; descargar por su API requiere la donación y clave descritas por el autor
- Equipo: Preparación según la ruta elegida. Binario oficial para tu sistema; cliente MCP; clave solo para descargas
**Repo:** https://github.com/iosifache/annas-mcp

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/iosifache/annas-mcp/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Localizar un documento de dominio público; Estudiar una interfaz de búsqueda documental MCP
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Busca un documento que puedas utilizar legalmente y revisa los metadatos antes de descargar
**Qué comprobar:** La búsqueda muestra título y origen sin necesitar clave de descarga
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `markitdown`, `docling`

## `awesome-mcp-clients`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=mcp

**Qué es:** Lista curada de clientes que soportan Model Context Protocol: apps, IDEs y agentes.
**Stack:** Navegador; preferencias de sistema y modelo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El directorio no cobra modelos; cada cliente puede tener suscripción, API o requisitos locales
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Un cliente descrito como basado en Claude Code no es necesariamente el producto oficial ni comparte sus condiciones
- Coste: Sin pago a un modelo en la ruta básica. El directorio no cobra modelos; cada cliente puede tener suscripción, API o requisitos locales
- Equipo: Preparación según la ruta elegida. Navegador; preferencias de sistema y modelo
**Repo:** https://github.com/punkpeye/awesome-mcp-clients

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una interfaz para herramientas MCP; Comparar clientes con modelos locales
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Compara dos clientes por transportes MCP, autenticación y modelos admitidos
**Qué comprobar:** Puedes elegir un cliente cuyo sistema y conexiones encajen con tu caso
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `awesome-mcp-servers`, `claude-code`, `cline`

## `awesome-mcp-servers`
role=directory · exec=hybrid · setup=easy · mcp=True · prov=— · tags=automation,mcp

**Qué es:** Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar.
**Stack:** Navegador; cliente y tarea elegidos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Leer no requiere API; cada servidor, servicio y modelo tiene condiciones propias
- Claude Code: Depende del recurso o la configuración
- Codex: Depende del recurso o la configuración
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. Es un directorio comunitario; sus enlaces y etiquetas no equivalen a una auditoría ni a compatibilidad uniforme
- Coste: Sin pago a un modelo en la ruta básica. Leer no requiere API; cada servidor, servicio y modelo tiene condiciones propias
- Equipo: Preparación según la ruta elegida. Navegador; cliente y tarea elegidos
**Repo:** https://github.com/punkpeye/awesome-mcp-servers

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Buscar una conexión a archivos propios; Encontrar un servidor para una base de datos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Filtra por función y sistema operativo y contrasta el README de dos servidores
**Qué comprobar:** Tienes dos candidatos con transporte, permisos y credenciales identificados
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `awesome-mcp-clients`, `servers`, `mcp-use`

## `blender-mcp`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,design,python

**Qué es:** Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP.
**Stack:** Blender >=3; uv; cliente MCP; escena de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. El control básico no requiere API extra; generación premium y proveedores de modelos 3D tienen condiciones propias
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. El paquete actual es mcp-for-blender; plugin comunitario sin afiliación con Blender Foundation
- Coste: El coste depende del proveedor o la ruta. El control básico no requiere API extra; generación premium y proveedores de modelos 3D tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Blender >=3; uv; cliente MCP; escena de prueba
**Repo:** https://github.com/ahujasid/mcp-for-blender

**Instalación** [+]:

```
winget install --id=astral-sh.uv -e
uvx mcp-for-blender setup
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Bocetar una escena 3D; Automatizar ajustes de objetos y materiales
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea un cubo y cambia su material en una escena vacía
**Qué comprobar:** Puedes ver el objeto y el material en Blender
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `blender`, `unity-mcp`, `blender-skills`, `dream-loop`, `chatdev`

## `chrome-devtools-mcp`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,browser,typescript

**Qué es:** Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento.
**Stack:** Node.js LTS; npm; Chrome estable; cliente MCP
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La herramienta no incluye un modelo; consume el agente y el equipo; estadísticas de uso se habilitan por defecto
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. MCP y CLI con skill son rutas diferentes; la recogida de métricas tiene una opción de exclusión documentada
- Coste: Consumo del agente que ya utilizas. La herramienta no incluye un modelo; consume el agente y el equipo; estadísticas de uso se habilitan por defecto
- Equipo: Preparación según la ruta elegida. Node.js LTS; npm; Chrome estable; cliente MCP
**Repo:** https://github.com/ChromeDevTools/chrome-devtools-mcp

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Diagnosticar una pantalla que falla; Inspeccionar rendimiento de una página propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre tu app local y pide revisar errores de consola y una petición de red
**Qué comprobar:** El informe identifica el error y la petición que puedes reproducir
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `gemini-cli`, `mcp-inspector`, `puppeteer`, `agent-browser`, `awesome-chrome-devtools`
**Alternativas (elige una):** `playwright-mcp`, `browser-harness`

## `context7`
role=runtime · exec=cloud · setup=easy · mcp=True · prov=mcp · tags=mcp,docs,typescript

**Qué es:** Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente.
**Stack:** Node.js >=22.13; cliente MCP; clave Context7 recomendada
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La documentación tiene cupos y modalidades de acceso; el modelo del agente se paga o limita aparte
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Conectar documentación actual no acredita que todo ejemplo sea válido para la versión instalada en tu proyecto
- Coste: El coste depende del proveedor o la ruta. La documentación tiene cupos y modalidades de acceso; el modelo del agente se paga o limita aparte
- Equipo: Preparación según la ruta elegida. Node.js >=22.13; cliente MCP; clave Context7 recomendada
**Repo:** https://github.com/upstash/context7

**Instalación** [+]:

```
npx ctx7 setup
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar APIs recientes durante programación; Evitar mezclar instrucciones de versiones distintas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide documentación de una versión concreta y contrasta el ejemplo devuelto con la fuente
**Qué comprobar:** El agente identifica la biblioteca y la versión consultada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `opencode`, `cline`

## `fastmcp`
role=library · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,python

**Qué es:** La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas.
**Stack:** Python y uv; proyecto de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca no necesita modelo; el cliente, alojamiento y servicios conectados pueden costar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un framework para construir servidores y clientes, no un servidor de negocio ya configurado
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca no necesita modelo; el cliente, alojamiento y servicios conectados pueden costar
- Equipo: Preparación según la ruta elegida. Python y uv; proyecto de prueba
**Repo:** https://github.com/PrefectHQ/fastmcp

**Instalación** [+]:

```
uv add fastmcp
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Exponer una función de inventario como herramienta; Probar autenticación de un servidor propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Copia la herramienta add del ejemplo y solicita sumar dos números con un cliente MCP
**Qué comprobar:** La herramienta devuelve la suma esperada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `mcp-inspector`, `pydantic-ai`
**Alternativas (elige una):** `mcp-python-sdk`

## `figma-context-mcp`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=mcp · tags=mcp,design,ui,typescript

**Qué es:** Servidor MCP que entrega a los agentes de código el layout de tus diseños de Figma para implementarlos.
**Stack:** Node.js; token Figma; archivo de diseño accesible; cliente MCP
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige modelo propio; Figma, límites de API y el agente tienen condiciones separadas
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. La configuración Windows utiliza un lanzador distinto; el token Figma no es una clave de IA
- Coste: El coste depende del proveedor o la ruta. No exige modelo propio; Figma, límites de API y el agente tienen condiciones separadas
- Equipo: Preparación según la ruta elegida. Node.js; token Figma; archivo de diseño accesible; cliente MCP
**Repo:** https://github.com/GLips/Figma-Context-MCP

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/GLips/Figma-Context-MCP/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Implementar una tarjeta a partir de un diseño; Consultar tipografía y espaciado de una pantalla
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Solicita los datos de un frame pequeño y compara dimensiones y textos con Figma
**Qué comprobar:** El agente obtiene información del frame correcto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `ui`, `tailwindcss`, `design-dna`

## `ghidramcp`
role=runtime · exec=local · setup=medium · mcp=True · prov=— · tags=servidores,mcp,java

**Qué es:** Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y analizar programas binarios.
**Stack:** Ghidra y su plugin; uv; binario propio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige API propia de IA; usa el cliente y los recursos de Ghidra
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. La integración de los clientes se basa en stdio o HTTP documentados; esta revisión no prueba su instalación ni el análisis de binarios
- Coste: Consumo del agente que ya utilizas. No exige API propia de IA; usa el cliente y los recursos de Ghidra
- Equipo: Preparación según la ruta elegida. Ghidra y su plugin; uv; binario propio de prueba
**Repo:** https://github.com/LaurieWired/GhidraMCP

**Instalación** [+]:

```
claude mcp add ghidra -- uvx --from git+https://github.com/LaurieWired/GhidraMCP ghidra-mcp --ghidra-server http://127.0.0.1:8080/
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Documentar funciones de un binario propio; Estudiar llamadas en un ejecutable de laboratorio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga un programa de prueba y pide enumerar funciones sin modificar el análisis
**Qué comprobar:** Obtienes nombres y ubicaciones verificables en Ghidra
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ghidra`, `claude-code`, `angr`, `awesome-ai-reverse-engineering`

## `github-mcp-server`
role=runtime · exec=hybrid · setup=easy · mcp=True · prov=mcp · tags=mcp,code,go

**Qué es:** Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código.
**Stack:** Cuenta GitHub; cliente MCP; token con permisos adecuados o autenticación remota
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La herramienta no exige modelo propio; el cliente, planes GitHub y acciones del servicio tienen límites y posibles costes
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Empieza con el conjunto de herramientas y permisos de lectura necesario; no copies tokens de ejemplo como credenciales reales
- Coste: El coste depende del proveedor o la ruta. La herramienta no exige modelo propio; el cliente, planes GitHub y acciones del servicio tienen límites y posibles costes
- Equipo: Preparación según la ruta elegida. Cuenta GitHub; cliente MCP; token con permisos adecuados o autenticación remota
**Repo:** https://github.com/github/github-mcp-server

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/github/github-mcp-server/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar una base de código; Revisar el estado de una pull request
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lista archivos y lee un README de un repositorio público antes de habilitar herramientas de escritura
**Qué comprobar:** El agente devuelve contenidos y enlaces del repositorio elegido
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `strix`, `agentes-chat`, `awesome-copilot`, `cli`

## `mcp`
role=directory · exec=hybrid · setup=medium · mcp=True · prov=— · tags=mcp

**Qué es:** Reúne servidores MCP de servicios Google y ejemplos de despliegue. Sirve para elegir una conexión y revisar sus credenciales y costes. No es el repositorio de la especificación general de MCP.
**Stack:** Navegador; servicio Google objetivo
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Leer es gratuito; servidores, APIs Google y recursos de nube pueden generar gasto
- Claude Code: Depende del recurso o la configuración
- Codex: Depende del recurso o la configuración
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. Este repositorio es google/mcp: catálogo y ejemplos Google, no el núcleo de la especificación Model Context Protocol
- Coste: Sin pago a un modelo en la ruta básica. Leer es gratuito; servidores, APIs Google y recursos de nube pueden generar gasto
- Equipo: Preparación según la ruta elegida. Navegador; servicio Google objetivo
**Repo:** https://github.com/google/mcp

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Conectar un servicio Google a un agente; Aprender a alojar un servidor MCP en Cloud Run
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige un servidor oficial Google y consulta su autenticación antes de desplegar
**Qué comprobar:** Distingues servicio gestionado, ejemplo y despliegue en Cloud Run
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `gemini-cli`, `mcp-use`, `mcp-inspector`

## `mcp-for-beginners`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=mcp,learning

**Qué es:** Curso abierto de Microsoft para aprender MCP con ejemplos en .NET, Java, TypeScript, JavaScript y Python.
**Stack:** Navegador; lenguaje elegido para los ejercicios
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El curso se lee sin API; los ejercicios concretos pueden usar modelos, nube o servicios de pago
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No necesitas ejecutar todos los lenguajes ni desplegar todos los ejemplos para empezar
- Coste: Sin pago a un modelo en la ruta básica. El curso se lee sin API; los ejercicios concretos pueden usar modelos, nube o servicios de pago
- Equipo: Preparación según la ruta elegida. Navegador; lenguaje elegido para los ejercicios
**Repo:** https://github.com/microsoft/mcp-for-beginners

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender conceptos MCP desde cero; Comparar un servidor Python con otro TypeScript
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee la introducción y completa un ejercicio de herramienta con entrada y salida pequeñas
**Qué comprobar:** Puedes explicar el papel del host, cliente y servidor
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mcp-python-sdk`, `fastmcp`, `mcp-inspector`, `ai-agents-for-beginners`, `generative-ai-for-beginners`

## `mcp-inspector`
role=app · exec=local · setup=easy · mcp=True · prov=— · tags=mcp,evaluation,typescript

**Qué es:** Herramienta oficial para probar y depurar servidores MCP desde una interfaz web.
**Stack:** Node ^22.23.4 o ^24.22.1 o >=26.12.1; servidor MCP de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La inspección no requiere modelo; una herramienta conectada puede llamar servicios de pago
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Las instrucciones CLAUDE.md del repositorio sirven para contribuir al código; no hacen del Inspector un plugin de Claude Code
- Coste: Sin pago a un modelo en la ruta básica. La inspección no requiere modelo; una herramienta conectada puede llamar servicios de pago
- Equipo: Preparación según la ruta elegida. Node ^22.23.4 o ^24.22.1 o >=26.12.1; servidor MCP de prueba
**Repo:** https://github.com/modelcontextprotocol/inspector

**Instalación** [+]:

```
npx @modelcontextprotocol/inspector                   # web UI (default)
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Depurar un esquema MCP; Reproducir un fallo de una herramienta
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta un servidor local, lista herramientas y llama una con datos ficticios
**Qué comprobar:** Puedes inspeccionar argumentos, respuesta y errores sin un agente de IA
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `fastmcp`, `mcp-typescript-sdk`, `mcp-python-sdk`

## `mcp-neo4j`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=— · tags=mcp,python

**Qué es:** Colección del programa Neo4j Labs, mantenida por el equipo Field GenAI, con servidores para Cypher, memoria, modelado y Aura. Los autores advierten que no tiene SLA ni garantías de compatibilidad del equipo de producto y enlazan un repositorio distinto para el servidor oficial de producto.
**Stack:** Neo4j; credenciales; APOC para inspección de esquema; servidor elegido
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El conector no necesita modelo propio; Neo4j Aura, base local y agente tienen costes distintos
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Son servidores Neo4j Labs experimentales sin SLA del equipo de producto; el producto oficial Neo4j MCP es otro repositorio
- Coste: El coste depende del proveedor o la ruta. El conector no necesita modelo propio; Neo4j Aura, base local y agente tienen costes distintos
- Equipo: Preparación según la ruta elegida. Neo4j; credenciales; APOC para inspección de esquema; servidor elegido
**Repo:** https://github.com/neo4j-contrib/mcp-neo4j

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/neo4j-contrib/mcp-neo4j/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Consultar relaciones en un grafo; Estudiar memoria de entidades entre sesiones
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Consulta el esquema de un grafo ficticio y revisa una consulta Cypher de lectura
**Qué comprobar:** Obtienes etiquetas y relaciones que coinciden con la base de prueba
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `graphrag`, `graphiti`
**Alternativas (elige una):** `neo4j-mcp`

## `mcp-python-sdk`
role=library · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,python

**Qué es:** SDK oficial de Python para crear servidores y clientes del Model Context Protocol.
**Stack:** Python 3.11+; uv; directorio de proyecto
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El SDK no necesita API de IA; el agente cliente y las herramientas externas mantienen sus costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La documentación revisada usa MCPServer y ofrece migración v2; no confundas este SDK con FastMCP independiente
- Coste: Sin pago a un modelo en la ruta básica. El SDK no necesita API de IA; el agente cliente y las herramientas externas mantienen sus costes
- Equipo: Preparación según la ruta elegida. Python 3.11+; uv; directorio de proyecto
**Repo:** https://github.com/modelcontextprotocol/python-sdk

**Instalación** [+]:

```
uv add "mcp[cli]"      # or: pip install "mcp[cli]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Conectar una función Python a MCP; Servir un recurso de texto desde una aplicación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Implementa el servidor add del ejemplo y comprueba su esquema con Inspector
**Qué comprobar:** Una llamada con dos enteros devuelve su suma
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mcp-inspector`, `pydantic-ai`, `claude-code`, `mcp-for-beginners`
**Alternativas (elige una):** `fastmcp`

## `mcp-typescript-sdk`
role=library · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,typescript

**Qué es:** SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol.
**Stack:** Node.js; TypeScript; gestor de paquetes
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El SDK no llama modelos por sí solo; servicios y despliegue se presupuestan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La rama revisada es v2 con paquetes server y client separados; no mezcles imports de tutoriales v1
- Coste: Sin pago a un modelo en la ruta básica. El SDK no llama modelos por sí solo; servicios y despliegue se presupuestan aparte
- Equipo: Preparación según la ruta elegida. Node.js; TypeScript; gestor de paquetes
**Repo:** https://github.com/modelcontextprotocol/typescript-sdk

**Instalación** [+]:

```
npm install @modelcontextprotocol/server
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un servidor MCP en TypeScript; Crear un cliente que enumere herramientas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Sigue el ejemplo v2 para exponer una herramienta y llámala desde Inspector
**Qué comprobar:** Ves el esquema y una respuesta válida de la herramienta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mcp-inspector`, `vercel-ai`, `claude-code`
**Alternativas (elige una):** `mcp-use`

## `mcp-use`
role=library · exec=hybrid · setup=medium · mcp=True · prov=— · tags=automation,mcp,typescript

**Qué es:** Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable.
**Stack:** Node.js; plantilla elegida; Python solo para su ruta correspondiente
**Acceso y costes:**
- API de IA: API de IA opcional. El servidor básico no exige LLM; agentes, proveedores y alojamiento tienen costes según ruta
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. MCP Apps con widgets requiere capacidades del cliente adicionales a las de un servidor MCP de texto
- Coste: El coste depende del proveedor o la ruta. El servidor básico no exige LLM; agentes, proveedores y alojamiento tienen costes según ruta
- Equipo: Preparación según la ruta elegida. Node.js; plantilla elegida; Python solo para su ruta correspondiente
**Repo:** https://github.com/mcp-use/mcp-use

**Instalación** [+]:

```
npx -y create-mcp-use-app@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir una herramienta con interfaz embebida; Desplegar un servidor MCP para una app propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera una app MCP de ejemplo y prueba su herramienta desde el inspector incluido
**Qué comprobar:** Puedes ver una respuesta y la interfaz asociada si el cliente admite MCP Apps
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `awesome-mcp-servers`, `mcp`, `servers`
**Alternativas (elige una):** `mcp-typescript-sdk`

## `neo4j-mcp`
role=runtime · exec=local · setup=medium · mcp=True · prov=— · tags=mcp,graph,neo4j,cypher,go

**Qué es:** Servidor MCP oficial de Neo4j para que un asistente lea el esquema de un grafo y ejecute consultas Cypher de lectura o escritura.
**Stack:** Go, Dockerfile, go.mod
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El servidor aporta herramientas a un cliente MCP; el cliente aporta el modelo. Revisar los servicios que usa cada herramienta.
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Consumo del agente que ya utilizas. El modelo se consume en el cliente MCP. Neo4j Aura y las ediciones comerciales tienen sus propias condiciones; con ellas el servidor queda cubierto por esos contratos.
- Equipo: Preparación según la ruta elegida. Necesitas una base Neo4j (local, Docker o Aura) y credenciales; GDS es opcional.
**Repo:** https://github.com/neo4j/mcp

**Instalación** [+]:

```
pip install neo4j-mcp-server
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preguntar en lenguaje natural por el esquema de un grafo de prueba; Consultar relaciones con Cypher de solo lectura desde el agente
**Evita si:** necesitas un producto autónomo y esta pieza requiere un cliente MCP y una base Neo4j
**Primera prueba propuesta:** Conecta el servidor en modo solo lectura a una base Neo4j de prueba y pide al agente que describa su esquema
**Qué comprobar:** El agente lista etiquetas y relaciones que coinciden con las de la base
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `graphiti`, `cognee`
**Alternativas (elige una):** `mcp-neo4j`

## `playwright-mcp`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,browser,typescript

**Qué es:** Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright.
**Stack:** Node.js; npm; cliente MCP; navegador de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita API adicional de modelo; usa el agente anfitrión y recursos del navegador
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. El README documenta los tres clientes; revisa el perfil elegido porque puede conservar sesiones y cookies
- Coste: Consumo del agente que ya utilizas. No necesita API adicional de modelo; usa el agente anfitrión y recursos del navegador
- Equipo: Preparación según la ruta elegida. Node.js; npm; cliente MCP; navegador de prueba
**Repo:** https://github.com/microsoft/playwright-mcp

**Instalación** [+]:

```
claude mcp add playwright npx @playwright/mcp@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar una navegación de tu app; Inspeccionar un formulario de desarrollo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una página local con un formulario ficticio y comprueba sus campos antes de rellenarla
**Qué comprobar:** La instantánea accesible identifica campos y el resultado de la acción
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `playwright`, `mcp-inspector`
**Alternativas (elige una):** `chrome-devtools-mcp`, `browser-use`, `browser-harness`

## `public-apis`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=mcp,python

**Qué es:** Directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyectos.
**Stack:** Navegador; necesidad concreta de datos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Consultar el directorio es gratuito; algunas APIs solo tienen un cupo gratuito o requieren una cuenta comercial
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El nombre CodeX de un compilador enlazado no es OpenAI Codex; no hereda compatibilidad con agentes
- Coste: Sin pago a un modelo en la ruta básica. Consultar el directorio es gratuito; algunas APIs solo tienen un cupo gratuito o requieren una cuenta comercial
- Equipo: Preparación según la ruta elegida. Navegador; necesidad concreta de datos
**Repo:** https://github.com/public-apis/public-apis

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar datos de clima para una demo; Comparar APIs públicas de geocodificación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige una API y verifica autenticación, HTTPS, límites y licencia en su sitio oficial
**Qué comprobar:** Sabes qué datos devuelve y si podrás usarlos en tu proyecto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `activepieces`, `firecrawl`, `claude-code`

## `serena`
role=runtime · exec=local · setup=easy · mcp=True · prov=mcp · tags=mcp,coding-agent,code,python

**Qué es:** Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE.
**Stack:** uv; servidor de lenguaje del proyecto; repositorio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El backend LSP usa recursos locales; el plugin JetBrains tiene pago separado; el modelo del agente conserva sus límites
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. El autor desaconseja marketplaces con instalaciones antiguas; configura el comando de lanzamiento oficial y el backend adecuado
- Coste: El coste depende del proveedor o la ruta. El backend LSP usa recursos locales; el plugin JetBrains tiene pago separado; el modelo del agente conserva sus límites
- Equipo: Preparación según la ruta elegida. uv; servidor de lenguaje del proyecto; repositorio de prueba
**Repo:** https://github.com/oraios/serena

**Instalación** [+]:

```
uv tool install -p 3.13 serena-agent
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Navegar una base de código grande; Refactorizar un símbolo con contexto semántico
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Pide localizar una función por símbolo y enumera sus referencias antes de editar
**Qué comprobar:** El agente identifica la definición y usos reales
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `context7`, `superclaude-framework`
**Alternativas (elige una):** `codegraph`, `gitnexus`, `codebase-memory-mcp`, `graphify`

## `servers`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=— · tags=mcp,typescript

**Qué es:** Colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enlaces a servidores de la comunidad.
**Stack:** Navegador; Node o Python según el servidor elegido
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Leer no requiere API; el cliente y cada implementación elegida tienen sus requisitos
- Claude Code: Depende del recurso o la configuración
- Codex: Depende del recurso o la configuración
- Antigravity: Depende del recurso o la configuración
- Modelos locales: La función básica no necesita un modelo. Los autores los presentan como implementaciones educativas de referencia, no servicios listos para producción
- Coste: Sin pago a un modelo en la ruta básica. Leer no requiere API; el cliente y cada implementación elegida tienen sus requisitos
- Equipo: Preparación según la ruta elegida. Navegador; Node o Python según el servidor elegido
**Repo:** https://github.com/modelcontextprotocol/servers

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender cómo se implementa memoria MCP; Estudiar acceso a un repositorio Git de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Elige un servidor de referencia y comprueba sus permisos sobre datos ficticios
**Qué comprobar:** Entiendes qué herramientas expone y qué datos puede modificar
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mcp-inspector`, `mcp-use`, `awesome-mcp-servers`, `opendots`

## `unity-mcp`
role=runtime · exec=local · setup=medium · mcp=True · prov=— · tags=servidores,mcp,c

**Qué es:** Servidor MCP que permite a un asistente operar escenas, scripts y recursos dentro de un proyecto del editor Unity.
**Stack:** Unity 2021.3 LTS a 6.x; Python 3.10+ mediante uv; cliente MCP
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El conector es MIT; el agente o LLM local y la licencia Unity mantienen sus condiciones
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Instala el paquete desde Package Manager y configura el cliente; guarda una copia del proyecto antes de automatizar ediciones
- Coste: Consumo del agente que ya utilizas. El conector es MIT; el agente o LLM local y la licencia Unity mantienen sus condiciones
- Equipo: Preparación según la ruta elegida. Unity 2021.3 LTS a 6.x; Python 3.10+ mediante uv; cliente MCP
**Repo:** https://github.com/CoplayDev/unity-mcp

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/CoplayDev/unity-mcp/blob/beta/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Bocetar escenas de una demo; Ejecutar pruebas del proyecto desde un agente
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** En un proyecto vacío pide crear un cubo en el origen con un Rigidbody
**Qué comprobar:** El cubo aparece y puedes inspeccionar el componente en Unity
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `codex`, `blender`, `blender-mcp`
