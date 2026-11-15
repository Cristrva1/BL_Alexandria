[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 👥 crewAI

> Framework para orquestar "crews" de agentes con roles y tareas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 60.9k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Las skills consumen tu agente; la crew utiliza su propio proveedor; AMP y servicios externos pueden costar aparte |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Compatibilidad por confirmar |
| Modelos locales | Modelos locales documentados. Claude Code y Codex tienen skills documentadas; Antigravity sigue sin confirmar para esta integración |
| Coste | El coste depende del proveedor o la ruta. Las skills consumen tu agente; la crew utiliza su propio proveedor; AMP y servicios externos pueden costar aparte |
| Equipo | Preparación según la ruta elegida. Python >=3.10 y <3.14; uv; proveedor o Ollama/LM Studio |

Claude Code y Codex tienen skills documentadas; Antigravity sigue sin confirmar para esta integración

## Qué puedes hacer con él

Framework para orquestar "crews" de agentes con roles y tareas.

## Por qué destaca

Usos propuestos: Preparar investigación de mercado; Separar investigación y redacción de producto.

## Cómo funciona

Claude Code y Codex tienen skills documentadas; Antigravity sigue sin confirmar para esta integración

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python >=3.10 y <3.14
- uv
- proveedor o Ollama/LM Studio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
uv tool install crewai
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/crewAIInc/crewAI/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar crewAI para mi objetivo y necesito pasos guiados. Lee https://github.com/crewAIInc/crewAI/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una crew que investiga y luego redacta una comparación de dos productos.

**Qué comprobar:** Puedes revisar la salida y las fuentes de cada tarea.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar investigación de mercado
- Separar investigación y redacción de producto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar investigación de mercado; Separar investigación y redacción de producto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Claude Code y Codex tienen skills documentadas; Antigravity sigue sin confirmar para esta integración

## Stack y modelos

- **Stack:** Python >=3.10 y <3.14; uv; proveedor o Ollama/LM Studio
- **Etiquetas:** `automation` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [mem0](mem0.md) | 69k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AutoGen](autogen.md) | 61.8k | Framework de Microsoft para conversaciones entre agentes, hoy en modo mantenimiento. |
| [LangGraph](langgraph.md) | 45k | Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. |
| [Agno](agno.md) | 43.2k | Framework y runtime de agentes en Python con memoria, conocimiento y equipos multiagente. |
| [MetaGPT](metagpt.md) | 71.3k | Framework de agentes que representa roles de un equipo de software para coordinar tareas de desarrollo. |

## Enlaces

- 🐙 GitHub: [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
- 🌐 Web: <https://crewai.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/crewAIInc/crewAI/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
