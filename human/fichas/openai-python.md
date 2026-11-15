[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › CLIs y SDKs de desarrollo

# 🐍 openai-python

> SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 32.1k | Apache-2.0 | Python | 2026-11-10 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Resuelve el glue HTTP: no escribes peticiones a mano, usas clientes tipados con streaming.

## Por qué destaca

Cliente oficial y al día mantenido por OpenAI, con amplia adopción y soporte inmediato de las novedades de la API. Su tipado, streaming y soporte síncrono/async lo hacen la base de facto para integrar GPT en Python.

## Cómo funciona

Envuelve las peticiones HTTP a la API en clientes Python síncronos y asíncronos, con tipado, streaming de respuestas, reintentos y manejo de errores integrados.

## Instalación rápida

`pip install openai` y configurar `OPENAI_API_KEY` (variable de entorno). Requiere una cuenta OpenAI con clave válida y saldo.

## Casos de uso

- Llamar a la API de OpenAI
- Base para apps que usan GPT
- Consumir embeddings, imágenes y audio desde Python

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| usas modelos de OpenAI desde Python y quieres el cliente oficial | quieres abstracción multi-proveedor (litellm) o no usas OpenAI |

## Stack y modelos

- **Stack:** Python
- **Modelos / API:** OpenAI (chat, embeddings, imágenes, audio).
- **Etiquetas:** `code` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| [langchain](langchain.md) | 149k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |

## Enlaces

- 🐙 GitHub: [openai/openai-python](https://github.com/openai/openai-python)
- 🌐 Web: <https://pypi.org/project/openai/>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
