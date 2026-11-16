[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Aprender LLMs desde cero

# 📘 how-to-train-your-gpt

> Guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librería de producción.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.2k | MIT | Jupyter Notebook | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere API para el recorrido local; cómputo y GPU opcional se pagan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Empieza por el capítulo de setup; los comandos del README ofrecen alternativas y no deben concatenarse como si todas fueran obligatorias |
| Coste | El coste depende del proveedor o la ruta. No requiere API para el recorrido local; cómputo y GPU opcional se pagan aparte |
| Equipo | Preparación según la ruta elegida. Python; Jupyter; entorno PyTorch; equipo adecuado al experimento |

Empieza por el capítulo de setup; los comandos del README ofrecen alternativas y no deben concatenarse como si todas fueran obligatorias

## Qué puedes hacer con él

Guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librería de producción.

## Por qué destaca

Usos propuestos: Aprender tokenización paso a paso; Comprender atención con ejemplos pequeños.

## Cómo funciona

Empieza por el capítulo de setup; los comandos del README ofrecen alternativas y no deben concatenarse como si todas fueran obligatorias

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- Jupyter
- entorno PyTorch
- equipo adecuado al experimento

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Install everything you need
pip install jupyter tiktoken torch numpy datasets matplotlib --index-url https://download.pytorch.org/whl/cpu

# Start with chapter 2 (tokenization)
jupyter notebook notebooks/02_tokenization.ipynb
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/raiyanyahya/how-to-train-your-gpt/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar how-to-train-your-gpt para mi objetivo y necesito pasos guiados. Lee https://github.com/raiyanyahya/how-to-train-your-gpt/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre el notebook de tokenización y procesa una frase antes de pasar a entrenamiento.

**Qué comprobar:** Puedes inspeccionar tokens y reconstrucción del texto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender tokenización paso a paso
- Comprender atención con ejemplos pequeños

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender tokenización paso a paso; Comprender atención con ejemplos pequeños | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Empieza por el capítulo de setup; los comandos del README ofrecen alternativas y no deben concatenarse como si todas fueran obligatorias

## Stack y modelos

- **Stack:** Python; Jupyter; entorno PyTorch; equipo adecuado al experimento
- **Etiquetas:** `learning`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [nanochat](nanochat.md) | 60.6k | Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible. |

## Enlaces

- 🐙 GitHub: [raiyanyahya/how-to-train-your-gpt](https://github.com/raiyanyahya/how-to-train-your-gpt)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/raiyanyahya/how-to-train-your-gpt/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
