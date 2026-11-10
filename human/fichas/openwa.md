[🏠 Inicio](../README.md) › [🤖 Automatización, Mensajería & CRM](../categorias/01-automatizaci-n-mensajer-a-crm.md) › WhatsApp y mensajería

# 🌐 OpenWA

> Gateway/SDK abierto para conectar y automatizar cuentas de WhatsApp de forma directa desde código, sin infraestructura pesada.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 16.7k | MIT | TypeScript | 2026-11-10 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Qué es

Envía y recibe mensajes de WhatsApp desde tu propio script con una API sencilla y expresiva.

## Por qué destaca

Muy adoptado para prototipos y bots individuales por su simplicidad y su API expresiva, con una comunidad consolidada alrededor de wa-automate. Es la opción ligera cuando evolution-api es excesivo.

## Cómo funciona

Controla una sesión de WhatsApp Web mediante automatización del navegador (Puppeteer) y expone eventos y métodos a tus scripts en Node.js, con bindings para Python. Cada sesión vive en un proceso, sin Redis ni orquestador.

## Instalación rápida

Vía `npm i @open-wa/wa-automate` en proyectos Node.js (o el paquete equivalente para Python); requiere un entorno con navegador headless para la sesión.

## Casos de uso

- Bot que escucha eventos y ejecuta scripts locales
- Respuestas rápidas con panel local
- Prototipo de agente conversacional en una sola máquina

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| desarrollas scripts o bots individuales y quieres arrancar rápido | necesitas infra multi-instancia o alta disponibilidad (evolution-api) |

**Limitaciones:** Depende de automatizar el navegador, lo que es frágil ante cambios de WhatsApp Web; no está pensado para producción a escala.

## Stack y modelos

- **Stack:** Node.js, Puppeteer, bindings Python
- **Modelos / API:** No nativa (requiere orquestación externa del LLM).
- **Etiquetas:** `whatsapp` `chatbot` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 210k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |

## Enlaces

- 🐙 GitHub: [rmyndharis/OpenWA](https://github.com/rmyndharis/OpenWA)
- 🌐 Web: <https://www.open-wa.org>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
