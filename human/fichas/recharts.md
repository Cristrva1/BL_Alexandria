[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Librerías de gráficos

# 📉 Recharts

> Librería de gráficos para React construida con D3, declarativa y componible.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.7k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## ¿Qué es?

Recharts, librería de gráficos para React construida con D3. Licencia MIT. Es madura (~28k estrellas, v3.10.1).

## ¿Qué hace?

Permite componer gráficos (líneas, barras, áreas, tartas, radar, dispersión…) con componentes React declarativos. Renderiza SVG nativo con pocas dependencias. Es la base de los componentes de gráficos de shadcn/ui.

## ¿Cómo lo hace?

Se instala con `npm install recharts react-is` y se usa dentro de componentes React. La documentación incluye ejemplos y un storybook.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ui](ui.md) | Los componentes Chart de shadcn/ui se construyen con Recharts. | Añade el componente chart de shadcn/ui. |
| [D3.js](d3.md) | Recharts usa módulos de D3 internamente. | No requiere instalación aparte. |
| [tailwindcss](tailwindcss.md) | Estilar los gráficos con las variables de tema de Tailwind. (combinación por arquitectura) | Pasa colores del tema a los componentes. |
| [Material UI](mui.md) | Combinación recíproca: Material UI lo enlaza como «Gráficos ligeros en dashboards si no quieres MUI X Charts. (combinación por arquitectura)». | Orden indicado desde Material UI: Instala recharts y envuélvelo en componentes Card o Paper de MUI. |
| [Mantine](mantine.md) | Combinación recíproca: Mantine lo enlaza como «Mantine Charts está construido sobre Recharts». | Orden indicado desde Mantine: Instala @mantine/charts y recharts; después usa los componentes de gráficos. |

**Notas:** Alternativas (elige una): chart-js, echarts.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v3.10.1 (2026-07-25) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/recharts/recharts/blob/main/README.md) · [2](https://ui.shadcn.com/docs/components/chart) · [3](https://recharts.github.io)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa modelo ni API; la fuente de datos se presupuesta aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El signo $ del ejemplo es un indicador de terminal y no parte del comando; ajusta react-is a la versión de React |
| Coste | Sin pago a un modelo en la ruta básica. No usa modelo ni API; la fuente de datos se presupuesta aparte |
| Equipo | Preparación según la ruta elegida. React; Node; react-is compatible; datos de prueba |

El signo $ del ejemplo es un indicador de terminal y no parte del comando; ajusta react-is a la versión de React

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- React
- Node
- react-is compatible
- datos de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (sh):**

```
# latest stable
npm install recharts react-is
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/recharts/recharts/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Recharts para mi objetivo y necesito pasos guiados. Lee https://github.com/recharts/recharts/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Dibuja una línea con cinco valores y comprueba etiquetas y tooltip.

**Qué comprobar:** Los puntos corresponden a los datos y el gráfico cabe en móvil.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Visualizar una serie de ventas
- Comparar categorías en un dashboard React

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Visualizar una serie de ventas; Comparar categorías en un dashboard React | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El signo $ del ejemplo es un indicador de terminal y no parte del comando; ajusta react-is a la versión de React

## Stack y modelos

- **Stack:** React; Node; react-is compatible; datos de prueba
- **Etiquetas:** `dataviz` `react` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Chart.js](chart-js.md) | 67.8k | Librería JavaScript para dibujar gráficos en canvas dentro de una página o aplicación web. |
| [echarts](echarts.md) | 67.7k | Librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos. |

## Enlaces

- 🐙 GitHub: [recharts/recharts](https://github.com/recharts/recharts)
- 🌐 Web: <https://recharts.github.io>
- 🧪 Receta: [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/recharts/recharts/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
