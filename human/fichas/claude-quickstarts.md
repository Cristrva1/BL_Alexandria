[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 🧠 claude-quickstarts

> Ejemplos oficiales de Anthropic para construir aplicaciones con Claude, herramientas y uso de computadora.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 21k | MIT | Python | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Colección oficial de Anthropic (MIT) de proyectos de inicio para construir aplicaciones con la API de Claude. Es activa (último push en noviembre de 2026) y se amplía con las novedades de la plataforma.

## ¿Qué hace?

Incluye agentes de atención al cliente y de análisis financiero, demos de computer use (contenedor con VNC y una implementación nativa para macOS), browser use, los nuevos toolsets de navegador y ordenador, un agente de programación autónomo, y varias plantillas de 'Managed Agents' (Chat SDK, CopilotKit con AG-UI, servidor MCP en TypeScript, Slack, Linear, Sentry y otras).

## ¿Cómo lo hace?

Proyectos independientes en Python, TypeScript y Next.js, algunos con Docker (la demo de computer use). Todos requieren una clave de API de Claude, y los de Managed Agents dependen de ese servicio de Anthropic. Las demos de computer y browser use controlan un escritorio o navegador, así que conviene ejecutarlas aisladas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [claude-agent-sdk-python](claude-agent-sdk-python.md) | Pasar de los ejemplos a agentes propios con el bucle de Claude Code. (combinación por arquitectura) | Usa los quickstarts como referencia y construye con el SDK. |
| [CopilotKit](copilotkit.md) | Frontend de la plantilla 'Managed Agents with CopilotKit and AG-UI' (documentada en el README). | Sigue la plantilla: backend de Managed Agents y frontend con CopilotKit. |
| [E2B](e2b.md) | Ejecutar las demos de computer use y del agente autónomo en un sandbox remoto en lugar de la máquina local. (combinación por arquitectura) | Crea el sandbox y despliega la demo dentro. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-06 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/anthropics/claude-quickstarts/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Lectura libre; ejecutar requiere API de Claude y posibles servicios adicionales |
| Claude Code | Depende del recurso o la configuración |
| Codex | Depende del recurso o la configuración |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | Modelo local no documentado. Incluye un ejemplo MCP para Managed Agents pero no todos los quickstarts son conectores; la demo de computadora requiere un entorno aislado de prueba |
| Coste | Consumo de APIs o servicios. Lectura libre; ejecutar requiere API de Claude y posibles servicios adicionales |
| Equipo | Preparación según la ruta elegida. Python o TypeScript según proyecto; clave Anthropic; servicios del ejemplo |

Incluye un ejemplo MCP para Managed Agents pero no todos los quickstarts son conectores; la demo de computadora requiere un entorno aislado de prueba

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python o TypeScript según proyecto
- clave Anthropic
- servicios del ejemplo

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/anthropics/claude-quickstarts/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar claude-quickstarts para mi objetivo y necesito pasos guiados. Lee https://github.com/anthropics/claude-quickstarts/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Escoge Customer Support Agent y revisa las herramientas que permite antes de enviar una consulta ficticia.

**Qué comprobar:** Puedes identificar acciones del agente y datos enviados a la API.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar soporte con Claude
- Estudiar una demo de uso de computadora

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar soporte con Claude; Estudiar una demo de uso de computadora | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Incluye un ejemplo MCP para Managed Agents pero no todos los quickstarts son conectores; la demo de computadora requiere un entorno aislado de prueba

## Stack y modelos

- **Stack:** Python o TypeScript según proyecto; clave Anthropic; servicios del ejemplo
- **Etiquetas:** `guias` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [anthropics/claude-quickstarts](https://github.com/anthropics/claude-quickstarts)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/anthropics/claude-quickstarts/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
