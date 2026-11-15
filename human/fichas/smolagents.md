[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🐍 smolagents

> Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.4k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Admite Transformers u Ollama locales y APIs; aislamiento y búsqueda externa pueden costar aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El agente ejecuta código: usa el aislamiento documentado y archivos de prueba |
| Coste | El coste depende del proveedor o la ruta. Admite Transformers u Ollama locales y APIs; aislamiento y búsqueda externa pueden costar aparte |
| Equipo | Preparación según la ruta elegida. Python; modelo; ejecutor aislado |

El agente ejecuta código: usa el aislamiento documentado y archivos de prueba

## Qué puedes hacer con él

Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python.

## Por qué destaca

Usos propuestos: Calcular indicadores de un CSV; Transformar datos consultados en un resumen.

## Cómo funciona

El agente ejecuta código: usa el aislamiento documentado y archivos de prueba

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- modelo
- ejecutor aislado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install "smolagents[toolkit]"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/huggingface/smolagents/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar smolagents para mi objetivo y necesito pasos guiados. Lee https://github.com/huggingface/smolagents/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Calcula el total y promedio de cinco importes ficticios y revisa el código generado.

**Qué comprobar:** Los resultados coinciden con los números de entrada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Calcular indicadores de un CSV
- Transformar datos consultados en un resumen

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Calcular indicadores de un CSV; Transformar datos consultados en un resumen | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El agente ejecuta código: usa el aislamiento documentado y archivos de prueba

## Stack y modelos

- **Stack:** Python; modelo; ejecutor aislado
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [E2B](e2b.md) | 14.9k | Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. |
| [Transformers](transformers.md) | 169k | Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Pydantic AI](pydantic-ai.md) | 21.2k | Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. |
| [OpenAI Agents SDK](openai-agents-python.md) | 30.7k | SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. |

## Enlaces

- 🐙 GitHub: [huggingface/smolagents](https://github.com/huggingface/smolagents)
- 🌐 Web: <https://huggingface.co/docs/smolagents>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/huggingface/smolagents/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
