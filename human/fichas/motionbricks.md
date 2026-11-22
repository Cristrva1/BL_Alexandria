[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Física y simulación

# 🧩 MotionBricks

> Genera movimiento de personajes a partir de poses y objetivos mediante modelos locales y una escena de demostración.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.6k | Apache-2.0 | Python | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada; necesita GPU

## ¿Qué es?

Genera movimiento de personajes a partir de poses y objetivos mediante modelos locales y una escena de demostración.

## ¿Qué hace?

Genera movimiento de personajes a partir de poses y objetivos mediante modelos locales y una escena de demostración.

## ¿Cómo lo hace?

Un modelo latente genera movimiento entre metas y combina primitivas según la demostración.

Estado en GitHub: activo · último push 2026-10-26 · licencia declarada NOASSERTION (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NVlabs/motionbricks/blob/54fc563aeaaf819a753d72cc9fdc6713989cdd43/README.md) · [2](https://github.com/NVlabs/motionbricks/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La prueba con los modelos locales indicados no necesita contratar una API de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La inferencia usa pesos compatibles en el equipo; comprueba memoria, acelerador y licencia. |
| Coste | Sin pago a un modelo en la ruta básica. La inferencia local usa hardware, energía y almacenamiento. Una GPU alquilada y una licencia de pesos pueden tener costes aparte. |
| Equipo | Memoria y GPU según el modelo. GPU NVIDIA con TensorRT, entorno x86-64 compatible y pesos para el ejemplo. Las pruebas del autor se hicieron con RTX 4090. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- GPU NVIDIA con TensorRT, entorno x86-64 compatible y pesos para el ejemplo. Las pruebas del autor se hicieron con RTX 4090.

1. Sigue Setup para descargar solo los pesos autorizados y elige la demostración que requiera el menor conjunto de recursos.
2. Sigue Setup y abre el ejemplo de poses recomendado con sus pesos autorizados.
3. Comprueba el resultado: ves el movimiento entre las poses y puedes revisar cambios de trayectoria.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/NVlabs/motionbricks/blob/54fc563aeaaf819a753d72cc9fdc6713989cdd43/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/NVlabs/motionbricks/blob/54fc563aeaaf819a753d72cc9fdc6713989cdd43/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MotionBricks para mi objetivo y necesito pasos guiados. Lee https://github.com/NVlabs/motionbricks/blob/54fc563aeaaf819a753d72cc9fdc6713989cdd43/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue Setup y abre el ejemplo de poses recomendado con sus pesos autorizados..

**Qué comprobar:** Ves el movimiento entre las poses y puedes revisar cambios de trayectoria..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Completar fotogramas entre dos poses de un personaje de prueba.
- Comparar un giro de personaje con dos recorridos virtuales.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Completar fotogramas entre dos poses de un personaje de prueba.; Comparar un giro de personaje con dos recorridos virtuales. | no quieres preparar modelos, dependencias y hardware propios |

**Limitaciones:** El código, los modelos y los movimientos de ejemplo tienen licencias diferentes; revisa la tabla del README antes de usar o redistribuir. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [NVlabs/motionbricks](https://github.com/NVlabs/motionbricks)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NVlabs/motionbricks/blob/54fc563aeaaf819a753d72cc9fdc6713989cdd43/README.md)
- [Fuente 2](https://github.com/NVlabs/motionbricks/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
