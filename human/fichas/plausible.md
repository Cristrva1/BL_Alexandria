[🏠 Inicio](../README.md) › [📊 Analizar datos, crear dashboards y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Analítica web y de producto

# 📈 Plausible Analytics

> Analítica web ligera, sin cookies y centrada en la privacidad, en la nube o auto-hospedada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 29.8k | AGPL-3.0 | Elixir | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

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

Un panel de una sola página con lo esencial: visitas, fuentes, páginas y objetivos.

## Por qué destaca

Script muy pequeño y cumplimiento de privacidad por diseño.

## Cómo funciona

Un script de menos de 1 KB envía eventos a un backend Elixir que guarda en ClickHouse.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/plausible/analytics/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Plausible Analytics para mi objetivo y necesito pasos guiados. Lee https://github.com/plausible/analytics/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Analítica de un blog
- Sitios con requisitos de privacidad
- Medir objetivos simples

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres analítica minimalista y privada | necesitas embudos y eventos complejos; mira `posthog` |

**Limitaciones:** Licencia AGPL-3.0.

## Stack y modelos

- **Stack:** Elixir, ClickHouse, PostgreSQL
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

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/plausible/analytics/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
