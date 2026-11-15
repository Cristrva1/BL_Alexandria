[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 LobeHub

> Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 85.5k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El workspace, servicios alojados y modelos tienen condiciones separadas; admite proveedores locales |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Las skills portables y conectar un agente externo son funciones distintas; la página de integración consultada aún está en migración documental |
| Coste | El coste depende del proveedor o la ruta. El workspace, servicios alojados y modelos tienen condiciones separadas; admite proveedores locales |
| Equipo | Preparación según la ruta elegida. Docker y Compose; modelo; servicios de la ruta elegida |

Las skills portables y conectar un agente externo son funciones distintas; la página de integración consultada aún está en migración documental

## Qué puedes hacer con él

Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible.

## Por qué destaca

Usos propuestos: Organizar agentes para tareas de equipo; Conectar un agente de código a un espacio de trabajo.

## Cómo funciona

Las skills portables y conectar un agente externo son funciones distintas; la página de integración consultada aún está en migración documental

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker y Compose
- modelo
- servicios de la ruta elegida

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
mkdir lobehub && cd lobehub
bash <(curl -fsSL https://lobe.li/setup.sh) -l en
docker compose up -d
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/lobehub/lobehub/blob/canary/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LobeHub para mi objetivo y necesito pasos guiados. Lee https://github.com/lobehub/lobehub/blob/canary/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un asistente de prueba y distingue su modelo del agente externo que puedas conectar.

**Qué comprobar:** Puedes identificar qué proveedor atiende cada conversación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar agentes para tareas de equipo
- Conectar un agente de código a un espacio de trabajo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar agentes para tareas de equipo; Conectar un agente de código a un espacio de trabajo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las skills portables y conectar un agente externo son funciones distintas; la página de integración consultada aún está en migración documental

## Stack y modelos

- **Stack:** Docker y Compose; modelo; servicios de la ruta elegida
- **Etiquetas:** `chatbot` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open WebUI](open-webui.md) | 159k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |
| [LibreChat](librechat.md) | 47.1k | Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada. |
| [Cherry Studio](cherry-studio.md) | 53.5k | App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad. |

## Enlaces

- 🐙 GitHub: [lobehub/lobehub](https://github.com/lobehub/lobehub)
- 🌐 Web: <https://lobehub.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/lobehub/lobehub/blob/canary/README.md)
- [Fuente 2](https://lobehub.com/docs/usage/agent/connect-external-agents)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
