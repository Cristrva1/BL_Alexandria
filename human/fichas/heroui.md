[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 🦸 heroui

> Librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, dashboards y landings consistentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.2k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de componentes React (Apache-2.0) antes llamada NextUI, de HeroUI Inc. Es madura y muy activa (v3.2.7).

## ¿Qué hace?

Combina la accesibilidad de React Aria (teclado, foco, lectores de pantalla conformes a WCAG) con estilos utilitarios de Tailwind CSS v4. Ofrece una API de componentes compuestos (`Card.Header`, `Card.Content`), no necesita un Provider envolvente y apunta a SaaS, paneles y tiendas. Es 'AI-native': incluye servidor MCP (`@heroui/react-mcp`), `llms.txt` y skills de agente.

## ¿Cómo lo hace?

Se instala con `npm install @heroui/styles @heroui/react`, con importaciones por componente disponibles. Requiere Tailwind CSS v4 y no usa CSS-in-JS en tiempo de ejecución. El servidor MCP se instala en Cursor, Claude Code, Windsurf u otros clientes MCP.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [tailwindcss](tailwindcss.md) | Motor de estilos requerido (Tailwind CSS v4). | Configura Tailwind v4 antes de instalar HeroUI. |
| [Claude Code](claude-code.md) | Componentes y tema accesibles para el asistente mediante el servidor MCP `@heroui/react-mcp`. | Instala HeroUI y registra su servidor MCP en Claude Code. |
| [swr](swr.md) | Carga de datos para los componentes. (combinación por arquitectura) | Añade swr y usa sus hooks en las vistas. |
| [echarts](echarts.md) | Combinación recíproca: echarts lo enlaza como «Paneles con componentes HeroUI y gráficos ECharts. (combinación por arquitectura)». | Orden indicado desde echarts: Envuelve el gráfico en un componente de tarjeta. |

**Notas:** Alternativas (elige una): mui.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.2.7 (2026-10-28) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/heroui-inc/heroui/blob/v3/README.md) · [2](https://www.heroui.com/docs/react/getting-started)</sub>

## Ver similares

Grupo **Bibliotecas de componentes React**: heroui ocupa la posición 5 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Ant Design](ant-design.md) ⭐ recomendado | 77 | Si construyes paneles empresariales densos en datos. |
| 2 | [ui](ui.md) | 73 | Si quieres copiar componentes Tailwind+Radix a tu proyecto y adaptarlos (shadcn/ui). |
| 3 | [Material UI](mui.md) | 70 | Si quieres Material Design y la biblioteca de componentes React más usada. |
| 4 | [Chakra UI](chakra-ui.md) | 64 | Si priorizas accesibilidad y estilos por props. |
| 5 | **heroui** (esta ficha) | 62 | Si quieres componentes bonitos sobre Tailwind (antes NextUI). |
| 6 | [Mantine](mantine.md) | 58 | Si quieres componentes y hooks completos con buena documentación y poca configuración. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca no exige modelo; servicios y contenidos comerciales relacionados tienen condiciones aparte |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Antes NextUI; el README actual usa paquetes styles y react; MCP y llms.txt son rutas auxiliares para agentes |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca no exige modelo; servicios y contenidos comerciales relacionados tienen condiciones aparte |
| Equipo | Preparación según la ruta elegida. React; Tailwind CSS v4 y configuración según guía; Node |

Antes NextUI; el README actual usa paquetes styles y react; MCP y llms.txt son rutas auxiliares para agentes

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- React
- Tailwind CSS v4 y configuración según guía
- Node

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm install @heroui/styles @heroui/react
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/heroui-inc/heroui/blob/v3/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar heroui para mi objetivo y necesito pasos guiados. Lee https://github.com/heroui-inc/heroui/blob/v3/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade un botón y un campo con un tema sencillo y prueba el foco por teclado.

**Qué comprobar:** Los componentes muestran el tema y estados interactivos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Construir formularios accesibles
- Crear una interfaz con temas compartidos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Construir formularios accesibles; Crear una interfaz con temas compartidos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Antes NextUI; el README actual usa paquetes styles y react; MCP y llms.txt son rutas auxiliares para agentes

## Stack y modelos

- **Stack:** React; Tailwind CSS v4 y configuración según guía; Node
- **Etiquetas:** `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Material UI](mui.md) | 99.3k | Librería de componentes React completa que implementa Material Design de Google. |

## Enlaces

- 🐙 GitHub: [heroui-inc/heroui](https://github.com/heroui-inc/heroui)
- 🌐 Web: <https://heroui.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/heroui-inc/heroui/blob/v3/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
