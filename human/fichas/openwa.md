[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › WhatsApp y mensajería

# 🌐 OpenWA

> Gateway autoalojado de WhatsApp con API, panel de sesiones y servidor MCP HTTP opcional, del proyecto rmyndharis/OpenWA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.9k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

## Qué puedes hacer con él

Gateway autoalojado de WhatsApp con API, panel de sesiones y servidor MCP HTTP opcional, del proyecto rmyndharis/OpenWA.

## Por qué destaca

Usos propuestos: Prototipar una integración de mensajería; Consultar estados desde un agente MCP.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |

## Enlaces

- 🐙 GitHub: [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA)
- 🌐 Web: <https://www.open-wa.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/rmyndharis/OpenWA/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
