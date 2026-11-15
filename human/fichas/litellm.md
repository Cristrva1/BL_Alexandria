[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Serving y gateways de LLM

# 🔀 litellm

> Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 63.3k | NOASSERTION | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Las llamadas siguen usando claves, cuotas y precios de cada proveedor; Ollama y LM Studio permiten rutas locales |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Documenta harnesses de Claude Code y Codex en el SDK; pasar por el gateway no incorpora suscripciones ni elimina diferencias entre protocolos |
| Coste | El coste depende del proveedor o la ruta. Las llamadas siguen usando claves, cuotas y precios de cada proveedor; Ollama y LM Studio permiten rutas locales |
| Equipo | Preparación según la ruta elegida. Python y uv; proveedor o endpoint local; presupuesto de prueba |

Documenta harnesses de Claude Code y Codex en el SDK; pasar por el gateway no incorpora suscripciones ni elimina diferencias entre protocolos

## Qué puedes hacer con él

Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI.

## Por qué destaca

Usos propuestos: Unificar llamadas a varios modelos; Enrutar un agente por un gateway propio.

## Cómo funciona

Documenta harnesses de Claude Code y Codex en el SDK; pasar por el gateway no incorpora suscripciones ni elimina diferencias entre protocolos

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- proveedor o endpoint local
- presupuesto de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
uv add litellm
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/BerriAI/litellm/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar litellm para mi objetivo y necesito pasos guiados. Lee https://github.com/BerriAI/litellm/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un único proveedor y envía una petición breve antes de activar fallback y balanceo.

**Qué comprobar:** Puedes identificar el proveedor real y su consumo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Unificar llamadas a varios modelos
- Enrutar un agente por un gateway propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Unificar llamadas a varios modelos; Enrutar un agente por un gateway propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta harnesses de Claude Code y Codex en el SDK; pasar por el gateway no incorpora suscripciones ni elimina diferencias entre protocolos

## Stack y modelos

- **Stack:** Python y uv; proveedor o endpoint local; presupuesto de prueba
- **Etiquetas:** `inference` `llmops` `python` `docker`
- **Modo de instalación sugerido:** 📦 **Dependencia del proyecto** — instálalo dentro de cada proyecto que lo use

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |
| [llm-council](llm-council.md) | 26.5k | "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. |

## Enlaces

- 🐙 GitHub: [BerriAI/litellm](https://github.com/BerriAI/litellm)
- 🌐 Web: <https://docs.litellm.ai/docs/>
- 🧪 Receta: [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md)
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)
- 🧪 Receta: [Agente de voz en tiempo real](../playbooks/agente-de-voz.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/BerriAI/litellm/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
