# mem0 vs mempalace

Generado: 2026-06-23T16:56:54.761958+00:00

| Criterio | mem0 | mempalace |
|---|---|---|
| Uso real | capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. | memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos. |
| Elegir si | quieres memoria estándar lista | la privacidad es prioridad |
| Evitar si | necesitas todo local sin API ([mempalace](#-mempalace)). | quieres un SaaS gestionado. |
| Instalacion | reference_only | reference_only |

## Regla practica

Elige `mem0` si su caso de uso encaja mejor ahora. Deja `mempalace` como alternativa, salvo que el proyecto necesite explicitamente ambos.
