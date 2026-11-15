[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › Componentes, iconos y sistemas de diseño

# 🔄 swr

> Librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 32.5k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Cubre el caso de consumir APIs en frontend sin manejar caché a mano.

## Por qué destaca

Creada por Vercel, ofrece una DX muy pulida para consumir APIs y es referencia junto a React Query. Su peso mínimo y la revalidación en foco/intervalo cubren la mayoría de apps sin configuración.

## Cómo funciona

Hook `useSWR(key, fetcher)` que cachea por clave, revalida al recuperar foco o en intervalo, y deduplica peticiones simultáneas al mismo key.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/vercel/swr/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar swr para mi objetivo y necesito pasos guiados. Lee https://github.com/vercel/swr/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/vercel/swr/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
