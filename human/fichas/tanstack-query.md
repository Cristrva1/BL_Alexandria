[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 📚 TanStack Query

> Biblioteca para obtener, cachear, sincronizar y actualizar datos del servidor en React, Vue, Solid, Svelte, Angular y otros frameworks.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 50.6k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca de gestión de estado asíncrono de TanStack (antes React Query), en TypeScript con licencia MIT. Proyecto maduro (desde 2019), ~50k estrellas, con publicaciones frecuentes (última: noviembre de 2026).

## ¿Qué hace?

Obtiene, cachea, sincroniza y actualiza «estado de servidor» en aplicaciones web: caché con invalidación, refetch en segundo plano, paginación y scroll infinito, mutaciones, consultas dependientes, prefetch, cancelación y soporte de Suspense. Funciona con cualquier fuente de promesas (REST, GraphQL…).

## ¿Cómo lo hace?

Es un núcleo agnóstico (`query-core`) con adaptadores para React, Vue, Solid, Svelte, Preact, Lit y Angular (experimental), más devtools, persistencia de caché y un plugin de ESLint. Se instala por npm con el paquete del framework (p. ej. `@tanstack/react-query`) según la documentación oficial; no tiene backend propio.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [supabase](supabase.md) | Las funciones de consulta pueden llamar al cliente de Supabase y dejar en TanStack Query la caché, reintentos y la invalidación tras mutaciones. (combinación por arquitectura) | Configura el cliente de Supabase y envuélvelo en `useQuery`/`useMutation`. |
| [ui](ui.md) | Los componentes de shadcn/ui muestran estados de carga, error y datos que TanStack Query expone. (combinación por arquitectura) | Añade los componentes al proyecto y conéctalos a los hooks de consulta. |
| [tailwindcss](tailwindcss.md) | Estilo de los estados de interfaz (skeletons, errores) en las mismas vistas. (combinación por arquitectura) | Configura Tailwind en el proyecto antes de construir las vistas. |

**Notas:** Alternativa (elige una): swr. Gestiona datos del servidor, no estado global de cliente.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada release-2026-11-06-2304 (2026-11-06) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/TanStack/query/blob/main/README.md) · [2](https://tanstack.com/query/latest/docs/framework/react/overview)</sub>

## Ver similares

Grupo **Obtención de datos en React**: TanStack Query ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **TanStack Query** (esta ficha) ⭐ recomendado | 74 | Si buscas esto: biblioteca para obtener, cachear, sincronizar y actualizar datos del servidor en React, Vue, Solid, Svelte, Angular y otros frameworks. |
| 2 | [swr](swr.md) | 59 | Si buscas esto: librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano. |

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
| Equipo | Equipo normal; revisar dependencias. Un proyecto JavaScript o TypeScript con el adaptador de tu framework. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/TanStack/query/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://tanstack.com/query/latest/docs/framework/react/overview)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar TanStack Query para mi objetivo y necesito pasos guiados. Lee https://github.com/TanStack/query/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Envuelve una llamada a una API pública de prueba en una consulta y muestra sus estados.

**Qué comprobar:** Ves carga, datos y un refetch al volver a enfocar la ventana.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Cachear y revalidar datos de una API en una app React
- Mostrar estados de carga y error sin estado global manual

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Cachear y revalidar datos de una API en una app React; Mostrar estados de carga y error sin estado global manual | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `frontend` `data-fetching` `cache` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [swr](swr.md) | 32.5k | Librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano. |

## Enlaces

- 🐙 GitHub: [TanStack/query](https://github.com/TanStack/query)
- 🌐 Web: <https://tanstack.com/query>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/TanStack/query/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
