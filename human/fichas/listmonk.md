[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Email, marketing y notificaciones

# 📬 listmonk

> Gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depender de un SaaS.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 24.2k | AGPL-3.0 | Go | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Qué es

Resuelve la primitiva de "enviar email a miles de suscriptores" con un footprint mínimo.

## Por qué destaca

Muy popular por su rapidez y su single-binary en Go, es una opción ligera y soberana muy recomendada para email masivo. Su simplicidad de despliegue contrasta con stacks más pesados como mautic.

## Cómo funciona

Gestiona listas, suscriptores y campañas desde un panel y envía vía SMTP, sobre un binario único en Go con base de datos PostgreSQL. Soporta plantillas, segmentación básica y envíos programados.

## Instalación rápida

Vía `docker compose` o descargando el binario único de Go y apuntándolo a PostgreSQL; requiere un servidor SMTP (o servicio como SES) para los envíos.

## Casos de uso

- Newsletter propia para leads
- Campañas de email desde workflows
- Envíos transaccionales a alta velocidad

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres email marketing simple, rápido y propio | necesitas nurturing avanzado o scoring de leads (mautic) |

## Stack y modelos

- **Stack:** Go, PostgreSQL, self-host
- **Modelos / API:** No nativa; integrable con generadores de contenido.
- **Etiquetas:** `automation` `email` `go` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mautic](mautic.md) | 11k | Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo. |
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Enlaces

- 🐙 GitHub: [knadh/listmonk](https://github.com/knadh/listmonk)
- 🌐 Web: <https://listmonk.app>
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
