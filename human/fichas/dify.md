[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Builders visuales y plataformas de agentes

# 🧱 dify

> Plataforma integral para construir apps de IA con backend y UI listos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 161k | Apache-2.0 modificada (condiciones adicionales) | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; varios servicios con Docker Compose

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** Apache-2.0 modificada (condiciones adicionales). Exige licencia comercial para servicio multi-inquilino y prohíbe quitar el logo o el copyright de la interfaz. Fuente: [LICENSE](https://github.com/langgenius/dify/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Plataforma de LangGenius para desarrollar aplicaciones con LLM, con versión cloud y autoalojada. La licencia es la 'Dify Open Source License', basada en Apache 2.0 con condiciones adicionales (GitHub la marca NOASSERTION), así que hay que revisarla antes de ofrecer Dify como servicio multi-inquilino o quitar su marca. Es muy madura y activa (1.19.0, ~161k estrellas).

## ¿Qué hace?

Combina en una interfaz visual workflows de IA, pipeline de RAG, agentes con sandbox propio que ejecutan comandos y gestionan archivos, gestión de modelos, Prompt IDE, LLMOps y Backend-as-a-Service (API para integrar las apps). Integra observabilidad con Opik, Langfuse y Arize Phoenix. Puede publicar sus aplicaciones como servidores MCP para Claude Desktop, Cursor y otras herramientas.

## ¿Cómo lo hace?

Se despliega con Docker Compose (v2.35.0+) desde `docker/` tras copiar `.env.example` y generar secretos con OpenSSL. Requisitos mínimos: 2 núcleos y 4 GiB de RAM. Incluye base de datos, Redis y un almacén vectorial configurable (la documentación de autoalojamiento incluye guías para Weaviate). Admite proveedores comerciales y locales (Ollama entre ellos) como plugins de modelo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [langfuse](langfuse.md) | Trazas y evaluación de las apps de Dify (integración oficial documentada por Dify). | Despliega Langfuse y configura sus claves en la sección de monitorización de la app. |
| [Ollama](ollama.md) | Modelos locales para despliegues autoalojados, citados en la documentación del nodo LLM. | Instala Ollama y descarga los modelos; añade después el proveedor en Dify. |
| [Claude Code](claude-code.md) | Consumir apps de Dify publicadas como servidor MCP desde un agente de programación (la documentación de Dify cita Claude Desktop y Cursor). (combinación por arquitectura para Claude Code) | Publica la app como MCP en Dify y registra la URL en el cliente. |
| [evolution-api](evolution-api.md) | Combinación recíproca: evolution-api lo enlaza como «Integración nativa para responder con agentes o RAG construidos en Dify». | Orden indicado desde evolution-api: Dify primero, con su app publicada; luego conéctala a la instancia. |
| [PaddleOCR](paddleocr.md) | Combinación recíproca: PaddleOCR lo enlaza como «El README cita Dify entre los proyectos que lo integran». | Orden indicado desde PaddleOCR: Úsalo como servicio externo de OCR o herramienta dentro de los flujos. |
| [TEN Framework](ten-framework.md) | Combinación recíproca: TEN Framework lo enlaza como «TEN incluye una extensión que conecta el agente de voz con aplicaciones de Dify». | Orden indicado desde TEN Framework: Crea la app en Dify; después configura la extensión de Dify en el grafo de TEN con su clave. |

**Notas:** Alternativas (elige una): sim, ragflow. Combinación anterior con langflow eliminada: son plataformas solapadas sin integración documentada. Licencia con condiciones adicionales sobre Apache 2.0.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 1.19.0 (2026-11-04) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/langgenius/dify/blob/main/README.md) · [2](https://docs.dify.ai/en/self-host/use-dify/monitor/integrations/integrate-langfuse.md) · [3](https://docs.dify.ai/en/self-host/use-dify/nodes/llm.md) · [4](https://docs.dify.ai/en/self-host/use-dify/publish/publish-mcp.md) · [5](https://www.comet.com/docs/opik/integrations/dify)</sub>

## Ver similares

Grupo **Builders visuales de agentes**: dify ocupa la posición 2 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [langflow](langflow.md) ⭐ recomendado | 70 | Si quieres diseñar flujos de LangChain visualmente y exportarlos. |
| 2 | **dify** (esta ficha) | 70 | Si quieres construir apps de LLM y RAG con interfaz visual y despliegue completo. |
| 3 | [AutoGPT](autogpt.md) | 70 | Si quieres una plataforma de agentes continuos con marketplace de bloques. |
| 4 | [Sim](sim.md) | 62 | Si quieres un lienzo colaborativo para agentes y workflows con monitorización. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Dify Cloud tiene planes y cupos; self-hosting paga infraestructura y modelos; su licencia añade condiciones a Apache-2.0 |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Genera y guarda el token de sandbox antes de arrancar; un modelo Ollama local necesita una dirección accesible desde Docker |
| Coste | El coste depende del proveedor o la ruta. Dify Cloud tiene planes y cupos; self-hosting paga infraestructura y modelos; su licencia añade condiciones a Apache-2.0 |
| Equipo | Preparación según la ruta elegida. Docker y Compose >=2.35; OpenSSL; 2 CPU y 4 GiB mínimos del servidor |

Genera y guarda el token de sandbox antes de arrancar; un modelo Ollama local necesita una dirección accesible desde Docker

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker y Compose >=2.35
- OpenSSL
- 2 CPU y 4 GiB mínimos del servidor

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker compose up -d
```

Comando copiado literalmente de el README (sección «Quick start»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/langgenius/dify/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dify para mi objetivo y necesito pasos guiados. Lee https://github.com/langgenius/dify/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una app de preguntas sobre un documento ficticio tras configurar el proveedor y los embeddings.

**Qué comprobar:** La respuesta recupera un fragmento comprobable del documento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un asistente sobre políticas
- Diseñar un workflow visual de clasificación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un asistente sobre políticas; Diseñar un workflow visual de clasificación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Genera y guarda el token de sandbox antes de arrancar; un modelo Ollama local necesita una dirección accesible desde Docker

## Stack y modelos

- **Stack:** Docker y Compose >=2.35; OpenSSL; 2 CPU y 4 GiB mínimos del servidor
- **Etiquetas:** `automation` `agents` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Sim](sim.md) | 30.1k | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. |
| [RAGFlow](ragflow.md) | 94.2k | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. |

## Enlaces

- 🐙 GitHub: [langgenius/dify](https://github.com/langgenius/dify)
- 🌐 Web: <https://dify.ai>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langgenius/dify/blob/main/README.md)
- [Fuente 2](https://marketplace.dify.ai/plugin/langgenius/ollama)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
