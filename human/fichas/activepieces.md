[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🧩 activepieces

> Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.5k | NOASSERTION | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

Plataforma de automatización con IA de código abierto, presentada como reemplazo libre de Zapier. La edición comunitaria tiene licencia MIT y las funciones Enterprise una licencia comercial; el proyecto es activo, con versiones mensuales.

## ¿Qué hace?

Permite que personas sin perfil técnico construyan flujos en un editor sin código, mientras los desarrolladores crean las integraciones. Conecta Google Sheets, OpenAI, Discord, RSS y más de 200 servicios, incluye piezas nativas de IA para probar proveedores o crear agentes, y pasos de intervención humana como esperas y aprobaciones. Todas sus piezas (más de 280) se exponen también como servidores MCP para usarlas desde Claude Desktop, Cursor o Windsurf.

## ¿Cómo lo hace?

Cada integración es una «pieza»: un paquete npm escrito en TypeScript con tipado estricto, publicado en npmjs.com y con recarga en caliente para desarrollo local; el 60 % lo aporta la comunidad. El constructor visual ejecuta los flujos sobre esas piezas y un SDK de IA ayuda a crear flujos dentro del editor. Se autoaloja (incluso en redes aisladas) o se usa en la nube del proveedor; la guía de despliegue está en su documentación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [NocoDB](nocodb.md) | Activepieces tiene una pieza de NocoDB para crear o actualizar registros desde un flujo, útil como base de datos tipo hoja de cálculo para los resultados. | NocoDB primero y un token de API; después la conexión en la pieza. |
| [Claude Code](claude-code.md) | Las piezas se exponen como servidores MCP, así que un agente de código puede usar las integraciones de Activepieces como herramientas. | Activepieces en marcha; luego registra el servidor MCP de las piezas en el cliente. |
| [litellm](litellm.md) | Centraliza las llamadas de IA de los flujos en un gateway compatible con OpenAI con presupuestos y registro de gasto (combinación por arquitectura). | LiteLLM primero; usa su URL y una clave virtual en las piezas que acepten un endpoint compatible con OpenAI. |

**Notas:** Sin alternativas declaradas. Antes de usarlo comercialmente, revisa qué funciones caen en la licencia Enterprise.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 0.93.0 (2026-11-08) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/activepieces/activepieces/blob/main/README.md) · [2](https://www.activepieces.com/pieces/nocodb)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La edición, licencia y alojamiento elegidos determinan el coste; las piezas de IA usan sus proveedores |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. El MCP documentado usa un endpoint de la instancia y autenticación; hay que conceder acceso al cliente y las piezas y servicios conservan sus propios requisitos |
| Coste | El coste depende del proveedor o la ruta. La edición, licencia y alojamiento elegidos determinan el coste; las piezas de IA usan sus proveedores |
| Equipo | Preparación según la ruta elegida. Docker Compose con PostgreSQL y Redis, o una cuenta alojada |

El MCP documentado usa un endpoint de la instancia y autenticación; hay que conceder acceso al cliente y las piezas y servicios conservan sus propios requisitos

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker Compose con PostgreSQL y Redis, o una cuenta alojada

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://www.activepieces.com/docs/install/overview)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar activepieces para mi objetivo y necesito pasos guiados. Lee https://www.activepieces.com/docs/install/overview. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un flujo con un disparador de prueba y una acción de texto.

**Qué comprobar:** El historial del flujo muestra la entrada y la salida de la acción.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Pasar respuestas de un formulario a una aplicación de negocio
- Solicitar aprobación humana antes de continuar una automatización

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Pasar respuestas de un formulario a una aplicación de negocio; Solicitar aprobación humana antes de continuar una automatización | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El MCP documentado usa un endpoint de la instancia y autenticación; hay que conceder acceso al cliente y las piezas y servicios conservan sus propios requisitos

## Stack y modelos

- **Stack:** Docker Compose con PostgreSQL y Redis, o una cuenta alojada
- **Etiquetas:** `automation` `typescript` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Enlaces

- 🐙 GitHub: [activepieces/activepieces](https://github.com/activepieces/activepieces)
- 🌐 Web: <https://www.activepieces.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/activepieces/activepieces/blob/main/README.md)
- [Fuente 2](https://www.activepieces.com/docs/mcp/overview)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
