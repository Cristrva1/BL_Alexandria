# 9. Diseñar y construir interfaces web — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `ai-website-cloner-template`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=ia-ui,template,typescript

**Qué es:** Plantilla para que un agente de código estudie una web de referencia y prepare una implementación de su interfaz.
**Stack:** Node; agente con acceso de navegador; web propia o referencia autorizada
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Usa el agente de código y sus límites; publicar, dominios y servicios del proyecto cuestan aparte
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Compatibilidad por confirmar
- Modelos locales: La función básica no necesita un modelo. La plantilla documenta Claude Code y Codex; la skill portable no prueba por sí sola toda la experiencia en Antigravity
- Coste: Consumo del agente que ya utilizas. Usa el agente de código y sus límites; publicar, dominios y servicios del proyecto cuestan aparte
- Equipo: Preparación según la ruta elegida. Node; agente con acceso de navegador; web propia o referencia autorizada
**Repo:** https://github.com/JCodesMore/ai-website-cloner-template

**Instalación** [+]:

```
docker compose up app --build
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar cómo traducir un diseño a componentes; Prototipar una variante de una página propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Usa una página de referencia propia y pide recrear una única sección en el proyecto de prueba
**Qué comprobar:** Puedes comparar referencia y resultado a la misma anchura y revisar el código
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `ui`, `playwright`

## `ant-design`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,react,typescript

**Qué es:** Lenguaje de diseño empresarial y librería de componentes React de Ant Group.
**Stack:** React; Node; gestor de paquetes
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca no necesita modelo; alojamiento y servicios del producto se pagan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una biblioteca React con su sistema visual; no se instala como una app final ni como agente de IA
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca no necesita modelo; alojamiento y servicios del producto se pagan aparte
- Equipo: Preparación según la ruta elegida. React; Node; gestor de paquetes
**Repo:** https://github.com/ant-design/ant-design

**Instalación** [+]:

```
npm install antd
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un panel administrativo; Montar formularios de gestión
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Muestra una tabla con tres filas ficticias y añade un filtro
**Qué comprobar:** El filtro cambia las filas y puedes revisar el estado seleccionado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `echarts`, `swr`, `vercel-ai`
**Alternativas (elige una):** `mui`, `ui`

## `assistant-ui`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,chatbot,react,typescript

**Qué es:** Librería React y TypeScript para interfaces de chat con IA de calidad producción.
**Stack:** React y TypeScript; Node; runtime y proveedor
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Los componentes no incluyen modelo; admite proveedores como Ollama además de APIs y servicios de pago
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Es la interfaz del chat; necesitas configurar el backend y no basta con instalar el paquete React
- Coste: El coste depende del proveedor o la ruta. Los componentes no incluyen modelo; admite proveedores como Ollama además de APIs y servicios de pago
- Equipo: Preparación según la ruta elegida. React y TypeScript; Node; runtime y proveedor
**Repo:** https://github.com/assistant-ui/assistant-ui

**Instalación** [+]:

```
npx assistant-ui@latest create   # new project
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un chat para una app; Añadir herramientas y adjuntos a una conversación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Arranca un chat mínimo y prueba estados de envío, streaming y error con un backend de prueba
**Qué comprobar:** Los mensajes y estados de la interfaz corresponden a la respuesta del backend
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vercel-ai`, `langgraph`, `ui`
**Alternativas (elige una):** `copilotkit`

## `astryx`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Añade a una web componentes y temas de un sistema de diseño que puedes adaptar sin construir cada elemento desde cero.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La primera prueba descrita no llama a un modelo generativo ni exige una clave de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. Sin pago a un modelo en esta ruta; los recursos, cuentas externas o despliegue elegidos pueden tener costes.
- Equipo: Equipo normal; revisar dependencias. Proyecto web React compatible con los paquetes de Astryx y StyleX.
**Repo:** https://github.com/meta/astryx

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/meta/astryx/blob/19b4b421ec4f81c7c09709e5e1b91a672240817e/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir una pantalla con botones y campos coherentes.; Probar un tema neutro y después ajustar tipografía y color.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Sigue el ejemplo React de la guía y monta un botón y un campo en una página de prueba.
**Qué comprobar:** Los componentes aparecen con el tema aplicado y puedes navegar con teclado.
Revisión documental individual; instalación no ejecutada por Alexandría.

## `chakra-ui`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,typescript,react,library

**Qué es:** Sistema de componentes React accesibles para crear productos y sistemas de diseño con rapidez, compatible con Next.js RSC.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/chakra-ui/chakra-ui

**Instalación** [+]:

```
yarn add @chakra-ui/react @emotion/react
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: construir el panel de un SaaS con componentes accesibles y tema propio; crear un sistema de diseño con tokens y recetas de estilo
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala `@chakra-ui/react` y `@emotion/react` en un proyecto React y renderiza un botón con el proveedor.
**Qué comprobar:** El componente se muestra con el tema por defecto y cambia a modo oscuro.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `storybook`, `lucide`, `claude-code`
**Alternativas (elige una):** `mantine`, `mui`

## `copilotkit`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic · tags=ui,agents,react,typescript

**Qué es:** Stack frontend para agentes y UI generativa en React, creadores del protocolo AG-UI.
**Stack:** Node; framework compatible; backend de agente; proveedor del modelo
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La interfaz y el protocolo no incluyen inferencia; backend, modelos y servicios gestionados se presupuestan aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El prompt de onboarding ayuda a un agente a instalar; no demuestra que el plan de Claude Code o Codex ejecute el backend del producto
- Coste: El coste depende del proveedor o la ruta. La interfaz y el protocolo no incluyen inferencia; backend, modelos y servicios gestionados se presupuestan aparte
- Equipo: Preparación según la ruta elegida. Node; framework compatible; backend de agente; proveedor del modelo
**Repo:** https://github.com/CopilotKit/CopilotKit

**Instalación** [+]:

```
npx copilotkit@latest create
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Añadir asistencia contextual a una app; Mostrar componentes generados a partir de respuestas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una app de ejemplo y una acción que lea un dato ficticio de la interfaz
**Qué comprobar:** El agente recibe el contexto y devuelve una acción que puedes revisar
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `mastra`, `agent-framework`, `crewai`, `openbot`
**Alternativas (elige una):** `assistant-ui`

## `daisyui`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,design,javascript

**Qué es:** La librería de componentes más popular para Tailwind CSS, con clases semánticas y temas.
**Stack:** Proyecto con Tailwind compatible; Node y gestor de paquetes
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca no requiere IA; plantillas o servicios comerciales relacionados son opcionales
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un plugin de estilos y clases de Tailwind; sigue la guía de la versión instalada para configurar el CSS
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca no requiere IA; plantillas o servicios comerciales relacionados son opcionales
- Equipo: Preparación según la ruta elegida. Proyecto con Tailwind compatible; Node y gestor de paquetes
**Repo:** https://github.com/saadeghi/daisyui

**Instalación** [+]:

```
npm i -D daisyui@latest
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar una web con clases semánticas; Añadir temas a un panel sencillo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade un botón y una tarjeta con un tema y cambia al segundo tema
**Qué comprobar:** Se actualizan colores sin reescribir cada componente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `tailwindcss`, `lucide`, `flexoki`
**Alternativas (elige una):** `ui`

## `excalidraw`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=design,docs,typescript

**Qué es:** Pizarra virtual open source para diagramas con estilo dibujado a mano, colaborativa.
**Stack:** Navegador para la app; React solo si integras el componente
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La pizarra básica no requiere IA; productos alojados adicionales pueden tener planes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Para dibujar puedes usar la app web; npm instala el componente para integrarlo en otra aplicación
- Coste: Sin pago a un modelo en la ruta básica. La pizarra básica no requiere IA; productos alojados adicionales pueden tener planes
- Equipo: Preparación según la ruta elegida. Navegador para la app; React solo si integras el componente
**Repo:** https://github.com/excalidraw/excalidraw

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/excalidraw/excalidraw/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explicar un flujo a un equipo; Bocetar una interfaz antes de construirla
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Dibuja tres pasos de un proceso y exporta el diagrama como imagen
**Qué comprobar:** Puedes abrir la imagen y conservar el archivo editable
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `penpot`, `flexoki`, `kroki`
**Alternativas (elige una):** `tldraw`, `mermaid`

## `flexoki`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=estilos,reference,css

**Qué es:** Paleta de color para texto, código e interfaces que puede servir de referencia al definir un sistema visual.
**Stack:** Navegador o editor con un tema compatible
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita modelo ni API; el proyecto pide atribución al portar la paleta
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una referencia de color y sus ports; no instala una aplicación ni garantiza contraste en cualquier combinación
- Coste: Sin pago a un modelo en la ruta básica. No necesita modelo ni API; el proyecto pide atribución al portar la paleta
- Equipo: Preparación según la ruta elegida. Navegador o editor con un tema compatible
**Repo:** https://github.com/kepano/flexoki

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Definir una paleta para una app de notas; Crear un tema de editor
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Aplica la paleta a una página de prueba y comprueba contraste de texto y controles
**Qué comprobar:** Puedes identificar colores semánticos legibles en claro y oscuro
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `tailwindcss`, `daisyui`, `excalidraw`, `normalize.css`

## `heroui`
role=library · exec=local · setup=easy · mcp=True · prov=— · tags=ui,typescript

**Qué es:** Librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, dashboards y landings consistentes.
**Stack:** React; Tailwind CSS v4 y configuración según guía; Node
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca no exige modelo; servicios y contenidos comerciales relacionados tienen condiciones aparte
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Antes NextUI; el README actual usa paquetes styles y react; MCP y llms.txt son rutas auxiliares para agentes
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca no exige modelo; servicios y contenidos comerciales relacionados tienen condiciones aparte
- Equipo: Preparación según la ruta elegida. React; Tailwind CSS v4 y configuración según guía; Node
**Repo:** https://github.com/heroui-inc/heroui

**Instalación** [+]:

```
npm install @heroui/styles @heroui/react
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir formularios accesibles; Crear una interfaz con temas compartidos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade un botón y un campo con un tema sencillo y prueba el foco por teclado
**Qué comprobar:** Los componentes muestran el tema y estados interactivos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `tailwindcss`, `claude-code`, `swr`, `echarts`
**Alternativas (elige una):** `mui`

## `json-render`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=ia-ui,library,typescript

**Qué es:** Framework para generar interfaces desde una representación JSON y un catálogo de componentes definido por el desarrollador.
**Stack:** Node; renderer del framework; catálogo y esquema; modelo solo para generación
**Acceso y costes:**
- API de IA: API de IA opcional. Renderizar JSON no exige modelo; generar el JSON con IA sí usa el proveedor elegido; otros renderers añaden dependencias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La integración MCP Apps necesita soporte de UI en el cliente; no equivale a soporte universal de todos los agentes MCP
- Coste: El coste depende del proveedor o la ruta. Renderizar JSON no exige modelo; generar el JSON con IA sí usa el proveedor elegido; otros renderers añaden dependencias
- Equipo: Preparación según la ruta elegida. Node; renderer del framework; catálogo y esquema; modelo solo para generación
**Repo:** https://github.com/vercel-labs/json-render

**Instalación** [+]:

```
# for React
npm install @json-render/core @json-render/react
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear interfaces dinámicas desde datos; Acotar la UI que puede proponer un modelo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Renderiza primero un JSON escrito a mano con una tarjeta y un botón permitido
**Qué comprobar:** La interfaz refleja el JSON y rechaza componentes fuera de catálogo
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ui`, `remotion`, `vercel-ai`

## `konva`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=componentes,library,typescript

**Qué es:** Biblioteca de canvas para construir editores gráficos, diagramas e interfaces con formas y objetos interactivos.
**Stack:** Node; proyecto web; wrapper si usas React u otro framework
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca MIT no exige licencia de pago ni modelo; backend y assets son independientes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El renderizado de servidor necesita un backend canvas adicional; no instales esas dependencias si solo lo usas en el navegador
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca MIT no exige licencia de pago ni modelo; backend y assets son independientes
- Equipo: Preparación según la ruta elegida. Node; proyecto web; wrapper si usas React u otro framework
**Repo:** https://github.com/konvajs/konva

**Instalación** [+]:

```
npm install konva
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un editor de anotaciones; Crear un pequeño diagrama interactivo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Dibuja un rectángulo arrastrable y exporta el canvas a imagen
**Qué comprobar:** Puedes mover la forma y abrir la exportación
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ui`, `tailwindcss`, `lucide`

## `lucide`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,design,typescript

**Qué es:** Librería de más de 1500 iconos SVG consistentes, con paquetes para React, Vue y más.
**Stack:** Paquete para tu framework o archivos SVG; proyecto web
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita modelo ni API; licencia ISC del proyecto para usos personales y comerciales
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Elige el paquete del framework y no dependas de un número fijo de iconos que cambia con las versiones
- Coste: Sin pago a un modelo en la ruta básica. No necesita modelo ni API; licencia ISC del proyecto para usos personales y comerciales
- Equipo: Preparación según la ruta elegida. Paquete para tu framework o archivos SVG; proyecto web
**Repo:** https://github.com/lucide-icons/lucide

**Instalación** [+]:

```
pnpm add lucide-static
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Unificar iconos de navegación; Ilustrar acciones en una interfaz
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade un icono de búsqueda junto a una etiqueta y cambia tamaño y grosor
**Qué comprobar:** El icono se ve consistente y el control conserva nombre accesible
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ui`, `tailwindcss`, `daisyui`, `konva`, `normalize.css`, `radix-primitives`

## `magicui`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui

**Qué es:** Componentes React para componer secciones de página con shadcn y Tailwind, como una cuadrícula Bento o un bloque de video.
**Stack:** React; dependencias del componente elegido; proyecto de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Los componentes del repositorio son MIT; productos o plantillas comerciales asociados tienen términos propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Copiar un componente puede añadir dependencias; verifica qué se incorpora antes de instalar varios efectos
- Coste: Sin pago a un modelo en la ruta básica. Los componentes del repositorio son MIT; productos o plantillas comerciales asociados tienen términos propios
- Equipo: Preparación según la ruta elegida. React; dependencias del componente elegido; proyecto de prueba
**Repo:** https://github.com/magicuidesign/magicui

**Instalación** [?]:

```
Seguir la instalación original: https://magicui.design/docs
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Quieres componer una sección React con una cuadrícula de funcionalidades, un bloque de video o un registro de componentes bajo MIT.
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade un componente visual pequeño y comprueba el diseño en móvil y con movimiento reducido
**Qué comprobar:** El contenido sigue siendo legible y el componente no desborda
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ui`, `tailwindcss`, `motion`, `claude-code`, `animejs`
**Alternativas (elige una):** `react-bits`

## `mantine`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,typescript,react,library

**Qué es:** Biblioteca de componentes React completa con más de 100 componentes, hooks, formularios, gráficos, fechas y notificaciones.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/mantinedev/mantine

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/mantinedev/mantine/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: montar un panel de administración con formularios, tablas y gráficos; prototipar una app React con componentes accesibles y modo oscuro
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala @mantine/core y @mantine/hooks, envuelve la app en MantineProvider y renderiza un formulario.
**Qué comprobar:** El formulario se muestra con estilos de Mantine y valida los campos.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `storybook`, `recharts`, `claude-code`
**Alternativas (elige una):** `chakra-ui`, `mui`

## `mui`
role=library · exec=local · setup=easy · mcp=True · prov=— · tags=ui,react,javascript

**Qué es:** Librería de componentes React completa que implementa Material Design de Google.
**Stack:** React y React DOM compatibles; Node; Emotion en ruta por defecto
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Material UI base es MIT; algunos productos MUI X, plantillas y soporte tienen condiciones comerciales
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. El MCP de documentación es un paquete separado stdio; no convierte las funciones de pago en gratuitas
- Coste: El coste depende del proveedor o la ruta. Material UI base es MIT; algunos productos MUI X, plantillas y soporte tienen condiciones comerciales
- Equipo: Preparación según la ruta elegida. React y React DOM compatibles; Node; Emotion en ruta por defecto
**Repo:** https://github.com/mui/material-ui

**Instalación** [?]:

```
Seguir la instalación original: https://mui.com/material-ui/getting-started/installation/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un dashboard Material Design; Construir una pantalla de ajustes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Construye un formulario pequeño y verifica estados de error y foco
**Qué comprobar:** Los campos muestran validación y se recorren con teclado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `recharts`, `swr`, `vercel-ai`
**Alternativas (elige una):** `ant-design`, `ui`, `heroui`, `chakra-ui`, `mantine`

## `normalize.css`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,design

**Qué es:** Hoja de estilos que normaliza los defaults entre navegadores para partir de una base de rendering uniforme.
**Stack:** Proyecto HTML/CSS; gestor npm o archivo de estilos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa modelo ni API; es una hoja de estilos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Normalizar no hace idéntico todo el diseño ni sustituye probar la página en sus navegadores objetivo
- Coste: Sin pago a un modelo en la ruta básica. No usa modelo ni API; es una hoja de estilos
- Equipo: Preparación según la ruta elegida. Proyecto HTML/CSS; gestor npm o archivo de estilos
**Repo:** https://github.com/necolas/normalize.css

**Instalación** [+]:

```
npm install --save normalize.css
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Unificar una base de estilos; Reducir diferencias iniciales de formularios
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Incluye la hoja en una página con formulario y compara dos navegadores
**Qué comprobar:** Puedes observar qué estilos base se normalizan y cuáles siguen siendo tuyos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `radix-primitives`, `flexoki`, `lucide`

## `onlook`
role=app · exec=local · setup=easy · mcp=False · prov=anthropic · tags=design,ui,coding-agent,typescript

**Qué es:** Editor visual con IA para construir, estilar y editar apps React y Tailwind como en Figma.
**Stack:** Proyecto React/Tailwind compatible; dependencias de desarrollo; modelo para AI
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El editor y las funciones AI tienen requisitos distintos; los proveedores y servicios alojados pueden cobrar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Un elemento pendiente de MCP en la hoja de ruta no acredita soporte ya implementado
- Coste: El coste depende del proveedor o la ruta. El editor y las funciones AI tienen requisitos distintos; los proveedores y servicios alojados pueden cobrar
- Equipo: Preparación según la ruta elegida. Proyecto React/Tailwind compatible; dependencias de desarrollo; modelo para AI
**Repo:** https://github.com/onlook-dev/onlook

**Instalación** [+]:

```
docker-compose up -d
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Ajustar una interfaz React de forma visual; Prototipar un rediseño sobre código
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una app de prueba, cambia un espaciado visualmente y revisa el diff de código
**Qué comprobar:** El cambio visible corresponde a un cambio identificable en los archivos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `tailwindcss`, `supabase`, `ui`
**Alternativas (elige una):** `open-design`

## `open-design`
role=app · exec=hybrid · setup=medium · mcp=True · prov=— · tags=agents,design,typescript

**Qué es:** Espacio de diseño colaborativo con IA que genera, maqueta y anima interfaces desde lenguaje natural.
**Stack:** Docker o distribución elegida; agente o proveedor; WSL2 según ruta Windows
**Acceso y costes:**
- API de IA: API de IA opcional. Admite agentes, BYOK y modelos locales; planes Go, proveedores y generación de medios tienen límites y gastos propios
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Las conexiones MCP de los tres clientes están documentadas; los endpoints internos de modelos requieren configuración explícita por su protección SSRF
- Coste: El coste depende del proveedor o la ruta. Admite agentes, BYOK y modelos locales; planes Go, proveedores y generación de medios tienen límites y gastos propios
- Equipo: Preparación según la ruta elegida. Docker o distribución elegida; agente o proveedor; WSL2 según ruta Windows
**Repo:** https://github.com/nexu-io/open-design

**Instalación** [+]:

```
git clone https://github.com/nexu-io/open-design.git
cd open-design/deploy
cp .env.example .env
echo "OD_API_TOKEN=$(openssl rand -hex 32)" >> .env
docker compose up -d
# open http://127.0.0.1:7456
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar un dashboard; Iterar una interfaz con feedback de equipo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un proyecto de prueba y pide una pantalla pequeña antes de activar generación de medios
**Qué comprobar:** Puedes revisar el artefacto y el agente o proveedor que lo generó
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `design.md`, `hyperframes`, `ollama`
**Alternativas (elige una):** `onlook`

## `openui`
role=library · exec=hybrid · setup=easy · mcp=False · prov=— · tags=ui,agents,typescript

**Qué es:** Estándar abierto de Thesys para UI generativa: el LLM responde con interfaces, no solo texto.
**Stack:** Node; framework elegido; backend y modelo; catálogo de componentes
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El framework y la skill no incluyen llamadas de modelo; proveedor y backend tienen costes separados
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: Modelo local no documentado. La skill sirve para construir y depurar; su portabilidad no implica que la app use la suscripción del agente para inferencia
- Coste: El coste depende del proveedor o la ruta. El framework y la skill no incluyen llamadas de modelo; proveedor y backend tienen costes separados
- Equipo: Preparación según la ruta elegida. Node; framework elegido; backend y modelo; catálogo de componentes
**Repo:** https://github.com/thesysdev/openui

**Instalación** [+]:

```
npx @openuidev/cli@latest create --name genui-chat-app
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear respuestas de chat con interfaz; Construir formularios generados y acotados
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Define una tarjeta permitida y pide al modelo una respuesta que la utilice
**Qué comprobar:** El renderer muestra solo componentes del catálogo esperado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `langchain`, `copilotkit`

## `penpot`
role=app · exec=local · setup=heavy · mcp=True · prov=— · tags=design,docker

**Qué es:** Plataforma open-source de diseño y prototipado colaborativo, pensada para equipos de producto y diseño que quieren soberanía sobre sus archivos.
**Stack:** Navegador y cuenta o despliegue propio; MCP y plugin solo para agentes
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El diseño básico no necesita modelo; hosting, planes y el agente MCP mantienen costes separados
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. MCP puede leer y modificar el workspace mediante su plugin; es opcional para diseñar manualmente
- Coste: El coste depende del proveedor o la ruta. El diseño básico no necesita modelo; hosting, planes y el agente MCP mantienen costes separados
- Equipo: Preparación según la ruta elegida. Navegador y cuenta o despliegue propio; MCP y plugin solo para agentes
**Repo:** https://github.com/penpot/penpot

**Instalación** [?]:

```
Seguir la instalación original: https://help.penpot.app/technical-guide/getting-started/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar una interfaz antes de programarla; Colaborar en un sistema de diseño
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Dibuja una tarjeta con texto y botón y comparte un prototipo de prueba
**Qué comprobar:** Se pueden inspeccionar componentes y recorrer la interacción
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `excalidraw`, `tailwindcss`

## `plasmic`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=design,typescript

**Qué es:** Builder visual para apps y sitios conectado a tu propia base de código, que permite diseñar y publicar sin perder el control del código real.
**Stack:** Cuenta o despliegue Studio; proyecto Next.js para este loader; Node
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El editor básico no exige LLM; plataforma alojada y planes tienen costes; loader y plataforma tienen licencias diferentes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El loader-nextjs no instala todo Studio; el código fuera de platform es MIT y platform usa AGPL
- Coste: El coste depende del proveedor o la ruta. El editor básico no exige LLM; plataforma alojada y planes tienen costes; loader y plataforma tienen licencias diferentes
- Equipo: Preparación según la ruta elegida. Cuenta o despliegue Studio; proyecto Next.js para este loader; Node
**Repo:** https://github.com/plasmicapp/plasmic

**Instalación** [+]:

```
npm install @plasmicapp/loader-nextjs
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Permitir editar contenido visual de una web; Prototipar una página conectada a React
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Diseña una sección de prueba y cárgala desde la aplicación conectada
**Qué comprobar:** Ves el contenido visual y puedes inspeccionar la integración en el código
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `tailwindcss`, `ui`, `supabase`

## `radix-primitives`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,react,typescript

**Qué es:** Componentes React sin estilos y accesibles para construir sistemas de diseño propios.
**Stack:** React; Node; estilos propios
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa modelos ni API; alojamiento es independiente
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Los comandos pnpm del README preparan el repositorio de contribución; para usarlo sigue la instalación de la primitiva en la guía
- Coste: Sin pago a un modelo en la ruta básica. No usa modelos ni API; alojamiento es independiente
- Equipo: Preparación según la ruta elegida. React; Node; estilos propios
**Repo:** https://github.com/radix-ui/primitives

**Instalación** [?]:

```
Seguir la instalación original: https://www.radix-ui.com/primitives/docs/overview/getting-started
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un menú accesible; Crear un sistema de diseño sin estilos impuestos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Construye el popover de inicio y prueba abrir, cerrar y devolver foco con teclado
**Qué comprobar:** El foco y el estado del popover se comportan como esperas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ui`, `tailwindcss`, `lucide`, `normalize.css`

## `react-bits`
role=library · exec=local · setup=easy · mcp=True · prov=— · tags=ui,react,javascript

**Qué es:** Efectos de texto, fondos gráficos y componentes interactivos para añadir animaciones puntuales a una interfaz React.
**Stack:** React o Next.js; Node; dependencias de la variante del componente
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El repositorio usa MIT más Commons Clause; Pro y productos externos se revisan por separado; no requiere modelo
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. MCP funciona mediante el registro shadcn; no todas las variantes JS, TS, CSS y Tailwind tienen las mismas dependencias
- Coste: El coste depende del proveedor o la ruta. El repositorio usa MIT más Commons Clause; Pro y productos externos se revisan por separado; no requiere modelo
- Equipo: Preparación según la ruta elegida. React o Next.js; Node; dependencias de la variante del componente
**Repo:** https://github.com/DavidHDev/react-bits

**Instalación** [+]:

```
npx shadcn@latest add @react-bits/SplitText-TS-TW
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear un encabezado animado; Prototipar una interacción visual
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instala un único componente SplitText en una página de prueba y comprueba su lectura sin animación
**Qué comprobar:** El texto sigue siendo legible y puedes ajustar duración y estilos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ui`, `tailwindcss`, `claude-code`
**Alternativas (elige una):** `magicui`

## `screenshot-to-code`
role=app · exec=cloud · setup=easy · mcp=False · prov=openai,anthropic,google · tags=ui,vision,code,python

**Qué es:** Convierte capturas, mockups o diseños de Figma en código limpio HTML, Tailwind, React o Vue.
**Stack:** Python y Poetry; Node y pnpm; clave de proveedor en ruta principal; Chromium para preview
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. La ruta principal pide al menos una clave; extracción y edición de imágenes pueden usar servicios adicionales; Ollama se remite a una adaptación que no se verifica aquí
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. Separa backend y frontend; la mención Claude code-gen significa modelo de generación y no Claude Code como agente anfitrión
- Coste: El coste depende del proveedor o la ruta. La ruta principal pide al menos una clave; extracción y edición de imágenes pueden usar servicios adicionales; Ollama se remite a una adaptación que no se verifica aquí
- Equipo: Preparación según la ruta elegida. Python y Poetry; Node y pnpm; clave de proveedor en ruta principal; Chromium para preview
**Repo:** https://github.com/abi/screenshot-to-code

**Instalación** [+]:

```
docker-compose up -d --build
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Convertir un mockup propio en prototipo; Explorar una estructura HTML a partir de una captura
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Carga una captura de una interfaz propia mínima y compara el HTML generado con ella
**Qué comprobar:** Puedes revisar código y vista previa y señalar diferencias
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `tailwindcss`, `ui`, `playwright`
**Alternativas (elige una):** `stitch-sdk`

## `stitch-sdk`
role=library · exec=cloud · setup=easy · mcp=True · prov=google · tags=ui,design,typescript

**Qué es:** SDK de Google Labs para generar pantallas de UI desde texto y extraer su HTML y capturas por código.
**Stack:** Node.js; clave Stitch u OAuth con proyecto; servicio Stitch
**Acceso y costes:**
- API de IA: API de IA necesaria. Requiere autenticación del servicio; el README no confirma aquí su tarifa o cupo, por lo que no se promete ni gratuidad ni cobro por llamada
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. El proxy stdio permite exponer herramientas a clientes MCP; su acceso no acredita que el plan de Antigravity pague las llamadas
- Coste: Coste por confirmar. Requiere autenticación del servicio; el README no confirma aquí su tarifa o cupo, por lo que no se promete ni gratuidad ni cobro por llamada
- Equipo: Preparación según la ruta elegida. Node.js; clave Stitch u OAuth con proyecto; servicio Stitch
**Repo:** https://github.com/google-labs-code/stitch-sdk

**Instalación** [+]:

```
npm install @google/stitch-sdk
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar borradores de UI; Conectar herramientas Stitch a un agente mediante proxy MCP
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Genera una pantalla sencilla con texto ficticio y guarda HTML y captura
**Qué comprobar:** Puedes abrir ambos archivos y revisar el resultado generado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vercel-ai`, `stitch-skills`, `design.md`
**Alternativas (elige una):** `screenshot-to-code`

## `storybook`
role=app · exec=local · setup=easy · mcp=False · prov=— · tags=ui,typescript,javascript,docs

**Qué es:** Taller de frontend para construir, documentar y probar componentes y páginas de UI de forma aislada en React, Vue, Angular y otros.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/storybookjs/storybook

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/storybookjs/storybook/blob/next/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: documentar el sistema de diseño de un producto con ejemplos interactivos; probar estados límite de componentes sin montar toda la aplicación
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Ejecuta el comando de inicialización de Storybook en un proyecto web de prueba y abre el servidor local.
**Qué comprobar:** Aparecen las stories de ejemplo y puedes cambiar sus props desde el panel de controles.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `playwright`, `tailwindcss`, `mantine`, `chakra-ui`, `cypress`

## `swr`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,typescript

**Qué es:** Librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano.
**Stack:** React; endpoint de datos de prueba; función fetcher
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere IA; el endpoint consultado y su alojamiento pueden cobrar por uso
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una herramienta de obtención y caché de datos, no una librería de botones ni un backend
- Coste: Sin pago a un modelo en la ruta básica. No requiere IA; el endpoint consultado y su alojamiento pueden cobrar por uso
- Equipo: Preparación según la ruta elegida. React; endpoint de datos de prueba; función fetcher
**Repo:** https://github.com/vercel/swr

**Instalación** [?]:

```
Seguir la instalación original: https://swr.vercel.app/docs/getting-started
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Actualizar un panel sin recargar; Revalidar datos al volver a una pestaña
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Muestra un perfil ficticio y cambia el dato del servidor para observar la revalidación
**Qué comprobar:** Se distinguen carga, error, datos cacheados y datos nuevos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ui`, `heroui`, `supabase`, `ant-design`, `mui`, `uplot`
**Alternativas (elige una):** `tanstack-query`

## `tailwindcss`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,design,typescript

**Qué es:** Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado.
**Stack:** Proyecto Vite u otra integración elegida; Node
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El framework no usa modelos ni API; productos de pago del ecosistema tienen condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Elige la integración de tu framework; la configuración actual no debe copiarse sin más de tutoriales de Tailwind v3
- Coste: Sin pago a un modelo en la ruta básica. El framework no usa modelos ni API; productos de pago del ecosistema tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Proyecto Vite u otra integración elegida; Node
**Repo:** https://github.com/tailwindlabs/tailwindcss

**Instalación** [?]:

```
Seguir la instalación original: https://tailwindcss.com/docs/installation/using-vite
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Diseñar un formulario responsive; Definir colores y espaciado consistentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Crea una tarjeta adaptable y cambia el espaciado con utilidades
**Qué comprobar:** Puedes comprobar diferencias entre móvil y escritorio
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ui`, `daisyui`, `heroui`, `magicui`

## `tanstack-query`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=frontend,data-fetching,cache,typescript

**Qué es:** Biblioteca para obtener, cachear, sincronizar y actualizar datos del servidor en React, Vue, Solid, Svelte, Angular y otros frameworks.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.
- Equipo: Equipo normal; revisar dependencias. Un proyecto JavaScript o TypeScript con el adaptador de tu framework.
**Repo:** https://github.com/TanStack/query

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/TanStack/query/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Cachear y revalidar datos de una API en una app React; Mostrar estados de carga y error sin estado global manual
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Envuelve una llamada a una API pública de prueba en una consulta y muestra sus estados
**Qué comprobar:** Ves carga, datos y un refetch al volver a enfocar la ventana
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `supabase`, `ui`, `tailwindcss`
**Alternativas (elige una):** `swr`

## `tldraw`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=design,ui,react,typescript

**Qué es:** SDK para construir apps de lienzo infinito en React, como pizarras y herramientas de diagramas.
**Stack:** React; Node; estilos del SDK; licencia para producción según condiciones
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El SDK permite desarrollo gratuito y exige clave de licencia para producción; starter kits MIT no cambian la licencia del SDK
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. No requiere modelo; no confundas el ejemplo de pizarra con una aplicación terminada con permisos y persistencia
- Coste: El coste depende del proveedor o la ruta. El SDK permite desarrollo gratuito y exige clave de licencia para producción; starter kits MIT no cambian la licencia del SDK
- Equipo: Preparación según la ruta elegida. React; Node; estilos del SDK; licencia para producción según condiciones
**Repo:** https://github.com/tldraw/tldraw

**Instalación** [+]:

```
npm i tldraw
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir una pizarra de colaboración; Crear un editor de diagramas propio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Muestra un lienzo y añade una forma personalizada en un proyecto de prueba
**Qué comprobar:** Puedes mover, editar y guardar el estado de la forma
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vercel-ai`, `ui`, `supabase`
**Alternativas (elige una):** `excalidraw`

## `ui`
role=library · exec=local · setup=easy · mcp=True · prov=— · tags=ui,typescript

**Qué es:** Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada.
**Stack:** Proyecto React compatible; Node; gestor de paquetes; configuración del framework
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Los componentes abiertos no necesitan IA; registros privados, servicios y el agente pueden tener costes
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. El MCP oficial permite consultar e instalar componentes desde los clientes; el componente sigue siendo código de tu aplicación
- Coste: Sin pago a un modelo en la ruta básica. Los componentes abiertos no necesitan IA; registros privados, servicios y el agente pueden tener costes
- Equipo: Preparación según la ruta elegida. Proyecto React compatible; Node; gestor de paquetes; configuración del framework
**Repo:** https://github.com/shadcn-ui/ui

**Instalación** [?]:

```
Seguir la instalación original: https://ui.shadcn.com/docs/installation
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Construir un formulario con componentes propios; Crear un sistema de interfaz con código modificable
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Añade una tarjeta con botón y modifica sus estilos desde el código copiado al proyecto
**Qué comprobar:** Ves el componente y puedes localizar su archivo editable
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `tailwindcss`, `radix-primitives`, `lucide`, `magicui`, `claude-code`
**Alternativas (elige una):** `mui`, `ant-design`, `daisyui`

## `ui-sdk`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=ia-ui,library,typescript

**Qué es:** Colección de comportamientos y recursos para que agentes construyan interfaces con patrones de interacción definidos.
**Stack:** Framework compatible; Node; skill opcional para el agente
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca no necesita modelo en ejecución; el agente que utilice su skill mantiene sus costes
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Está en beta; instala el adaptador correcto para React, Vue, Svelte, Solid o web y revisa cambios de API
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca no necesita modelo en ejecución; el agente que utilice su skill mantiene sus costes
- Equipo: Preparación según la ruta elegida. Framework compatible; Node; skill opcional para el agente
**Repo:** https://github.com/vercel-labs/ui

**Instalación** [+]:

```
npm install @ui-sdk/react @ui-sdk/core
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Crear componentes con comportamientos reutilizables; Guiar a un agente con patrones de interfaz
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Construye una primitiva con comportamiento de foco y prueba abrir y cerrar su contenido
**Qué comprobar:** Puedes verificar recuperación de foco y estados interactivos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `tailwindcss`, `playwright`
