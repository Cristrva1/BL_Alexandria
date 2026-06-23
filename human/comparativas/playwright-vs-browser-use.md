# playwright vs browser-use

Generado: 2026-06-23T16:56:54.761958+00:00

| Criterio | playwright | browser-use |
|---|---|---|
| Uso real | framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. | biblioteca que da a los LLMs la capacidad de usar navegadores reales con interfaz para modelos de visión, dejando que el agente perciba la pantalla y actúe sin selectores fijos. |
| Elegir si | necesitas control preciso del browser | quieres navegación como humano |
| Evitar si | quieres que el agente navegue por visión ([browser-use](#-browser-use)). | necesitas scripts deterministas ([playwright](#-playwright)). |
| Instalacion | reference_only | reference_only |

## Regla practica

Elige `playwright` si su caso de uso encaja mejor ahora. Deja `browser-use` como alternativa, salvo que el proyecto necesite explicitamente ambos.
