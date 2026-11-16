[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🧬 DeepWiki Open

> Generador de wikis con IA para repos de GitHub, GitLab o Bitbucket, versión abierta de DeepWiki.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.4k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

DeepWiki-Open, implementación abierta de DeepWiki que genera wikis con IA de repos de GitHub, GitLab o Bitbucket, de AsyncFuncAI. Licencia MIT. Es popular (~18k estrellas, sin releases); el README anuncia una versión 2.0, «Grok Wiki», como descarga aparte.

## ¿Qué hace?

Analiza la estructura del código, genera documentación, diagramas y un mapa del código para visitas guiadas, y lo organiza como wiki navegable. Admite proveedores Google, OpenAI, OpenRouter, Azure, Bedrock, DashScope y Ollama.

## ¿Cómo lo hace?

Tiene backend en Python (FastAPI y adalflow) y frontend Next.js. Se despliega con Docker Compose (incluida una variante con LiteLLM y otra con Ollama local) o con Helm en Kubernetes, configurando claves de proveedor. Los repos privados requieren un token de acceso.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Configuración y Dockerfile para Ollama local. | Arranca Ollama y usa la configuración local. |
| [litellm](litellm.md) | Variante oficial de Docker Compose con LiteLLM. | Usa `docker-compose-litellm.yml` con tu `litellm-config.yml`. |
| [Mermaid](mermaid.md) | Revisar o editar los diagramas generados. (combinación por arquitectura) | Exporta los diagramas y edítalos con Mermaid. |

**Notas:** Alternativas (elige una): context7. El README actual es muy escueto y remite a Grok Wiki; la relación entre ambos no está clara.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/AsyncFuncAI/deepwiki-open/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La generación usa modelos y embeddings según configuración; Kubernetes y otros despliegues añaden costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Implementación independiente inspirada en DeepWiki, no versión oficial de ese servicio; el ejemplo Helm necesita una infraestructura previa |
| Coste | El coste depende del proveedor o la ruta. La generación usa modelos y embeddings según configuración; Kubernetes y otros despliegues añaden costes |
| Equipo | Preparación según la ruta elegida. Dependencias de la ruta elegida; repositorio de prueba; credenciales de modelos |

Implementación independiente inspirada en DeepWiki, no versión oficial de ese servicio; el ejemplo Helm necesita una infraestructura previa

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Dependencias de la ruta elegida
- repositorio de prueba
- credenciales de modelos

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/AsyncFuncAI/deepwiki-open/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DeepWiki Open para mi objetivo y necesito pasos guiados. Lee https://github.com/AsyncFuncAI/deepwiki-open/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera una wiki de un repositorio pequeño y contrasta una página con sus archivos.

**Qué comprobar:** La explicación enlaza partes del código que puedes abrir.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar documentación inicial de una app
- Crear una guía para incorporarse a un proyecto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar documentación inicial de una app; Crear una guía para incorporarse a un proyecto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Implementación independiente inspirada en DeepWiki, no versión oficial de ese servicio; el ejemplo Helm necesita una infraestructura previa

## Stack y modelos

- **Stack:** Dependencias de la ruta elegida; repositorio de prueba; credenciales de modelos
- **Etiquetas:** `code` `docs` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Context7](context7.md) | 64.8k | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. |

## Enlaces

- 🐙 GitHub: [AsyncFuncAI/deepwiki-open](https://github.com/AsyncFuncAI/deepwiki-open)
- 🌐 Web: <https://grok-wiki.com/>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/AsyncFuncAI/deepwiki-open/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
