[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Ahorro de contexto y tokens

# 📚 LLMLingua

> Acorta texto de entrada para modelos de lenguaje y permite medir cuánto contexto conservas antes de enviar el prompt.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.9k | MIT | Python | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

## ¿Qué es?

Acorta texto de entrada para modelos de lenguaje y permite medir cuánto contexto conservas antes de enviar el prompt.

## ¿Qué hace?

Acorta texto de entrada para modelos de lenguaje y permite medir cuánto contexto conservas antes de enviar el prompt.

## ¿Cómo lo hace?

El compresor usa un modelo local para conservar términos relevantes y retirar partes menos útiles.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada v0.2.2 (2024-04-09) · licencia declarada MIT (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/microsoft/LLMLingua/blob/01b9e9481d7395e1e83a48df4a062b11f6304325/README.md) · [2](https://llmlingua.com/) · [3](https://github.com/microsoft/LLMLingua/blob/main/LICENSE)</sub>

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
| Equipo | Memoria y GPU según el modelo. Python, PyTorch y un modelo de compresión compatible con el hardware. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python, PyTorch y un modelo de compresión compatible con el hardware.

1. Prepara Python con PyTorch, instala llmlingua y sigue Quick Start para elegir un modelo de compresión pequeño.
2. Comprime un texto público breve con un modelo local pequeño del proyecto.
3. Comprueba el resultado: obtienes dos textos y puedes comparar tamaño, instrucciones conservadas y pérdidas.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://llmlingua.com/)

[Abrir la web o descarga indicada por el autor](https://llmlingua.com/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LLMLingua para mi objetivo y necesito pasos guiados. Lee https://llmlingua.com/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Comprime un texto público breve con un modelo local pequeño del proyecto..

**Qué comprobar:** Obtienes dos textos y puedes comparar tamaño, instrucciones conservadas y pérdidas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comparar un prompt largo con su versión comprimida.
- Medir tokens ahorrados y revisar si mantuvo una restricción importante.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comparar un prompt largo con su versión comprimida.; Medir tokens ahorrados y revisar si mantuvo una restricción importante. | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Menos tokens no garantiza la misma calidad; si después llamas a un LLM remoto, su tarifa es independiente. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python, Makefile, pyproject.toml, setup.py
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [microsoft/LLMLingua](https://github.com/microsoft/LLMLingua)
- 🌐 Web: <https://llmlingua.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/LLMLingua/blob/01b9e9481d7395e1e83a48df4a062b11f6304325/README.md)
- [Fuente 2](https://llmlingua.com/)
- [Fuente 3](https://github.com/microsoft/LLMLingua/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
