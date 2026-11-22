[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🎨 Improve de shadcn

> Organiza una auditoría de código en un plan que un modelo diferente puede implementar después de una revisión humana.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.1k | MIT | — | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

## ¿Qué es?

Organiza una auditoría de código en un plan que un modelo diferente puede implementar después de una revisión humana.

## ¿Qué hace?

Organiza una auditoría de código en un plan que un modelo diferente puede implementar después de una revisión humana.

## ¿Cómo lo hace?

Da un método para separar diagnóstico, plan e implementación y transferir el plan entre sesiones.

Estado en GitHub: activo · último push 2026-09-12 · licencia declarada MIT (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/shadcn/improve/blob/cac56e1ebd3c279aa9153616cfeac7b174ab90f9/README.md) · [2](https://github.com/shadcn/improve/blob/main/LICENSE.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El componente se usa dentro del agente. El modelo y los conectores externos se contratan por separado. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. El código o las instrucciones no incluyen el consumo del agente ni de los servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Un agente con soporte de skills y un repositorio desechable o una copia de prueba. |

Consume el acceso y los límites del agente donde lo configures. No incluye servicios externos de generación, datos o alojamiento.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente con soporte de skills y un repositorio desechable o una copia de prueba.

1. Lee la skill en el README y carga únicamente Improve en una carpeta de prueba con tu cliente de skills.
2. Revisa un módulo pequeño con la skill y solicita solo el plan, sin aplicar cambios.
3. Comprueba el resultado: el plan nombra archivos, cambios propuestos y una forma de comprobarlos.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/shadcn/improve/blob/cac56e1ebd3c279aa9153616cfeac7b174ab90f9/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/shadcn/improve/blob/cac56e1ebd3c279aa9153616cfeac7b174ab90f9/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Improve de shadcn para mi objetivo y necesito pasos guiados. Lee https://github.com/shadcn/improve/blob/cac56e1ebd3c279aa9153616cfeac7b174ab90f9/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Revisa un módulo pequeño con la skill y solicita solo el plan, sin aplicar cambios..

**Qué comprobar:** El plan nombra archivos, cambios propuestos y una forma de comprobarlos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Separar el análisis de un formulario y su corrección.
- Convertir un diagnóstico de rendimiento en tareas verificables.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Separar el análisis de un formulario y su corrección.; Convertir un diagnóstico de rendimiento en tareas verificables. | no usas un agente compatible con skills |

**Limitaciones:** Los modelos se pagan o limitan por el anfitrión; el proyecto no incluye un modelo ni promete ahorro fijo. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [shadcn/improve](https://github.com/shadcn/improve)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/shadcn/improve/blob/cac56e1ebd3c279aa9153616cfeac7b174ab90f9/README.md)
- [Fuente 2](https://github.com/shadcn/improve/blob/main/LICENSE.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
