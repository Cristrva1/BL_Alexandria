[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Analítica web y de producto

# 📈 Plausible Analytics

> Analítica web ligera, sin cookies y centrada en la privacidad, en la nube o auto-hospedada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 29.8k | AGPL-3.0 | Elixir | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plausible Analytics, analítica web ligera y sin cookies hecha y alojada en la UE. Plausible CE es AGPL-3.0 o posterior y el script de seguimiento es MIT. Es madura (~30k estrellas, v3.2.1).

## ¿Qué hace?

Mide visitas, fuentes, páginas, objetivos y eventos con un panel simple y un script muy ligero, cumpliendo GDPR, CCPA y PECR. Envía informes por email o Slack y ofrece API de estadísticas. La versión de pago incluye funciones premium (embudos, ingresos de ecommerce, SSO) que no están en CE.

## ¿Cómo lo hace?

Se usa como servicio de pago en plausible.io o se autoaloja Plausible Community Edition con Docker (Elixir/Phoenix con PostgreSQL y ClickHouse). Se integra añadiendo el script al sitio.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Activepieces tiene una pieza oficial `plausible` para usar Plausible Analytics en flujos. | Plausible Analytics en marcha con sus credenciales; después añade la pieza `plausible` en un flujo de Activepieces. |
| [Grafana](grafana.md) | Paneles propios sobre la API o la base ClickHouse de CE. (combinación por arquitectura) | Conecta Grafana a ClickHouse en una instancia CE. |
| [supabase](supabase.md) | Analítica sin cookies para apps alojadas sobre Supabase. (combinación por arquitectura) | Añade el script de Plausible al frontend. |

**Notas:** Alternativas (elige una): umami, matomo.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v3.2.1 (2026-05-15) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/plausible/analytics/blob/master/README.md) · [2](https://plausible.io/docs/stats-api) · [3](https://github.com/activepieces/activepieces/tree/main/packages/pieces/community/plausible)</sub>

## Ver similares

Grupo **Analítica web auto-hospedada**: Plausible Analytics ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Umami](umami.md) ⭐ recomendado | 74 | Si buscas esto: analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics. |
| 2 | **Plausible Analytics** (esta ficha) | 59 | Si buscas esto: analítica web ligera, sin cookies y centrada en la privacidad, en la nube o auto-hospedada. |
| 3 | [Matomo](matomo.md) | 57 | Si buscas esto: alternativa open source a Google Analytics con control total de los datos. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Cloud cobra suscripción; Community Edition requiere infraestructura; la analítica básica no necesita LLM |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Para self-hosting sigue el repositorio Community Edition enlazado, no asumas que clonar analytics completa el despliegue |
| Coste | El coste depende del proveedor o la ruta. Cloud cobra suscripción; Community Edition requiere infraestructura; la analítica básica no necesita LLM |
| Equipo | Preparación según la ruta elegida. Cuenta Cloud o servidor CE; web propia para el script |

Para self-hosting sigue el repositorio Community Edition enlazado, no asumas que clonar analytics completa el despliegue

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cuenta Cloud o servidor CE
- web propia para el script

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/plausible/community-edition/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Plausible Analytics para mi objetivo y necesito pasos guiados. Lee https://github.com/plausible/community-edition/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Mide una visita y un objetivo de prueba sin añadir datos personales al evento.

**Qué comprobar:** El panel muestra el sitio, la visita y el objetivo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Medir una web de contenido
- Comparar conversiones de una landing

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Medir una web de contenido; Comparar conversiones de una landing | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Para self-hosting sigue el repositorio Community Edition enlazado, no asumas que clonar analytics completa el despliegue

## Stack y modelos

- **Stack:** Cuenta Cloud o servidor CE; web propia para el script
- **Etiquetas:** `analytics` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Umami](umami.md) | 40.2k | Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics. |
| [Matomo](matomo.md) | 22k | Alternativa open source a Google Analytics con control total de los datos. |

## Enlaces

- 🐙 GitHub: [plausible/analytics](https://github.com/plausible/analytics)
- 🌐 Web: <https://plausible.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/plausible/analytics/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
