[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 🧱 Ant Design

> Lenguaje de diseño empresarial y librería de componentes React de Ant Group.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 100k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Puntuación de calidad** 77/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Lenguaje de diseño empresarial y biblioteca de componentes React (MIT) de Ant Group. Es muy madura (versión 6.7.0, ~100k estrellas), está escrita en TypeScript y se financia con patrocinios en Open Collective.

## ¿Qué hace?

Ofrece un conjunto amplio de componentes de alta calidad para aplicaciones web empresariales: tablas, formularios, árboles, calendarios, layouts y más. Trae internacionalización para decenas de idiomas y personalización de temas basada en CSS-in-JS. El ecosistema añade Ant Design Pro (plantillas), Pro Components y Ant Design Charts.

## ¿Cómo lo hace?

Se instala con `npm install antd` o `pnpm add antd`. Funciona en navegadores modernos, con renderizado en servidor y en Electron. Al usar CSS-in-JS, los estilos se generan en tiempo de ejecución, lo que conviene tener en cuenta si combinas con Tailwind o buscas un CSS mínimo. Su estética es la propia de Ant Design; adaptarla a otra marca exige trabajo de tema.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [echarts](echarts.md) | Gráficos avanzados en paneles de administración junto a las tablas y formularios de antd. (combinación por arquitectura); el ecosistema oficial ofrece Ant Design Charts como opción integrada | Instala echarts y su envoltorio para React; úsalo en componentes Card o layouts de antd. |
| [swr](swr.md) | Carga de datos con caché para alimentar tablas y formularios. (combinación por arquitectura) | Añade swr y conecta sus hooks a los componentes. |
| [AI SDK (Vercel)](vercel-ai.md) | Añadir funciones de IA (chat, streaming) a una aplicación empresarial construida con antd. (combinación por arquitectura) | Usa los hooks de AI SDK UI y renderiza con componentes de antd. |

**Notas:** Alternativas (elige una): mui, ui.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 6.7.0 (2026-11-04) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ant-design/ant-design/blob/master/README.md) · [2](https://ant.design/)</sub>

## Ver similares

Grupo **Bibliotecas de componentes React**: Ant Design ocupa la posición 1 de 6 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Ant Design** (esta ficha) ⭐ recomendado | 77 | Si construyes paneles empresariales densos en datos. |
| 2 | [ui](ui.md) | 73 | Si quieres copiar componentes Tailwind+Radix a tu proyecto y adaptarlos (shadcn/ui). |
| 3 | [Material UI](mui.md) | 70 | Si quieres Material Design y la biblioteca de componentes React más usada. |
| 4 | [Chakra UI](chakra-ui.md) | 64 | Si priorizas accesibilidad y estilos por props. |
| 5 | [heroui](heroui.md) | 62 | Si quieres componentes bonitos sobre Tailwind (antes NextUI). |
| 6 | [Mantine](mantine.md) | 58 | Si quieres componentes y hooks completos con buena documentación y poca configuración. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca no necesita modelo; alojamiento y servicios del producto se pagan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una biblioteca React con su sistema visual; no se instala como una app final ni como agente de IA |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca no necesita modelo; alojamiento y servicios del producto se pagan aparte |
| Equipo | Preparación según la ruta elegida. React; Node; gestor de paquetes |

Es una biblioteca React con su sistema visual; no se instala como una app final ni como agente de IA

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- React
- Node
- gestor de paquetes

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm install antd
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ant-design/ant-design/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Ant Design para mi objetivo y necesito pasos guiados. Lee https://github.com/ant-design/ant-design/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Muestra una tabla con tres filas ficticias y añade un filtro.

**Qué comprobar:** El filtro cambia las filas y puedes revisar el estado seleccionado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un panel administrativo
- Montar formularios de gestión

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un panel administrativo; Montar formularios de gestión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una biblioteca React con su sistema visual; no se instala como una app final ni como agente de IA

## Stack y modelos

- **Stack:** React; Node; gestor de paquetes
- **Etiquetas:** `ui` `react` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Material UI](mui.md) | 99.3k | Librería de componentes React completa que implementa Material Design de Google. |
| [ui](ui.md) | 128k | Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada. |

## Enlaces

- 🐙 GitHub: [ant-design/ant-design](https://github.com/ant-design/ant-design)
- 🌐 Web: <https://ant.design>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ant-design/ant-design/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
