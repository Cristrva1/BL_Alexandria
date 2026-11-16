[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Motores de video y escenas por código

# 🎞️ HyperFrames

> Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 84.4k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 73/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

HyperFrames, framework de HeyGen que convierte HTML, CSS, medios y animaciones navegables en vídeos MP4 deterministas, pensado para agentes. Licencia Apache-2.0, sin tarifas por render ni umbrales comerciales. Creado en marzo de 2026, ya tiene ~85k estrellas (v0.9.56).

## ¿Qué hace?

Los agentes escriben HTML con animaciones (por ejemplo, GSAP) y HyperFrames los renderiza fotograma a fotograma a vídeo. Incluye un Studio de previsualización y skills para agentes.

## ¿Cómo lo hace?

Requiere Node.js 22+ y FFmpeg. Las skills se instalan con `npx hyperframes skills update` o con el plugin de Claude Code (`claude plugin marketplace add heygen-com/hyperframes`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin oficial. | Añade el marketplace e instala el plugin. |
| [GSAP](gsap.md) | Animaciones navegables en las composiciones. | Usa timelines GSAP en el HTML. |
| [Kokoro](kokoro.md) | Narración local. (combinación por arquitectura) | Genera el audio y añádelo a la composición. |
| [whisperX](whisperx.md) | Subtítulos sincronizados. (combinación por arquitectura) | Genera marcas por palabra. |
| [Arcads AI Video Skill Pack](arcads-claude-code.md) | Combinación recíproca: Arcads AI Video Skill Pack lo enlaza como «Usado para incrustar subtítulos». | Orden indicado desde Arcads AI Video Skill Pack: Requiere Node.js; se ejecuta con npx bajo demanda. |
| [brag](brag.md) | Combinación recíproca: brag lo enlaza como «Motor de render en el que se basa». | Orden indicado desde brag: Viene integrado. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Creative Architect](creative-architect.md) · [open-design](open-design.md)

**Notas:** Alternativas (elige una): remotion, moviepy. Su README compara explícitamente su licencia con la de Remotion.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.9.56 (2026-11-16) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/heygen-com/hyperframes/blob/main/README.md)</sub>

## Ver similares

Grupo **Video y escenas por código**: HyperFrames ocupa la posición 1 de 5 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **HyperFrames** (esta ficha) ⭐ recomendado | 73 | Si quieres que un agente componga video desde HTML con HeyGen HyperFrames. |
| 2 | [remotion](remotion.md) | 68 | Si sabes React y quieres generar videos programáticos con calidad de producción (revisa su licencia). |
| 3 | [Motion Canvas](motion-canvas.md) | 56 | Si haces animaciones explicativas en TypeScript con editor en tiempo real. |
| 4 | [MoviePy](moviepy.md) | 54 | Si editas video desde Python (cortes, composición, texto) sin interfaz. |
| 5 | [Revideo](revideo.md) | 51 | Si quieres renderizar videos desde código TypeScript como API o servicio. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El render local Apache no cobra por render; el agente y generaciones o planes Pro usan recursos separados |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Los skills deben coincidir con la versión del CLI; el núcleo basta para empezar y no es necesario instalar todo el catálogo de extensiones |
| Coste | El coste depende del proveedor o la ruta. El render local Apache no cobra por render; el agente y generaciones o planes Pro usan recursos separados |
| Equipo | Preparación según la ruta elegida. Node 22+; FFmpeg; composición pequeña; agente opcional |

Los skills deben coincidir con la versión del CLI; el núcleo basta para empezar y no es necesario instalar todo el catálogo de extensiones

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node 22+
- FFmpeg
- composición pequeña
- agente opcional

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
npx hyperframes init my-video
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/heygen-com/hyperframes/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar HyperFrames para mi objetivo y necesito pasos guiados. Lee https://github.com/heygen-com/hyperframes/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un proyecto con un título de pocos segundos, previsualiza y renderiza un MP4.

**Qué comprobar:** Puedes comprobar duración, primer y último frame y archivo exportado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un video explicativo por código
- Crear una pieza de presentación con HTML

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un video explicativo por código; Crear una pieza de presentación con HTML | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los skills deben coincidir con la versión del CLI; el núcleo basta para empezar y no es necesario instalar todo el catálogo de extensiones

## Stack y modelos

- **Stack:** Node 22+; FFmpeg; composición pequeña; agente opcional
- **Etiquetas:** `video` `agents` `skills` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [remotion](remotion.md) | 73.2k | Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. |
| [MoviePy](moviepy.md) | 15.2k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |

## Enlaces

- 🐙 GitHub: [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)
- 🌐 Web: <https://hyperframes.heygen.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/heygen-com/hyperframes/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
