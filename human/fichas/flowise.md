[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Builders visuales y plataformas de agentes

# 🌊 Flowise

> Constructor visual para diseñar aplicaciones de IA conectando modelos, herramientas, memoria y fuentes de datos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 55.6k | NOASSERTION | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

> ⚠️ Archivado en GitHub: ya no recibe cambios.

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Ollama local usa tu equipo; Ollama Cloud y otros proveedores usan credenciales y tarifas propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Comprueba el puerto real de Ollama y la red de Docker; la guía conserva ejemplos con puertos distintos |
| Coste | El coste depende del proveedor o la ruta. Ollama local usa tu equipo; Ollama Cloud y otros proveedores usan credenciales y tarifas propias |
| Equipo | Preparación según la ruta elegida. Node.js >=20; proveedor o instancia Ollama |

Comprueba el puerto real de Ollama y la red de Docker; la guía conserva ejemplos con puertos distintos

## Qué puedes hacer con él

Constructor visual para diseñar aplicaciones de IA conectando modelos, herramientas, memoria y fuentes de datos.

## Por qué destaca

Usos propuestos: Prototipar un chatbot sobre documentos; Comparar modelos en un flujo visual.

## Cómo funciona

Comprueba el puerto real de Ollama y la red de Docker; la guía conserva ejemplos con puertos distintos

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js >=20
- proveedor o instancia Ollama

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm install -g flowise

npx flowise start
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/FlowiseAI/Flowise/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Flowise para mi objetivo y necesito pasos guiados. Lee https://github.com/FlowiseAI/Flowise/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta un nodo ChatOllama a un flujo de conversación y formula dos preguntas relacionadas.

**Qué comprobar:** El flujo devuelve respuestas usando el modelo configurado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar un chatbot sobre documentos
- Comparar modelos en un flujo visual

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar un chatbot sobre documentos; Comparar modelos en un flujo visual | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Comprueba el puerto real de Ollama y la red de Docker; la guía conserva ejemplos con puertos distintos

## Stack y modelos

- **Stack:** Node.js >=20; proveedor o instancia Ollama
- **Etiquetas:** `automation` `agents` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [dify](dify.md) | 161k | Plataforma integral para construir apps de IA con backend y UI listos. |
| [langflow](langflow.md) | 157k | Constructor visual de flujos LLM/agentes construido sobre LangChain. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Sim](sim.md) | 30.1k | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. |
| [AutoGPT](autogpt.md) | 188k | Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. |

## Enlaces

- 🐙 GitHub: [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)
- 🌐 Web: <https://flowiseai.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/FlowiseAI/Flowise/blob/main/README.md)
- [Fuente 2](https://docs.flowiseai.com/integrations/langchain/chat-models/chatollama)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
