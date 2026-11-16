[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › Email, marketing y notificaciones

# 📣 mautic

> Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11k | NOASSERTION | PHP | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de automatización de marketing de código abierto, presentada como el mayor proyecto abierto de su tipo y con comunidad mundial. Se distribuye bajo GPL v3 [DATO NO VERIFICADO: GitHub no reconoce la licencia como estándar] y publica versiones activas (7.2 en 2026); también existen pruebas alojadas por terceros.

## ¿Qué hace?

Crea campañas de marketing integradas y multicanal con segmentación y automatización sin límites, formularios, páginas y seguimiento de contactos, con foco en privacidad y en ser dueño de tus datos. Permite crear integraciones propias y personalizar frontend y backend. Casos típicos: nutrir clientes potenciales, campañas de email por comportamiento y puntuación de leads.

## ¿Cómo lo hace?

Es una aplicación PHP que se instala con Composer siguiendo la documentación de línea de comandos (o descargando el paquete), con requisitos y versiones soportadas publicados en su documentación; el repositorio incluye configuración DDEV para desarrollo local. Necesita un servidor web con PHP y una base de datos MySQL/MariaDB [DATO NO VERIFICADO: versiones exactas] y tareas cron para procesar segmentos y campañas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Activepieces tiene una pieza oficial `mautic` para usar mautic en flujos. | mautic en marcha con sus credenciales; después añade la pieza `mautic` en un flujo de Activepieces. |
| [Marketing Skills](marketingskills.md) | Skills de marketing para que un agente redacte secuencias, segmentos y copys que luego se cargan en Mautic (combinación por arquitectura). | Independientes; revisa los textos generados antes de activarlos. |
| [posthog](posthog.md) | PostHog mide el comportamiento en producto y Mautic actúa con campañas sobre esos segmentos (combinación por arquitectura). | Define un identificador común de contacto antes de sincronizar datos entre ambos. |

**Notas:** Se solapa con listmonk en envío masivo de email; usa uno como canal principal de boletines.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 7.2.2 (2026-10-26) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mautic/mautic/blob/7.x/README.md) · [2](https://github.com/activepieces/activepieces/tree/main/packages/pieces/community/mautic)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita LLM para automatización; hosting, correo y servicios conectados tienen costes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Las campañas pueden ejecutar acciones y envíos; una plantilla dibujada no demuestra que cron, colas y entrega estén configurados |
| Coste | El coste depende del proveedor o la ruta. No necesita LLM para automatización; hosting, correo y servicios conectados tienen costes propios |
| Equipo | Preparación según la ruta elegida. Servidor y versión compatibles; SMTP; contactos ficticios; colas y tareas según guía |

Las campañas pueden ejecutar acciones y envíos; una plantilla dibujada no demuestra que cron, colas y entrega estén configurados

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Servidor y versión compatibles
- SMTP
- contactos ficticios
- colas y tareas según guía

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.mautic.org/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mautic para mi objetivo y necesito pasos guiados. Lee https://docs.mautic.org/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Diseña una campaña de prueba con un contacto ficticio y revisa condiciones y acciones antes de activarla.

**Qué comprobar:** Puedes explicar qué evento dispara cada paso del flujo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar segmentación de audiencias
- Prototipar una secuencia de marketing

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar segmentación de audiencias; Prototipar una secuencia de marketing | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las campañas pueden ejecutar acciones y envíos; una plantilla dibujada no demuestra que cron, colas y entrega estén configurados

## Stack y modelos

- **Stack:** Servidor y versión compatibles; SMTP; contactos ficticios; colas y tareas según guía
- **Etiquetas:** `automation` `email` `php`
- **Modo de instalación sugerido:** 🐳 **Servicio Docker** — levántalo con Docker cuando el proyecto lo necesite

## Enlaces

- 🐙 GitHub: [mautic/mautic](https://github.com/mautic/mautic)
- 🌐 Web: <https://www.mautic.org>
- 🧪 Receta: [Marketing de agencia](../playbooks/marketing-de-agencia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mautic/mautic/blob/7.x/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
