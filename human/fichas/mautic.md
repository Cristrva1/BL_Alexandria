[🏠 Inicio](../README.md) › [🤖 Automatizar negocios y comunicación](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Email, marketing y notificaciones

# 📣 mautic

> Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11k | NOASSERTION | PHP | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

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

Nutre leads por email con reglas y segmentos automáticos, sin ceder los datos de tus clientes a un SaaS.

## Por qué destaca

Es la solución de marketing automation open-source más conocida y madura, respaldada por la Fundación Mautic y una comunidad amplia. Su madurez la hace apta para operaciones de marketing reales, no solo prototipos.

## Cómo funciona

Ejecuta campañas, scoring de leads y nurturing por email mediante reglas y segmentos, sobre una aplicación PHP/Symfony con base de datos MySQL. Las campañas se definen como secuencias de pasos condicionales que disparan emails o acciones.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/mautic/mautic/blob/7.x/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mautic para mi objetivo y necesito pasos guiados. Lee https://github.com/mautic/mautic/blob/7.x/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `automation` `email` `php`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [listmonk](listmonk.md) | 24.3k | Gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depender de un SaaS. |
| [Marketing Skills](marketingskills.md) | 60.4k | Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code, Codex, Cursor y otros. |

## Enlaces

- 🐙 GitHub: [mautic/mautic](https://github.com/mautic/mautic)
- 🌐 Web: <https://www.mautic.org>
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/mautic/mautic/blob/7.x/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
