[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 Text Generation WebUI

> App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 47.7k | AGPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

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

La clásica "oobabooga": carga modelos en muchos formatos y backends, con chat, modo notebook y entrenamiento LoRA.

## Por qué destaca

Soporta casi todos los backends y formatos de modelos locales.

## Cómo funciona

Una interfaz Gradio carga modelos con llama.cpp, Transformers, ExLlama u otros, y expone una API.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/oobabooga/textgen/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Text Generation WebUI para mi objetivo y necesito pasos guiados. Lee https://github.com/oobabooga/textgen/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Probar modelos en varios formatos
- Rol y escritura creativa local
- Entrenar LoRAs simples

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres experimentar con muchos backends locales | quieres algo sencillo; mira `jan` u `ollama` |

**Limitaciones:** Licencia AGPL-3.0.

## Stack y modelos

- **Stack:** Python, Gradio
- **Etiquetas:** `chatbot` `local` `inference` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Jan](jan.md) | 45.7k | Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. |
| [Open WebUI](open-webui.md) | 159k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |

## Enlaces

- 🐙 GitHub: [oobabooga/textgen](https://github.com/oobabooga/textgen)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/oobabooga/textgen/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
