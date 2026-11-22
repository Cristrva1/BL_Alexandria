[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Física y simulación

# 🎨 Robotics for Antigravity

> Añade a Antigravity instrucciones para crear, probar y observar escenas de robótica con flujos como la simulación en MuJoCo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 212 | Apache-2.0 | Python | 2026-11-22 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

## ¿Qué es?

Añade a Antigravity instrucciones para crear, probar y observar escenas de robótica con flujos como la simulación en MuJoCo.

## ¿Qué hace?

Añade a Antigravity instrucciones para crear, probar y observar escenas de robótica con flujos como la simulación en MuJoCo.

## ¿Cómo lo hace?

Las skills guían al asistente en el uso de simuladores y herramientas definidas para cada ejercicio.

Estado en GitHub: activo · último push 2026-11-20 · licencia declarada Apache-2.0 (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google-deepmind/robotics-antigravity-plugin/blob/3dde33820355c70fe8d8e33e42707cdcb742ceb4/README.md) · [2](https://github.com/google-deepmind/robotics-antigravity-plugin/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La simulación y las skills se preparan aparte de las funciones que llamen a Gemini API. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión. |
| Coste | El coste depende del proveedor o la ruta. El código o las instrucciones no incluyen el consumo del agente ni de los servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Antigravity, dependencias de simulación indicadas y una escena de ejemplo sin robot físico. |

Consume el acceso y los límites del agente donde lo configures. No incluye servicios externos de generación, datos o alojamiento.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Antigravity, dependencias de simulación indicadas y una escena de ejemplo sin robot físico.

1. Sigue la ruta oficial para agregar únicamente los recursos de simulación; prepara la escena de ejemplo y MuJoCo si lo solicita la guía.
2. Selecciona un ejemplo de solo simulación y revisa qué herramientas pide antes de autorizarlo.
3. Comprueba el resultado: se observa el comportamiento de la escena virtual y queda un resultado que puedes comparar.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/google-deepmind/robotics-antigravity-plugin/blob/3dde33820355c70fe8d8e33e42707cdcb742ceb4/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/google-deepmind/robotics-antigravity-plugin/blob/3dde33820355c70fe8d8e33e42707cdcb742ceb4/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Robotics for Antigravity para mi objetivo y necesito pasos guiados. Lee https://github.com/google-deepmind/robotics-antigravity-plugin/blob/3dde33820355c70fe8d8e33e42707cdcb742ceb4/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Selecciona un ejemplo de solo simulación y revisa qué herramientas pide antes de autorizarlo..

**Qué comprobar:** Se observa el comportamiento de la escena virtual y queda un resultado que puedes comparar..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Abrir un escenario de simulación y cambiar la posición de un objeto virtual.
- Documentar cómo medir el recorrido de un brazo virtual en una escena de ejemplo.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Abrir un escenario de simulación y cambiar la posición de un objeto virtual.; Documentar cómo medir el recorrido de un brazo virtual en una escena de ejemplo. | no usas un agente compatible con skills |

**Limitaciones:** Gemini API, hardware y componentes externos pueden tener costes y requisitos aparte. Alcance de la ficha: simulación, sin control de hardware. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [google-deepmind/robotics-antigravity-plugin](https://github.com/google-deepmind/robotics-antigravity-plugin)
- 🌐 Web: <https://deepmind.google/models/gemini-robotics/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google-deepmind/robotics-antigravity-plugin/blob/3dde33820355c70fe8d8e33e42707cdcb742ceb4/README.md)
- [Fuente 2](https://github.com/google-deepmind/robotics-antigravity-plugin/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
