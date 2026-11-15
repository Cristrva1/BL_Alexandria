[🏠 Inicio](../README.md) › [🎬 Crear audio, voz y video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🎞️ OpenCut

> Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 98.4k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

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

Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe. El README diferencia opencut.app y opencut-classic de la reescritura en curso; comprueba qué versión necesitas antes de compilar.

## Por qué destaca

Cubre lo básico de CapCut sin muros de pago ni subir tus videos a un servidor. La reescritura anuncia API de editor, plugins de terceros, modo headless para render por lotes y servidor MCP para agentes.

## Cómo funciona

La versión clásica permite probar el flujo de edición; la nueva arquitectura sigue otra ruta de desarrollo.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un navegador y un clip pequeño de prueba.

1. Abre opencut.app para probar la versión clásica; el README indica que este repositorio está en reescritura.
2. Usa un clip de prueba para comprobar el flujo de edición disponible en esa versión.
3. Revisa la exportación y sus límites. Preparar el nuevo código desde fuente es una ruta de desarrollo diferente.

[Instrucciones originales de instalación](https://github.com/OpenCut-app/OpenCut/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://opencut.app)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenCut para mi objetivo y necesito pasos guiados. Lee https://github.com/OpenCut-app/OpenCut/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Editar reels y videos cortos sin pagar suscripción
- Montar clips con texto y música sin subirlos a la nube
- Auto-hospedar un editor web para tu equipo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un editor con línea de tiempo, libre y privado, como alternativa a CapCut | necesitas estabilidad o automatización hoy; para montar por código mira `moviepy` o `remotion`, y para cortes sin pérdida `lossless-cut` |

**Limitaciones:** Está en plena reescritura: el repo principal aún no es apto para producción y la versión clásica (opencut-classic) está archivada.

## Stack y modelos

- **Stack:** TypeScript, Rust, WebAssembly, Next.js
- **Etiquetas:** `video` `ui` `typescript` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LosslessCut](lossless-cut.md) | 46k | App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. |
| [OBS Studio](obs-studio.md) | 79.6k | App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real. |
| [whisperX](whisperx.md) | 25.3k | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. |

## Enlaces

- 🐙 GitHub: [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut)
- 🌐 Web: <https://opencut.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/OpenCut-app/OpenCut/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
