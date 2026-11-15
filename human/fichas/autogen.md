[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 AutoGen

> Framework de Microsoft para conversaciones entre agentes, hoy en modo mantenimiento.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 61.8k | CC-BY-4.0 | Python | 2026-06-24 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El ejemplo usa OpenAI API; Ollama ofrece una ruta local experimental; Studio no incluye modelos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Está en mantenimiento; no mezcles autogen-agentchat con los paquetes de AG2 Classic |
| Coste | El coste depende del proveedor o la ruta. El ejemplo usa OpenAI API; Ollama ofrece una ruta local experimental; Studio no incluye modelos |
| Equipo | Preparación según la ruta elegida. Python 3.10+; entorno virtual; cliente de modelo |

Está en mantenimiento; no mezcles autogen-agentchat con los paquetes de AG2 Classic

## Qué puedes hacer con él

Framework de Microsoft para conversaciones entre agentes, hoy en modo mantenimiento.

## Por qué destaca

Usos propuestos: Revisar un resumen entre dos agentes; Comparar dos soluciones de programación.

## Cómo funciona

Está en mantenimiento; no mezcles autogen-agentchat con los paquetes de AG2 Classic

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10+
- entorno virtual
- cliente de modelo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Install AgentChat and OpenAI client from Extensions
pip install -U "autogen-agentchat" "autogen-ext[openai]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/microsoft/autogen/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AutoGen para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/autogen/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prueba un redactor y un revisor sobre un párrafo breve.

**Qué comprobar:** Distingues ambos mensajes y puedes detener la conversación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar un resumen entre dos agentes
- Comparar dos soluciones de programación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar un resumen entre dos agentes; Comparar dos soluciones de programación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Está en mantenimiento; no mezcles autogen-agentchat con los paquetes de AG2 Classic

## Stack y modelos

- **Stack:** Python 3.10+; entorno virtual; cliente de modelo
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [litellm](litellm.md) | 63.3k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Microsoft Agent Framework](agent-framework.md) | 14.7k | Framework de Microsoft para agentes y workflows multiagente en Python y .NET, sucesor de AutoGen y Semantic Kernel. |
| [ag2](ag2.md) | 5.1k | Framework AG2 actual para agentes y redes de colaboración en Python; AG2 Classic conserva por separado la API heredada autogen. |
| [crewAI](crewai.md) | 60.9k | Framework para orquestar "crews" de agentes con roles y tareas. |

## Enlaces

- 🐙 GitHub: [microsoft/autogen](https://github.com/microsoft/autogen)
- 🌐 Web: <https://microsoft.github.io/autogen/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/autogen/blob/main/README.md)
- [Fuente 2](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/components/model-clients.html)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
