[🏠 Inicio](../README.md) › [🧑‍💻 Entender código, trabajar con datos y entrenar modelos](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › CLIs y SDKs de desarrollo

# 🐍 openai-python

> SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 32.2k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | Consumo de APIs o servicios. Revisar el plan, créditos, cuotas y facturación del proveedor antes de ejecutar. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve el glue HTTP: no escribes peticiones a mano, usas clientes tipados con streaming.

## Por qué destaca

Cliente oficial y al día mantenido por OpenAI, con amplia adopción y soporte inmediato de las novedades de la API. Su tipado, streaming y soporte síncrono/async lo hacen la base de facto para integrar GPT en Python.

## Cómo funciona

Envuelve las peticiones HTTP a la API en clientes Python síncronos y asíncronos, con tipado, streaming de respuestas, reintentos y manejo de errores integrados.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install openai
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/openai/openai-python/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar openai-python para mi objetivo y necesito pasos guiados. Lee https://github.com/openai/openai-python/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `code` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |

## Enlaces

- 🐙 GitHub: [openai/openai-python](https://github.com/openai/openai-python)
- 🌐 Web: <https://pypi.org/project/openai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/openai/openai-python/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
