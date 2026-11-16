[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🕸️ codex-chatgpt-web

> Integración de terceros que conecta una sesión de ChatGPT Web con el selector de modelos y herramientas de Codex.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.7k | MIT | TypeScript | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

Integración no oficial de terceros que permite usar en Codex los modelos de ChatGPT Web de tu cuenta, incluido Pro, de @miuuyy. Licencia MIT. Tiene ~16k estrellas.

## ¿Qué hace?

Envía los mensajes a través de tu sesión iniciada en ChatGPT Web, con los límites de esa cuenta, desde el selector de modelos nativo de Codex. En modo «Full harness», ChatGPT accede a los archivos, la terminal y las herramientas de la tarea mediante MCP.

## ¿Cómo lo hace?

Se distribuye como lanzador descargable con navegador integrado; el modo MCP requiere un túnel y una clave. El propio README advierte que es automatización de navegador no oficial (no la API de OpenAI), que los cambios de la interfaz pueden romperla, que el perfil del navegador es un artefacto sensible y que el listener de loopback es accesible para otros procesos del mismo usuario.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Codex CLI](codex.md) | Cliente que integra. | Instala Codex y luego el lanzador. |
| [T3 Code](t3code.md) | Controlar Codex desde web o móvil. (combinación por arquitectura) | Usa T3 Code sobre Codex. |
| [Context7](context7.md) | Documentación vía MCP en modo harness. (combinación por arquitectura) | Añade el MCP a Codex. |

**Notas:** Sin alternativas declaradas. Riesgo de términos de servicio y de seguridad (automatiza una sesión de consumidor). Pregunta de pertenencia al catálogo (solo anotada). No se descargaron sus binarios.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v6.1.18 (2026-11-08) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/miuuyy/codex-chatgpt-web/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa la sesión y los límites de ChatGPT; el proyecto no garantiza consumo ilimitado ni exención de las condiciones del servicio |
| Claude Code | Integración no documentada |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Es automatización de navegador no oficial y sin respaldo de OpenAI; las versiones publicadas no están firmadas y los cambios de UI pueden romper la integración |
| Coste | Consumo del agente que ya utilizas. Usa la sesión y los límites de ChatGPT; el proyecto no garantiza consumo ilimitado ni exención de las condiciones del servicio |
| Equipo | Preparación según la ruta elegida. Cuenta propia ChatGPT; Codex; aplicación para tu sistema; equipo de confianza |

Es automatización de navegador no oficial y sin respaldo de OpenAI; las versiones publicadas no están firmadas y los cambios de UI pueden romper la integración

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cuenta propia ChatGPT
- Codex
- aplicación para tu sistema
- equipo de confianza

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/miuuyy/codex-chatgpt-web/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar codex-chatgpt-web para mi objetivo y necesito pasos guiados. Lee https://github.com/miuuyy/codex-chatgpt-web/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee el modelo de seguridad y usa una tarea sin datos sensibles antes de activar full harness.

**Qué comprobar:** Puedes identificar sesión web, modelo elegido y permisos expuestos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar un adaptador de navegador para Codex
- Comparar transporte web con acceso oficial

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar un adaptador de navegador para Codex; Comparar transporte web con acceso oficial | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es automatización de navegador no oficial y sin respaldo de OpenAI; las versiones publicadas no están firmadas y los cambios de UI pueden romper la integración

## Stack y modelos

- **Stack:** Cuenta propia ChatGPT; Codex; aplicación para tu sistema; equipo de confianza
- **Etiquetas:** `infra` `chatgpt` `chatgpt-pro` `codex` `free-ai` `mcp` `openai` `playwright`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/miuuyy/codex-chatgpt-web/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
