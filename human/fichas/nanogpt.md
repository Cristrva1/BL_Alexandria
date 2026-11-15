[🏠 Inicio](../README.md) › [🧑‍💻 Entender código, trabajar con datos y entrenar modelos](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Aprender LLMs desde cero

# 🔬 nanoGPT

> Implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 64.8k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve la opacidad de los frameworks: ves exactamente cómo se entrena un GPT sin capas de abstracción.

## Por qué destaca

Referencia didáctica de Karpathy ampliamente usada para aprender cómo funciona realmente el entrenamiento de un GPT, sin capas de abstracción. Su minimalismo (unos pocos cientos de líneas) lo hace el punto de partida habitual para entender y experimentar.

## Cómo funciona

Define el modelo GPT y su bucle de entrenamiento en PyTorch sobre GPU, reproduciendo resultados tipo GPT-2 con unos pocos cientos de líneas y dependencias mínimas.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/karpathy/nanoGPT/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar nanoGPT para mi objetivo y necesito pasos guiados. Lee https://github.com/karpathy/nanoGPT/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Aprender cómo se entrena un GPT
- Experimentos pequeños reproducibles
- Base para afinar modelos propios sobre datos propios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres entender el entrenamiento de un GPT desde cero | solo consumes modelos vía API o necesitas un pipeline de chat completo (nanochat) |

**Limitaciones:** Entrenar a escala real exige GPU y tiempo; no es una librería de producción, sino un recurso educativo minimalista.

## Stack y modelos

- **Stack:** Python, PyTorch, GPU
- **Etiquetas:** `learning` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [nanochat](nanochat.md) | 60.6k | Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LLMs from Scratch](llms-from-scratch.md) | 108k | Código del libro de Sebastian Raschka para implementar un LLM tipo ChatGPT en PyTorch paso a paso. |

## Enlaces

- 🐙 GitHub: [karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/karpathy/nanoGPT/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
