[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › Email, marketing y notificaciones

# 📬 listmonk

> Gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depender de un SaaS.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 24.3k | AGPL-3.0 | Go | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Envía newsletters y campañas a miles de suscriptores desde un solo binario ligero que consume muy pocos recursos.

## Por qué destaca

Muy popular por su rapidez y su single-binary en Go, es una opción ligera y soberana muy recomendada para email masivo. Su simplicidad de despliegue contrasta con stacks más pesados como mautic.

## Cómo funciona

Gestiona listas, suscriptores y campañas desde un panel y envía vía SMTP, sobre un binario único en Go con base de datos PostgreSQL. Soporta plantillas, segmentación básica y envíos programados.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/knadh/listmonk/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar listmonk para mi objetivo y necesito pasos guiados. Lee https://github.com/knadh/listmonk/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `automation` `email` `go` `docker`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [mautic](mautic.md) | 11k | Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo. |
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Enlaces

- 🐙 GitHub: [knadh/listmonk](https://github.com/knadh/listmonk)
- 🌐 Web: <https://listmonk.app>
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/knadh/listmonk/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
