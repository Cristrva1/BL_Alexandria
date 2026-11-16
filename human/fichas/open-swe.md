[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes para issues y tareas de ingeniería

# 👨‍💻 Open SWE

> Robin, fábrica de cambios sobre Deep Agents que despliega con Managed Deep Agents y entrega propuestas revisables.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.2k | MIT | Python | 2026-08-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## ¿Qué es?

Robin (repo open-swe), «fábrica de software» open source de LangChain construida sobre Deep Agents. El código propio es MIT y `vendor/` no está cubierto. Tiene ~11k estrellas (desktop-v0.3.18), está en desarrollo activo con cambios incompatibles y no acepta contribuciones externas.

## ¿Qué hace?

Investiga una base de código, implementa cambios en un sandbox aislado, los valida y entrega un pull request. También revisa PRs, aprende preferencias de revisión del repo, vigila la CI y responde a comentarios.

## ¿Cómo lo hace?

Desplegarlo tal cual requiere Managed Deep Agents de LangSmith; las herramientas MCP llegan mediante kits de LangSmith Managed Tools. Funciona sobre LangGraph y permite elegir modelos, skills, integraciones y proveedores de sandbox.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Deep Agents](deepagents.md) | Framework sobre el que está construido. | Viene incluido. |
| [LangGraph](langgraph.md) | Runtime de orquestación. | Viene incluido. |
| [E2B](e2b.md) | Proveedor de sandbox para ejecutar los cambios. (combinación por arquitectura) | Configura E2B como proveedor de sandbox si lo admite tu despliegue. |

**Notas:** Alternativas (elige una): openhands. Fuerte dependencia de servicios de LangSmith.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada desktop-v0.3.18 (2026-11-16) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/langchain-ai/open-swe/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. El despliegue tal como está requiere Managed Deep Agents y servicios asociados; adaptar a otro runtime requiere trabajo adicional |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El proyecto se presenta actualmente como Robin construido sobre Deep Agents; MIT cubre su código y no concede acceso a todos los servicios |
| Coste | Consumo de APIs o servicios. El despliegue tal como está requiere Managed Deep Agents y servicios asociados; adaptar a otro runtime requiere trabajo adicional |
| Equipo | Preparación según la ruta elegida. Managed Deep Agents para despliegue actual; repositorio y permisos de prueba; servicios integrados |

El proyecto se presenta actualmente como Robin construido sobre Deep Agents; MIT cubre su código y no concede acceso a todos los servicios

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Managed Deep Agents para despliegue actual
- repositorio y permisos de prueba
- servicios integrados

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/langchain-ai/open-swe/blob/main/docs/INSTALLATION.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Open SWE para mi objetivo y necesito pasos guiados. Lee https://github.com/langchain-ai/open-swe/blob/main/docs/INSTALLATION.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee el flujo de issue a PR y prueba un issue ficticio sin habilitar entregas automáticas.

**Qué comprobar:** Puedes inspeccionar planificación, sandbox y validación por separado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Diseñar una fábrica interna de cambios
- Estudiar un agente asíncrono con revisión

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Diseñar una fábrica interna de cambios; Estudiar un agente asíncrono con revisión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El proyecto se presenta actualmente como Robin construido sobre Deep Agents; MIT cubre su código y no concede acceso a todos los servicios

## Stack y modelos

- **Stack:** Managed Deep Agents para despliegue actual; repositorio y permisos de prueba; servicios integrados
- **Etiquetas:** `coding-agent` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenHands](openhands.md) | 93.5k | Agent Canvas: centro de sesiones autoalojado para OpenHands, Claude Code, Codex y agentes ACP. |

## Enlaces

- 🐙 GitHub: [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe)
- 🌐 Web: <https://www.langchain.com/blog/open-swe-an-open-source-framework-for-internal-coding-agents>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langchain-ai/open-swe/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
