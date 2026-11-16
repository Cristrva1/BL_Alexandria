[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 📎 PageIndex

> Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.4k | MIT | Python | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Sistema RAG «sin vectores» basado en razonamiento, de VectifyAI. La versión de código abierto es MIT (v0.7.0) y convive con productos en la nube: PageIndex Cloud, una API de búsqueda de páginas y una app de análisis de documentos.

## ¿Qué hace?

Sustituye el índice vectorial por un índice jerárquico en árbol de cada documento y deja que un LLM razone recorriéndolo, como haría un experto con un informe largo, sin troceado ni base vectorial. Pensado para documentos profesionales largos (financieros, legales, técnicos) donde la similitud semántica no equivale a relevancia. El SDK indexa, recupera y chatea en local con tu clave o en la nube.

## ¿Cómo lo hace?

SDK Python (`pip install -U pageindex`) con modo local y nube; en local usa por defecto «PageIndex Flash» para generar árboles rápido en PDF de texto y llama a un LLM (por ejemplo con `OPENAI_API_KEY`) o a Claude a través de Claude Code usando tu suscripción. Sus herramientas se integran en OpenAI Agents SDK, Claude Agent SDK u otros frameworks. La versión abierta está pensada para PDF con mucho texto.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Puede usar tu suscripción de Claude a través de Claude Code, sin clave de API. | Claude Code con sesión iniciada antes de configurar PageIndex en ese modo. |
| [OpenAI Agents SDK](openai-agents-python.md) | El README documenta añadir las herramientas de PageIndex al OpenAI Agents SDK. | Instala ambos en el mismo entorno Python. |
| [claude-agent-sdk-python](claude-agent-sdk-python.md) | Integración documentada con el Claude Agent SDK. | Igual que arriba. |

**Notas:** Alternativa (elige una): lightrag. Cada consulta implica razonamiento del LLM: más latencia y coste por pregunta que una búsqueda vectorial.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.7.0 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/VectifyAI/PageIndex/blob/main/README.md)</sub>

## Ver similares

Grupo **RAG con grafos e índices de conocimiento**: PageIndex ocupa la posición 3 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [RAGFlow](ragflow.md) ⭐ recomendado | 82 | Si quieres un motor de RAG completo con comprensión profunda de documentos e interfaz. |
| 2 | [LightRAG](lightrag.md) | 66 | Si quieres RAG con grafo de conocimiento ligero y rápido de indexar. |
| 3 | **PageIndex** (esta ficha) | 60 | Si quieres RAG sin vectores que razona sobre la tabla de contenidos de documentos largos. |
| 4 | [graphrag](graphrag.md) | 54 | Si necesitas la metodología GraphRAG de Microsoft para preguntas globales sobre un corpus. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El autor documenta API propia, Cloud y una ruta Claude Code con plan del usuario; revisa límites y condiciones de autenticación de esa ruta |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Sin base vectorial no significa sin modelo ni coste; su adaptador Claude es integración del proyecto y no una aprobación universal de planes |
| Coste | El coste depende del proveedor o la ruta. El autor documenta API propia, Cloud y una ruta Claude Code con plan del usuario; revisa límites y condiciones de autenticación de esa ruta |
| Equipo | Preparación según la ruta elegida. Python; documento de prueba; proveedor para modo local o cuenta Cloud |

Sin base vectorial no significa sin modelo ni coste; su adaptador Claude es integración del proyecto y no una aprobación universal de planes

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- documento de prueba
- proveedor para modo local o cuenta Cloud

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install -U pageindex
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/VectifyAI/PageIndex/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PageIndex para mi objetivo y necesito pasos guiados. Lee https://github.com/VectifyAI/PageIndex/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Indexa un PDF con secciones y pregunta por un dato de una sección concreta.

**Qué comprobar:** La recuperación señala la parte pertinente del documento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar informes largos por su estructura
- Encontrar una sección de un contrato

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar informes largos por su estructura; Encontrar una sección de un contrato | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Sin base vectorial no significa sin modelo ni coste; su adaptador Claude es integración del proyecto y no una aprobación universal de planes

## Stack y modelos

- **Stack:** Python; documento de prueba; proveedor para modo local o cuenta Cloud
- **Etiquetas:** `rag` `docs` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LightRAG](lightrag.md) | 40.7k | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. |

## Enlaces

- 🐙 GitHub: [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)
- 🌐 Web: <https://pageindex.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/VectifyAI/PageIndex/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
