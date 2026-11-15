# 9. Diseño, UI & Frontend — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `animejs`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** API simple y potente para líneas de tiempo, scroll y animaciones complejas.
**Stack:** JavaScript
**Repo:** https://github.com/juliangarnier/anime

**Instalación** [~]: `npm install anime.js   (o: pnpm add anime.js)`
_Nombre npm puede diferir de 'Anime.js'; verifica en npmjs.com._

**Elige si:** quieres animaciones potentes sin framework
**Evita si:** usas React y quieres animaciones declarativas; mira `motion`
**Alternativas (elige una):** `gsap`, `motion`

## `ant-design`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Componentes muy completos para apps de negocio: tablas, formularios, fechas y layouts de backoffice.
**Stack:** TypeScript, React
**Repo:** https://github.com/ant-design/ant-design

**Instalación** [~]: `npm install ant design   (o: pnpm add ant design)`
_Nombre npm puede diferir de 'Ant Design'; verifica en npmjs.com._

**Elige si:** construyes apps empresariales con muchos datos
**Evita si:** quieres un estilo más personalizado; mira `ui`
**Combina con:** `echarts`
**Alternativas (elige una):** `mui`, `ui`

## `assistant-ui`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Componentes componibles de chat con streaming, adjuntos, markdown y herramientas, compatibles con AI SDK y LangGraph.
**Stack:** TypeScript, React
**Repo:** https://github.com/assistant-ui/assistant-ui

**Instalación** [~]: `npm install assistant-ui   (o: pnpm add assistant-ui)`
_Nombre npm puede diferir de 'assistant-ui'; verifica en npmjs.com._

**Elige si:** necesitas una UI de chat pulida en React
**Evita si:** quieres agentes que manipulen tu app; mira `copilotkit`
**Combina con:** `vercel-ai`, `ui`
**Alternativas (elige una):** `copilotkit`

## `copilotkit`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'anthropic']

**Qué es:** Añade copilotos, chat y agentes que actúan sobre tu app, con estado compartido entre agente y UI. Se integra con LangGraph, Mastra y más.
**Stack:** TypeScript, React
**Repo:** https://github.com/CopilotKit/CopilotKit

**Instalación** [~]: `npm install copilotkit   (o: pnpm add copilotkit)`
_Nombre npm puede diferir de 'CopilotKit'; verifica en npmjs.com._

**Elige si:** quieres agentes que interactúen con la UI de tu app
**Evita si:** solo necesitas una ventana de chat; mira `assistant-ui`
**Combina con:** `langgraph`, `mastra`
**Alternativas (elige una):** `assistant-ui`

## `daisyui`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Añade clases como `btn` o `card` sobre Tailwind para escribir menos HTML, sin JavaScript.
**Stack:** JavaScript, CSS, Tailwind
**Repo:** https://github.com/saadeghi/daisyui

**Instalación** [~]: `npm install daisyui   (o: pnpm add daisyui)`
_Nombre npm puede diferir de 'daisyUI'; verifica en npmjs.com._

**Elige si:** usas Tailwind y quieres componentes sin JavaScript
**Evita si:** usas React y quieres control total; mira `ui`
**Combina con:** `tailwindcss`
**Alternativas (elige una):** `ui`

## `design.md`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve la inconsistencia de marca cuando varias personas o agentes tocan la UI.
**Stack:** Markdown/YAML
**Repo:** https://github.com/google-labs-code/design.md

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/design.md/). Si necesitas el código: git clone https://github.com/google-labs-code/design.md`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres consistencia de marca con IA y usas agentes para UI
**Evita si:** no usas agentes para generar código de UI
**Combina con:** `impeccable`

## `excalidraw`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Dibuja diagramas rápidos que parecen bocetos, colabora en tiempo real y embébela en tus apps como componente React.
**Stack:** TypeScript, React, Canvas
**Repo:** https://github.com/excalidraw/excalidraw

**Instalación** [~]: `git clone https://github.com/excalidraw/excalidraw && cd excalidraw && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres diagramas rápidos con estilo boceto
**Evita si:** prefieres diagramas como texto; mira `mermaid`
**Alternativas (elige una):** `tldraw`, `mermaid`

## `gsap`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Es la herramienta de referencia del motion web profesional.
**Stack:** JavaScript
**Repo:** https://github.com/greensock/GSAP

**Instalación** [~]: `npm install gsap   (o: pnpm add gsap)`
_Nombre npm puede diferir de 'GSAP'; verifica en npmjs.com._

**Elige si:** necesitas animación avanzada y control fino de timelines
**Evita si:** te basta animar componentes React con API declarativa (motion)
**Combina con:** `motion`
**Alternativas (elige una):** `animejs`

## `heroui`
role=library · exec=local · setup=easy · mcp=True · prov=—

**Qué es:** Resuelve la accesibilidad seria sin renunciar a un estilado moderno.
**Stack:** Node.js, React, Tailwind
**Repo:** https://github.com/heroui-inc/heroui

**Instalación** [~]: `npm install heroui   (o: pnpm add heroui)`
_Nombre npm puede diferir de 'heroui'; verifica en npmjs.com._

**Elige si:** quieres calidad + accesibilidad listas
**Evita si:** quieres control copy-paste del código (ui)
**Combina con:** `tailwindcss`, `swr`
**Alternativas (elige una):** `mui`

## `impeccable`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Ataca el patrón repetitivo de interfaces que "huelen" a IA.
**Stack:** Node (`npx impeccable`)
**Repo:** https://github.com/pbakaus/impeccable

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/impeccable/). Si necesitas el código: git clone https://github.com/pbakaus/impeccable`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres frontends que no parezcan generados por IA
**Evita si:** no generas UI con agentes
**Combina con:** `taste-skill`, `ui-ux-pro-max-skill`

## `lucide`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Iconos limpios y uniformes, usados por shadcn/ui y muchas apps.
**Stack:** TypeScript, SVG
**Repo:** https://github.com/lucide-icons/lucide

**Instalación** [~]: `npm install lucide   (o: pnpm add lucide)`
_Nombre npm puede diferir de 'Lucide'; verifica en npmjs.com._

**Elige si:** necesitas iconos consistentes
**Evita si:** buscas ilustraciones, no iconos
**Combina con:** `ui`

## `magicui`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Apunta al impacto visual más que a la accesibilidad estricta.
**Stack:** Node.js, React/Next.js
**Repo:** https://github.com/magicuidesign/magicui

**Instalación** [~]: `npm install magicui   (o: pnpm add magicui)`
_Nombre npm puede diferir de 'magicui'; verifica en npmjs.com._

**Elige si:** priorizas estética y velocidad
**Evita si:** necesitas accesibilidad estricta (heroui)
**Combina con:** `tailwindcss`, `motion`
**Alternativas (elige una):** `react-bits`

## `motion`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Hizo accesible la animación en el ecosistema React.
**Stack:** JavaScript/React
**Repo:** https://github.com/motiondivision/motion

**Instalación** [~]: `npm install motion   (o: pnpm add motion)`
_Nombre npm puede diferir de 'motion'; verifica en npmjs.com._

**Elige si:** animas componentes React con API declarativa
**Evita si:** necesitas timelines complejos no ligados a React (GSAP)
**Combina con:** `magicui`, `react-three-fiber`
**Alternativas (elige una):** `animejs`

## `mui`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Cientos de componentes accesibles y personalizables para apps React, con temas y sistema de estilos propio.
**Stack:** JavaScript, TypeScript, React
**Repo:** https://github.com/mui/material-ui

**Instalación** [~]: `npm install material ui   (o: pnpm add material ui)`
_Nombre npm puede diferir de 'Material UI'; verifica en npmjs.com._

**Elige si:** quieres una librería React completa y probada
**Evita si:** prefieres copiar componentes y estilarlos con Tailwind; mira `ui`
**Combina con:** `recharts`
**Alternativas (elige una):** `ant-design`, `ui`, `heroui`

## `normalize.css`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve las inconsistencias de margen, tipografía y formularios entre Chrome, Firefox y Safari.
**Stack:** CSS
**Repo:** https://github.com/necolas/normalize.css

**Instalación** [?]: `git clone https://github.com/necolas/normalize.css (verificar README para install)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres base CSS uniforme y ligera
**Evita si:** ya usas el preflight de Tailwind, que cubre lo mismo
**Combina con:** `tailwindcss`

## `onlook`
role=app · exec=local · setup=easy · mcp=False · prov=['anthropic']

**Qué es:** Edita tu app en un lienzo visual o pide cambios a la IA, y Onlook escribe el código en tu proyecto.
**Stack:** TypeScript, Next.js, Tailwind
**Repo:** https://github.com/onlook-dev/onlook

**Instalación** [~]: `git clone https://github.com/onlook-dev/onlook && cd onlook && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres editar tu app React visualmente con ayuda de IA
**Evita si:** necesitas diseño desde cero en vectores; mira `penpot`
**Combina con:** `tailwindcss`, `ui`
**Alternativas (elige una):** `open-design`

## `open-design`
role=app · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Resuelve el ir y venir entre prompt, preview y código exportable.
**Stack:** TypeScript/React, Tauri (Rust)
**Repo:** https://github.com/nexu-io/open-design

**Instalación** [~]: `git clone https://github.com/nexu-io/open-design && cd open-design && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** generas UI desde texto y quieres edición visual
**Evita si:** prefieres editar visualmente sobre tu código existente (plasmic)
**Combina con:** `tailwindcss`, `heroui`
**Alternativas (elige una):** `onlook`

## `openui`
role=library · exec=hybrid · setup=easy · mcp=False · prov=—

**Qué es:** Permite que el modelo devuelva componentes interactivos (tablas, formularios, gráficos) que tu app renderiza.
**Stack:** TypeScript, React
**Repo:** https://github.com/thesysdev/openui

**Instalación** [~]: `npm install openui   (o: pnpm add openui)`
_Nombre npm puede diferir de 'OpenUI'; verifica en npmjs.com._

**Elige si:** quieres que tu agente responda con interfaces
**Evita si:** solo necesitas chat de texto; mira `assistant-ui`
**Combina con:** `copilotkit`

## `penpot`
role=app · exec=local · setup=heavy · mcp=False · prov=—

**Qué es:** Es la alternativa abierta a Figma más conocida.
**Stack:** stack web self-host, Docker (Clojure/ClojureScript)
**Repo:** https://github.com/penpot/penpot

**Instalación** [~]: `git clone https://github.com/penpot/penpot && cd penpot && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres diseño abierto y soberano, self-host
**Evita si:** necesitas generación por IA (open-design) o no quieres operar Docker
**Combina con:** `plasmic`

## `plasmic`
role=app · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Cubre el hueco entre no-code y desarrollo a medida.
**Stack:** Node.js, React/Next.js
**Repo:** https://github.com/plasmicapp/plasmic

**Instalación** [~]: `git clone https://github.com/plasmicapp/plasmic && cd plasmic && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres editar visual sobre tu código React
**Evita si:** generas desde texto sin codebase previo (open-design)
**Combina con:** `tailwindcss`

## `radix-primitives`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Resuelven accesibilidad, foco y teclado en diálogos, menús o tooltips, dejándote el estilo. Son la base de shadcn/ui.
**Stack:** TypeScript, React
**Repo:** https://github.com/radix-ui/primitives

**Instalación** [~]: `npm install radix primitives   (o: pnpm add radix primitives)`
_Nombre npm puede diferir de 'Radix Primitives'; verifica en npmjs.com._

**Elige si:** construyes tu propio sistema de diseño
**Evita si:** quieres componentes ya estilados; mira `ui`
**Combina con:** `ui`, `tailwindcss`

## `react-bits`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Fondos, textos animados y efectos listos para copiar en proyectos React y Next.js.
**Stack:** JavaScript, React
**Repo:** https://github.com/DavidHDev/react-bits

**Instalación** [~]: `npm install react bits   (o: pnpm add react bits)`
_Nombre npm puede diferir de 'React Bits'; verifica en npmjs.com._

**Elige si:** quieres efectos visuales llamativos en React
**Evita si:** necesitas componentes de formulario y datos; mira `ui`
**Combina con:** `ui`, `motion`
**Alternativas (elige una):** `magicui`

## `react-three-fiber`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Lleva la mentalidad componible de React al 3D sin abandonar three.js por debajo.
**Stack:** JavaScript/React
**Repo:** https://github.com/pmndrs/react-three-fiber

**Instalación** [~]: `npm install react-three-fiber   (o: pnpm add react-three-fiber)`
_Nombre npm puede diferir de 'react-three-fiber'; verifica en npmjs.com._

**Elige si:** haces 3D en React y quieres reactividad
**Evita si:** no usas React o necesitas control a bajo nivel (three.js directo)
**Combina con:** `motion`

## `screenshot-to-code`
role=app · exec=cloud · setup=easy · mcp=False · prov=['openai', 'anthropic', 'google']

**Qué es:** Sube una imagen o graba un video de una web y obtén código funcional que puedes iterar.
**Stack:** Python, TypeScript, React
**Repo:** https://github.com/abi/screenshot-to-code

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres pasar imágenes de diseño a código
**Evita si:** trabajas desde Figma; mira `figma-context-mcp`
**Combina con:** `tailwindcss`
**Alternativas (elige una):** `stitch-sdk`

## `skills-emil`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el handoff diseño↔código, no solo la estética final.
**Stack:** Markdown (skills), TypeScript/React
**Repo:** https://github.com/emilkowalski/skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/skills_emil/). Si necesitas el código: git clone https://github.com/emilkowalski/skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** trabajas diseño+dev en equipo y sufres el handoff
**Evita si:** buscas componentes listos o trabajas solo
**Combina con:** `ui-ux-pro-max-skill`

## `stitch-sdk`
role=library · exec=cloud · setup=easy · mcp=False · prov=['google']

**Qué es:** Automatiza Stitch, el generador de interfaces de Google, para integrarlo en tus flujos y agentes.
**Stack:** TypeScript
**Repo:** https://github.com/google-labs-code/stitch-sdk

**Instalación** [~]: `npm install stitch sdk   (o: pnpm add stitch sdk)`
_Nombre npm puede diferir de 'Stitch SDK'; verifica en npmjs.com._

**Elige si:** quieres automatizar Stitch
**Evita si:** prefieres herramientas locales; mira `screenshot-to-code`
**Combina con:** `stitch-skills`
**Alternativas (elige una):** `screenshot-to-code`

## `stitch-skills`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Skills en el estándar abierto Agent Skills que enseñan a Claude Code, Codex o Gemini CLI a diseñar con Stitch.
**Stack:** TypeScript, Markdown
**Repo:** https://github.com/google-labs-code/stitch-skills

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/Stitch Skills/). Si necesitas el código: git clone https://github.com/google-labs-code/stitch-skills`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** usas Stitch con un agente de código
**Evita si:** no usas Stitch
**Combina con:** `stitch-sdk`, `gemini-cli`

## `swr`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Cubre el caso de consumir APIs en frontend sin manejar caché a mano.
**Stack:** JavaScript/React
**Repo:** https://github.com/vercel/swr

**Instalación** [~]: `npm install swr   (o: pnpm add swr)`
_Nombre npm puede diferir de 'swr'; verifica en npmjs.com._

**Elige si:** manejas datos remotos en React y quieres caché simple
**Evita si:** prefieres React Query con su modelo de caché global más rico
**Combina con:** `heroui`

## `tailwindcss`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Elimina el contexto de estilos disperso entre hojas y componentes.
**Stack:** Node.js, CSS
**Repo:** https://github.com/tailwindlabs/tailwindcss

**Instalación** [~]: `npm install tailwindcss   (o: pnpm add tailwindcss)`
_Nombre npm puede diferir de 'tailwindcss'; verifica en npmjs.com._

**Elige si:** quieres estilar rápido y consistente
**Evita si:** prefieres CSS-in-JS o estilos scoped por componente
**Combina con:** `heroui`, `magicui`

## `taste-skill`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Ataca el acabado "de plantilla" que delata a las UIs generadas por IA.
**Stack:** Markdown/skills
**Repo:** https://github.com/Leonxlnx/taste-skill

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/taste-skill/). Si necesitas el código: git clone https://github.com/Leonxlnx/taste-skill`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres frontends con gusto y no te basta con UI funcional
**Evita si:** ya tienes un design system cerrado o no usas generadores de imagen
**Combina con:** `ui-ux-pro-max-skill`, `impeccable`

## `three.js`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Abstrae la complejidad de WebGL en escenas, cámaras, luces y mallas.
**Stack:** JavaScript/WebGL
**Repo:** https://github.com/mrdoob/three.js

**Instalación** [~]: `npm install three.js   (o: pnpm add three.js)`
_Nombre npm puede diferir de 'three.js'; verifica en npmjs.com._

**Elige si:** renderizas 3D en web y quieres control a bajo nivel
**Evita si:** trabajas solo 2D o prefieres la ergonomía de React (react-three-fiber)
**Combina con:** `react-three-fiber`, `gsap`

## `tldraw`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Base de muchas herramientas de pizarra y de UI generativa con IA. Ofrece colaboración y personalización completa.
**Stack:** TypeScript, React
**Repo:** https://github.com/tldraw/tldraw

**Instalación** [~]: `npm install tldraw   (o: pnpm add tldraw)`
_Nombre npm puede diferir de 'tldraw'; verifica en npmjs.com._

**Elige si:** construyes una app con lienzo infinito
**Evita si:** solo necesitas una pizarra lista; usa `excalidraw`
**Alternativas (elige una):** `excalidraw`

## `ui`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** El código fuente pasa a ser tuyo y lo editas a voluntad.
**Stack:** Node.js, React, Tailwind, Radix UI
**Repo:** https://github.com/shadcn-ui/ui

**Instalación** [~]: `npm install ui   (o: pnpm add ui)`
_Nombre npm puede diferir de 'ui'; verifica en npmjs.com._

**Elige si:** quieres ser dueño del código de UI
**Evita si:** prefieres una lib "llave en mano" con updates automáticos (heroui)
**Combina con:** `tailwindcss`, `plasmic`
**Alternativas (elige una):** `mui`, `ant-design`, `daisyui`

## `ui-ux-pro-max-skill`
role=skill · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Resuelve el punto débil habitual del código asistido por IA: la jerarquía visual y el acabado.
**Stack:** Node.js (uipro-cli), TypeScript/React
**Repo:** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/ui-ux-pro-max-skill/). Si necesitas el código: git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** generas UI con IA y el resultado se ve genérico o despulido
**Evita si:** no trabajas frontend o ya tienes un sistema de diseño impuesto
**Combina con:** `taste-skill`, `impeccable`, `tailwindcss`
