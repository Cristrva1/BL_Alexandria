# Memoria, LLM Ops & Observabilidad

Generado: 2026-06-23T16:56:54.761958+00:00

| Repo | Rol | Instalacion | Decision | Uso real |
|---|---|---|---|---|
| mem0 | library | reference_only | reference | capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| agentmemory | library | reference_only | reference | memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. |
| mempalace | library | reference_only | reference | memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos. |
| turbovec | library | reference_only | reference | librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida. |
| litellm | library | reference_only | reference | gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| langfuse | platform | reference_only | reference | plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |
| llmfit | library | reference_only | reference | herramienta para evaluar y medir el "fit" y la calidad de LLMs en una tarea concreta, orientada a comparar modelos con datos. |
| headroom | library | reference_only | reference | utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. |
| sandbox | platform | reference_only | reference | entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. |
| loguru | library | reference_only | reference | librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa. |
