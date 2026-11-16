[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 📦 sandbox

> Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.3k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

AIO Sandbox, entorno sandbox todo en uno para agentes (navegador, terminal, archivos, VSCode, Jupyter y MCP en un contenedor), de agent-infra. Licencia Apache-2.0. Tiene ~6.3k estrellas (v1.11.0) y artículo asociado.

## ¿Qué hace?

Expone navegador (con VNC), shell, sistema de archivos, VSCode Server, JupyterLab y servicios MCP preconfigurados mediante una API común para agentes.

## ¿Cómo lo hace?

Se ejecuta con `docker run … ghcr.io/agent-infra/sandbox:<tag>` (hay espejo en China). Se recomienda definir `SANDBOX_API_KEY`, porque sin ella los servicios quedan abiertos, y publicar solo en 127.0.0.1. Usa `seccomp=unconfined`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenHands](openhands.md) | Backend aislado para agentes. (combinación por arquitectura) | Apunta el agente a la API del sandbox. |
| [browser-use](browser-use.md) | Navegador del sandbox para automatización. (combinación por arquitectura) | Conecta browser-use al navegador expuesto. |
| [deer-flow](deer-flow.md) | Sandbox para el harness. (combinación por arquitectura) | Configúralo como entorno de ejecución. |

**Notas:** Alternativas (elige una): nemoclaw, e2b. Se quita ecc (sin relación documentada). Riesgo: sin API key, todo queda expuesto.

Estado en GitHub: activo · último push 2026-09-14 · última versión publicada v1.11.0 (2026-06-23) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/agent-infra/sandbox/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El contenedor básico no necesita LLM; equipo, hosting y modelos del agente se pagan o configuran aparte |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Expone MCP en /mcp; sin SANDBOX_API_KEY los servicios quedan abiertos y el ejemplo usa seccomp unconfined, por lo que no es una garantía absoluta de aislamiento |
| Coste | Sin pago a un modelo en la ruta básica. El contenedor básico no necesita LLM; equipo, hosting y modelos del agente se pagan o configuran aparte |
| Equipo | Preparación según la ruta elegida. Docker; recursos para navegador; clave de acceso propia; cliente MCP opcional |

Expone MCP en /mcp; sin SANDBOX_API_KEY los servicios quedan abiertos y el ejemplo usa seccomp unconfined, por lo que no es una garantía absoluta de aislamiento

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- recursos para navegador
- clave de acceso propia
- cliente MCP opcional

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
# Recommended: Enable API Key authentication (protects all services: API, JupyterLab, VNC)
# - Supports three methods: X-AIO-API-Key header, Authorization: Bearer header, ?api_key= query parameter
# - Without SANDBOX_API_KEY, services remain open (backward compatible)
docker run --security-opt seccomp=unconfined --rm -it \
  -e SANDBOX_API_KEY=your-secret-key \
  -p 127.0.0.1:8080:8080 ghcr.io/agent-infra/sandbox:latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/agent-infra/sandbox/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar sandbox para mi objetivo y necesito pasos guiados. Lee https://github.com/agent-infra/sandbox/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca el contenedor limitado a loopback y consulta el contexto o una captura antes de ejecutar comandos.

**Qué comprobar:** Puedes acceder al entorno autenticado y reconocer navegador, terminal y archivos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar herramientas de un agente en un contenedor
- Consultar una interfaz de navegador aislada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar herramientas de un agente en un contenedor; Consultar una interfaz de navegador aislada | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Expone MCP en /mcp; sin SANDBOX_API_KEY los servicios quedan abiertos y el ejemplo usa seccomp unconfined, por lo que no es una garantía absoluta de aislamiento

## Stack y modelos

- **Stack:** Docker; recursos para navegador; clave de acceso propia; cliente MCP opcional
- **Etiquetas:** `agents` `automation` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [NemoClaw](nemoclaw.md) | 23k | Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes. |
| [E2B](e2b.md) | 14.9k | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. |

## Enlaces

- 🐙 GitHub: [agent-infra/sandbox](https://github.com/agent-infra/sandbox)
- 🌐 Web: <https://sandbox.agent-infra.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/agent-infra/sandbox/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
