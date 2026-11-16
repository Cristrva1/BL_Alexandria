[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🧩 MCP servers for AWS

> Colección oficial de AWS Labs con decenas de servidores MCP para documentación, infraestructura como código, EKS, ECS, serverless y otros servicios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.9k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Conjunto de servidores MCP de código abierto (Apache-2.0) publicado por AWS Labs. Muy activo; desde mayo de 2026 AWS recomienda para producción el Agent Toolkit for AWS, presentado como sucesor, aunque este repositorio sigue funcionando y aceptando contribuciones.

## ¿Qué hace?

Ofrece servidores especializados: documentación de AWS, infraestructura como código (CloudFormation y CDK), Amazon EKS y ECS, aplicaciones serverless con SAM, ejecución de funciones Lambda como herramientas, construcción de contenedores con Finch, bases de datos, costes y más. También enlaza el AWS MCP Server gestionado (en preview).

## ¿Cómo lo hace?

Cada servidor vive en `src/` y se ejecuta normalmente con `uvx awslabs.<servidor>@latest` usando el transporte stdio (el soporte SSE se retiró). La autenticación usa perfiles y credenciales estándar de AWS; el README incluye botones de instalación para varios clientes y configuraciones JSON.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Los servidores se registran como servidores MCP stdio en Claude Code con sus comandos uvx (combinación por arquitectura). | Configura credenciales y perfil de AWS; después añade el servidor elegido en Claude Code. |
| [Codex CLI](codex.md) | Codex puede usar los mismos servidores stdio para consultar documentación o generar infraestructura (combinación por arquitectura). | Perfil de AWS listo; después registra el servidor en la configuración MCP de Codex. |
| [MCP Inspector](mcp-inspector.md) | MCP Inspector permite probar las herramientas de un servidor de AWS antes de dárselas a un agente (combinación por arquitectura). | Instala uv y el servidor; después lánzalo desde MCP Inspector. |

**Notas:** Empieza por servidores de solo lectura (documentación) y usa permisos IAM mínimos. Para producción, AWS recomienda el Agent Toolkit for AWS.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 2026.11.20261109200750 (2026-11-09) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/awslabs/mcp/blob/main/README.md) · [2](https://awslabs.github.io/mcp/) · [3](https://aws.amazon.com/about-aws/whats-new/2026/05/agent-toolkit/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El servidor aporta herramientas a un cliente MCP; el cliente aporta el modelo. Revisar los servicios que usa cada herramienta. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Consumo del agente que ya utilizas. El modelo se consume en el cliente MCP. Programas, licencias y servicios conectados pueden tener requisitos y tarifas independientes. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Configura este servidor en un cliente MCP compatible, incluido Claude Code o Codex. Sus servicios y permisos se preparan aparte.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible y el programa o servicio que va a controlar la herramienta.

1. Prepara el servidor y sus dependencias siguiendo la configuración del README.
2. Añade el comando o la URL en el cliente MCP y configura los permisos y credenciales de los servicios conectados.
3. Comprueba que aparecen sus herramientas y prueba una consulta pequeña antes de permitir modificaciones.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/awslabs/mcp/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MCP servers for AWS para mi objetivo y necesito pasos guiados. Lee https://github.com/awslabs/mcp/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura el servidor de documentación de AWS con uvx en tu cliente MCP y pregunta por un servicio concreto..

**Qué comprobar:** El agente devuelve fragmentos de la documentación oficial con su enlace..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- consultar la documentación actualizada de AWS desde tu agente de código
- revisar y generar plantillas de CloudFormation o CDK con validación de seguridad

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: consultar la documentación actualizada de AWS desde tu agente de código; revisar y generar plantillas de CloudFormation o CDK con validación de seguridad | necesitas un producto autónomo y esta pieza requiere un cliente MCP |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. La mayoría de servidores necesitan una cuenta de AWS; las acciones sobre recursos pueden generar costes.

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `mcp` `python` `cloud` `aws`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [awslabs/mcp](https://github.com/awslabs/mcp)
- 🌐 Web: <https://awslabs.github.io/mcp/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/awslabs/mcp/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
