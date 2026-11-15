[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Agentes de research autónomo

# 🔎 STORM

> Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.9k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Simula conversaciones entre perspectivas para hacer preguntas, busca fuentes y redacta un artículo estructurado y citado. Útil para informes de fondo.

## Por qué destaca

Método publicado y probado para artículos largos y bien citados.

## Cómo funciona

Genera preguntas desde varias perspectivas, recupera fuentes con un buscador, crea un esquema y redacta sección por sección.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/stanford-oval/storm/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar STORM para mi objetivo y necesito pasos guiados. Lee https://github.com/stanford-oval/storm/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Informes de fondo con citas
- Borradores de artículos tipo wiki
- Revisiones de un tema nuevo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas informes largos y citados sobre un tema | quieres respuestas cortas con fuentes; mira `gpt-researcher` |

## Stack y modelos

- **Stack:** Python, DSPy
- **Etiquetas:** `research` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SearXNG](searxng.md) | 39.6k | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. |
| [firecrawl](firecrawl.md) | 202k | Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [gpt-researcher](gpt-researcher.md) | 30.7k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |

## Enlaces

- 🐙 GitHub: [stanford-oval/storm](https://github.com/stanford-oval/storm)
- 🌐 Web: <http://storm.genie.stanford.edu>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/stanford-oval/storm/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
