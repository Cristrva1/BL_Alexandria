[🏠 Inicio](../README.md) › [🕷️ Buscar y extraer información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# 🔍 Vane

> Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.2k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Busca en la web con SearXNG y responde con citas usando modelos locales o en la nube. Incluye modos de enfoque para académico, YouTube o Reddit.

## Por qué destaca

Ofrece la experiencia de Perplexity en tu propia máquina.

## Cómo funciona

Recupera resultados con SearXNG, los reordena con embeddings y genera la respuesta citada con el LLM elegido.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/ItzCrazyKns/Vane/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Vane para mi objetivo y necesito pasos guiados. Lee https://github.com/ItzCrazyKns/Vane/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Perplexity privado para el equipo
- Búsqueda con modelos locales
- Respuestas citadas rápidas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un buscador con respuestas citadas auto-hospedado | necesitas informes largos; mira `gpt-researcher` |

## Stack y modelos

- **Stack:** TypeScript, Next.js, Docker
- **Etiquetas:** `search` `research` `local` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SearXNG](searxng.md) | 39.6k | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. |
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [gpt-researcher](gpt-researcher.md) | 30.7k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |

## Enlaces

- 🐙 GitHub: [ItzCrazyKns/Vane](https://github.com/ItzCrazyKns/Vane)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/ItzCrazyKns/Vane/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
