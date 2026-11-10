[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › CRM, ERP y soporte al cliente

# 👥 twenty-main

> CRM open-source orientado a equipos técnicos, pensado como alternativa moderna a Salesforce/HubSpot que modelas con tus propios objetos, campos y relaciones.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 60.7k | Otra (ver repo) | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Qué es

La premisa es tratar el CRM como una pieza más de tu stack: lo construyes, lo despliegas y lo versionas igual que el código.

## Por qué destaca

Combina una UI cuidada con un modelo de datos totalmente personalizable, lo que evita el "molde" rígido de los CRM SaaS. Su enfoque "construye tu propio CRM" y su comunidad activa lo han vuelto una de las opciones open-source de referencia para este caso.

## Cómo funciona

Una arquitectura dirigida por metadatos describe objetos, campos y relaciones que se materializan en PostgreSQL; el backend en NestJS expone una API (GraphQL/REST) que consume un frontend en React. Todo corre en contenedores para reproducir el entorno.

## Instalación rápida

La vía soportada es `docker compose` con la imagen oficial (levanta app, base de datos y worker); también puedes clonar el repo y arrancar los servicios con el stack Node/PostgreSQL para desarrollo. Requiere PostgreSQL y recursos no triviales (de ahí el setup 🔴).

## Casos de uso

- Pipelines de venta versionados como código
- Panel a medida con objetos/campos propios
- Base de datos de clientes integrada con tus automatizaciones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un CRM que se adapte 1:1 a tu negocio y vivir en self-host | buscas algo plug-and-play gestionado o no quieres operar PostgreSQL y Docker |

**Limitaciones:** Self-host con setup pesado; necesitas mantener la base de datos y las actualizaciones tú mismo.

## Stack y modelos

- **Stack:** TypeScript, React, NestJS, PostgreSQL, Docker
- **Modelos / API:** No requiere LLM; opcionalmente, plugins de Claude Code/Codex permiten consultar el CRM en lenguaje natural.
- **Etiquetas:** `automation` `crm` `typescript` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Enlaces

- 🐙 GitHub: [twentyhq/twenty](https://github.com/twentyhq/twenty)
- 🌐 Web: <https://twenty.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
