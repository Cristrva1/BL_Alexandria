[Inicio](README.md) · [Rutas por objetivo](rutas.md) · [Explorador](../docs/index.html)

# Suscripción, API o modelo local

Primero identifica quién ejecuta el modelo. Después comprueba cómo se autentica, qué límites tiene y qué servicios externos utiliza.

## Ya tengo Claude Code,Codex o Antigravity

Una skill aporta instrucciones al agente y una herramienta MCP le aporta acciones o datos. Consumen el acceso del agente anfitrión cuando se usan dentro de él. Eso no incluye automáticamente las tarifas de servicios conectados,por ejemplo una API de video o de datos sociales. Las fichas distinguen cliente oficial,integración del proyecto,recurso de referencia y compatibilidad pendiente.

## La aplicación usa mi sesión del agente

Algunos proyectos documentan integraciones con Claude Code o Codex. La ficha distingue el acceso oficial del proveedor de una integración descrita por un tercero. Configura esa ruta concreta; poder pedir al agente que instale un repo no demuestra que su sesión ejecute la IA de la aplicación.

## La aplicación pide una API key

Una API permite que un programa utilice un servicio. Su key es una credencial de acceso, parecida a una contraseña del programa. Una API de IA puede aplicar cuotas, créditos o cobro por consumo. Otras claves son para GitHub, Figma o un entorno de pruebas y no pertenecen a un modelo. Revisa qué servicio las pide y su plan: tener una clave no implica uso ilimitado.

## Algunos planes incluyen créditos de API

La sesión del agente y la API siguen siendo rutas distintas. Determinados planes pueden ofrecer créditos de API con requisitos de activación, vinculación o caducidad. Comprueba tu plan y el método de autenticación; no asumir que toda suscripción incluye una API para cualquier aplicación.

## Quiero usar un modelo local

Necesitas un backend local documentado, pesos compatibles y suficiente memoria y almacenamiento. Esto evita la factura por llamada de un proveedor remoto en esa ruta, pero mantiene costes de hardware y energía. Una interfaz local puede usar un modelo remoto, y un modelo local puede necesitar internet para descargar pesos o consultar datos.

## Sin clave no significa offline ni gratis

El filtro Sin clave de API de IA indica que existe una ruta básica sin esa credencial propia. Puede usar tu suscripción de agente o un servicio online. Los datos,el alojamiento,la telefonía,los medios y las licencias pueden cobrar aparte. Modelos locales documentados puede referirse a una etapa,como transcribir o crear embeddings,y no a todo el flujo.

## Software abierto y servicio gratuito

Revisa por separado el código, los pesos del modelo, la licencia comercial, el alojamiento y los servicios externos. Alexandria no publica un precio fijo cuando depende del proveedor o del uso. La ficha muestra la fuente y la fecha de revisión para que puedas confirmar los cambios.

## Fuentes y fecha

Documentación consultada el 2026-11-15. Las condiciones de los proveedores pueden cambiar.

- [Autenticación de Codex](https://learn.chatgpt.com/docs/auth)
- [Claude Code y los planes de Claude](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan)
- [Claude Agent SDK y el plan de Claude](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)
- [Créditos de API para suscriptores de ChatGPT](https://developers.openai.com/api/docs/guides/chatgpt-api-credits)
- [Créditos de API en planes de Claude](https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-ultra-and-team-plans)
