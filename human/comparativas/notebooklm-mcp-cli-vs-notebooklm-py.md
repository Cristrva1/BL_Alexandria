# notebooklm-mcp-cli vs notebooklm-py

Generado: 2026-06-25T03:39:27.698706+00:00

| Criterio | notebooklm-mcp-cli | notebooklm-py |
|---|---|---|
| Uso real | CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP. | API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código. |
| Elegir si | integras NotebookLM con tu asistente | automatizas el NotebookLM real |
| Evitar si | prefieres la API directa ([notebooklm-py](#-notebooklm-py)). | quieres todo local ([open-notebook](#-open-notebook)). |
| Instalacion | reference_only | reference_only |

## Regla practica

Elige `notebooklm-mcp-cli` si su caso de uso encaja mejor ahora. Deja `notebooklm-py` como alternativa, salvo que el proyecto necesite explicitamente ambos.
