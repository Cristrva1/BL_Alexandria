[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🧩 activepieces

> Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 25.5k | Otra (ver repo) | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

## Qué es

Resuelve la primitiva de "orquestar mis apps sin código" manteniéndote en self-host.

## Por qué destaca

Muy adoptada como reemplazo open-source de Zapier, destaca por su soporte temprano de MCP y por permitir crear piezas propias en TypeScript. Su editor visual y su catálogo de conectores la hacen accesible para perfiles mixtos técnico/no-técnico.

## Cómo funciona

Ejecuta flujos de pasos (triggers y acciones) basados en "pieces" escritas en TypeScript, con un motor Node.js y soporte de conectores de IA y MCP. Las pieces son paquetes versionables que puedes compartir entre proyectos.

## Instalación rápida

Vía `docker compose` para self-host, o usando su versión cloud si prefieres no operar la infra; requiere Node.js y una base de datos para el modo local.

## Casos de uso

- Lead → consulta CRM → notifica al equipo
- Flujos para usuarios técnicos y no técnicos
- Integraciones con IA vía piezas MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres reemplazar Zapier con piezas propias en TypeScript | ya dominas n8n y su ecosistema te basta |

## Stack y modelos

- **Stack:** Node.js, TypeScript, self-host/web
- **Modelos / API:** OpenAI, Anthropic, MCP.
- **Etiquetas:** `automation` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [novu](novu.md) | 40.3k | Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Enlaces

- 🐙 GitHub: [activepieces/activepieces](https://github.com/activepieces/activepieces)
- 🌐 Web: <https://www.activepieces.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
