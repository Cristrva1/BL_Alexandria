[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Motores para correr modelos en local

# 🧩 InferSSD

> Ejecuta modelos locales de tipo MoE leyendo partes de sus pesos desde un SSD cuando no caben completos en memoria o VRAM.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.3k | Apache-2.0 | C++ | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

## ¿Qué es?

Ejecuta modelos locales de tipo MoE leyendo partes de sus pesos desde un SSD cuando no caben completos en memoria o VRAM.

## ¿Qué hace?

Ejecuta modelos locales de tipo MoE leyendo partes de sus pesos desde un SSD cuando no caben completos en memoria o VRAM.

## ¿Cómo lo hace?

Mantiene activos los pesos necesarios y lee desde SSD partes del modelo MoE cuando las solicita la inferencia.

Estado en GitHub: activo · último push 2026-11-22 · última versión publicada 261122.341 (2026-11-22) · licencia declarada Apache-2.0 (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/wici-ai/inferssd/blob/910afae91c3c2578f890df7ffd9a1e55b6237680/README.md) · [2](https://github.com/wici-ai/inferssd/blob/main/LICENSE)</sub>

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
| Equipo | Memoria y GPU según el modelo. SSD y un modelo MoE compatible; backend de sistema y GPU según las guías de la variante. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- SSD y un modelo MoE compatible; backend de sistema y GPU según las guías de la variante.

1. Abre Get started, elige la distribución compatible con tu GPU y descarga la variante de pesos que el proyecto documenta.
2. Selecciona un modelo de prueba compatible y registra carga, latencia y memoria con una pregunta corta.
3. Comprueba el resultado: obtienes una respuesta y medidas de rendimiento que puedes cotejar con tu equipo.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/wici-ai/inferssd/blob/910afae91c3c2578f890df7ffd9a1e55b6237680/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/wici-ai/inferssd/blob/910afae91c3c2578f890df7ffd9a1e55b6237680/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar InferSSD para mi objetivo y necesito pasos guiados. Lee https://github.com/wici-ai/inferssd/blob/910afae91c3c2578f890df7ffd9a1e55b6237680/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Selecciona un modelo de prueba compatible y registra carga, latencia y memoria con una pregunta corta..

**Qué comprobar:** Obtienes una respuesta y medidas de rendimiento que puedes cotejar con tu equipo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Medir si un modelo compatible arranca con la memoria disponible.
- Comparar tiempos de respuesta con dos tamaños de contexto.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Medir si un modelo compatible arranca con la memoria disponible.; Comparar tiempos de respuesta con dos tamaños de contexto. | no quieres preparar modelos, dependencias y hardware propios |

**Limitaciones:** No acelera cualquier modelo. La velocidad del SSD y la variante influyen; las licencias de los pesos se revisan por separado. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [wici-ai/inferssd](https://github.com/wici-ai/inferssd)
- 🌐 Web: <https://wici.ai/wici-infer>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/wici-ai/inferssd/blob/910afae91c3c2578f890df7ffd9a1e55b6237680/README.md)
- [Fuente 2](https://github.com/wici-ai/inferssd/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
