[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Motores de video y escenas por código

# ⚛️ remotion

> Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 73.2k | NOASSERTION | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Remotion, framework de React para crear vídeos por código, de remotion-dev. Licencia «Remotion License» especial (GitHub muestra NOASSERTION): exige licencia de empresa en algunos casos. Es maduro (~73k estrellas, v4.0.543).

## ¿Qué hace?

Compone vídeos con componentes React, animaciones y medios, y los renderiza localmente, en servidor o en la nube (Lambda). Permite crear vídeos de forma agéntica, interactiva o programática.

## ¿Cómo lo hace?

Se inicia con `npx create-video@latest` (Node.js). Tiene APIs de Node para renderizar en servidor; los términos están en remotion.dev/license.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Remotion Agent Skills](skills-remotion.md) | Skills oficiales para agentes. | Añade las skills al proyecto. |
| [Remotion Superpowers](remotion-superpowers.md) | Orquestación de voz, música y material. | Instala el plugin en el agente. |
| [GSAP](gsap.md) | Animaciones avanzadas dentro de composiciones. (combinación por arquitectura) | Controla timelines por frame. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (11). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[AudioCraft](audiocraft.md) · [claude-animated-shorts](claude-animated-shorts.md) · [Creative Architect](creative-architect.md) · [earshot](earshot.md) · [json-render](json-render.md) · [mediabunny](mediabunny.md) · [OpenMontage](openmontage.md) · [rea-video](rea-video.md) · [scenejs](scenejs.md) · [video-shotcraft](video-shotcraft.md) · [videofy_minimal](videofy-minimal.md)

**Notas:** Alternativas (elige una): moviepy, hyperframes. Revisa la licencia antes de un uso comercial.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v4.0.543 (2026-11-11) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/remotion-dev/remotion/blob/main/README.md) · [2](https://remotion.dev/license)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. No requiere API de IA para renderizar; usa una licencia especial que exige licencia de empresa en ciertos casos y servicios externos aparte |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. La ruta con agentes utiliza las skills oficiales del proyecto compañero; no todo uso comercial es gratuito por estar disponible el código |
| Coste | El coste depende del proveedor o la ruta. No requiere API de IA para renderizar; usa una licencia especial que exige licencia de empresa en ciertos casos y servicios externos aparte |
| Equipo | Preparación según la ruta elegida. Node; proyecto React; recursos propios; licencia según uso; agente opcional |

La ruta con agentes utiliza las skills oficiales del proyecto compañero; no todo uso comercial es gratuito por estar disponible el código

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- proyecto React
- recursos propios
- licencia según uso
- agente opcional

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (console):**

```
npx create-video@latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/remotion-dev/remotion/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar remotion para mi objetivo y necesito pasos guiados. Lee https://github.com/remotion-dev/remotion/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una composición de prueba y comprueba que la cantidad de frames corresponde a su duración.

**Qué comprobar:** Puedes reproducir y exportar un clip con inicio y fin definidos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear una plantilla de video con datos
- Preparar títulos animados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear una plantilla de video con datos; Preparar títulos animados | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La ruta con agentes utiliza las skills oficiales del proyecto compañero; no todo uso comercial es gratuito por estar disponible el código

## Stack y modelos

- **Stack:** Node; proyecto React; recursos propios; licencia según uso; agente opcional
- **Etiquetas:** `video` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [MoviePy](moviepy.md) | 15.2k | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. |
| [HyperFrames](hyperframes.md) | 84.4k | Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo usen agentes. |

## Enlaces

- 🐙 GitHub: [remotion-dev/remotion](https://github.com/remotion-dev/remotion)
- 🌐 Web: <https://remotion.dev>
- 🧪 Receta: [Pipeline de Reels / video corto](../playbooks/pipeline-de-reels-video-corto.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/remotion-dev/remotion/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
