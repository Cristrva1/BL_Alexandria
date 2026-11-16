[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Aplicaciones y flujos de producción

# 📲 videofy_minimal

> Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 656 | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 42/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Videofy Minimal, herramienta local para convertir artículos de noticias en vídeos cortos para pantallas de señalización digital, del grupo de medios Schibsted. Licencia Apache-2.0. Es de nicho (~650 estrellas) y no cambia desde marzo de 2026.

## ¿Qué hace?

Obtiene el artículo, genera un guion corto, busca imágenes, produce narración y renderiza el vídeo con un flujo de revisión en una interfaz CMS.

## ¿Cómo lo hace?

Requiere Python 3.12, Node, uv y FFmpeg (`brew install uv node ffmpeg`). Renderiza con Remotion, cuya licencia el README pide revisar para uso comercial; las fuentes Reuters o AP requieren credenciales.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [remotion](remotion.md) | Motor de composición y render. | Viene integrado; revisa la licencia. |
| [whisper](whisper.md) | Transcripción o subtítulos. (combinación por arquitectura) | Combina según el flujo. |
| [FFmpeg](ffmpeg.md) | Procesado de medios. | Instala FFmpeg. |

**Notas:** Alternativas (elige una): moneyprinterturbo.

Estado en GitHub: activo · último push 2026-03-13 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/schibsted/videofy_minimal/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. Necesita modelos y voz por API; Reuters o AP requieren además acceso a sus fuentes si los eliges |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La aplicación local usa servicios remotos y no incluye derechos de noticias o medios; las fuentes y afirmaciones requieren revisión |
| Coste | Consumo de APIs o servicios. Necesita modelos y voz por API; Reuters o AP requieren además acceso a sus fuentes si los eliges |
| Equipo | Preparación según la ruta elegida. uv; Node; FFmpeg; claves OpenAI y ElevenLabs; artículo autorizado |

La aplicación local usa servicios remotos y no incluye derechos de noticias o medios; las fuentes y afirmaciones requieren revisión

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- uv
- Node
- FFmpeg
- claves OpenAI y ElevenLabs
- artículo autorizado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv sync
npm install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/schibsted/videofy_minimal/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar videofy_minimal para mi objetivo y necesito pasos guiados. Lee https://github.com/schibsted/videofy_minimal/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un borrador desde un artículo de prueba y revisa guion, voz y fuentes antes de exportar.

**Qué comprobar:** Puedes identificar qué contenido se usó y verificar el video.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una noticia para señalización
- Probar una pieza informativa breve

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una noticia para señalización; Probar una pieza informativa breve | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La aplicación local usa servicios remotos y no incluye derechos de noticias o medios; las fuentes y afirmaciones requieren revisión

## Stack y modelos

- **Stack:** uv; Node; FFmpeg; claves OpenAI y ElevenLabs; artículo autorizado
- **Etiquetas:** `video` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MoneyPrinterTurbo](moneyprinterturbo.md) | 144k | App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música en un solo paso. |

## Enlaces

- 🐙 GitHub: [schibsted/videofy_minimal](https://github.com/schibsted/videofy_minimal)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/schibsted/videofy_minimal/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
