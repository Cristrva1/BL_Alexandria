[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › RAG y motores de conocimiento

# 📎 LightRAG

> RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.7k | MIT | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Indexar y responder pueden llamar varios modelos; admite configuración Ollama; el coste depende de roles, corpus y proveedor |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Configura HOST o autenticación antes de arrancar en red; conserva el mismo modelo de embeddings entre indexación y consulta |
| Coste | El coste depende del proveedor o la ruta. Indexar y responder pueden llamar varios modelos; admite configuración Ollama; el coste depende de roles, corpus y proveedor |
| Equipo | Preparación según la ruta elegida. Python y uv; LLM; embeddings; almacenamiento; configuración .env |

Configura HOST o autenticación antes de arrancar en red; conserva el mismo modelo de embeddings entre indexación y consulta

## Qué puedes hacer con él

RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong.

## Por qué destaca

Usos propuestos: Consultar relaciones entre conceptos; Combinar búsqueda de grafos y vectores.

## Cómo funciona

Configura HOST o autenticación antes de arrancar en red; conserva el mismo modelo de embeddings entre indexación y consulta

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv
- LLM
- embeddings
- almacenamiento
- configuración .env

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Install LightRAG Server as a tool using uv (recommended)
uv tool install "lightrag-hku[api]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/HKUDS/LightRAG/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LightRAG para mi objetivo y necesito pasos guiados. Lee https://github.com/HKUDS/LightRAG/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Indexa un documento ficticio y compara una consulta sobre una entidad con otra sobre sus relaciones.

**Qué comprobar:** Puedes inspeccionar los resultados y las relaciones recuperadas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar relaciones entre conceptos
- Combinar búsqueda de grafos y vectores

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar relaciones entre conceptos; Combinar búsqueda de grafos y vectores | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Configura HOST o autenticación antes de arrancar en red; conserva el mismo modelo de embeddings entre indexación y consulta

## Stack y modelos

- **Stack:** Python y uv; LLM; embeddings; almacenamiento; configuración .env
- **Etiquetas:** `rag` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [Qdrant](qdrant.md) | 35.6k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [graphrag](graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |
| [RAGFlow](ragflow.md) | 94.2k | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. |
| [PageIndex](pageindex.md) | 40.4k | Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos. |

## Enlaces

- 🐙 GitHub: [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)
- 🌐 Web: <https://arxiv.org/abs/2410.05779>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/HKUDS/LightRAG/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
