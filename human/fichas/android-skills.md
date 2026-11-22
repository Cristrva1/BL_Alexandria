[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 Android Skills

> Añade guías oficiales de Android a Claude Code, Codex o Antigravity para revisar, compilar y probar aplicaciones Android.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.7k | Apache-2.0 | Kotlin | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

## ¿Qué es?

Una colección oficial de instrucciones de desarrollo Android para asistentes compatibles con Agent Skills.

## ¿Qué hace?

Añade guías oficiales de Android a Claude Code, Codex o Antigravity para revisar, compilar y probar aplicaciones Android.

## ¿Cómo lo hace?

El cliente carga la skill relacionada con la tarea y aplica las guías y herramientas de Android disponibles en el proyecto.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Codex CLI](codex.md) | Anfitrión documentado de la colección para un proyecto Android. | — |

Estado en GitHub: activo · último push 2026-11-17 · última versión publicada v1.0.23 (2026-11-15) · licencia declarada Apache-2.0 (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/android/skills/blob/c72942584fff970dac86ced78b367fce0c441e52/README.md) · [2](https://developer.android.com/tools/agents/android-skills) · [3](https://developer.android.com/tools/agents/android-cli) · [4](https://github.com/android/skills/blob/main/LICENSE.txt)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las instrucciones no necesitan una clave propia. Usan el acceso del asistente; los servicios opcionales tienen requisitos separados. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. El SDK o emulador puede correr localmente; eso no implica que el modelo del asistente sea local. |
| Coste | Consumo del agente que ya utilizas. Skills Apache-2.0. El consumo del asistente y cualquier dispositivo o servicio remoto siguen sus propias condiciones. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |
| Otras rutas | Google documenta Android CLI y Gemini como rutas adicionales. |

Consume el acceso y los límites del agente donde lo configures. No incluye servicios externos de generación, datos o alojamiento.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code, Codex o Antigravity con skills o plugins habilitados.
- Proyecto Android de prueba y herramientas indicadas por la skill seleccionada.

1. Confirma el asistente que usas y abre la instalación para ese cliente.
2. Instala solo la skill que necesitas, en un proyecto Android de ejemplo. Prepara Android CLI, el SDK o el emulador si la tarea lo requiere.
3. Pide una revisión de un archivo sin autorizar cambios amplios. Comprueba las herramientas que pide y el resultado antes de ampliar el alcance.

**Entrada documentada (consulta la sintaxis original):**

```
android skills add r8-analyzer --project=.
```

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://developer.android.com/tools/agents/android-skills)

[Abrir la web o descarga indicada por el autor](https://developer.android.com/tools/agents/android-skills)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Android Skills para mi objetivo y necesito pasos guiados. Lee https://developer.android.com/tools/agents/android-skills. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En un proyecto Android de prueba instala una sola skill desde la ruta de tu cliente y pide una revisión acotada..

**Qué comprobar:** El asistente identifica la skill y aporta una revisión o propuesta que puedes comprobar en el proyecto..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Pedir una revisión de cómo maneja una pantalla los bordes del sistema.
- Examinar en un proyecto de ejemplo por qué R8 conserva clases que se esperaban eliminar.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Pedir una revisión de cómo maneja una pantalla los bordes del sistema.; Examinar en un proyecto de ejemplo por qué R8 conserva clases que se esperaban eliminar. | no usas un agente compatible con skills |

**Limitaciones:** Revisa las instrucciones SKILL.md y el alcance de las herramientas antes de dar acceso a un dispositivo real o a un proyecto de producción. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Kotlin
- **Etiquetas:** `android` `skills` `móvil`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [android/skills](https://github.com/android/skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/android/skills/blob/c72942584fff970dac86ced78b367fce0c441e52/README.md)
- [Fuente 2](https://developer.android.com/tools/agents/android-skills)
- [Fuente 3](https://developer.android.com/tools/agents/android-cli)
- [Fuente 4](https://github.com/android/skills/blob/main/LICENSE.txt)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
