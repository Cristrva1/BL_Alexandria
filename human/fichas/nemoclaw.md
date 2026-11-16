[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🛠️ NemoClaw

> Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23k | Apache-2.0 | TypeScript | 2026-08-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Puntuación de calidad** 69/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

NVIDIA NemoClaw, stack de referencia open source para ejecutar agentes con más seguridad dentro de sandboxes NVIDIA OpenShell. Licencia Apache-2.0. Tiene ~23k estrellas y está activo.

## ¿Qué hace?

Ofrece onboarding guiado, inferencia gestionada, políticas de red, integraciones gestionadas, persistencia de estado y operaciones de ciclo de vida mediante la CLI NemoClaw. Los agentes soportados son OpenClaw (por defecto), Hermes y LangChain Deep Agents Code.

## ¿Cómo lo hace?

Tiene instalador y un prompt de inicio para que un agente de programación (Cursor, Claude Code, Codex…) lo instale contigo con aprobación de cada comando. Depende de OpenShell.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenClaw](openclaw.md) | Agente por defecto. | Instala NemoClaw y elige OpenClaw. |
| [hermes-agent](hermes-agent.md) | Agente soportado. | Elige Hermes en el onboarding. |
| [Deep Agents](deepagents.md) | Deep Agents Code soportado. | Elige Deep Agents Code. |
| [Nemotron (NVIDIA)](nemotron.md) | Modelos de NVIDIA para la inferencia gestionada. (combinación por arquitectura) | Configura la inferencia. |

**Notas:** Alternativas (elige una): sandbox.

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NVIDIA/NemoClaw/blob/main/README.md) · [2](https://docs.nvidia.com/nemoclaw/latest/)</sub>

## Ver similares

Grupo **Sandboxes para agentes**: NemoClaw ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **NemoClaw** (esta ficha) ⭐ recomendado | 69 | Si buscas esto: stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes. |
| 2 | [E2B](e2b.md) | 65 | Si buscas esto: sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. |
| 3 | [sandbox](sandbox.md) | 52 | Si buscas esto: entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Infraestructura e inferencia gestionada tienen requisitos y costes propios; no incluye acceso universal gratuito |
| Claude Code | Referencia para la herramienta; no es una integración |
| Codex | Referencia para la herramienta; no es una integración |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El prompt para que Claude Code o Codex ayude a instalar es una guía de instalación asistida y no una integración runtime de sus planes |
| Coste | El coste depende del proveedor o la ruta. Infraestructura e inferencia gestionada tienen requisitos y costes propios; no incluye acceso universal gratuito |
| Equipo | Preparación según la ruta elegida. Plataforma compatible según prerequisites; OpenShell; agente y proveedor |

El prompt para que Claude Code o Codex ayude a instalar es una guía de instalación asistida y no una integración runtime de sus planes

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Plataforma compatible según prerequisites
- OpenShell
- agente y proveedor

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/get-started/quickstart)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar NemoClaw para mi objetivo y necesito pasos guiados. Lee https://docs.nvidia.com/nemoclaw/latest/user-guide/openclaw/get-started/quickstart. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee los requisitos y prueba la política con una tarea de consulta en un entorno descartable.

**Qué comprobar:** Puedes identificar los permisos de archivos, red e inferencia configurados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar aislamiento para OpenClaw
- Comparar políticas de ejecución de agentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar aislamiento para OpenClaw; Comparar políticas de ejecución de agentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El prompt para que Claude Code o Codex ayude a instalar es una guía de instalación asistida y no una integración runtime de sus planes

## Stack y modelos

- **Stack:** Plataforma compatible según prerequisites; OpenShell; agente y proveedor
- **Etiquetas:** `agents` `security` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [sandbox](sandbox.md) | 6.3k | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. |

## Enlaces

- 🐙 GitHub: [NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)
- 🌐 Web: <https://docs.nvidia.com/nemoclaw/latest/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NVIDIA/NemoClaw/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
