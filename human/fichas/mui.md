[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 🧱 Material UI

> Librería de componentes React completa que implementa Material Design de Google.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 99.3k | MIT | JavaScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Material UI es una biblioteca completa de componentes React (MIT) con una implementación independiente de Material Design de Google, desarrollada por MUI. Es muy madura (v9.5.0, más de una década de desarrollo). La empresa tiene productos de pago: MUI X Pro y Premium, con licencia comercial, y plantillas premium.

## ¿Qué hace?

Ofrece decenas de componentes listos para producción (entradas, navegación, superficies, tablas, diálogos y más) con un sistema de temas y personalización. MUI X amplía con componentes complejos (data grid, selectores de fecha, gráficos, árboles). Algunas funciones avanzadas solo están en los planes Pro o Premium.

## ¿Cómo lo hace?

Se instala `@mui/material` junto con su motor de estilos: Emotion por defecto, o styled-components como alternativa documentada. La documentación incluye guías de migración entre versiones mayores (v5 → v6 y siguientes), que conviene revisar antes de actualizar, y plantillas gratuitas y de pago.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Recharts](recharts.md) | Gráficos ligeros en dashboards si no quieres MUI X Charts. (combinación por arquitectura) | Instala recharts y envuélvelo en componentes Card o Paper de MUI. |
| [swr](swr.md) | Carga de datos con caché para alimentar los componentes. (combinación por arquitectura) | Añade swr y usa sus hooks en las vistas. |
| [AI SDK (Vercel)](vercel-ai.md) | Añadir chat o streaming de IA sobre una interfaz Material. (combinación por arquitectura) | Usa los hooks de AI SDK UI y renderiza con componentes MUI. |

**Notas:** Alternativas (elige una): ant-design, ui, heroui. MUI X Pro/Premium tiene licencia comercial.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v9.5.0 (2026-10-09) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mui/material-ui/blob/master/README.md) · [2](https://mui.com/x/introduction/licensing/) · [3](https://mui.com/material-ui/getting-started/installation/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Material UI base es MIT; algunos productos MUI X, plantillas y soporte tienen condiciones comerciales |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. El MCP de documentación es un paquete separado stdio; no convierte las funciones de pago en gratuitas |
| Coste | El coste depende del proveedor o la ruta. Material UI base es MIT; algunos productos MUI X, plantillas y soporte tienen condiciones comerciales |
| Equipo | Preparación según la ruta elegida. React y React DOM compatibles; Node; Emotion en ruta por defecto |

El MCP de documentación es un paquete separado stdio; no convierte las funciones de pago en gratuitas

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- React y React DOM compatibles
- Node
- Emotion en ruta por defecto

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://mui.com/material-ui/getting-started/installation/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Material UI para mi objetivo y necesito pasos guiados. Lee https://mui.com/material-ui/getting-started/installation/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Construye un formulario pequeño y verifica estados de error y foco.

**Qué comprobar:** Los campos muestran validación y se recorren con teclado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un dashboard Material Design
- Construir una pantalla de ajustes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un dashboard Material Design; Construir una pantalla de ajustes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP de documentación es un paquete separado stdio; no convierte las funciones de pago en gratuitas

## Stack y modelos

- **Stack:** React y React DOM compatibles; Node; Emotion en ruta por defecto
- **Etiquetas:** `ui` `react` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ant Design](ant-design.md) | 100k | Lenguaje de diseño empresarial y librería de componentes React de Ant Group. |
| [ui](ui.md) | 128k | Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada. |
| [heroui](heroui.md) | 31.2k | Librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, dashboards y landings consistentes. |

## Enlaces

- 🐙 GitHub: [mui/material-ui](https://github.com/mui/material-ui)
- 🌐 Web: <https://mui.com/material-ui/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mui/material-ui/blob/master/README.md)
- [Fuente 2](https://mui.com/material-ui/getting-started/installation/)
- [Fuente 3](https://mui.com/material-ui/getting-started/mcp/)
- [Fuente 4](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
