[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 🧱 ui

> Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 128k | MIT | TypeScript | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

shadcn/ui es un conjunto de componentes React (MIT) pensado para construir tu propia biblioteca de componentes: no se instala como dependencia, sino que el código se copia en tu proyecto. Es muy maduro y popular (~128k estrellas), con una CLI muy activa (shadcn@4.23.0).

## ¿Qué hace?

Ofrece componentes accesibles y personalizables (botones, formularios, diálogos, tablas, gráficos, barras laterales y otros) que pasan a ser código propio. Su sistema de registros permite distribuir componentes, bloques y temas propios o de terceros (por ejemplo `@magicui/...`) con la misma CLI. Incluye un servidor MCP para que asistentes como Claude Code, Cursor, Codex o VS Code busquen e instalen componentes de los registros.

## ¿Cómo lo hace?

La CLI (`npx shadcn@latest init`, `add`, `create`) configura `components.json` y copia los componentes al proyecto. Se apoya en Tailwind CSS y en primitivas accesibles: Radix UI o Base UI, según la documentación actual. Por defecto usa iconos de Lucide. Funciona con Next.js, Vite, React Router, Astro y otros frameworks. Como el código es tuyo, las actualizaciones no llegan solas: hay que volver a traerlas con la CLI y revisar las diferencias.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [tailwindcss](tailwindcss.md) | Sistema de estilos sobre el que están escritos todos los componentes. | Configura Tailwind (o deja que lo haga `shadcn init`) antes de añadir componentes. |
| [Radix Primitives](radix-primitives.md) | Primitivas accesibles sin estilos que usan muchos componentes (alternativa: Base UI). | Se instalan automáticamente al añadir cada componente. |
| [Lucide](lucide.md) | Biblioteca de iconos por defecto (`iconLibrary` en components.json). | Se instala con los componentes que la necesitan. |
| [magicui](magicui.md) | Componentes animados distribuidos como registro de shadcn (`npx shadcn@latest add @magicui/...`). | Inicializa shadcn/ui y luego añade componentes de Magic UI con la misma CLI. |
| [Claude Code](claude-code.md) | Explorar e instalar componentes de los registros desde el asistente vía el servidor MCP de shadcn. | Configura el proyecto con shadcn y registra el servidor MCP según su documentación. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (15). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[AI SDK (Vercel)](vercel-ai.md) · [ai-website-cloner-template](ai-website-cloner-template.md) · [assistant-ui](assistant-ui.md) · [Figma Context MCP](figma-context-mcp.md) · [jev-fraud](jev-fraud.md) · [json-render](json-render.md) · [konva](konva.md) · [Onlook](onlook.md) · [plasmic](plasmic.md) · [React Bits](react-bits.md) · [Recharts](recharts.md) · [screenshot-to-code](screenshot-to-code.md) · [swr](swr.md) · [TanStack Query](tanstack-query.md) · [tldraw](tldraw.md)

**Notas:** Alternativas (elige una): mui, ant-design, daisyui. Combinación anterior con plasmic eliminada: sin integración documentada.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada shadcn@4.23.0 (2026-10-27) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/shadcn-ui/ui/blob/main/README.md) · [2](https://ui.shadcn.com/docs/cli) · [3](https://ui.shadcn.com/docs/registry) · [4](https://ui.shadcn.com/docs/mcp) · [5](https://ui.shadcn.com/docs/components-json) · [6](https://magicui.design/docs/installation)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Los componentes abiertos no necesitan IA; registros privados, servicios y el agente pueden tener costes |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. El MCP oficial permite consultar e instalar componentes desde los clientes; el componente sigue siendo código de tu aplicación |
| Coste | Sin pago a un modelo en la ruta básica. Los componentes abiertos no necesitan IA; registros privados, servicios y el agente pueden tener costes |
| Equipo | Preparación según la ruta elegida. Proyecto React compatible; Node; gestor de paquetes; configuración del framework |

El MCP oficial permite consultar e instalar componentes desde los clientes; el componente sigue siendo código de tu aplicación

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Proyecto React compatible
- Node
- gestor de paquetes
- configuración del framework

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://ui.shadcn.com/docs/installation)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ui para mi objetivo y necesito pasos guiados. Lee https://ui.shadcn.com/docs/installation. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade una tarjeta con botón y modifica sus estilos desde el código copiado al proyecto.

**Qué comprobar:** Ves el componente y puedes localizar su archivo editable.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir un formulario con componentes propios
- Crear un sistema de interfaz con código modificable

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir un formulario con componentes propios; Crear un sistema de interfaz con código modificable | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP oficial permite consultar e instalar componentes desde los clientes; el componente sigue siendo código de tu aplicación

## Stack y modelos

- **Stack:** Proyecto React compatible; Node; gestor de paquetes; configuración del framework
- **Etiquetas:** `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Material UI](mui.md) | 99.3k | Librería de componentes React completa que implementa Material Design de Google. |
| [Ant Design](ant-design.md) | 100k | Lenguaje de diseño empresarial y librería de componentes React de Ant Group. |
| [daisyUI](daisyui.md) | 42.8k | La librería de componentes más popular para Tailwind CSS, con clases semánticas y temas. |

## Enlaces

- 🐙 GitHub: [shadcn-ui/ui](https://github.com/shadcn-ui/ui)
- 🌐 Web: <https://ui.shadcn.com>
- 🧪 Receta: [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/shadcn-ui/ui/blob/main/README.md)
- [Fuente 2](https://ui.shadcn.com/docs/mcp)
- [Fuente 3](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
