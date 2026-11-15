[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Aplicaciones y flujos de producción

# 📲 videofy_minimal

> Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 656 | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | Consumo de APIs o servicios. El flujo documentado usa OPENAI_API_KEY y ELEVENLABS_API_KEY. La interfaz local no elimina esas llamadas remotas. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión. La ruta documentada requiere APIs de OpenAI y ElevenLabs aunque la interfaz y el montaje se ejecuten en tu equipo.

## Por qué destaca

Prioriza la simplicidad para pasar de texto a reel rápido; es un proyecto pequeño y experimental, conviene revisar su estado antes de usarlo en serio.

## Cómo funciona

La interfaz coordina la obtención del artículo, guion, imágenes, narración y render del video.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/schibsted/videofy_minimal/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar videofy_minimal para mi objetivo y necesito pasos guiados. Lee https://github.com/schibsted/videofy_minimal/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Transformar noticias/contenido en reels
- Video corto rápido sin pipeline complejo
- Prototipos de texto-a-video local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres reels simples ya, sin montar un pipeline entero | necesitas variantes programáticas a escala (remotion) o control fino por código (moviepy) |

**Limitaciones:** Proyecto pequeño y experimental; valida mantenimiento y calidad antes de depender de él.

## Stack y modelos

- **Stack:** Python/Node
- **Etiquetas:** `video` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [whisper](whisper.md) | 113k | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. |
| [supertonic](supertonic.md) | 13.8k | Motor de texto a voz que ofrece modelos y ejemplos para sintetizar audio en dispositivos y navegadores compatibles. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MoneyPrinterTurbo](moneyprinterturbo.md) | 144k | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. |

## Enlaces

- 🐙 GitHub: [schibsted/videofy_minimal](https://github.com/schibsted/videofy_minimal)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/schibsted/videofy_minimal/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
