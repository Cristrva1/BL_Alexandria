[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Aprender LLMs desde cero

# 💬 nanochat

> Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 60.6k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere API de modelos; entrenar requiere cómputo y el speedrun del autor usa un nodo de ocho H100 |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El lema de cien dólares depende del benchmark, hardware y tarifas del autor; no es el coste garantizado de cualquier entrenamiento ni una configuración de portátil |
| Coste | El coste depende del proveedor o la ruta. No requiere API de modelos; entrenar requiere cómputo y el speedrun del autor usa un nodo de ocho H100 |
| Equipo | Preparación según la ruta elegida. uv; Python; CPU o GPU según ruta; presupuesto de cómputo |

El lema de cien dólares depende del benchmark, hardware y tarifas del autor; no es el coste garantizado de cualquier entrenamiento ni una configuración de portátil

## Qué puedes hacer con él

Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible.

## Por qué destaca

Usos propuestos: Estudiar una cadena de entrenamiento a chat; Reproducir un experimento con presupuesto delimitado.

## Cómo funciona

El lema de cien dólares depende del benchmark, hardware y tarifas del autor; no es el coste garantizado de cualquier entrenamiento ni una configuración de portátil

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- uv
- Python
- CPU o GPU según ruta
- presupuesto de cómputo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
uv sync --extra cpu    # (or) Use for CPU-only / MPS
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/karpathy/nanochat/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar nanochat para mi objetivo y necesito pasos guiados. Lee https://github.com/karpathy/nanochat/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prepara la ruta CPU para estudiar el código y lee speedrun antes de contratar un nodo GPU.

**Qué comprobar:** Distingues la instalación de dependencias del entrenamiento completo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar una cadena de entrenamiento a chat
- Reproducir un experimento con presupuesto delimitado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar una cadena de entrenamiento a chat; Reproducir un experimento con presupuesto delimitado | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El lema de cien dólares depende del benchmark, hardware y tarifas del autor; no es el coste garantizado de cualquier entrenamiento ni una configuración de portátil

## Stack y modelos

- **Stack:** uv; Python; CPU o GPU según ruta; presupuesto de cómputo
- **Etiquetas:** `learning` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [nanoGPT](nanogpt.md) | 64.8k | Implementación educativa histórica de GPT en PyTorch, declarada obsoleta por su autor; remite a nanochat. |

## Enlaces

- 🐙 GitHub: [karpathy/nanochat](https://github.com/karpathy/nanochat)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/karpathy/nanochat/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
