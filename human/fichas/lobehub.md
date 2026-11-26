[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Interfaces de chat auto-hospedadas

# 💬 LobeHub

> Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 85.5k | LobeHub Community License (Apache-2.0 + condiciones) | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación sencilla; varios servicios con Docker Compose

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** LobeHub Community License (Apache-2.0 + condiciones). Las obras derivadas distribuidas comercialmente requieren licencia. Fuente: [LICENSE](https://github.com/lobehub/lobehub/blob/canary/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Plataforma de agentes de código abierto de LobeHub, antes conocida como Lobe Chat, que se presenta como «superagentes en tu equipo». Su README indica Apache 2.0, aunque GitHub no reconoce la licencia como estándar [DATO NO VERIFICADO: condiciones adicionales en LICENSE]; avisa que está en desarrollo activo (v2.3.3).

## ¿Qué hace?

Añade agentes a los chats que el equipo ya usa; estos asumen trabajo por su cuenta y mejoran con el tiempo. Ofrece un marketplace de agentes, servidores MCP y skills que puedes añadir o publicar, guías para más de 40 proveedores de modelos y modelos locales, y autenticación con Better Auth y SSO.

## ¿Cómo lo hace?

Aplicación full-stack en TypeScript (Next.js con SPA de Vite, Bun en desarrollo). El Docker Compose recomendado levanta LobeHub con PostgreSQL, Redis, almacenamiento RustFS, búsqueda SearXNG y el gateway de agentes, accesible en el puerto 3210; funciona en Linux, macOS o Windows con WSL 2. También se despliega en Vercel con una base PostgreSQL, almacenamiento compatible con S3 y secretos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Ollama está entre los proveedores locales documentados. | Ollama accesible desde el contenedor (no uses localhost dentro de Docker); configura su URL en las variables de entorno. |
| [litellm](litellm.md) | Centralizar claves y gasto de varios proveedores en un proxy compatible con OpenAI (combinación por arquitectura). | LiteLLM primero; apunta el proveedor OpenAI de LobeHub a su URL. |
| [Playwright MCP](playwright-mcp.md) | Servidor MCP de navegador para los agentes (combinación por arquitectura). | Añádelo desde la configuración de MCP y restringe permisos. |

**Notas:** Alternativas (elige una): open-webui, librechat, cherry-studio. SearXNG ya viene en su Compose; no instales otro aparte.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.3.3 (2026-11-12) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/lobehub/lobehub/blob/canary/README.md)</sub>

## Ver similares

Grupo **Interfaces de chat con LLM**: LobeHub ocupa la posición 3 de 8 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Open WebUI](open-webui.md) ⭐ recomendado | 74 | Si quieres la interfaz más completa para Ollama o APIs, multiusuario y con RAG. |
| 2 | [Cherry Studio](cherry-studio.md) | 72 | Si quieres un cliente de escritorio para muchos proveedores con asistentes predefinidos. |
| 3 | **LobeHub** (esta ficha) | 70 | Si quieres una interfaz moderna con plugins, agentes y despliegue sencillo. |
| 4 | [LibreChat](librechat.md) | 69 | Si necesitas un clon de ChatGPT multiusuario con muchos proveedores, agentes y control de acceso. |
| 5 | [Jan](jan.md) | 66 | Si prefieres una app de escritorio que funcione sin conexión con modelos locales. |
| 6 | [NextChat](nextchat.md) | 64 | Si quieres desplegar una interfaz ligera en Vercel con un clic. |
| 7 | [chatbox](chatbox.md) | 52 | Si quieres un cliente de escritorio y móvil sencillo para tus claves de API. |
| 8 | [Text Generation WebUI](textgen.md) | 51 | Si quieres experimentar con muchos backends y formatos de modelos locales (GGUF, EXL2, Transformers). |

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

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open WebUI](open-webui.md) | 159k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |
| [LibreChat](librechat.md) | 47.1k | Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada. |
| [Cherry Studio](cherry-studio.md) | 53.5k | App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad. |
| [NextChat](nextchat.md) | 89k | Cliente de chat de IA ligero y multiplataforma (web, escritorio y móvil) para Claude, GPT, Gemini, DeepSeek y modelos autoalojados, con soporte MCP. |
| [chatbox](chatbox.md) | 42.3k | Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz común. |

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
