[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Motores de video y escenas por código

# 📚 mediabunny

> Biblioteca TypeScript para leer, escribir y convertir archivos de audio y video directamente en aplicaciones web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.5k | MPL-2.0 | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Mediabunny, librería JavaScript para leer, escribir y convertir medios (MP4, WebM, MP3, HLS) directamente en el navegador, de @Vanilagy. Licencia MPL-2.0. Es activa (~7.5k estrellas, v1.66.0) y la patrocina, entre otros, Remotion.

## ¿Qué hace?

Hace mux y demux, codifica y decodifica más de 25 códecs de vídeo, audio y subtítulos con aceleración por hardware vía WebCodecs, y procesa medios sin servidor.

## ¿Cómo lo hace?

Escrita en TypeScript puro sin dependencias, se instala con `npm install mediabunny`. Requiere ECMAScript 2021+ y está pensada para navegadores modernos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [remotion](remotion.md) | Patrocinador; procesado de medios en navegador. (combinación por arquitectura) | Úsalo en pipelines web de vídeo. |
| [FFmpeg](ffmpeg.md) | Equivalente en servidor para formatos no cubiertos. (combinación por arquitectura) | Reparte trabajo cliente/servidor. |
| [openfilm](openfilm.md) | Exportación de vídeo desde HTML. (combinación por arquitectura) | Evalúalo para codificar en el navegador. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v1.66.0 (2026-11-13) · licencia declarada MPL-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Vanilagy/mediabunny/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La biblioteca MPL-2.0 no exige IA; codecs y capacidades del navegador pueden limitar la ruta |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una biblioteca de medios, no una app de edición completa; comprueba soporte de codecs y destino en los navegadores de tus usuarios |
| Coste | Sin pago a un modelo en la ruta básica. La biblioteca MPL-2.0 no exige IA; codecs y capacidades del navegador pueden limitar la ruta |
| Equipo | Preparación según la ruta elegida. JavaScript ES2021+; navegador moderno; TypeScript >=5.7 para tipos; medio de prueba |

Es una biblioteca de medios, no una app de edición completa; comprueba soporte de codecs y destino en los navegadores de tus usuarios

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- JavaScript ES2021+
- navegador moderno
- TypeScript >=5.7 para tipos
- medio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npm install mediabunny
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Vanilagy/mediabunny/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mediabunny para mi objetivo y necesito pasos guiados. Lee https://github.com/Vanilagy/mediabunny/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee duración y pistas de un archivo y convierte una copia a un formato admitido.

**Qué comprobar:** Puedes contrastar metadatos y reproducir la salida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Procesar video dentro de una aplicación web
- Construir una herramienta de conversión en navegador

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Procesar video dentro de una aplicación web; Construir una herramienta de conversión en navegador | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una biblioteca de medios, no una app de edición completa; comprueba soporte de codecs y destino en los navegadores de tus usuarios

## Stack y modelos

- **Stack:** JavaScript ES2021+; navegador moderno; TypeScript >=5.7 para tipos; medio de prueba
- **Etiquetas:** `edicion` `library` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Vanilagy/mediabunny](https://github.com/Vanilagy/mediabunny)
- 🌐 Web: <https://mediabunny.dev/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría corregida en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Vanilagy/mediabunny/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
