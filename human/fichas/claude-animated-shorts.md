[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎨 claude-animated-shorts

> Skill de Claude para crear cortos animados por código combinando personajes y escenas con Three.js y Remotion.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.4k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 47/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Claude Animated Shorts, skill gratuita de Claude que acompaña a un vídeo tutorial, de @mromidev. Licencia MIT (los fotogramas de referencia solo sirven para estudiar el estilo). Creada en noviembre de 2026, tiene ~3.6k estrellas y sin releases.

## ¿Qué hace?

Produce cortos verticales animados de 55–70 s: personajes 2D en un mundo 3D colorido con contornos de tinta, cámaras suaves, música y efectos.

## ¿Cómo lo hace?

Requiere Remotion con `@remotion/three`, Node, Python 3 y FFmpeg; el render 3D usa three.js.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [remotion](remotion.md) | Motor de composición. | Instala Remotion y `@remotion/three`; revisa su licencia. |
| [three.js](three-js.md) | Render 3D de las escenas. | Viene vía @remotion/three. |
| [Claude Code](claude-code.md) | Anfitrión de la skill. (combinación por arquitectura) | Instala la skill. |

**Notas:** Sin alternativas declaradas. Proyecto de un solo autor ligado a un vídeo.

Estado en GitHub: activo · último push 2026-11-01 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mromidev/claude-animated-shorts/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La skill usa el agente y recursos de render; Remotion y assets mantienen condiciones propias |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Código y documentos MIT; los frames de referencia son solo para estudio de estilo y no se entregan como assets comerciales reutilizables; viral no es garantía |
| Coste | Consumo del agente que ya utilizas. La skill usa el agente y recursos de render; Remotion y assets mantienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Claude Code; Three.js y Remotion; dependencias de render; historia propia |

Código y documentos MIT; los frames de referencia son solo para estudio de estilo y no se entregan como assets comerciales reutilizables; viral no es garantía

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
- Three.js y Remotion
- dependencias de render
- historia propia

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mromidev/claude-animated-shorts/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar claude-animated-shorts para mi objetivo y necesito pasos guiados. Lee https://github.com/mromidev/claude-animated-shorts/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prepara un plano de pocos segundos y revisa personajes, cámara y tiempos antes de un corto completo.

**Qué comprobar:** Puedes reproducir la escena y contrastarla con el guion.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un corto animado de prueba
- Estudiar personajes 2D en escena 3D

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un corto animado de prueba; Estudiar personajes 2D en escena 3D | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Código y documentos MIT; los frames de referencia son solo para estudio de estilo y no se entregan como assets comerciales reutilizables; viral no es garantía

## Stack y modelos

- **Stack:** Claude Code; Three.js y Remotion; dependencias de render; historia propia
- **Etiquetas:** `programatico` `skill` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mromidev/claude-animated-shorts/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
