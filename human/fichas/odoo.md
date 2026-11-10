[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › CRM, ERP y soporte al cliente

# 👥 Odoo

> Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 55.7k | Otra (ver repo) | Python | 2026-11-10 | 🆕 Aún no (sugerido) |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Qué es

Integra CRM, ventas, facturación, inventario, RR. HH. y sitio web en una sola plataforma modular. La usan pymes y grandes empresas en todo el mundo.

## Por qué destaca

Ecosistema enorme de módulos y partners; cubre casi cualquier proceso de negocio.

## Cómo funciona

Un servidor Python con ORM propio sobre PostgreSQL carga módulos que añaden modelos, vistas y lógica.

## Instalación rápida

`docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name db postgres:16` y `docker run -p 8069:8069 --link db:db odoo`.

## Casos de uso

- CRM y ventas de una pyme
- Inventario y facturación integrados
- Portal de clientes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas un ERP completo con CRM integrado | solo quieres un CRM ligero; mira `twenty-main` |

**Limitaciones:** La edición Community no incluye varios módulos de la Enterprise (p. ej. contabilidad completa).

## Stack y modelos

- **Stack:** Python, PostgreSQL, JavaScript
- **Modelos / API:** No usa LLM de serie; hay módulos de IA.
- **Etiquetas:** `crm` `python` `postgres`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [metabase](metabase.md) | 50.3k | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ERPNext](erpnext.md) | 41.1k | ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y manufactura. |

## Enlaces

- 🐙 GitHub: [odoo/odoo](https://github.com/odoo/odoo)
- 🌐 Web: <https://www.odoo.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
