[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Aprender LLMs desde cero

# 💬 nanochat

> Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 60.4k | MIT | Python | 2026-09-07 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Qué es

Resuelve la pregunta "¿cómo se monta un asistente entero?": lo muestra en un solo repo compacto y legible.

## Por qué destaca

Referencia didáctica de Karpathy que muestra el ciclo completo de un asistente conversacional en un solo repo compacto y legible. Su encadenamiento pretrain → SFT → inferencia lo hace el complemento natural de nanoGPT para ver el flujo end-to-end.

## Cómo funciona

Encadena las etapas pretrain → SFT → inferencia en PyTorch sobre GPU, con scripts que entrenan y luego sirven el modelo de chat para que puedas interactuar con él.

## Instalación rápida

`git clone https://github.com/karpathy/nanochat` y seguir el script de entrenamiento del README (entorno PyTorch con GPU). Requiere GPU seria para entrenar y datos de preentrenamiento.

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
- **Modelos / API:** Entrena modelos propios.
- **Etiquetas:** `learning` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [nanoGPT](nanogpt.md) | 64.6k | Implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo. |

## Enlaces

- 🐙 GitHub: [karpathy/nanochat](https://github.com/karpathy/nanochat)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
