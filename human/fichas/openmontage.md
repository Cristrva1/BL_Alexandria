[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎞️ OpenMontage

> Pipelines y herramientas para producir video con un agente,recursos propios,modelos locales o servicios opcionales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 80.5k | AGPL-3.0 | Python | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

OpenMontage, «sistema de producción de vídeo agéntico» open source, de OpenMontageInc (antes calesthio). Licencia AGPL-3.0. Creado en marzo de 2026, tiene ~81k estrellas, una cifra inusual; el README anuncia un nuevo producto en preparación.

## ¿Qué hace?

Pipelines y herramientas para que un agente produzca vídeo de principio a fin: concepto, guion, plan de escenas, clips generados, banda sonora y composición en Remotion. Funciona con herramientas gratuitas o con proveedores de pago (Atlas Cloud, Veo, Kling y otros).

## ¿Cómo lo hace?

Requiere Python 3.10+, FFmpeg y Node.js parcheado (22.23.4+, 24.22.1+ o 26.12.1+), y se instala con `make setup` o pip.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [remotion](remotion.md) | Composición final. | Viene integrado; revisa la licencia de Remotion. |
| [FFmpeg](ffmpeg.md) | Procesado de medios. | Instala FFmpeg. |
| [Kokoro](kokoro.md) | Narración local sin claves. (combinación por arquitectura) | Configura un TTS local. |
| [ElevenLabs (SDK de Python)](elevenlabs-python.md) | OpenMontage usa ElevenLabs para TTS premium, música y efectos; su código importa este SDK. | Añade `ELEVENLABS_API_KEY` al `.env`. |

**Notas:** Alternativas (elige una): remotion-superpowers, moneyprinterturbo.

Estado en GitHub: activo · último push 2026-11-09 · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OpenMontageInc/OpenMontage/blob/main/README.md)</sub>

## Ver similares

Grupo **Skills y flujos de producción de video**: OpenMontage ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **OpenMontage** (esta ficha) ⭐ recomendado | 72 | Si buscas esto: pipelines y herramientas para producir video con un agente,recursos propios,modelos locales o servicios opcionales. |
| 2 | [video-use](video-use.md) | 60 | Si buscas esto: edición con agentes y FFmpeg,con transcripción documentada mediante ElevenLabs Scribe. |
| 3 | [Remotion Superpowers](remotion-superpowers.md) | 48 | Si buscas esto: orquestación de video con Remotion y servicios audiovisuales externos; requiere claves y revisar costes por etapa. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. API keys opcionales amplían proveedores; el agente, render, Remotion y recursos tienen condiciones propias |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelos locales documentados. Documenta asistentes con archivos y ejecución de código; Piper permite voz offline, pero no implica que el modelo del agente o todos los pipelines sean locales |
| Coste | El coste depende del proveedor o la ruta. API keys opcionales amplían proveedores; el agente, render, Remotion y recursos tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Python; Node; FFmpeg; dependencias de la ruta; material autorizado |

Documenta asistentes con archivos y ejecución de código; Piper permite voz offline, pero no implica que el modelo del agente o todos los pipelines sean locales

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- Node
- FFmpeg
- dependencias de la ruta
- material autorizado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/OpenMontageInc/OpenMontage/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenMontage para mi objetivo y necesito pasos guiados. Lee https://github.com/OpenMontageInc/OpenMontage/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Empieza con material propio y narración Piper y comprueba guion, timeline y exportación.

**Qué comprobar:** Puedes revisar la procedencia de cada asset y abrir el MP4.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un video con recursos locales
- Comparar un pipeline con servicios opcionales

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un video con recursos locales; Comparar un pipeline con servicios opcionales | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta asistentes con archivos y ejecución de código; Piper permite voz offline, pero no implica que el modelo del agente o todos los pipelines sean locales

## Stack y modelos

- **Stack:** Python; Node; FFmpeg; dependencias de la ruta; material autorizado
- **Etiquetas:** `video` `coding-agent` `skills`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Remotion Superpowers](remotion-superpowers.md) | 168 | Orquestación de video con Remotion y servicios audiovisuales externos; requiere claves y revisar costes por etapa. |
| [MoneyPrinterTurbo](moneyprinterturbo.md) | 144k | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. |

## Enlaces

- 🐙 GitHub: [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OpenMontageInc/OpenMontage/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
