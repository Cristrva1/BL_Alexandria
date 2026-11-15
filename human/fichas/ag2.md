[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🤝 ag2

> Framework AG2 actual para agentes y redes de colaboración en Python; AG2 Classic conserva por separado la API heredada autogen.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.1k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Ofrece extras para OpenAI, Anthropic, Gemini y Ollama; cada proveedor conserva sus costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. AG2 v1 no sustituye directamente Classic: ConversableAgent y GroupChat siguen en ag2-classic con import autogen |
| Coste | El coste depende del proveedor o la ruta. Ofrece extras para OpenAI, Anthropic, Gemini y Ollama; cada proveedor conserva sus costes |
| Equipo | Preparación según la ruta elegida. Python 3.11+; extra del proveedor elegido |

AG2 v1 no sustituye directamente Classic: ConversableAgent y GroupChat siguen en ag2-classic con import autogen

## Qué puedes hacer con él

AG2 v1 utiliza import ag2 y su propia arquitectura de agentes y redes. Los proyectos con ConversableAgent, GroupChat e import autogen deben seguir la distribución ag2-classic y su documentación de migración.

## Por qué destaca

Usos propuestos: Coordinar redactor y verificador; Incluir intervención humana en un equipo.

## Cómo funciona

AG2 v1 no sustituye directamente Classic: ConversableAgent y GroupChat siguen en ag2-classic con import autogen

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.11+
- extra del proveedor elegido

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install ag2[openai]
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ag2ai/ag2/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ag2 para mi objetivo y necesito pasos guiados. Lee https://github.com/ag2ai/ag2/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Haz que un agente resuma una conversación y otro revise las omisiones.

**Qué comprobar:** Se registran los intercambios usando import ag2.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Coordinar redactor y verificador
- Incluir intervención humana en un equipo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Coordinar redactor y verificador; Incluir intervención humana en un equipo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** AG2 v1 no sustituye directamente Classic: ConversableAgent y GroupChat siguen en ag2-classic con import autogen

## Stack y modelos

- **Stack:** Python 3.11+; extra del proveedor elegido
- **Etiquetas:** `automation` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AutoGen](autogen.md) | 61.8k | Framework de Microsoft para conversaciones entre agentes, hoy en modo mantenimiento. |

## Enlaces

- 🐙 GitHub: [ag2ai/ag2](https://github.com/ag2ai/ag2)
- 🌐 Web: <https://ag2.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ag2ai/ag2/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
