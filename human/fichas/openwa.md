[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › WhatsApp y mensajería

# 🌐 OpenWA

> Gateway autoalojado de WhatsApp con API, panel de sesiones y servidor MCP HTTP opcional, del proyecto rmyndharis/OpenWA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.9k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación sencilla; varios servicios con Docker Compose

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Gateway de API de WhatsApp de código abierto (MIT) y autoalojado, creado en 2026 y con versiones muy frecuentes. Es un proyecto comunitario no oficial que se conecta a WhatsApp mediante clientes de ingeniería inversa, no mediante la Cloud API de Meta.

## ¿Qué hace?

Gestiona varias sesiones de WhatsApp con API REST, webhooks y un panel React para sesiones, webhooks y claves de API. Permite claves limitadas a ciertas sesiones o chats, útil para dar a un agente de IA acceso solo a algunos grupos. Ofrece plugins oficiales para Chatwoot y Typebot, nodos comunitarios para n8n y un servidor MCP opcional con 26 herramientas de solo lectura por defecto.

## ¿Cómo lo hace?

Backend NestJS en TypeScript con arquitectura de adaptadores: base de datos SQLite o PostgreSQL, almacenamiento de medios local o S3 y Redis opcional para colas, límites y WebSocket, todo elegido por configuración. Puede usar dos motores: `whatsapp-web.js` (Chromium sin interfaz, menor riesgo de bloqueo, 300–500 MB por sesión) o `baileys` (WebSocket directo, 30–80 MB por sesión, más fácil de detectar). Se despliega con Docker; el MCP se activa con `MCP_ENABLED=true` en `POST /mcp` del mismo puerto.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [chatwoot](chatwoot.md) | Plugin oficial de OpenWA: las conversaciones de WhatsApp llegan a la bandeja de Chatwoot. | Chatwoot primero; luego instala y configura el plugin desde OpenWA-plugins. |
| [Typebot](typebot.md) | Plugin oficial para responder con flujos conversacionales visuales de Typebot. | Typebot con el bot publicado; después activa el plugin en OpenWA. |
| [Claude Code](claude-code.md) | El servidor MCP de OpenWA permite que un agente lea sesiones y mensajes con una clave restringida a ciertos chats. | Activa `MCP_ENABLED=true`, crea una clave limitada y registra el endpoint `/mcp` en el agente. |

**Notas:** Riesgo de bloqueo: no envíes mensajes en frío a números que nunca te escribieron y usa destinatarios que hayan dado su consentimiento. Con S3, el script de respaldo no copia el bucket.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.30.3 (2026-11-16) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/rmyndharis/OpenWA/blob/main/README.md) · [2](https://github.com/rmyndharis/OpenWA-plugins)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El gateway no requiere modelo; hosting y servicios conectados tienen costes propios |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Este proyecto es rmyndharis/OpenWA; MCP HTTP añade herramientas de lectura por defecto y capacidades de escritura se habilitan aparte |
| Coste | El coste depende del proveedor o la ruta. El gateway no requiere modelo; hosting y servicios conectados tienen costes propios |
| Equipo | Preparación según la ruta elegida. Docker; cuenta y número propios; configuración de autenticación y persistencia |

Este proyecto es rmyndharis/OpenWA; MCP HTTP añade herramientas de lectura por defecto y capacidades de escritura se habilitan aparte

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- cuenta y número propios
- configuración de autenticación y persistencia

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
# Clone and start
git clone https://github.com/rmyndharis/OpenWA.git
cd OpenWA
docker compose -f docker-compose.dev.yml up -d

# Access (the dashboard is bundled into the API image and served on the same port)
# Dashboard: http://localhost:2785
# API: http://localhost:2785/api
# Swagger: http://localhost:2785/api/docs
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/rmyndharis/OpenWA/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenWA para mi objetivo y necesito pasos guiados. Lee https://github.com/rmyndharis/OpenWA/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre el dashboard y consulta el estado de una sesión de prueba antes de automatizar mensajes.

**Qué comprobar:** Puedes ver sesión, API y permisos del usuario configurado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar una integración de mensajería
- Consultar estados desde un agente MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar una integración de mensajería; Consultar estados desde un agente MCP | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Este proyecto es rmyndharis/OpenWA; MCP HTTP añade herramientas de lectura por defecto y capacidades de escritura se habilitan aparte

## Stack y modelos

- **Stack:** Docker; cuenta y número propios; configuración de autenticación y persistencia
- **Etiquetas:** `whatsapp` `chatbot` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA)
- 🌐 Web: <https://www.open-wa.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/rmyndharis/OpenWA/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
