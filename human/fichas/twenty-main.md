[🏠 Inicio](../README.md) › [🤖 Automatizar negocios y comunicación](../categorias/01-automatizaci-n-mensajer-a-crm.md) › CRM, ERP y soporte al cliente

# 👥 twenty-main

> CRM open-source orientado a equipos técnicos, pensado como alternativa moderna a Salesforce/HubSpot que modelas con tus propios objetos, campos y relaciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 60.9k | NOASSERTION | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica puede usarse sin un LLM remoto; activar funciones de IA cambia los requisitos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | El coste depende del proveedor o la ruta. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

La premisa es tratar el CRM como una pieza más de tu stack: lo construyes, lo despliegas y lo versionas igual que el código.

## Por qué destaca

Combina una UI cuidada con un modelo de datos totalmente personalizable, lo que evita el "molde" rígido de los CRM SaaS. Su enfoque "construye tu propio CRM" y su comunidad activa lo han vuelto una de las opciones open-source de referencia para este caso.

## Cómo funciona

Una arquitectura dirigida por metadatos describe objetos, campos y relaciones que se materializan en PostgreSQL; el backend en NestJS expone una API (GraphQL/REST) que consume un frontend en React. Todo corre en contenedores para reproducir el entorno.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/twentyhq/twenty/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar twenty-main para mi objetivo y necesito pasos guiados. Lee https://github.com/twentyhq/twenty/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `automation` `crm` `typescript` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [evolution-api](evolution-api.md) | 10.1k | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. |
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Enlaces

- 🐙 GitHub: [twentyhq/twenty](https://github.com/twentyhq/twenty)
- 🌐 Web: <https://twenty.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/twentyhq/twenty/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
