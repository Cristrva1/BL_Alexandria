[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › Email, marketing y notificaciones

# ⚙️ cloud-mail

> Plataforma de correo basada en servicios de Cloudflare para gestionar buzones y funciones de mensajería de un dominio.

## Cuándo elegir esta ficha

Se perderían buzones y enrutamiento basados en Cloudflare. Listmonk, Mautic y Novu solo sustituyen etapas de campañas/notificaciones y necesitan transporte. No hay reemplazo de buzón en esas tres fichas.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/maillab/cloud-mail/blob/HEAD/README.md) · [Fuente 2](https://github.com/maillab/cloud-mail/commit/152b890b3350faf40a9c7739f02bc13f03a93bf6)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16k | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de correo de código abierto (MIT) basada en Cloudflare, del proyecto maillab, que permite crear muchos buzones con un solo dominio. Su documentación principal está en chino, con traducciones al inglés y japonés; publica versiones activas (v3.5 en 2026).

## ¿Qué hace?

Crea múltiples direcciones de correo con tu dominio, recibe y envía emails (incluido envío masivo) con adjuntos, y reenvía correos recibidos a un bot de Telegram u otro buzón. Incluye administración de usuarios y correos con permisos RBAC, API abierta para crear usuarios en lote y consultar correos, reconocimiento automático de códigos de verificación con Workers AI y gráficos de uso con ECharts.

## ¿Cómo lo hace?

Se despliega en Cloudflare Workers para reducir costes de servidor: backend con el framework Hono y el ORM Drizzle, frontend Vue 3 con Element Plus, base de datos Cloudflare D1, caché KV y archivos en R2. El envío usa Cloudflare Email o Resend.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Usar la API abierta para crear buzones en lote o procesar correos recibidos en flujos (combinación por arquitectura). | Despliega cloud-mail y crea un token de API; después llama a la API desde Activepieces. |
| [open-seo](open-seo.md) | Ambos se despliegan en el plan gratuito de Cloudflare y pueden compartir cuenta y dominio (combinación por arquitectura). | Configura el dominio en Cloudflare primero; separa subdominios por servicio. |
| [changedetection.io](changedetection.md) | Usar una dirección de cloud-mail como buzón de alertas de cambios web y reenviarlas a Telegram (combinación por arquitectura). | Crea la dirección en cloud-mail y configúrala como destino de notificación en changedetection. |

**Notas:** Depende de servicios de Cloudflare (Workers, D1, KV, R2) y de sus límites de plan.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v3.5.0 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/maillab/cloud-mail/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere LLM para correo básico; dominio, Workers, almacenamiento y proveedor de envío tienen cuotas y costes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. No es una app totalmente local: se apoya en servicios Cloudflare y en la configuración del dominio |
| Coste | El coste depende del proveedor o la ruta. No requiere LLM para correo básico; dominio, Workers, almacenamiento y proveedor de envío tienen cuotas y costes propios |
| Equipo | Preparación según la ruta elegida. Cuenta Cloudflare; dominio propio; Workers y almacenamiento de la guía; canal de envío |

No es una app totalmente local: se apoya en servicios Cloudflare y en la configuración del dominio

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cuenta Cloudflare
- dominio propio
- Workers y almacenamiento de la guía
- canal de envío

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/maillab/cloud-mail/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar cloud-mail para mi objetivo y necesito pasos guiados. Lee https://github.com/maillab/cloud-mail/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega un entorno de prueba y comprueba recepción con un buzón propio antes de usar correo real.

**Qué comprobar:** Puedes identificar dónde se guarda el mensaje y qué servicio lo entrega.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar correo sobre Workers
- Gestionar buzones de un dominio de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar correo sobre Workers; Gestionar buzones de un dominio de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No es una app totalmente local: se apoya en servicios Cloudflare y en la configuración del dominio

## Stack y modelos

- **Stack:** Cuenta Cloudflare; dominio propio; Workers y almacenamiento de la guía; canal de envío
- **Etiquetas:** `marketing` `server` `javascript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [maillab/cloud-mail](https://github.com/maillab/cloud-mail)
- 🌐 Web: <https://docs.skymail.ink>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/maillab/cloud-mail/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
