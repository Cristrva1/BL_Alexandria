[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes para issues y tareas de ingeniería

# 🖥️ mini-swe-agent

> Agente de ingeniería de software mínimo (unas 100 líneas) del equipo de SWE-bench y SWE-agent: solo usa bash y rinde alto en SWE-bench.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.6k | MIT | Python | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 52/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Agente de código abierto (MIT) de los autores de SWE-bench y SWE-agent (Princeton y Stanford), que lo presentan como sucesor del SWE-agent original. Activo.

## ¿Qué hace?

Resuelve tareas de ingeniería en repositorios con un agente deliberadamente simple que solo usa bash, sin interfaz de llamadas a herramientas, con historial lineal fácil de depurar y despliegue en entornos locales o aislados; incluye scripts para SWE-bench.

## ¿Cómo lo hace?

Paquete Python; se ejecuta con `uvx mini-swe-agent` o pip. Usa LiteLLM para los modelos y admite entornos local, Docker/Podman, Singularity/Apptainer, bubblewrap y otros.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | mini-swe-agent llama a los modelos a través de su clase de modelo basada en LiteLLM. | Configura las claves o el endpoint en LiteLLM; después selecciona el modelo en mini-swe-agent. |
| [Ollama](ollama.md) | Mediante LiteLLM, mini-swe-agent puede usar modelos locales servidos por Ollama (combinación por arquitectura). | Ollama con un modelo de código; después configúralo como modelo LiteLLM. |
| [vLLM](vllm.md) | Un modelo servido con vLLM puede alimentar mini-swe-agent a través de LiteLLM (combinación por arquitectura). | Lanza vLLM; después apunta LiteLLM a su endpoint. |

**Notas:** Alternativas (elige una): openhands. Ejecuta el agente en un contenedor para aislar los comandos.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada v2.4.6 (2026-07-23) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/SWE-agent/mini-swe-agent/blob/main/README.md) · [2](https://mini-swe-agent.com/)</sub>

## Ver similares

Grupo **Agentes que resuelven issues de software**: mini-swe-agent ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OpenHands](openhands.md) ⭐ recomendado | 74 | Si buscas esto: agent Canvas: centro de sesiones autoalojado para OpenHands, Claude Code, Codex y agentes ACP. |
| 2 | [Open SWE](open-swe.md) | 61 | Si buscas esto: robin, fábrica de cambios sobre Deep Agents que despliega con Managed Deep Agents y entrega propuestas revisables. |
| 3 | **mini-swe-agent** (esta ficha) | 52 | Si buscas esto: agente de ingeniería de software mínimo (unas 100 líneas) del equipo de SWE-bench y SWE-agent: solo usa bash y rinde alto en SWE-bench. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. |
| Equipo | Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (consulta la sintaxis original):**

```
pip install uv && uvx mini-swe-agent
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/SWE-agent/mini-swe-agent/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mini-swe-agent para mi objetivo y necesito pasos guiados. Lee https://github.com/SWE-agent/mini-swe-agent/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta `pip install uv && uvx mini-swe-agent` con una clave de modelo y pídele una tarea pequeña en un repositorio de prueba..

**Qué comprobar:** El agente ejecuta comandos bash y propone el cambio..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- resolver issues de un repositorio de forma autónoma en un contenedor
- usar un agente simple como base para investigación o benchmarks

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: resolver issues de un repositorio de forma autónoma en un contenedor; usar un agente simple como base para investigación o benchmarks | necesitas una herramienta estable y auditada para datos sensibles |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `coding` `agent` `python` `research`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenHands](openhands.md) | 93.5k | Agent Canvas: centro de sesiones autoalojado para OpenHands, Claude Code, Codex y agentes ACP. |

## Enlaces

- 🐙 GitHub: [SWE-agent/mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent)
- 🌐 Web: <https://mini-swe-agent.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/SWE-agent/mini-swe-agent/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
