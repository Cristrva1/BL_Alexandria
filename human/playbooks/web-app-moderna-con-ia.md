[🏠 Inicio](../README.md) · [🧪 Todas las recetas](README.md)

# 🌐 Web app moderna con IA

> **Objetivo:** Construir un frontend pulido con chat o funciones de IA integradas.

## Empieza con una versión pequeña

Propuesta editorial; no es una integración ejecutada ni una lista completa de dependencias.

**Piezas iniciales:** [ui](../fichas/ui.md), [tailwindcss](../fichas/tailwindcss.md), [AI SDK (Vercel)](../fichas/vercel-ai.md), [assistant-ui](../fichas/assistant-ui.md)

**Prepara:** Una aplicación de prueba y una ruta de modelo elegida

**Primera prueba propuesta:** Construye una pantalla de chat y envía una pregunta de prueba

**Qué comprobar:** Puedes revisar respuesta, estado de carga y un error de conexión

Motion, gráficos y caché se añaden cuando la función los necesita; revisa API, alojamiento y autenticación por separado

## Orden propuesto para preparar las piezas

```mermaid
flowchart LR
  ui["ui"] --> tailwindcss["tailwindcss"]
  tailwindcss["tailwindcss"] --> vercel_ai["AI SDK (Vercel)"]
  vercel_ai["AI SDK (Vercel)"] --> assistant_ui["assistant-ui"]
```

## 🧩 Piezas

| # | Repo | Papel en la receta | ⭐ | Instalación |
|---:|---|---|---:|---|
| 1 | [ui](../fichas/ui.md) | Componentes accesibles que copias a tu código (shadcn/ui) | 128k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |
| 2 | [tailwindcss](../fichas/tailwindcss.md) | Estilos utilitarios | 98.6k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |
| 3 | [AI SDK (Vercel)](../fichas/vercel-ai.md) | AI SDK: streaming, tools y llamadas a cualquier LLM | 28k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 4 | [assistant-ui](../fichas/assistant-ui.md) | Componentes de chat listos para conectar al AI SDK | 13.2k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 5 | [motion](../fichas/motion.md) | Animaciones e interacciones | 35.2k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 6 | [Recharts](../fichas/recharts.md) | Gráficos para dashboards | 27.7k | Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola rut… |
| 7 | [swr](../fichas/swr.md) | Fetching y caché de datos en React | 32.5k | Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o códi… |

## 🔌 Cómo se conecta

shadcn/ui y Tailwind dan la base visual; el AI SDK de Vercel resuelve streaming, tool calling y proveedores; assistant-ui aporta la interfaz de chat; Motion anima y Recharts dibuja datos; SWR gestiona el fetching. Para diseñar antes de codificar, prueba Open Design o Penpot.

## 🚫 Cuándo NO usar esta receta

Si es una landing estática, Tailwind y un par de componentes bastan. Si es un dashboard interno de datos, Streamlit o Superset son más rápidos.

## 🔁 Variantes

- En lugar de [ui](../fichas/ui.md): [Material UI](../fichas/mui.md), [Ant Design](../fichas/ant-design.md), [daisyUI](../fichas/daisyui.md)
- En lugar de [AI SDK (Vercel)](../fichas/vercel-ai.md): [LangGraph.js](../fichas/langgraphjs.md), [Mastra](../fichas/mastra.md)
- En lugar de [assistant-ui](../fichas/assistant-ui.md): [CopilotKit](../fichas/copilotkit.md)
- En lugar de [motion](../fichas/motion.md): [Anime.js](../fichas/animejs.md)
- En lugar de [Recharts](../fichas/recharts.md): [Chart.js](../fichas/chart-js.md), [echarts](../fichas/echarts.md)
- En lugar de [swr](../fichas/swr.md): [TanStack Query](../fichas/tanstack-query.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
