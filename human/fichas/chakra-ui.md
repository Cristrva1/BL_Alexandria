[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 📚 Chakra UI

> Sistema de componentes React accesibles para crear productos y sistemas de diseño con rapidez, compatible con Next.js RSC.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.7k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de componentes de código abierto (MIT) mantenida por Segun Adebayo y la comunidad Chakra UI. Madura; la versión 3 es la actual y mantiene documentación de v2, v1 y v0.

## ¿Qué hace?

Proporciona componentes React accesibles y componibles, un sistema de estilos con tokens, recetas y temas, modo oscuro y compatibilidad con React Server Components de Next.js. Ofrece documentación para IA, incluido un servidor MCP.

## ¿Cómo lo hace?

Se instala con `npm i @chakra-ui/react @emotion/react` y se envuelve la app en su proveedor. La v3 se basa en Ark UI y Zag.js para la lógica accesible.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Storybook](storybook.md) | Los componentes Chakra se documentan en Storybook envolviendo las stories con su proveedor (combinación por arquitectura). | Instala Storybook; después añade un decorador con el Provider de Chakra. |
| [Lucide](lucide.md) | Los iconos de Lucide se usan dentro de los componentes de Chakra como componentes React (combinación por arquitectura). | Instala lucide-react; después pásalos como iconos a los componentes. |
| [Claude Code](claude-code.md) | Chakra UI publica un servidor MCP con la documentación y ejemplos de sus componentes para asistentes de código. | Configura el servidor MCP de Chakra en Claude Code; después pide componentes basados en la versión que usas. |

**Notas:** Alternativas (elige una): mantine, mui.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada @chakra-ui/panda-preset@3.38.0 (2026-11-03) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/chakra-ui/chakra-ui/blob/main/README.md) · [2](https://chakra-ui.com/docs/get-started/ai/mcp-server)</sub>

## Ver similares

Grupo **Bibliotecas de componentes React**: Chakra UI ocupa la posición 4 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Ant Design](ant-design.md) ⭐ recomendado | 77 | Si construyes paneles empresariales densos en datos. |
| 2 | [ui](ui.md) | 73 | Si quieres copiar componentes Tailwind+Radix a tu proyecto y adaptarlos (shadcn/ui). |
| 3 | [Material UI](mui.md) | 70 | Si quieres Material Design y la biblioteca de componentes React más usada. |
| 4 | **Chakra UI** (esta ficha) | 64 | Si priorizas accesibilidad y estilos por props. |
| 5 | [heroui](heroui.md) | 62 | Si quieres componentes bonitos sobre Tailwind (antes NextUI). |
| 6 | [Mantine](mantine.md) | 58 | Si quieres componentes y hooks completos con buena documentación y poca configuración. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/chakra-ui/chakra-ui/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Chakra UI para mi objetivo y necesito pasos guiados. Lee https://github.com/chakra-ui/chakra-ui/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala `@chakra-ui/react` y `@emotion/react` en un proyecto React y renderiza un botón con el proveedor..

**Qué comprobar:** El componente se muestra con el tema por defecto y cambia a modo oscuro..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- construir el panel de un SaaS con componentes accesibles y tema propio
- crear un sistema de diseño con tokens y recetas de estilo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: construir el panel de un SaaS con componentes accesibles y tema propio; crear un sistema de diseño con tokens y recetas de estilo | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `ui` `typescript` `react` `library`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Mantine](mantine.md) | 31.9k | Biblioteca de componentes React completa con más de 100 componentes, hooks, formularios, gráficos, fechas y notificaciones. |
| [Material UI](mui.md) | 99.3k | Librería de componentes React completa que implementa Material Design de Google. |

## Enlaces

- 🐙 GitHub: [chakra-ui/chakra-ui](https://github.com/chakra-ui/chakra-ui)
- 🌐 Web: <https://chakra-ui.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/chakra-ui/chakra-ui/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
