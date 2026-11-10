[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Email, marketing y notificaciones

# 📣 mautic

> Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 11k | Otra (ver repo) | PHP | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Qué es

Nutre leads por email con reglas y segmentos automáticos, sin ceder los datos de tus clientes a un SaaS.

## Por qué destaca

Es la solución de marketing automation open-source más conocida y madura, respaldada por la Fundación Mautic y una comunidad amplia. Su madurez la hace apta para operaciones de marketing reales, no solo prototipos.

## Cómo funciona

Ejecuta campañas, scoring de leads y nurturing por email mediante reglas y segmentos, sobre una aplicación PHP/Symfony con base de datos MySQL. Las campañas se definen como secuencias de pasos condicionales que disparan emails o acciones.

## Instalación rápida

Vía `docker compose` o instalación PHP/MySQL tradicional sobre un servidor web; requiere MySQL y un MTA o servicio SMTP para los envíos.

## Casos de uso

- Nurturing por email
- Campañas segmentadas y scoring de leads
- Base de datos de audiencia soberana para tu agencia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas automatización de marketing seria y soberana | te basta una newsletter simple (listmonk) |

**Limitaciones:** Setup PHP/MySQL pesado y mantenimiento exigente; la curva de configuración de campañas no es trivial.

## Stack y modelos

- **Stack:** PHP/Symfony, MySQL, self-host
- **Modelos / API:** No nativa; complementa flujos de contenido IA.
- **Etiquetas:** `automation` `email` `php`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [listmonk](listmonk.md) | 24.2k | Gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depender de un SaaS. |
| [Marketing Skills](marketingskills.md) | 59.5k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. |

## Enlaces

- 🐙 GitHub: [mautic/mautic](https://github.com/mautic/mautic)
- 🌐 Web: <https://www.mautic.org>
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
