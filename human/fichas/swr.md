[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 🔄 swr

> Librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 32.5k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de hooks React para cargar datos (MIT), creada por Vercel. Su nombre viene de la estrategia de caché stale-while-revalidate (RFC 5861). Es madura y estable (v2.5.1); último push en octubre de 2026.

## ¿Qué hace?

Con un solo hook (`useSWR`) devuelve primero los datos en caché, después revalida con una nueva petición y actualiza la vista. Incluye caché y deduplicación de peticiones, revalidación al recuperar el foco o la red, polling, paginación, mutaciones optimistas, soporte de Suspense y SSR/SSG. Es agnóstica del transporte (REST, GraphQL…).

## ¿Cómo lo hace?

Se instala con `npm i swr` y se usa con una función `fetcher` propia. Tiene integración documentada con Next.js. Es ligera y no impone backend ni cliente HTTP.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ui](ui.md) | Alimentar los componentes shadcn/ui (tablas, listas) con datos cacheados. (combinación por arquitectura) | Añade swr y conecta sus hooks a los componentes. |
| [heroui](heroui.md) | Combinación anterior del catálogo: datos para componentes HeroUI. (combinación por arquitectura) | Instala ambas y usa useSWR en las vistas. |
| [supabase](supabase.md) | Consultar un backend Supabase desde React con caché y revalidación. (combinación por arquitectura) | Usa el cliente de Supabase dentro del fetcher de SWR. |
| [Ant Design](ant-design.md) | Combinación recíproca: Ant Design lo enlaza como «Carga de datos con caché para alimentar tablas y formularios. (combinación por arquitectura)». | Orden indicado desde Ant Design: Añade swr y conecta sus hooks a los componentes. |
| [Material UI](mui.md) | Combinación recíproca: Material UI lo enlaza como «Carga de datos con caché para alimentar los componentes. (combinación por arquitectura)». | Orden indicado desde Material UI: Añade swr y usa sus hooks en las vistas. |
| [uPlot](uplot.md) | Combinación recíproca: uPlot lo enlaza como «Actualizar series en vivo con la recarga de datos de SWR. (combinación por arquitectura)». | Orden indicado desde uPlot: Obtén los datos con SWR y llama a `setData`. |

**Notas:** Alternativa (elige una): tanstack-query.

Estado en GitHub: activo · último push 2026-10-16 · última versión publicada v2.5.1 (2026-08-12) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/vercel/swr/blob/main/README.md) · [2](https://swr.vercel.app/docs/with-nextjs)</sub>

## Ver similares

Grupo **Obtención de datos en React**: swr ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [TanStack Query](tanstack-query.md) ⭐ recomendado | 74 | Si buscas esto: biblioteca para obtener, cachear, sincronizar y actualizar datos del servidor en React, Vue, Solid, Svelte, Angular y otros frameworks. |
| 2 | **swr** (esta ficha) | 59 | Si buscas esto: librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere IA; el endpoint consultado y su alojamiento pueden cobrar por uso |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una herramienta de obtención y caché de datos, no una librería de botones ni un backend |
| Coste | Sin pago a un modelo en la ruta básica. No requiere IA; el endpoint consultado y su alojamiento pueden cobrar por uso |
| Equipo | Preparación según la ruta elegida. React; endpoint de datos de prueba; función fetcher |

Es una herramienta de obtención y caché de datos, no una librería de botones ni un backend

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- React
- endpoint de datos de prueba
- función fetcher

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://swr.vercel.app/docs/getting-started)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar swr para mi objetivo y necesito pasos guiados. Lee https://swr.vercel.app/docs/getting-started. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Muestra un perfil ficticio y cambia el dato del servidor para observar la revalidación.

**Qué comprobar:** Se distinguen carga, error, datos cacheados y datos nuevos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Actualizar un panel sin recargar
- Revalidar datos al volver a una pestaña

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Actualizar un panel sin recargar; Revalidar datos al volver a una pestaña | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una herramienta de obtención y caché de datos, no una librería de botones ni un backend

## Stack y modelos

- **Stack:** React; endpoint de datos de prueba; función fetcher
- **Etiquetas:** `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [TanStack Query](tanstack-query.md) | 50.6k | Biblioteca para obtener, cachear, sincronizar y actualizar datos del servidor en React, Vue, Solid, Svelte, Angular y otros frameworks. |

## Enlaces

- 🐙 GitHub: [vercel/swr](https://github.com/vercel/swr)
- 🌐 Web: <https://swr.vercel.app>
- 🧪 Receta: [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/vercel/swr/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
