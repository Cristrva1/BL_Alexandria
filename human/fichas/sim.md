[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Builders visuales y plataformas de agentes

# 🧩 Sim

> Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 30.1k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Cloud y servicios adicionales tienen planes; self-hosting añade infraestructura; las llamadas a modelos se presupuestan según ruta |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. MCP HTTP permite operar workflows desde clientes; inicia sesión y distingue ese acceso de las credenciales del modelo |
| Coste | El coste depende del proveedor o la ruta. Cloud y servicios adicionales tienen planes; self-hosting añade infraestructura; las llamadas a modelos se presupuestan según ruta |
| Equipo | Preparación según la ruta elegida. Node.js 20+; Docker; proveedor o modelo local |

MCP HTTP permite operar workflows desde clientes; inicia sesión y distingue ese acceso de las credenciales del modelo

## Qué puedes hacer con él

Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual.

## Por qué destaca

Usos propuestos: Automatizar una clasificación de mensajes; Probar un flujo con Ollama antes de usar una API.

## Cómo funciona

MCP HTTP permite operar workflows desde clientes; inicia sesión y distingue ese acceso de las credenciales del modelo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js 20+
- Docker
- proveedor o modelo local

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx sim-setup
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/simstudioai/sim/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Sim para mi objetivo y necesito pasos guiados. Lee https://github.com/simstudioai/sim/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Construye un flujo visual que recibe texto, lo resume y registra la salida.

**Qué comprobar:** La ejecución muestra cada bloque y el resumen final.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Automatizar una clasificación de mensajes
- Probar un flujo con Ollama antes de usar una API

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Automatizar una clasificación de mensajes; Probar un flujo con Ollama antes de usar una API | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP HTTP permite operar workflows desde clientes; inicia sesión y distingue ese acceso de las credenciales del modelo

## Stack y modelos

- **Stack:** Node.js 20+; Docker; proveedor o modelo local
- **Etiquetas:** `agents` `automation` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langflow](langflow.md) | 157k | Constructor visual de flujos LLM/agentes construido sobre LangChain. |
| [dify](dify.md) | 161k | Plataforma integral para construir apps de IA con backend y UI listos. |
| [AutoGPT](autogpt.md) | 188k | Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. |

## Enlaces

- 🐙 GitHub: [simstudioai/sim](https://github.com/simstudioai/sim)
- 🌐 Web: <https://www.sim.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/simstudioai/sim/blob/main/README.md)
- [Fuente 2](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
