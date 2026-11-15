[🏠 Inicio](../README.md) › [🎨 Diseño, UI & Frontend](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 🔄 swr

> Librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 32.5k | MIT | TypeScript | 2026-10-16 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Cubre el caso de consumir APIs en frontend sin manejar caché a mano.

## Por qué destaca

Creada por Vercel, ofrece una DX muy pulida para consumir APIs y es referencia junto a React Query. Su peso mínimo y la revalidación en foco/intervalo cubren la mayoría de apps sin configuración.

## Cómo funciona

Hook `useSWR(key, fetcher)` que cachea por clave, revalida al recuperar foco o en intervalo, y deduplica peticiones simultáneas al mismo key.

## Instalación rápida

`npm i swr`. Solo necesita un fetcher (una función async) por clave; funciona con cualquier API REST/GraphQL.

## Casos de uso

- Consumir APIs en frontend con caché y revalidación
- Datos en tiempo casi real sin WebSocket
- Mutaciones optimistas con `useSWRMutation`

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| manejas datos remotos en React y quieres caché simple | prefieres React Query con su modelo de caché global más rico |

## Stack y modelos

- **Stack:** JavaScript/React
- **Modelos / API:** N/A.
- **Etiquetas:** `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [heroui](heroui.md) | 31.2k | Librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, dashboards y landings consistentes. |

## Enlaces

- 🐙 GitHub: [vercel/swr](https://github.com/vercel/swr)
- 🌐 Web: <https://swr.vercel.app>
- 🧪 Receta: [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
