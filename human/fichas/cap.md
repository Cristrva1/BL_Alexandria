[🏠 Inicio](../README.md) › [🎬 Editar, grabar y generar video](../categorias/12-audio-voz-video.md) › Edición, grabación y subtítulos

# 🖥️ Cap

> Graba pantalla, cámara y micrófono, edita el video en tu equipo con fondos, zoom y recortes, y expórtalo o compártelo con un enlace.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.7k | AGPL-3.0 (partes MIT) | Rust | 2026-11-27 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 68/100 · métricas del 2026-11-28 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia y costes:** GitHub muestra NOASSERTION porque el archivo LICENSE combina licencias: los crates cap-camera* y scap-* son MIT, los componentes de terceros conservan su licencia y el resto es AGPL-3.0. Quien compila desde el código lo recibe bajo AGPL-3.0. La app oficial de cap.so es gratuita para uso personal; el uso comercial requiere la licencia de escritorio o Cap Pro, ambas de pago.

## ¿Qué es?

App de escritorio de código abierto para grabar la pantalla y compartir los videos, pensada como alternativa a Loom.

## ¿Qué hace?

Graba pantalla, cámara y micrófono, permite editar el resultado y exportarlo como archivo o compartirlo con un enlace.

## ¿Cómo lo hace?

Captura con las interfaces de grabación de cada sistema operativo y procesa el video en tu equipo. El modo Instant y los enlaces usan la nube de Cap o un servidor que tú alojes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Convierte o comprime el MP4 exportado a otros formatos cuando lo necesites. | — |
| [LosslessCut](lossless-cut.md) | Corta o une las grabaciones exportadas sin volver a codificarlas. | — |
| [HandBrake](handbrake.md) | Reduce el tamaño del video exportado con ajustes predefinidos antes de enviarlo. | — |

Estado en GitHub: activo · último push 2026-11-27 · última versión publicada cap-v0.6.3 (2026-11-11) · licencia declarada NOASSERTION (consultado el 2026-11-27).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-27); no se instaló ni ejecutó. Fuentes: [1](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/README.md) · [2](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/LICENSE) · [3](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/licenses/LICENSE-MIT) · [4](https://github.com/CapSoftware/Cap/releases/tag/cap-v0.6.3) · [5](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/apps/desktop-gpui/locales/es.toml) · [6](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/.github/workflows/engine-verify.yml) · [7](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/.github/workflows/recording-reliability.yml) · [8](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/.github/workflows/verify-recording.yml) · [9](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/.github/workflows/publish.yml) · [10](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/.github/workflows/desktop-release.yml) · [11](https://github.com/CapSoftware/Cap/actions/runs/43092047100) · [12](https://github.com/CapSoftware/Cap/actions/runs/43092046841) · [13](https://github.com/CapSoftware/Cap/actions/runs/43099158030) · [14](https://github.com/CapSoftware/Cap/actions/runs/43150140258) · [15](https://github.com/CapSoftware/Cap/security/advisories) · [16](https://cap.so/download) · [17](https://cap.so/download/versions) · [18](https://cap.so/pricing)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El modo Studio graba y exporta en el equipo. El modo Instant, los enlaces compartidos y Cap AI usan la nube de Cap o un servidor propio. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Grabar y editar no necesita un modelo de IA. Las notas de la 0.6.3 describen una transcripción en el equipo con modelos que se descargan aparte; no se comprobó en el plan gratuito. |
| Coste | Sin pago a un modelo en la ruta básica. Gratis para uso personal. La licencia de escritorio para uso comercial y Cap Pro, con nube, funciones de IA y enlaces ilimitados, son de pago según la página de precios consultada el 27 de noviembre de 2026. |
| Equipo | Equipo normal; revisar dependencias. macOS 13.1 o posterior recomendado, Windows, o Linux con glibc 2.39 o posterior. Ubuntu 22.04 no está soportado. |

Un agente de código puede ayudarte a instalarla, pero Cap no se ejecuta dentro de Claude Code, Codex ni Antigravity. Para grabar y editar en tu equipo basta la app.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Usa macOS (se recomienda 13.1 o posterior), Windows o Linux con glibc 2.39 o posterior, por ejemplo Ubuntu 24.04. Ubuntu 22.04 no está soportado. El modo Studio no necesita cuenta.
2. Descarga Cap 0.6.3 desde cap.so/download, la página de descarga que enlaza el README oficial. Instálalo y concede los permisos de grabación de pantalla y micrófono que pida el sistema. Si quieres, desactiva la telemetría anónima en Ajustes.
3. Si aparece el aviso para iniciar sesión, elige «Usar Studio» o «Ahora no». Haz la grabación de prueba, expórtala a MP4 desde el editor y reprodúcela para comprobar imagen y sonido.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/CapSoftware/Cap/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/CapSoftware/Cap/releases/tag/cap-v0.6.3)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Cap para mi objetivo y necesito pasos guiados. Lee https://github.com/CapSoftware/Cap/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En el modo Studio, sin iniciar sesión, graba 15 segundos de una ventana con un documento de prueba propio mientras dices una frase al micrófono.

**Qué comprobar:** Al detener la grabación se abre el editor. Exporta a MP4, abre el archivo en tu reproductor y comprueba que se ve la ventana y se oye la frase.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Grabar un tutorial corto sobre una hoja de cálculo propia y exportarlo en MP4
- Mostrar a un compañero cómo aparece un fallo en tu propia aplicación con una grabación editada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Grabar un tutorial corto sobre una hoja de cálculo propia y exportarlo en MP4; Mostrar a un compañero cómo aparece un fallo en tu propia aplicación con una grabación editada | necesitas transmitir en directo con escenas y varias fuentes, o vas a grabar para un uso comercial sin pagar la licencia. |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Pide permisos de pantalla, micrófono y cámara: graba solo ventanas sin datos sensibles. El modo Instant sube el video a la nube de Cap y exige cuenta. El plan gratuito es solo para uso personal y limita los enlaces compartidos. En Linux exige glibc 2.39 o posterior.

## Stack y modelos

- **Stack:** Rust, Cargo.toml, docker-compose.yml, package.json
- **Etiquetas:** `grabar pantalla` `edición de video` `tutoriales` `enlaces para compartir`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OBS Studio](obs-studio.md) | 79.6k | App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio en tiempo real. |

## Enlaces

- 🐙 GitHub: [CapSoftware/Cap](https://github.com/CapSoftware/Cap)
- 🌐 Web: <https://cap.so>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-27. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/README.md)
- [Fuente 2](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/LICENSE)
- [Fuente 3](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/licenses/LICENSE-MIT)
- [Fuente 4](https://github.com/CapSoftware/Cap/releases/tag/cap-v0.6.3)
- [Fuente 5](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/apps/desktop-gpui/locales/es.toml)
- [Fuente 6](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/.github/workflows/engine-verify.yml)
- [Fuente 7](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/.github/workflows/recording-reliability.yml)
- [Fuente 8](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/.github/workflows/verify-recording.yml)
- [Fuente 9](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/.github/workflows/publish.yml)
- [Fuente 10](https://github.com/CapSoftware/Cap/blob/029aa29a4c1cebf66f585829aef5ff8dbbca908c/.github/workflows/desktop-release.yml)
- [Fuente 11](https://github.com/CapSoftware/Cap/actions/runs/43092047100)
- [Fuente 12](https://github.com/CapSoftware/Cap/actions/runs/43092046841)
- [Fuente 13](https://github.com/CapSoftware/Cap/actions/runs/43099158030)
- [Fuente 14](https://github.com/CapSoftware/Cap/actions/runs/43150140258)
- [Fuente 15](https://github.com/CapSoftware/Cap/security/advisories)
- [Fuente 16](https://cap.so/download)
- [Fuente 17](https://cap.so/download/versions)
- [Fuente 18](https://cap.so/pricing)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
