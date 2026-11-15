[🏠 Inicio](../README.md) › [🧠 Mejorar tu agente: skills y prompts](../categorias/02-skills-prompts-gu-as-de-agente.md) › Skills de dominio: marketing, SEO y negocio

# 📈 Arcads AI Video Skill Pack

> Pack de skills para Claude Code y Cursor que crea anuncios en video e imagen con la API de Arcads (Seedance, Sora, Veo, Kling).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.7k | MIT | Python | 2026-08-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo de APIs o servicios. La skill funciona dentro del agente, pero las generaciones consumen la API de Arcads; la suscripción del agente no paga Arcads. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Repo de trabajo que convierte Claude Code o Cursor en un estudio de anuncios: genera videos UGC, presentaciones de producto, lookbooks y miniaturas de YouTube con los modelos de Arcads, y anuncios estáticos para Meta con 37 plantillas. Incluye pipelines multipaso (estilo Pixar o plastilina con ffmpeg), subtitulado con Whisper y HyperFrames, y publicación como anuncios pausados en Meta.

## Por qué destaca

Trae fórmulas de prompt probadas para cada modelo, estimación de coste en créditos antes de cada generación y un log por llamada. Cubre del brief al anuncio subido a Meta sin salir del editor.

## Cómo funciona

Las skills de `skills/` y `shared/skills/` guían al agente para llamar a la API de Arcads, esperar el resultado y ordenar los archivos. Un hook SessionStart revisa `.env` y `MASTER_CONTEXT.md` y copia las skills a `.claude/` y `.cursor/`.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

[Instrucciones originales de instalación](https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Arcads AI Video Skill Pack para mi objetivo y necesito pasos guiados. Lee https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Generar un video UGC de producto con Seedance 2.0
- Crear anuncios estáticos para Meta a partir de plantillas
- Clonar la estructura de un anuncio de referencia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| ya tienes cuenta de Arcads y quieres producir creatividades publicitarias desde Claude Code o Cursor | quieres generar video con modelos abiertos sin servicio de pago; mira `comfyui` u `openmontage` |

**Limitaciones:** Requiere cuenta de pago de Arcads (cada generación consume créditos) y el README promociona una comunidad de pago; los pipelines avanzados piden ffmpeg, jq y Node.

## Stack y modelos

- **Stack:** Python, Bash, ffmpeg, Node.js (HyperFrames), Whisper
- **Etiquetas:** `video` `image` `skills` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [HyperFrames](hyperframes.md) | 84.4k | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes. |
| [whisper](whisper.md) | 113k | Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. |
| [FFmpeg](ffmpeg.md) | 67.3k | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. |
| [Marketing Skills](marketingskills.md) | 60.4k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. |

## Enlaces

- 🐙 GitHub: [mrpaidsocial/arcads-claude-code-mrpaidsocial](https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
