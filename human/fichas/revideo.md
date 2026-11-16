[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Motores de video y escenas por código

# 📚 Revideo

> Motor TypeScript para crear vídeos con código y renderizarlos sin interfaz desde una API, con reproductor React para previsualizar escenas en el navegador.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.2k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Framework de código abierto (MIT) mantenido por Midrender (es el motor de su producto), derivado históricamente de Motion Canvas. Actividad moderada: el último push es de julio de 2026.

## ¿Qué hace?

Permite definir vídeos con TypeScript (escenas, texto, vídeo, audio, imágenes) y renderizarlos sin interfaz desde código o una API, con reproductor React para previsualizar en la web y plantillas de ejemplo.

## ¿Cómo lo hace?

Las escenas son funciones generadoras en TypeScript; el renderizado headless se ejecuta donde haya Node y un navegador headless (incluido Google Cloud Run) y puede repartirse entre workers. El paquete `@revideo/ffmpeg` usa fluent-ffmpeg con binarios de FFmpeg instalados por npm. Se crea un proyecto con `npm init @revideo@latest`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | El README de Revideo indica que, como una escena es TypeScript plano, Claude o Codex pueden generarla a partir de un prompt. | Crea el proyecto con `npm init @revideo@latest`; después abre la carpeta con el agente. |
| [Codex CLI](codex.md) | El README de Revideo indica que Codex (o Claude) puede generar una escena a partir de un prompt. | Crea el proyecto; después pide a Codex las escenas. |
| [FFmpeg](ffmpeg.md) | El paquete `@revideo/ffmpeg` usa FFmpeg (vía fluent-ffmpeg y @ffmpeg-installer) para codificar y procesar audio y vídeo. | Crea el proyecto (las dependencias instalan los binarios de FFmpeg); después renderiza con `renderVideo()`. |

**Notas:** Alternativa de Motion Canvas y Remotion; frente a Remotion, su licencia MIT no exige licencia comercial para empresas.

Estado en GitHub: activo · último push 2026-07-15 · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/midrender/revideo/blob/main/README.md) · [2](https://github.com/midrender/revideo/blob/main/packages/ffmpeg/package.json)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (consulta la sintaxis original):**

```
npm init @revideo@latest
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/midrender/revideo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Revideo para mi objetivo y necesito pasos guiados. Lee https://github.com/midrender/revideo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta `npm init @revideo@latest` y sigue el asistente; después renderiza el proyecto de ejemplo..

**Qué comprobar:** Obtienes un MP4 generado desde código..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- generar muchas variantes de un vídeo a partir de datos o plantillas
- añadir un renderizador de vídeo a una aplicación web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: generar muchas variantes de un vídeo a partir de datos o plantillas; añadir un renderizador de vídeo a una aplicación web | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Envía telemetría por defecto (se desactiva con DISABLE_TELEMETRY=true). El último push es de julio de 2026.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `video` `typescript` `rendering` `code`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Motion Canvas](motion-canvas.md) | 20k | Biblioteca TypeScript para crear animaciones y vídeos explicativos con código, con editor en tiempo real que sincroniza animaciones con una pista de voz. |
| [remotion](remotion.md) | 73.2k | Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. |

## Enlaces

- 🐙 GitHub: [midrender/revideo](https://github.com/midrender/revideo)
- 🌐 Web: <https://midrender.com/revideo>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/midrender/revideo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
