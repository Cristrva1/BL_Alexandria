# browser-use vs playwright

Generado: 2026-06-24T18:45:16.466468+00:00

| Criterio | browser-use | playwright |
|---|---|---|
| Uso real | biblioteca que da a los LLMs la capacidad de usar navegadores reales con interfaz para modelos de visión, dejando que el agente perciba la pantalla y actúe sin selectores fijos. | framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |
| Elegir si | quieres navegación como humano | necesitas control preciso del browser |
| Evitar si | necesitas scripts deterministas ([playwright](#-playwright)). | quieres que el agente navegue por visión ([browser-use](#-browser-use)). |
| Instalacion | reference_only | reference_only |

## Regla practica

Elige `browser-use` si su caso de uso encaja mejor ahora. Deja `playwright` como alternativa, salvo que el proyecto necesite explicitamente ambos.
