# 22. Infraestructura, despliegue y herramientas para agentes — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agent-desktop`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=infra,accessibility,accessibility-api,ai-agents,automation,cli,computer-use,computer-use-agent

**Qué es:** CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y operar aplicaciones de escritorio. Expone elementos de la interfaz como referencias sobre las que el agente puede actuar y comprobar resultados.
**Stack:** Rust, Cargo
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/vercel-labs/agent-desktop

**Instalación** [+]: `npm install -g agent-desktop`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas automatizar aplicaciones nativas desde un agente
**Evita si:** un flujo determinista resuelve el problema sin un agente
**Combina con:** `codex`

## `agent-protocol`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=agents,python

**Qué es:** Define cómo se ejecuta un agente, cómo recibe entradas y cómo guarda su estado, sin atarse a un framework. Es una especificación, no un runtime.
**Stack:** OpenAPI, Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/langchain-ai/agent-protocol

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** diseñas una plataforma que sirve agentes de distintos frameworks
**Evita si:** solo necesitas construir un agente
**Combina con:** `langgraph`

## `casaos`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=infraestructura,server,go

**Qué es:** Entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos.
**Stack:** Go, go.mod, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/IceWhaleTech/CasaOS

**Instalación** [?]: `Seguir la instalación original: https://github.com/IceWhaleTech/CasaOS/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `claude-task-master`
role=app · exec=hybrid · setup=medium · mcp=True · prov=— · tags=infra,agent,javascript

**Qué es:** Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP.
**Stack:** JavaScript, package.json
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Consumo de APIs o servicios. Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/eyaltoledano/claude-task-master

**Instalación** [?]: `Seguir la instalación original: https://github.com/eyaltoledano/claude-task-master/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `codex-chatgpt-web`
role=app · exec=cloud · setup=medium · mcp=True · prov=— · tags=infra,chatgpt,chatgpt-pro,codex,free-ai,mcp,openai,playwright

**Qué es:** Integración de terceros que conecta una sesión de ChatGPT Web con el selector de modelos y herramientas de Codex. Un launcher usa la sesión de la cuenta y enlaza herramientas mediante MCP para conservar el contexto de la tarea.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: API: por confirmar. No se da por verificada la autenticación o el coste real de esta integración de terceros.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Ejecución con modelos locales por confirmar. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Coste por confirmar. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/miuuyy/codex-chatgpt-web

**Instalación** [?]: `Seguir la instalación original: https://github.com/miuuyy/codex-chatgpt-web/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar una integración entre ChatGPT Web y Codex
**Evita si:** un flujo determinista resuelve el problema sin un agente

## `composio`
role=platform · exec=cloud · setup=easy · mcp=True · prov=openai,anthropic,mcp · tags=agents,mcp,automation,typescript

**Qué es:** Da a cualquier agente herramientas listas para Gmail, Slack, GitHub, Notion y cientos más, gestionando OAuth por ti. Funciona con los principales frameworks y por MCP.
**Stack:** TypeScript, Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ComposioHQ/composio

**Instalación** [+]: `pip install composio`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** tu agente necesita actuar en muchas apps SaaS
**Evita si:** quieres todo auto-hospedado sin servicio externo
**Combina con:** `langgraph`, `openai-agents-python`, `mastra`

## `computer-use-preview`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=google · tags=browser,agents,python

**Qué es:** Muestra cómo un modelo Gemini con computer use controla un navegador para completar tareas. Es una vista previa, no un agente de propósito general.
**Stack:** Python, Playwright
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Consumo de APIs o servicios. Este repositorio demuestra computer use con Gemini y requiere su API key; el nombre no implica una integración de OpenAI.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/google-gemini/computer-use-preview

**Instalación** [?]: `Seguir la instalación original: https://github.com/google-gemini/computer-use-preview/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres probar computer use con Gemini
**Evita si:** buscas automatización web robusta; mira `browser-use` o `stagehand`
**Combina con:** `playwright`
**Alternativas (elige una):** `browser-use`, `skyvern`

## `coolify`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=infraestructura,server,php

**Qué es:** Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios.
**Stack:** PHP, docker-compose.yml, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/coollabsio/coolify

**Instalación** [?]: `Seguir la instalación original: https://github.com/coollabsio/coolify/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `e2b`
role=platform · exec=cloud · setup=easy · mcp=False · prov=— · tags=agents,security,python

**Qué es:** Arranca microVMs aisladas en milisegundos donde el agente puede ejecutar código, instalar paquetes o usar un escritorio. Muy usado para intérpretes de código y agentes de datos.
**Stack:** Python, TypeScript, Firecracker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La clave exigida es de un servicio externo. No es una API de un modelo de lenguaje; el agente o aplicación que use sus datos tiene su propio acceso a IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Consumo de APIs o servicios. La clave E2B_API_KEY da acceso al servicio de sandboxes, con sus propios límites y tarifas; el modelo se configura aparte.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/e2b-dev/E2B

**Instalación** [+]: `pip install e2b-code-interpreter`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** tu agente ejecuta código y necesitas aislarlo
**Evita si:** solo necesitas ejecutar código localmente de confianza
**Combina con:** `smolagents`, `open-swe`
**Alternativas (elige una):** `sandbox`

## `free-for-dev`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=recursos,awesome-list,free-for-developers,html

**Qué es:** Directorio de servicios de infraestructura y desarrollo que ofrecen planes o niveles gratuitos. Agrupa servicios por capacidad para comparar opciones antes de configurar un proyecto.
**Stack:** HTML
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ripienaar/free-for-dev

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas servicios de desarrollo con un nivel gratuito disponible
**Evita si:** una conexión directa cubre el caso sin añadir infraestructura

## `freedomain`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=recursos,digitalplat,dns,dns-tutorial,documentation,domain,domain-platform,domain-registration

**Qué es:** Recursos de registro de dominios y aprendizaje práctico de DNS publicados por DigitalPlat. Reúne instrucciones para registrar un dominio, configurar nameservers y conectar un proyecto.
**Stack:** Markdown
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/DigitalPlatDev/FreeDomain

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres aprender el flujo de dominios y DNS con sus recursos de referencia
**Evita si:** una conexión directa cubre el caso sin añadir infraestructura

## `masterdnsvpn`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=redes,dns,dns-client,dns-proxy,dns-server,dns-tunnel,dns-tunneling,dnstt

**Qué es:** Implementación en Go de un túnel que transporta tráfico TCP mediante consultas y respuestas DNS. Coordina cliente y servidor con retransmisión y selección de resolvers para enlaces con restricciones.
**Stack:** Go, Go modules
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/masterking32/MasterDnsVPN

**Instalación** [?]: `Seguir la instalación original: https://github.com/masterking32/MasterDnsVPN/blob/main/README.MD`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar transporte de red sobre DNS en un entorno de pruebas
**Evita si:** una conexión directa cubre el caso sin añadir infraestructura

## `nemo-agent-toolkit`
role=library · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=automation,agents,python

**Qué es:** Aporta componentes para conectar, evaluar y desplegar agentes en infraestructura empresarial.
**Stack:** Python, FastAPI (Apache-2.0)
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/NVIDIA/NeMo-Agent-Toolkit

**Instalación** [+]: `pip install nvidia-nat`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** trabajas con infra NVIDIA o necesitas guardrails/eval empresarial
**Evita si:** quieres algo ligero y agnóstico
**Combina con:** `langchain`

## `nemoclaw`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=agents,security,typescript

**Qué es:** Ejecuta agentes populares dentro de los sandboxes de NVIDIA OpenShell con inferencia gestionada y políticas de seguridad. Pensado para empresas.
**Stack:** TypeScript, contenedores
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/NVIDIA/NemoClaw

**Instalación** [?]: `Seguir la instalación original: https://github.com/NVIDIA/NemoClaw/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres correr agentes potentes con aislamiento corporativo
**Evita si:** solo necesitas un sandbox para ejecutar código; mira `e2b`
**Combina con:** `openclaw`, `hermes-agent`, `nemotron`
**Alternativas (elige una):** `sandbox`

## `nodeterm`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=infra,adhd,agent-orchestration,ai-agents,canvas,claude-code,codex,coding-agents

**Qué es:** Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con organización por proyecto. Mantiene terminales reales en nodos movibles y muestra sesiones de trabajo en un tablero.
**Stack:** TypeScript, Docker, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/eneskirca/nodeterm

**Instalación** [?]: `Seguir la instalación original: https://github.com/eneskirca/nodeterm/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** gestionas muchas terminales o sesiones de agentes y prefieres una organización visual
**Evita si:** un flujo determinista resuelve el problema sin un agente

## `sandbox`
role=platform · exec=hybrid · setup=medium · mcp=True · prov=— · tags=agents,automation,python,docker

**Qué es:** Resuelve el riesgo de dejar que un agente toque tu host: todo corre contenido en un contenedor reproducible.
**Stack:** Docker, web, MCP
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/agent-infra/sandbox

**Instalación** [?]: `Seguir la instalación original: https://github.com/agent-infra/sandbox/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres aislar la ejecución de agentes y reproducibilidad
**Evita si:** te basta correr local sin sandbox o no puedes asumir el overhead de Docker
**Combina con:** `openhands`, `ecc`
**Alternativas (elige una):** `nemoclaw`, `e2b`

## `shepherd`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=infra,framework,python

**Qué es:** Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus recorridos.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/shepherd-agents/shepherd

**Instalación** [?]: `Seguir la instalación original: https://github.com/shepherd-agents/shepherd/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus recorridos.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `supabase`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=infraestructura,server,typescript

**Qué es:** Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/supabase/supabase

**Instalación** [?]: `Seguir la instalación original: https://github.com/supabase/supabase/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución
