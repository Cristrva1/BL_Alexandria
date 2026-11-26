[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › CLIs y SDKs de desarrollo

# 📚 PyBreaker

> Protege una integración Python con un interruptor que pausa llamadas tras varios fallos y después permite comprobar si volvió el servicio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 706 | BSD-3-Clause | Python | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 43/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Protege una integración Python con un interruptor que pausa llamadas tras varios fallos y después permite comprobar si volvió el servicio.

## ¿Qué hace?

Protege una integración Python con un interruptor que pausa llamadas tras varios fallos y después permite comprobar si volvió el servicio.

## ¿Cómo lo hace?

Cuenta fallos y controla cuándo se dejan pasar nuevas llamadas y cuándo se comprueba la recuperación.

Estado en GitHub: activo · último push 2026-09-25 · última versión publicada v1.4.1 (2025-09-21) · licencia declarada BSD-3-Clause (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/danielfm/pybreaker/blob/2b0b965fcfc7705ca9a776c614ea6cb3ec3fe783/README.rst) · [2](https://github.com/danielfm/pybreaker/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La primera prueba descrita no llama a un modelo generativo ni exige una clave de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. Sin pago a un modelo en esta ruta; los recursos, cuentas externas o despliegue elegidos pueden tener costes. |
| Equipo | Equipo normal; revisar dependencias. Un entorno Python con una función ficticia que pueda fallar. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno Python con una función ficticia que pueda fallar.

1. Instala pybreaker en un entorno Python de prueba y decora una función local siguiendo Usage.
2. Configura un ejemplo con una función local que falle repetidamente.
3. Comprueba el resultado: el interruptor abre y deja de invocar la función hasta el periodo de recuperación.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/danielfm/pybreaker/blob/2b0b965fcfc7705ca9a776c614ea6cb3ec3fe783/README.rst)

[Abrir la web o descarga indicada por el autor](https://github.com/danielfm/pybreaker/blob/2b0b965fcfc7705ca9a776c614ea6cb3ec3fe783/README.rst)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PyBreaker para mi objetivo y necesito pasos guiados. Lee https://github.com/danielfm/pybreaker/blob/2b0b965fcfc7705ca9a776c614ea6cb3ec3fe783/README.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un ejemplo con una función local que falle repetidamente..

**Qué comprobar:** El interruptor abre y deja de invocar la función hasta el periodo de recuperación..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Evitar que una integración lenta bloquee todos los trabajos.
- Probar cómo se recupera un cliente tras una caída ficticia.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Evitar que una integración lenta bloquee todos los trabajos.; Probar cómo se recupera un cliente tras una caída ficticia. | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Redis es opcional para guardar el estado compartido; no sirve por sí solo para reintentos ni para definir tiempos de espera. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [danielfm/pybreaker](https://github.com/danielfm/pybreaker)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/danielfm/pybreaker/blob/2b0b965fcfc7705ca9a776c614ea6cb3ec3fe783/README.rst)
- [Fuente 2](https://github.com/danielfm/pybreaker/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
