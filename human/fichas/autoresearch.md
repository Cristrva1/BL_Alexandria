[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Agentes de research autónomo

# 🔬 autoresearch

> Enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 100k | — | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. El proveedor y la función elegidos determinan si hacen falta credenciales de IA. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | Consumo del agente que ya utilizas. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Proyecto pequeño y exploratorio de Karpathy, más que una herramienta pulida.

## Por qué destaca

Propuesta sencilla para experimentar con investigación autónoma en varias pasadas; valioso como punto de partida y referencia didáctica más que como producto cerrado.

## Cómo funciona

Repite ciclos de búsqueda y refinamiento sobre un tema, refinando consultas con cada iteración; implementado en Python con llamadas a LLM y búsqueda web.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/karpathy/autoresearch/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar autoresearch para mi objetivo y necesito pasos guiados. Lee https://github.com/karpathy/autoresearch/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Loops de búsqueda y refinamiento
- Exploración de un tema en varias pasadas
- Base para montar tu propio agente de research

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| experimentas con research iterativo o quieres un punto de partida | quieres salida pulida y lista (gpt-researcher) |

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `research` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [gpt-researcher](gpt-researcher.md) | 30.7k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |
| [crawl4ai](crawl4ai.md) | 87.4k | Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. |

## Enlaces

- 🐙 GitHub: [karpathy/autoresearch](https://github.com/karpathy/autoresearch)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/karpathy/autoresearch/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
