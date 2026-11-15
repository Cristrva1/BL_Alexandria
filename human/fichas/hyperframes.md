[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Motores de video y escenas por código

# 🎞️ HyperFrames

> Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 84.4k | Apache-2.0 | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

## Qué puedes hacer con él

Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes.

## Por qué destaca

Usos propuestos: Preparar un video explicativo por código; Crear una pieza de presentación con HTML.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [GSAP](gsap.md) | 30.6k | Librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincronizados sobre cualquier propiedad del DOM. |
| [Kokoro](kokoro.md) | 10.1k | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. |
| [whisperX](whisperx.md) | 25.3k | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. |

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
