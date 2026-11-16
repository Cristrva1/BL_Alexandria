[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🖥️ OpenManus

> Agente general de código abierto inspirado en Manus: planifica tareas y usa navegador, Python y archivos mediante herramientas y MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 59k | MIT | Python | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere clave de API

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Implementación abierta (MIT) de un agente general al estilo Manus, creada por miembros de MetaGPT y la comunidad FoundationAgents. Los autores la describen como una implementación sencilla; ritmo de cambios alto y sin versiones estables marcadas.

## ¿Qué hace?

Recibe una instrucción en lenguaje natural y la resuelve en varios pasos: navega con Browser Use, ejecuta código Python, edita archivos y puede trabajar con flujos de varios agentes. Sirve para experimentar con agentes autónomos de propósito general.

## ¿Cómo lo hace?

Se instala clonando el repositorio y creando un entorno con conda o uv (`uv venv --python 3.12` y `uv pip install -r requirements.txt`); la configuración del modelo se copia de `config/config.example.toml`. Inicia Browser Use CLI como servidor MCP por defecto; BrowserGym requiere navegadores de Playwright.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [browser-use](browser-use.md) | OpenManus arranca Browser Use CLI como servidor MCP por defecto para sus acciones de navegador. | Prepara uv y ejecuta `uvx browser-use install`; después lanza OpenManus. |
| [playwright](playwright.md) | Algunas rutas (BrowserGym) requieren los navegadores de Playwright instalados. | Instala los navegadores de Playwright; después ejecuta las tareas que los usan. |
| [litellm](litellm.md) | OpenManus usa una API compatible con OpenAI configurable: un proxy LiteLLM permite apuntar a otros proveedores o a modelos locales (combinación por arquitectura). | LiteLLM en marcha; después pon su base_url en config.toml. |

**Notas:** El agente ejecuta código y navega por sí mismo: úsalo en un entorno aislado y con datos de prueba.

Estado en GitHub: activo · último push 2026-11-02 · última versión publicada v0.3.0 (2025-04-10) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/FoundationAgents/OpenManus/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Consumo de APIs o servicios. Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/FoundationAgents/OpenManus/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenManus para mi objetivo y necesito pasos guiados. Lee https://github.com/FoundationAgents/OpenManus/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea el entorno con uv según el README, configura la clave del modelo en config.toml y lanza una tarea pequeña de búsqueda..

**Qué comprobar:** El agente completa los pasos visibles en consola y deja el resultado en el espacio de trabajo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- delegar una investigación web que termine en un informe guardado en disco
- experimentar con un agente general en local antes de elegir un framework

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: delegar una investigación web que termine en un informe guardado en disco; experimentar con un agente general en local antes de elegir un framework | necesitas una herramienta estable y auditada para datos sensibles |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, Dockerfile, requirements.txt, setup.py
- **Etiquetas:** `agents` `python` `browser`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [FoundationAgents/OpenManus](https://github.com/FoundationAgents/OpenManus)
- 🌐 Web: <https://openmanus.github.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/FoundationAgents/OpenManus/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
