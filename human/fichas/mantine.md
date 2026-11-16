[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 📚 Mantine

> Biblioteca de componentes React completa con más de 100 componentes, hooks, formularios, gráficos, fechas y notificaciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.9k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de componentes de código abierto (MIT) creada por Vitaly Rtishchev y financiada por patrocinadores en Open Collective. Madura y muy activa.

## ¿Qué hace?

Ofrece más de 100 componentes y 50 hooks, gestión de formularios, gráficos (Mantine Charts, sobre Recharts), selectores de fecha, notificaciones, editor de texto enriquecido, spotlight y modales, con temas y modo oscuro.

## ¿Cómo lo hace?

Paquetes npm en TypeScript con estilos basados en CSS modules y variables CSS; plantillas para Next.js y Vite. Publica guías de integración (Storybook, entre otras) y documentación en formato llms.txt.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Storybook](storybook.md) | Mantine documenta una guía oficial para usar sus componentes en Storybook. | Instala Storybook; después sigue la guía de Mantine para el tema. |
| [Recharts](recharts.md) | Mantine Charts está construido sobre Recharts. | Instala @mantine/charts y recharts; después usa los componentes de gráficos. |
| [Claude Code](claude-code.md) | Mantine publica su documentación en formato llms.txt, útil como contexto para agentes de código (combinación por arquitectura). | Añade la URL de llms.txt al contexto del agente; después pide los componentes. |

**Notas:** Alternativas (elige una): chakra-ui, mui.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 9.8.1 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mantinedev/mantine/blob/master/README.md) · [2](https://mantine.dev/guides/storybook/) · [3](https://mantine.dev/llms.txt)</sub>

## Ver similares

Grupo **Bibliotecas de componentes React**: Mantine ocupa la posición 6 de 6 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Ant Design](ant-design.md) ⭐ recomendado | 77 | Si construyes paneles empresariales densos en datos. |
| 2 | [ui](ui.md) | 73 | Si quieres copiar componentes Tailwind+Radix a tu proyecto y adaptarlos (shadcn/ui). |
| 3 | [Material UI](mui.md) | 70 | Si quieres Material Design y la biblioteca de componentes React más usada. |
| 4 | [Chakra UI](chakra-ui.md) | 64 | Si priorizas accesibilidad y estilos por props. |
| 5 | [heroui](heroui.md) | 62 | Si quieres componentes bonitos sobre Tailwind (antes NextUI). |
| 6 | **Mantine** (esta ficha) | 58 | Si quieres componentes y hooks completos con buena documentación y poca configuración. |

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

[Instrucciones originales de instalación](https://github.com/mantinedev/mantine/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Mantine para mi objetivo y necesito pasos guiados. Lee https://github.com/mantinedev/mantine/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala @mantine/core y @mantine/hooks, envuelve la app en MantineProvider y renderiza un formulario..

**Qué comprobar:** El formulario se muestra con estilos de Mantine y valida los campos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- montar un panel de administración con formularios, tablas y gráficos
- prototipar una app React con componentes accesibles y modo oscuro

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: montar un panel de administración con formularios, tablas y gráficos; prototipar una app React con componentes accesibles y modo oscuro | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `ui` `typescript` `react` `library`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Chakra UI](chakra-ui.md) | 40.7k | Sistema de componentes React accesibles para crear productos y sistemas de diseño con rapidez, compatible con Next.js RSC. |
| [Material UI](mui.md) | 99.3k | Librería de componentes React completa que implementa Material Design de Google. |

## Enlaces

- 🐙 GitHub: [mantinedev/mantine](https://github.com/mantinedev/mantine)
- 🌐 Web: <https://mantine.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mantinedev/mantine/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
