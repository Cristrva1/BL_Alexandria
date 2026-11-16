[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🕸️ MetaGPT

> Framework de agentes que representa roles de un equipo de software para coordinar tareas de desarrollo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 71.3k | MIT | Python | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework multiagente open source (MIT) de FoundationAgents (antes geekan/MetaGPT) que asigna roles a LLMs para que colaboren como un equipo. Tiene mucha repercusión (~71k estrellas), pero poca actividad: la última release es la v0.8.1 de abril de 2024 y el último push, de enero de 2026. Sus autores se han centrado en el producto comercial MGX/Atoms y en investigación (AFlow, SPO, AOT).

## ¿Qué hace?

Recibe un requisito de una línea y simula una empresa de software con roles de product manager, arquitecto, project manager e ingeniero. Produce historias de usuario, análisis competitivo, requisitos, estructuras de datos, APIs, documentos y código. Sigue procedimientos operativos estándar (SOPs) codificados como prompts. El repositorio también incluye código de los artículos de investigación del equipo.

## ¿Cómo lo hace?

Python 3.9 a 3.11 (no admite 3.12+), instalable con `pip install --upgrade metagpt`. Requiere Node.js y pnpm para algunas funciones. Se configura con `~/.metagpt/config2.yaml`, donde se define el proveedor de LLM: OpenAI, Azure, Ollama y otros según la documentación. Por la versión antigua de Python y la falta de releases, conviene aislarlo en un entorno propio.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Modelos locales mediante la configuración de LLM documentada por MetaGPT. | Instala Ollama y define api_type ollama en config2.yaml. |
| [E2B](e2b.md) | Ejecutar el código generado en un sandbox aislado en lugar del equipo local. (combinación por arquitectura) | Genera el proyecto con MetaGPT y pruébalo dentro de un sandbox de E2B. |
| [Claude Code](claude-code.md) | Revisar y completar el código que genera MetaGPT, que suele necesitar correcciones. (combinación por arquitectura) | MetaGPT genera el esqueleto; después itera sobre él con un agente de programación. |

**Notas:** Alternativas (elige una): crewai. Mantenimiento bajo: sin releases desde 2024.

Estado en GitHub: activo · último push 2026-01-21 · última versión publicada v0.8.1 (2024-04-22) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/FoundationAgents/MetaGPT/blob/main/README.md) · [2](https://docs.deepwisdom.ai/main/en/guide/get_started/configuration/llm_api_configuration.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Cada rol puede llamar varias veces al modelo; Ollama está en la configuración; APIs y herramientas externas cuestan según uso |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Los artefactos generados no acreditan una aplicación lista ni sustituyen pruebas y revisión |
| Coste | El coste depende del proveedor o la ruta. Cada rol puede llamar varias veces al modelo; Ollama está en la configuración; APIs y herramientas externas cuestan según uso |
| Equipo | Preparación según la ruta elegida. Python según guía estable; proveedor o Ollama; directorio de salida de prueba |

Los artefactos generados no acreditan una aplicación lista ni sustituyen pruebas y revisión

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python según guía estable
- proveedor o Ollama
- directorio de salida de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install --upgrade metagpt
# or `pip install --upgrade git+https://github.com/geekan/MetaGPT.git`
# or `git clone https://github.com/geekan/MetaGPT && cd MetaGPT && pip install --upgrade -e .`
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/FoundationAgents/MetaGPT/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MetaGPT para mi objetivo y necesito pasos guiados. Lee https://github.com/FoundationAgents/MetaGPT/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide el diseño de una lista de tareas mínima y revisa requisitos y estructura antes del código.

**Qué comprobar:** Obtienes artefactos separados que puedes revisar y corregir.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Bocetar requisitos de una app
- Simular roles de un equipo de software

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Bocetar requisitos de una app; Simular roles de un equipo de software | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los artefactos generados no acreditan una aplicación lista ni sustituyen pruebas y revisión

## Stack y modelos

- **Stack:** Python según guía estable; proveedor o Ollama; directorio de salida de prueba
- **Etiquetas:** `py` `agent` `gpt` `llm` `metagpt` `multi-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [crewAI](crewai.md) | 60.9k | Framework para orquestar "crews" de agentes con roles y tareas. |

## Enlaces

- 🐙 GitHub: [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)
- 🌐 Web: <https://atoms.dev/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/FoundationAgents/MetaGPT/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
