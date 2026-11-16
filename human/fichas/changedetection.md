[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# 🔍 changedetection.io

> Monitor de cambios en páginas web con alertas por email, Slack, Telegram y más.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 35.8k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Monitor autoalojado de cambios en páginas web (changedetection.io), de @dgtlmoon. Licencia Apache-2.0. Es maduro y activo (~36k estrellas, 0.70.3) y tiene versión alojada de pago.

## ¿Qué hace?

Vigila páginas y avisa por Discord, email, Slack, Telegram, webhook y muchos otros canales cuando cambian precios, textos o condiciones. Puede filtrar por selectores, ejecutar pasos de navegador (login, clics) y resumir o filtrar los cambios con un LLM (OpenAI, Gemini, Anthropic u Ollama local). Incluye servidor MCP para conectar asistentes.

## ¿Cómo lo hace?

Se instala con Docker o Docker Compose (`docker compose up -d`). Los pasos de navegador y las páginas con JavaScript requieren activar Playwright con un navegador aparte. Tiene selector visual para elegir qué parte de la página vigilar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Resúmenes y filtros de cambios con un modelo local, soportado según el README. | Levanta Ollama y configúralo como proveedor de LLM. |
| [Claude Code](claude-code.md) | Consultar y gestionar vigilancias desde un asistente con el servidor MCP de changedetection.io. | Activa el MCP en tu instancia y regístralo en el cliente. |
| [activepieces](activepieces.md) | Recibir los avisos por webhook y encadenar acciones. (combinación por arquitectura) | Configura una notificación webhook hacia un flujo de Activepieces. |
| [ArchiveBox](archivebox.md) | Combinación recíproca: ArchiveBox lo enlaza como «Archivar una nueva copia cuando una página cambia. (combinación por arquitectura)». | Orden indicado desde ArchiveBox: Usa una notificación de changedetection (webhook) para añadir la URL a ArchiveBox. |
| [cloud-mail](cloud-mail.md) | Combinación recíproca: cloud-mail lo enlaza como «Usar una dirección de cloud-mail como buzón de alertas de cambios web y reenviarlas a Telegram (combinación por arquitectura)». | Orden indicado desde cloud-mail: Crea la dirección en cloud-mail y configúrala como destino de notificación en changedetection. |
| [huginn](huginn.md) | Combinación recíproca: huginn lo enlaza como «Changedetection vigila cambios visuales o de texto en páginas complejas y puede notificar por webhook a Huginn, que encadena acciones posteriores (combinación por arquitectura)». | Orden indicado desde huginn: Independientes; crea en Huginn un agente receptor de webhooks y pon su URL como notificación en changedetection. Evita vigilar la misma página con los dos. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Maxun](maxun.md)

**Notas:** Sin alternativas declaradas. Respeta los términos de uso de cada plataforma y la privacidad de las personas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 0.70.3 (2026-11-09) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/dgtlmoon/changedetection.io/blob/master/README.md) · [2](https://changedetection.io/MCP)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Las comparaciones clásicas no necesitan LLM; filtros semánticos usan API o modelo local; SaaS y proxies tienen condiciones propias |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. MCP requiere versión que lo incluya; su acceso al historial no acredita que el agente haya observado cambios futuros |
| Coste | El coste depende del proveedor o la ruta. Las comparaciones clásicas no necesitan LLM; filtros semánticos usan API o modelo local; SaaS y proxies tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Docker; URL a vigilar; canal de aviso opcional |

MCP requiere versión que lo incluya; su acceso al historial no acredita que el agente haya observado cambios futuros

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- URL a vigilar
- canal de aviso opcional

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker run -d --restart always -p "127.0.0.1:5000:5000" -v datastore-volume:/datastore --name changedetection.io docker.io/dgtlmoon/changedetection.io
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/dgtlmoon/changedetection.io/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar changedetection.io para mi objetivo y necesito pasos guiados. Lee https://github.com/dgtlmoon/changedetection.io/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Vigila un texto en una página propia y modifícalo una vez para revisar la diferencia.

**Qué comprobar:** El historial identifica el cambio concreto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Detectar cambios de precio permitidos
- Monitorear avisos de una página

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Detectar cambios de precio permitidos; Monitorear avisos de una página | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** MCP requiere versión que lo incluya; su acceso al historial no acredita que el agente haya observado cambios futuros

## Stack y modelos

- **Stack:** Docker; URL a vigilar; canal de aviso opcional
- **Etiquetas:** `scraping` `notifications` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [dgtlmoon/changedetection.io](https://github.com/dgtlmoon/changedetection.io)
- 🌐 Web: <https://changedetection.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/dgtlmoon/changedetection.io/blob/master/README.md)
- [Fuente 2](https://changedetection.io/MCP)
- [Fuente 3](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
