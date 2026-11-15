# 9. Diseñar y construir interfaces web — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `ai-website-cloner-template`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=ia-ui,template,typescript

**Qué es:** Plantilla para que un agente de código estudie una web de referencia y prepare una implementación de su interfaz.
**Stack:** TypeScript, Dockerfile, docker-compose.yml, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/JCodesMore/ai-website-cloner-template

**Instalación** [?]: `Seguir la instalación original: https://github.com/JCodesMore/ai-website-cloner-template/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Plantilla para que un agente de código estudie una web de referencia y prepare una implementación de su interfaz.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `ant-design`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,react,typescript

**Qué es:** Componentes muy completos para apps de negocio: tablas, formularios, fechas y layouts de backoffice.
**Stack:** TypeScript, React
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ant-design/ant-design

**Instalación** [+]: `npm install antd`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** construyes apps empresariales con muchos datos
**Evita si:** quieres un estilo más personalizado; mira `ui`
**Combina con:** `echarts`
**Alternativas (elige una):** `mui`, `ui`

## `assistant-ui`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,chatbot,react,typescript

**Qué es:** Componentes componibles de chat con streaming, adjuntos, markdown y herramientas, compatibles con AI SDK y LangGraph.
**Stack:** TypeScript, React
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/assistant-ui/assistant-ui

**Instalación** [+]: `npx assistant-ui@latest init`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas una UI de chat pulida en React
**Evita si:** quieres agentes que manipulen tu app; mira `copilotkit`
**Combina con:** `vercel-ai`, `ui`
**Alternativas (elige una):** `copilotkit`

## `copilotkit`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic · tags=ui,agents,react,typescript

**Qué es:** Añade copilotos, chat y agentes que actúan sobre tu app, con estado compartido entre agente y UI. Se integra con LangGraph, Mastra y más.
**Stack:** TypeScript, React
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/CopilotKit/CopilotKit

**Instalación** [?]: `Seguir la instalación original: https://github.com/CopilotKit/CopilotKit/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres agentes que interactúen con la UI de tu app
**Evita si:** solo necesitas una ventana de chat; mira `assistant-ui`
**Combina con:** `langgraph`, `mastra`
**Alternativas (elige una):** `assistant-ui`

## `daisyui`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,design,javascript

**Qué es:** Añade clases como `btn` o `card` sobre Tailwind para escribir menos HTML, sin JavaScript.
**Stack:** JavaScript, CSS, Tailwind
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/saadeghi/daisyui

**Instalación** [?]: `Seguir la instalación original: https://github.com/saadeghi/daisyui/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** usas Tailwind y quieres componentes sin JavaScript
**Evita si:** usas React y quieres control total; mira `ui`
**Combina con:** `tailwindcss`
**Alternativas (elige una):** `ui`

## `excalidraw`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=design,docs,typescript

**Qué es:** Dibuja diagramas rápidos que parecen bocetos, colabora en tiempo real y embébela en tus apps como componente React.
**Stack:** TypeScript, React, Canvas
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/excalidraw/excalidraw

**Instalación** [?]: `Seguir la instalación original: https://github.com/excalidraw/excalidraw/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres diagramas rápidos con estilo boceto
**Evita si:** prefieres diagramas como texto; mira `mermaid`
**Alternativas (elige una):** `tldraw`, `mermaid`

## `flexoki`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=estilos,reference,css

**Qué es:** Paleta de color para texto, código e interfaces que puede servir de referencia al definir un sistema visual.
**Stack:** CSS
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/kepano/flexoki

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** buscas esta función: Paleta de color para texto, código e interfaces que puede servir de referencia al definir un sistema visual.
**Evita si:** necesitas una aplicación lista para ejecutar en lugar de material de consulta

## `heroui`
role=library · exec=local · setup=easy · mcp=True · prov=— · tags=ui,typescript

**Qué es:** Resuelve la accesibilidad seria sin renunciar a un estilado moderno.
**Stack:** Node.js, React, Tailwind
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/heroui-inc/heroui

**Instalación** [+]: `npm install @heroui/styles @heroui/react`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres calidad + accesibilidad listas
**Evita si:** quieres control copy-paste del código (ui)
**Combina con:** `tailwindcss`, `swr`
**Alternativas (elige una):** `mui`

## `json-render`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=ia-ui,library,typescript

**Qué es:** Framework para generar interfaces desde una representación JSON y un catálogo de componentes definido por el desarrollador.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica y las funciones de IA se configuran por separado; activar un proveedor puede añadir credenciales y consumo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: El coste depende del proveedor o la ruta. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/vercel-labs/json-render

**Instalación** [?]: `Seguir la instalación original: https://github.com/vercel-labs/json-render/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Framework para generar interfaces desde una representación JSON y un catálogo de componentes definido por el desarrollador.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `konva`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=componentes,library,typescript

**Qué es:** Biblioteca de canvas para construir editores gráficos, diagramas e interfaces con formas y objetos interactivos.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/konvajs/konva

**Instalación** [+]: `npm install konva`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: Biblioteca de canvas para construir editores gráficos, diagramas e interfaces con formas y objetos interactivos.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `lucide`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,design,typescript

**Qué es:** Iconos limpios y uniformes, usados por shadcn/ui y muchas apps.
**Stack:** TypeScript, SVG
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/lucide-icons/lucide

**Instalación** [?]: `Seguir la instalación original: https://github.com/lucide-icons/lucide/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas iconos consistentes
**Evita si:** buscas ilustraciones, no iconos
**Combina con:** `ui`

## `magicui`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui

**Qué es:** Apunta al impacto visual más que a la accesibilidad estricta.
**Stack:** Node.js, React/Next.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/magicuidesign/magicui

**Instalación** [?]: `Seguir la instalación original: https://github.com/magicuidesign/magicui/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** priorizas estética y velocidad
**Evita si:** necesitas accesibilidad estricta (heroui)
**Combina con:** `tailwindcss`, `motion`
**Alternativas (elige una):** `react-bits`

## `mui`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,react,javascript

**Qué es:** Cientos de componentes accesibles y personalizables para apps React, con temas y sistema de estilos propio.
**Stack:** JavaScript, TypeScript, React
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/mui/material-ui

**Instalación** [?]: `Seguir la instalación original: https://github.com/mui/material-ui/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres una librería React completa y probada
**Evita si:** prefieres copiar componentes y estilarlos con Tailwind; mira `ui`
**Combina con:** `recharts`
**Alternativas (elige una):** `ant-design`, `ui`, `heroui`

## `normalize.css`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,design

**Qué es:** Resuelve las inconsistencias de margen, tipografía y formularios entre Chrome, Firefox y Safari.
**Stack:** CSS
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/necolas/normalize.css

**Instalación** [+]: `npm install --save normalize.css`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres base CSS uniforme y ligera
**Evita si:** ya usas el preflight de Tailwind, que cubre lo mismo
**Combina con:** `tailwindcss`

## `onlook`
role=app · exec=local · setup=easy · mcp=False · prov=anthropic · tags=design,ui,coding-agent,typescript

**Qué es:** Edita tu app en un lienzo visual o pide cambios a la IA, y Onlook escribe el código en tu proyecto.
**Stack:** TypeScript, Next.js, Tailwind
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/onlook-dev/onlook

**Instalación** [?]: `Seguir la instalación original: https://github.com/onlook-dev/onlook/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres editar tu app React visualmente con ayuda de IA
**Evita si:** necesitas diseño desde cero en vectores; mira `penpot`
**Combina con:** `tailwindcss`, `ui`
**Alternativas (elige una):** `open-design`

## `open-design`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=agents,design,typescript

**Qué es:** Resuelve el ir y venir entre prompt, preview y código exportable.
**Stack:** TypeScript/React, Tauri (Rust)
**Acceso y costes:**
- API de IA: API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
- Otras rutas: El servicio ofrece sus propios planes y rutas de API. Consultar las condiciones de OpenDesign por separado del plan del agente que lo conecte.
**Repo:** https://github.com/nexu-io/open-design

**Instalación** [?]: `Seguir la instalación original: https://github.com/nexu-io/open-design/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** generas UI desde texto y quieres edición visual
**Evita si:** prefieres editar visualmente sobre tu código existente (plasmic)
**Combina con:** `tailwindcss`, `heroui`
**Alternativas (elige una):** `onlook`

## `openui`
role=library · exec=hybrid · setup=easy · mcp=False · prov=— · tags=ui,agents,typescript

**Qué es:** Permite que el modelo devuelva componentes interactivos (tablas, formularios, gráficos) que tu app renderiza.
**Stack:** TypeScript, React
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/thesysdev/openui

**Instalación** [?]: `Seguir la instalación original: https://github.com/thesysdev/openui/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres que tu agente responda con interfaces
**Evita si:** solo necesitas chat de texto; mira `assistant-ui`
**Combina con:** `copilotkit`

## `penpot`
role=app · exec=local · setup=heavy · mcp=False · prov=— · tags=design,docker

**Qué es:** Es la alternativa abierta a Figma más conocida.
**Stack:** stack web self-host, Docker (Clojure/ClojureScript)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/penpot/penpot

**Instalación** [?]: `Seguir la instalación original: https://github.com/penpot/penpot/blob/develop/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres diseño abierto y soberano, self-host
**Evita si:** necesitas generación por IA (open-design) o no quieres operar Docker
**Combina con:** `plasmic`

## `plasmic`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=design,typescript

**Qué es:** Cubre el hueco entre no-code y desarrollo a medida.
**Stack:** Node.js, React/Next.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/plasmicapp/plasmic

**Instalación** [?]: `Seguir la instalación original: https://github.com/plasmicapp/plasmic/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres editar visual sobre tu código React
**Evita si:** generas desde texto sin codebase previo (open-design)
**Combina con:** `tailwindcss`

## `radix-primitives`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,react,typescript

**Qué es:** Resuelven accesibilidad, foco y teclado en diálogos, menús o tooltips, dejándote el estilo. Son la base de shadcn/ui.
**Stack:** TypeScript, React
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/radix-ui/primitives

**Instalación** [?]: `Seguir la instalación original: https://github.com/radix-ui/primitives/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** construyes tu propio sistema de diseño
**Evita si:** quieres componentes ya estilados; mira `ui`
**Combina con:** `ui`, `tailwindcss`

## `react-bits`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,react,javascript

**Qué es:** Fondos, textos animados y efectos listos para copiar en proyectos React y Next.js.
**Stack:** JavaScript, React
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/DavidHDev/react-bits

**Instalación** [?]: `Seguir la instalación original: https://github.com/DavidHDev/react-bits/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres efectos visuales llamativos en React
**Evita si:** necesitas componentes de formulario y datos; mira `ui`
**Combina con:** `ui`, `motion`
**Alternativas (elige una):** `magicui`

## `screenshot-to-code`
role=app · exec=cloud · setup=easy · mcp=False · prov=openai,anthropic,google · tags=ui,vision,code,python

**Qué es:** Sube una imagen o graba un video de una web y obtén código funcional que puedes iterar.
**Stack:** Python, TypeScript, React
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/abi/screenshot-to-code

**Instalación** [?]: `Seguir la instalación original: https://github.com/abi/screenshot-to-code/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres pasar imágenes de diseño a código
**Evita si:** trabajas desde Figma; mira `figma-context-mcp`
**Combina con:** `tailwindcss`
**Alternativas (elige una):** `stitch-sdk`

## `stitch-sdk`
role=library · exec=cloud · setup=easy · mcp=False · prov=google · tags=ui,design,typescript

**Qué es:** Automatiza Stitch, el generador de interfaces de Google, para integrarlo en tus flujos y agentes.
**Stack:** TypeScript
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Consumo de APIs o servicios. La ruta documentada necesita STITCH_API_KEY del servicio de Google. Verificar sus cuotas y condiciones; la sesión de Claude Code o Codex no sustituye esa credencial.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/google-labs-code/stitch-sdk

**Instalación** [+]: `npm install @google/stitch-sdk`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres automatizar Stitch
**Evita si:** prefieres herramientas locales; mira `screenshot-to-code`
**Combina con:** `stitch-skills`
**Alternativas (elige una):** `screenshot-to-code`

## `swr`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,typescript

**Qué es:** Cubre el caso de consumir APIs en frontend sin manejar caché a mano.
**Stack:** JavaScript/React
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/vercel/swr

**Instalación** [?]: `Seguir la instalación original: https://github.com/vercel/swr/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** manejas datos remotos en React y quieres caché simple
**Evita si:** prefieres React Query con su modelo de caché global más rico
**Combina con:** `heroui`

## `tailwindcss`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,design,typescript

**Qué es:** Elimina el contexto de estilos disperso entre hojas y componentes.
**Stack:** Node.js, CSS
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/tailwindlabs/tailwindcss

**Instalación** [?]: `Seguir la instalación original: https://github.com/tailwindlabs/tailwindcss/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estilar rápido y consistente
**Evita si:** prefieres CSS-in-JS o estilos scoped por componente
**Combina con:** `heroui`, `magicui`

## `tldraw`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=design,ui,react,typescript

**Qué es:** Base de muchas herramientas de pizarra y de UI generativa con IA. Ofrece colaboración y personalización completa.
**Stack:** TypeScript, React
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/tldraw/tldraw

**Instalación** [+]: `npm i tldraw`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** construyes una app con lienzo infinito
**Evita si:** solo necesitas una pizarra lista; usa `excalidraw`
**Alternativas (elige una):** `excalidraw`

## `ui`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,typescript

**Qué es:** El código fuente pasa a ser tuyo y lo editas a voluntad.
**Stack:** Node.js, React, Tailwind, Radix UI
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/shadcn-ui/ui

**Instalación** [?]: `Seguir la instalación original: https://github.com/shadcn-ui/ui/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres ser dueño del código de UI
**Evita si:** prefieres una lib "llave en mano" con updates automáticos (heroui)
**Combina con:** `tailwindcss`, `plasmic`
**Alternativas (elige una):** `mui`, `ant-design`, `daisyui`

## `ui-sdk`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=ia-ui,library,typescript

**Qué es:** Colección de comportamientos y recursos para que agentes construyan interfaces con patrones de interacción definidos.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/vercel-labs/ui

**Instalación** [+]: `npm install @ui-sdk/react @ui-sdk/core`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: Colección de comportamientos y recursos para que agentes construyan interfaces con patrones de interacción definidos.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
