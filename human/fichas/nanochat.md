[🏠 Inicio](../README.md) › [🧑‍💻 Entender código, trabajar con datos y entrenar modelos](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Aprender LLMs desde cero

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
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. No hay factura por llamada a un proveedor en la ruta local; sí hay hardware, energía y posibles condiciones de los pesos. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve la pregunta "¿cómo se monta un asistente entero?": lo muestra en un solo repo compacto y legible.

## Por qué destaca

Referencia didáctica de Karpathy que muestra el ciclo completo de un asistente conversacional en un solo repo compacto y legible. Su encadenamiento pretrain → SFT → inferencia lo hace el complemento natural de nanoGPT para ver el flujo end-to-end.

## Cómo funciona

Encadena las etapas pretrain → SFT → inferencia en PyTorch sobre GPU, con scripts que entrenan y luego sirven el modelo de chat para que puedas interactuar con él.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/karpathy/nanochat/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar nanochat para mi objetivo y necesito pasos guiados. Lee https://github.com/karpathy/nanochat/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Ver el ciclo completo (pretrain→SFT→chat)
- Base educativa para entender un asistente entero
- Punto de partida para experimentos de fine-tuning

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres el pipeline completo de un chat end-to-end | solo necesitas el core del modelo (nanoGPT) o un modelo listo para usar |

**Limitaciones:** Entrenar de cero exige GPU y corpus; es educativo, no una alternativa a un modelo comercial servido.

## Stack y modelos

- **Stack:** Python, PyTorch, GPU
- **Etiquetas:** `learning` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [nanoGPT](nanogpt.md) | 64.8k | Implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo. |

## Enlaces

- 🐙 GitHub: [karpathy/nanochat](https://github.com/karpathy/nanochat)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/karpathy/nanochat/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
