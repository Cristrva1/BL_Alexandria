[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 🏋️ PEFT

> Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 21.9k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Sin API de modelo alojado; entrenar y almacenar pesos requiere cómputo propio o alquilado |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Reducir parámetros entrenables no elimina toda la memoria del modelo base; los ejemplos de hardware no se generalizan a cualquier modelo |
| Coste | Sin pago a un modelo en la ruta básica. Sin API de modelo alojado; entrenar y almacenar pesos requiere cómputo propio o alquilado |
| Equipo | Preparación según la ruta elegida. Python; modelo Transformers; dataset; hardware suficiente |

Reducir parámetros entrenables no elimina toda la memoria del modelo base; los ejemplos de hardware no se generalizan a cualquier modelo

## Qué puedes hacer con él

Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA.

## Por qué destaca

Usos propuestos: Ajustar un modelo con menos parámetros; Reutilizar un adaptador entrenado.

## Cómo funciona

Reducir parámetros entrenables no elimina toda la memoria del modelo base; los ejemplos de hardware no se generalizan a cualquier modelo

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- modelo Transformers
- dataset
- hardware suficiente

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install peft
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/huggingface/peft/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PEFT para mi objetivo y necesito pasos guiados. Lee https://github.com/huggingface/peft/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Estudia el ejemplo LoRA y comprueba qué parámetros serán entrenables.

**Qué comprobar:** Puedes distinguir modelo base de adaptador.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Ajustar un modelo con menos parámetros
- Reutilizar un adaptador entrenado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Ajustar un modelo con menos parámetros; Reutilizar un adaptador entrenado | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Reducir parámetros entrenables no elimina toda la memoria del modelo base; los ejemplos de hardware no se generalizan a cualquier modelo

## Stack y modelos

- **Stack:** Python; modelo Transformers; dataset; hardware suficiente
- **Etiquetas:** `training` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Transformers](transformers.md) | 169k | Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. |
| [TRL](trl.md) | 19.7k | Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más. |

## Enlaces

- 🐙 GitHub: [huggingface/peft](https://github.com/huggingface/peft)
- 🌐 Web: <https://huggingface.co/docs/peft>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/huggingface/peft/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
