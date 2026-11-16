[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 n8n

> Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 211k | NOASSERTION | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Plataforma de automatización de flujos de trabajo y agentes de IA con código disponible bajo licencia fair-code (Sustainable Use License). Se puede autoalojar o usar en n8n Cloud.

## ¿Qué hace?

Conecta más de 1500 integraciones (APIs, bases de datos y apps SaaS) en flujos que se disparan por eventos, horarios o webhooks. Incluye nodos de IA para crear agentes de varios pasos con herramientas, aprobaciones humanas y modelos de OpenAI, Anthropic, Google o modelos abiertos, y ofrece más de 9000 plantillas.

## ¿Cómo lo hace?

Es una aplicación TypeScript/Node.js con un editor visual de nodos en el navegador (puerto 5678); cada nodo recibe datos JSON, los transforma y los pasa al siguiente. Cuando lo visual no alcanza, admite nodos de código en JavaScript o Python y paquetes npm. Se instala normalmente con Docker y un volumen persistente (`n8n_data`); sus nodos de IA forman la familia `n8n-nodes-langchain`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [n8n-mcp](n8n-mcp.md) | Permite que Claude Code, Cursor u otro cliente MCP lea ejecuciones fallidas, valide, pruebe y edite flujos de n8n mediante su API pública. | Primero n8n en marcha con la Public API activada y una API key; después n8n-mcp. Prueba en una copia: n8n-mcp reescribe el flujo completo y pisa cambios hechos a la vez en la interfaz. |
| [n8n-skills](n8n-skills.md) | Skills de Claude Code que enseñan sintaxis de expresiones, patrones de flujo y uso correcto de las herramientas de n8n-mcp. | Tercera pieza: se aprovecha cuando n8n-mcp ya está conectado. |
| [evolution-api](evolution-api.md) | Añade el canal de WhatsApp: Evolution API envía eventos a un webhook de n8n y n8n responde llamando a su API REST; Evolution lista n8n entre sus integraciones de chatbot. | Servicios independientes. Levanta ambos y apunta el webhook de la instancia de Evolution a una URL de webhook de n8n. |
| [Ollama](ollama.md) | Los nodos de IA de n8n pueden usar modelos locales servidos por Ollama (credencial documentada por n8n), sin pagar una API remota. | Ollama primero. Si n8n corre en Docker, `localhost` apunta al contenedor: usa la dirección del host para llegar al puerto 11434. |
| [Qdrant](qdrant.md) | n8n incluye el nodo Qdrant Vector Store para guardar y consultar embeddings dentro de un flujo (RAG). | Qdrant primero (puerto 6333) y luego la credencial en n8n. Qdrant arranca sin autenticación: no lo expongas a internet. |

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/n8n-io/n8n/blob/master/README.md) · [2](https://docs.n8n.io/integrations/builtin/credentials/ollama/) · [3](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreqdrant/) · [4](https://github.com/evolution-foundation/evolution-api/blob/main/README.md) · [5](https://github.com/czlonkowski/n8n-mcp/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Autoalojar consume equipo o servidor; n8n Cloud y las APIs conectadas tienen tarifas separadas |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Ollama está documentado por n8n; el agente que diseña el flujo no paga automáticamente sus llamadas de IA |
| Coste | El coste depende del proveedor o la ruta. Autoalojar consume equipo o servidor; n8n Cloud y las APIs conectadas tienen tarifas separadas |
| Equipo | Preparación según la ruta elegida. Docker activo;  una carpeta para datos de prueba |

Ollama está documentado por n8n; el agente que diseña el flujo no paga automáticamente sus llamadas de IA

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker activo
-  una carpeta para datos de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
docker volume create n8n_data
docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/n8n-io/n8n/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar n8n para mi objetivo y necesito pasos guiados. Lee https://github.com/n8n-io/n8n/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un flujo manual que devuelva un texto y ejecútalo en el editor.

**Qué comprobar:** La ejecución termina y su salida contiene el texto que escribiste.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Un formulario de contacto genera un registro para seguimiento comercial
- Un flujo resume documentos con Ollama en lugar de una API remota

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Un formulario de contacto genera un registro para seguimiento comercial; Un flujo resume documentos con Ollama en lugar de una API remota | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ollama está documentado por n8n; el agente que diseña el flujo no paga automáticamente sus llamadas de IA

## Stack y modelos

- **Stack:** Docker activo;  una carpeta para datos de prueba
- **Etiquetas:** `automation` `typescript` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [activepieces](activepieces.md) | 25.5k | Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables. |
| [huginn](huginn.md) | 50.5k | Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú". |
| [Windmill](windmill.md) | 18.6k | Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. |
| [Node-RED](node-red.md) | 23.8k | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. |

## Enlaces

- 🐙 GitHub: [n8n-io/n8n](https://github.com/n8n-io/n8n)
- 🌐 Web: <https://n8n.io>
- 🧪 Receta: [Bot de WhatsApp con IA](../playbooks/bot-de-whatsapp-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/n8n-io/n8n/blob/master/README.md)
- [Fuente 2](https://docs.n8n.io/integrations/builtin/credentials/ollama)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
