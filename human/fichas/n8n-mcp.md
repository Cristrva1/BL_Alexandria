[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Ecosistema n8n

# 🔌 n8n-mcp

> Servidor MCP que permite a un agente consultar nodos, esquemas y ejemplos de n8n para preparar workflows.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.3k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

n8n-mcp, servidor MCP de código abierto de @czlonkowski que permite a asistentes como Claude, ChatGPT, Cursor o Codex operar una instancia de n8n. Licencia MIT. Es muy activo (~23k estrellas, v2.102.0) y es independiente del servidor MCP que trae n8n.

## ¿Qué hace?

Lee ejecuciones fallidas y señala el nodo que falló, edita flujos de forma parcial, los valida y autocorrige, los prueba por webhook, formulario o chat y gestiona credenciales, tablas de datos y una auditoría de seguridad. Sin conexión a n8n también sirve como referencia de 3501 nodos y 2352 plantillas.

## ¿Cómo lo hace?

Corre como proceso aparte (npx, Docker, Railway o el servicio alojado del autor, con 100 llamadas diarias gratis) y habla con n8n por su Public API usando `N8N_API_URL` y `N8N_API_KEY`; trae una base de datos empaquetada de nodos y plantillas para documentar y validar. Antes de cambiar un flujo guarda hasta 10 versiones para revertir, y con `N8N_MCP_ACCESS_TOKEN` delega en el MCP integrado de n8n lo que la API pública no cubre.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [n8n](n8n.md) | Es la instancia que opera; sin ella solo funcionan las herramientas de documentación y validación. | n8n primero, con la Public API habilitada y una API key. No edites el mismo flujo en la interfaz mientras trabaja el asistente. |
| [n8n-skills](n8n-skills.md) | Del mismo autor: enseña al agente a usar las herramientas de n8n-mcp sin bucles de errores de validación. | Después de conectar n8n-mcp a tu cliente. |
| [Claude Code](claude-code.md) | Cliente MCP con guía de configuración propia en el repositorio (docs/CLAUDE_CODE_SETUP.md). | Instala Claude Code y luego registra n8n-mcp siguiendo esa guía. |
| [MCP Inspector](mcp-inspector.md) | Herramienta oficial para listar y probar las herramientas de un servidor MCP antes de dárselas a un agente (combinación por arquitectura). | Opcional, solo para depurar la conexión. |

**Notas:** Sin alternativas declaradas. La documentación de n8n usa el nombre «n8n MCP» para su propio servidor integrado; no es este proyecto. El servicio alojado lo opera el autor (nivel gratuito de 100 llamadas al día): tus credenciales de n8n pasan por un tercero.

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada v2.102.0 (2026-11-09) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/czlonkowski/n8n-mcp/blob/main/README.md) · [2](https://github.com/czlonkowski/n8n-skills/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El cliente consume su acceso habitual; el servicio alojado tiene cuotas y planes; el autoalojado requiere infraestructura |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. El README enlaza guías para los tres clientes. Empieza en lectura y evita editar el mismo flujo simultáneamente desde la UI |
| Coste | El coste depende del proveedor o la ruta. El cliente consume su acceso habitual; el servicio alojado tiene cuotas y planes; el autoalojado requiere infraestructura |
| Equipo | Preparación según la ruta elegida. Cliente MCP;  n8n y sus credenciales solo para operar una instancia |

El README enlaza guías para los tres clientes. Empieza en lectura y evita editar el mismo flujo simultáneamente desde la UI

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cliente MCP
-  n8n y sus credenciales solo para operar una instancia

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/czlonkowski/n8n-mcp/blob/main/docs/SELF_HOSTING.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar n8n-mcp para mi objetivo y necesito pasos guiados. Lee https://github.com/czlonkowski/n8n-mcp/blob/main/docs/SELF_HOSTING.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide al cliente buscar un nodo de n8n y consultar su esquema antes de editar un flujo.

**Qué comprobar:** La respuesta contiene las propiedades del nodo y una validación comprensible.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Investigar por qué falló una ejecución de un flujo propio
- Preparar y validar un flujo de prueba con ayuda del agente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Investigar por qué falló una ejecución de un flujo propio; Preparar y validar un flujo de prueba con ayuda del agente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README enlaza guías para los tres clientes. Empieza en lectura y evita editar el mismo flujo simultáneamente desde la UI

## Stack y modelos

- **Stack:** Cliente MCP;  n8n y sus credenciales solo para operar una instancia
- **Etiquetas:** `automation` `mcp` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [czlonkowski/n8n-mcp](https://github.com/czlonkowski/n8n-mcp)
- 🌐 Web: <https://www.n8n-mcp.com/>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/czlonkowski/n8n-mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
