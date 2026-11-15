[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Entrenar y afinar modelos

# 🏋️ Transformers

> Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 169k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita API para inferencia descargada; modelos restringidos pueden pedir acceso y cada peso tiene licencia |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Es una biblioteca de modelos y no un agente de código ni una aplicación lista para todo hardware |
| Coste | Sin pago a un modelo en la ruta básica. No necesita API para inferencia descargada; modelos restringidos pueden pedir acceso y cada peso tiene licencia |
| Equipo | Preparación según la ruta elegida. Python; PyTorch; pesos de un modelo; memoria suficiente |

Es una biblioteca de modelos y no un agente de código ni una aplicación lista para todo hardware

## Qué puedes hacer con él

Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación.

## Por qué destaca

Usos propuestos: Clasificar un texto localmente; Probar un modelo de visión.

## Cómo funciona

Es una biblioteca de modelos y no un agente de código ni una aplicación lista para todo hardware

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- PyTorch
- pesos de un modelo
- memoria suficiente

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (py):**

```
# pip
pip install "transformers[torch]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/huggingface/transformers/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Transformers para mi objetivo y necesito pasos guiados. Lee https://github.com/huggingface/transformers/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta un pipeline de clasificación con un texto breve y revisa sus etiquetas.

**Qué comprobar:** Puedes identificar modelo descargado y salida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Clasificar un texto localmente
- Probar un modelo de visión

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Clasificar un texto localmente; Probar un modelo de visión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una biblioteca de modelos y no un agente de código ni una aplicación lista para todo hardware

## Stack y modelos

- **Stack:** Python; PyTorch; pesos de un modelo; memoria suficiente
- **Etiquetas:** `training` `inference` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PEFT](peft.md) | 21.9k | Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA. |
| [TRL](trl.md) | 19.7k | Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más. |
| [PyTorch](pytorch.md) | 106k | Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU. |

## Enlaces

- 🐙 GitHub: [huggingface/transformers](https://github.com/huggingface/transformers)
- 🌐 Web: <https://huggingface.co/transformers>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/huggingface/transformers/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
