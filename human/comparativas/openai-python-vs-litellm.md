# openai-python vs litellm

Generado: 2026-06-25T03:39:27.698706+00:00

| Criterio | openai-python | litellm |
|---|---|---|
| Uso real | SDK oficial de OpenAI para Python, que expone de forma tipada y cómoda la API (chat, embeddings, imágenes, audio) y es la base habitual para apps que usan sus modelos. | gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| Elegir si | usas modelos de OpenAI | trabajas con múltiples modelos |
| Evitar si | quieres abstracción multi-proveedor ([litellm](06-memoria-llm-ops-observabilidad.md#-litellm)). | usas un único proveedor fijo. |
| Instalacion | reference_only | reference_only |

## Regla practica

Elige `openai-python` si su caso de uso encaja mejor ahora. Deja `litellm` como alternativa, salvo que el proyecto necesite explicitamente ambos.
