[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Transcripción (voz a texto)

# 🖥️ Buzz

> Transcribe grabaciones y exporta subtítulos en una aplicación de escritorio que puede usar Whisper en tu propio equipo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23k | MIT | Python | 2026-11-22 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

## ¿Qué es?

Una aplicación con interfaz para convertir voz grabada en texto, basada en Whisper y otros backends compatibles.

## ¿Qué hace?

Transcribe grabaciones y exporta subtítulos en una aplicación de escritorio que puede usar Whisper en tu propio equipo.

## ¿Cómo lo hace?

Importa un audio o video, ejecuta el modelo elegido y permite revisar el texto junto a la grabación antes de exportar TXT, SRT o VTT.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Prepara audio en un formato que la aplicación pueda importar. | — |

Estado en GitHub: activo · último push 2026-11-20 · última versión publicada v1.4.5 (2026-08-23) · licencia declarada MIT (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/chidiwilliams/buzz/blob/ac3d9da57dd155c8f8fba5f40644392e38423e6f/README.md) · [2](https://flathub.org/apps/io.github.chidiwilliams.Buzz) · [3](https://github.com/chidiwilliams/buzz/releases) · [4](https://pypi.org/project/buzz-captions/1.4.5/) · [5](https://github.com/chidiwilliams/buzz/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Whisper local no requiere clave de OpenAI; las opciones remotas se configuran aparte. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Elige explícitamente un backend local. La descarga inicial de pesos usa internet. |
| Coste | El coste depende del proveedor o la ruta. La app es MIT y no hay pago por transcribir con Whisper local. Las opciones de API se cobran según su proveedor. |
| Equipo | Memoria y GPU según el modelo. El tamaño del modelo y el backend determinan memoria, disco y velocidad. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Distribución para tu sistema. En versiones recientes de macOS consulta la distinción entre Apple Silicon e Intel.
- Espacio para el modelo y un audio de prueba; CPU o GPU según el backend.

1. Abre la distribución enlazada por el proyecto y elige la versión de tu sistema; en Linux hay Flatpak.
2. En Windows el proyecto avisa que el instalador no está firmado. No desactives las protecciones: coteja el archivo y su SHA-256 con el release, o elige otra distribución.
3. Alternativa documentada: instala el paquete oficial de PyPI 1.4.5 en un entorno de Python 3.12 con FFmpeg. Su metadato admite 3.12 y difiere de la rama de desarrollo.
4. Abre un audio breve, selecciona Whisper local y descarga los pesos si los necesita; revisa el resultado y expórtalo.

**Entrada documentada (consulta la sintaxis original):**

```
pip install buzz-captions
```

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/chidiwilliams/buzz/blob/ac3d9da57dd155c8f8fba5f40644392e38423e6f/README.md)

[Abrir la web o descarga indicada por el autor](https://flathub.org/apps/io.github.chidiwilliams.Buzz)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Buzz para mi objetivo y necesito pasos guiados. Lee https://github.com/chidiwilliams/buzz/blob/ac3d9da57dd155c8f8fba5f40644392e38423e6f/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Importa diez segundos de audio propio y elige un modelo Whisper local pequeño..

**Qué comprobar:** Aparece una transcripción que puedes revisar y exportar como SRT..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Convertir una nota de voz propia en texto editable.
- Crear subtítulos en SRT para una demostración grabada.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Convertir una nota de voz propia en texto editable.; Crear subtítulos en SRT para una demostración grabada. | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Instalador Windows sin firma según el autor; GitHub publica digests para los archivos del release revisado. El digest permite cotejar integridad, no prueba ausencia de malware. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python, Makefile, pyproject.toml
- **Etiquetas:** `whisper` `subtítulos` `transcripción`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [chidiwilliams/buzz](https://github.com/chidiwilliams/buzz)
- 🌐 Web: <https://chidiwilliams.github.io/buzz>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/chidiwilliams/buzz/blob/ac3d9da57dd155c8f8fba5f40644392e38423e6f/README.md)
- [Fuente 2](https://flathub.org/apps/io.github.chidiwilliams.Buzz)
- [Fuente 3](https://github.com/chidiwilliams/buzz/releases)
- [Fuente 4](https://pypi.org/project/buzz-captions/1.4.5/)
- [Fuente 5](https://github.com/chidiwilliams/buzz/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
