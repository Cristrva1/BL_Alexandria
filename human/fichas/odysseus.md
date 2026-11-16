[🏠 Inicio](../README.md) › [🏠 Chats, modelos locales y espacios privados](../categorias/08-ia-local-modelos-chats-workspaces.md) › Workspaces privados y segundos cerebros

# ⛺ odysseus

> Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 95.6k | AGPL-3.0 | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Puntuación de calidad** 73/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Espacio de trabajo de IA autoalojado de código abierto (AGPL-3.0) de odysseus-dev que reúne chat, agentes, investigación, documentos, correo, notas, calendario y flujos con modelos locales. Proyecto activo sin releases formales: la rama `dev` recibe los cambios primero y `main` es la más curada.

## ¿Qué hace?

Ofrece chat y agentes con modelos locales o por API, herramientas, MCP, archivos, shell, skills y memoria; un «Cookbook» que recomienda, descarga y sirve modelos según tu hardware; investigación web profunda con lectura de fuentes e informes; comparación ciega de modelos; editor de documentos con edición por IA; bandeja IMAP/SMTP con triaje, resúmenes y borradores; y notas, tareas y calendario con sincronización CalDAV y tareas programadas de agentes.

## ¿Cómo lo hace?

Aplicación Python (servidor uvicorn) con interfaz web en el puerto 7011 vía Docker Compose, que también arranca ChromaDB y SearXNG; usa la imagen multiarquitectura `ghcr.io/odysseus-dev/odysseus` (en producción recomienda fijar una etiqueta inmutable). La instalación nativa requiere Python 3.11+ y tmux para el Cookbook. En Docker sobre Mac no hay acceso a la GPU Metal, así que el Cookbook sirve modelos solo con CPU; puede usar endpoints existentes de Ollama, vLLM u otros compatibles con OpenAI.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | La guía de instalación documenta el uso de un Ollama existente como endpoint de modelos. | Ollama primero (en Mac, fuera de Docker para usar Metal); después configura su URL en Odysseus. |
| [vLLM](vllm.md) | Endpoint compatible con OpenAI documentado para servir modelos con GPU. | vLLM en un servidor con GPU; registra su URL en Odysseus y no expongas su puerto públicamente. |
| [Playwright MCP](playwright-mcp.md) | Dar a los agentes un navegador mediante MCP (combinación por arquitectura). | Después de activar la autenticación; restringe qué agentes pueden usarlo. |

**Notas:** Mantén `AUTH_ENABLED=true` y `LOCALHOST_BYPASS=false` en cualquier despliegue en red. ChromaDB y SearXNG ya vienen en su Compose. Se retiraron las combinaciones antiguas con open-notebook, ecc y mem0 por falta de relación documentada.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/odysseus-dev/odysseus/blob/dev/README.md) · [2](https://github.com/odysseus-dev/odysseus/blob/dev/website/setup.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Admite modelos locales o API; correo, búsqueda y otros servicios mantienen sus credenciales y costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Local/API describe el modelo elegido; conservar la app en tu servidor no impide enviar datos a un proveedor remoto |
| Coste | El coste depende del proveedor o la ruta. Admite modelos locales o API; correo, búsqueda y otros servicios mantienen sus credenciales y costes |
| Equipo | Preparación según la ruta elegida. Docker; configuración .env; proveedor o modelos locales |

Local/API describe el modelo elegido; conservar la app en tu servidor no impide enviar datos a un proveedor remoto

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- configuración .env
- proveedor o modelos locales

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/odysseus-dev/odysseus.git
cd odysseus
cp .env.example .env
docker compose up -d --build
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/odysseus-dev/odysseus/blob/dev/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar odysseus para mi objetivo y necesito pasos guiados. Lee https://github.com/odysseus-dev/odysseus/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre un chat con un texto ficticio y prueba el editor de documentos sin conectar correo real.

**Qué comprobar:** Puedes distinguir conversación, documento y herramientas habilitadas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar notas y tareas con IA
- Comparar respuestas de modelos desde un workspace

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar notas y tareas con IA; Comparar respuestas de modelos desde un workspace | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Local/API describe el modelo elegido; conservar la app en tu servidor no impide enviar datos a un proveedor remoto

## Stack y modelos

- **Stack:** Docker; configuración .env; proveedor o modelos locales
- **Etiquetas:** `agents` `local` `python` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [odysseus-dev/odysseus](https://github.com/odysseus-dev/odysseus)
- 🌐 Web: <https://odysseus-dev.github.io/odysseus>
- 🧪 Receta: [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/odysseus-dev/odysseus/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
