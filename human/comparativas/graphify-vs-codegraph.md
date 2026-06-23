# graphify vs codegraph

Generado: 2026-06-23T16:56:54.761958+00:00

| Criterio | graphify | codegraph |
|---|---|---|
| Uso real | generador de grafos de conocimiento para proyectos locales que mapea código, PDFs, imágenes y video en diagramas interactivos, revelando cómo se conectan las piezas de un sistema. | CLI que indexa tu código y da a los asistentes de IA inteligencia semántica 100% local, permitiéndoles entender la estructura y el flujo de un repo sin leer archivo por archivo ni gastar llamadas a herramientas. |
| Elegir si | quieres ver conexiones visualmente | trabajas repos grandes |
| Evitar si | solo necesitas índice textual ([codegraph](#-codegraph)). | tu base de código es pequeña. |
| Instalacion | reference_only | reference_only |

## Regla practica

Elige `graphify` si su caso de uso encaja mejor ahora. Deja `codegraph` como alternativa, salvo que el proyecto necesite explicitamente ambos.
