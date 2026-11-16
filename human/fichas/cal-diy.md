[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › Reservas y programación de citas

# 🤖 cal.diy

> Edición comunitaria de Cal.com para experimentar con agendas y reservas en una instalación propia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 50k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

Plataforma de agendamiento de código abierto y comunitaria: un fork de Cal.com con todo el código Enterprise eliminado, 100 % bajo licencia MIT. Sus autores la recomiendan para uso personal y no productivo, y remiten a Cal.com para usos comerciales; no existe versión alojada.

## ¿Qué hace?

Permite publicar tipos de evento, compartir enlaces de reserva, conectar calendarios y recibir citas sin cuenta ni clave de licencia de Cal.com. Respecto a Cal.com elimina equipos, organizaciones, Insights, Workflows, SSO/SAML y otras funciones EE. Las integraciones disponibles requieren credenciales propias de cada servicio.

## ¿Cómo lo hace?

Monorepo en TypeScript con Next.js, tRPC y Prisma sobre PostgreSQL 13 o superior; requiere Node.js 18 o superior y se recomienda Yarn. Se instala clonando el repositorio, instalando paquetes con yarn y configurando variables de entorno, o con la imagen Docker `calcom/cal.diy`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [n8n](n8n.md) | n8n tiene un disparador de Cal.com para reaccionar a reservas, cancelaciones o reprogramaciones; con cal.diy hay que apuntarlo a tu instancia [DATO NO VERIFICADO: compatibilidad con instancia propia]. | cal.diy accesible para n8n y clave de API; después el disparador. |
| [twenty-main](twenty-main.md) | Registrar cada reserva como actividad u oportunidad en el CRM (combinación por arquitectura, con webhooks y un flujo intermedio). | Configura el webhook de cal.diy hacia el flujo que escribe en Twenty. |
| [Botpress](botpress.md) | Botpress Cloud tiene integración con Cal.com para que un bot ofrezca horarios; con cal.diy es [DATO NO VERIFICADO]. | Instancia accesible por internet y token de API antes de configurar la integración. |

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v6.2.0 (2026-03-01) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/calcom/cal.diy/blob/main/README.md) · [2](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.caltrigger/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere licencia Cal.com ni un LLM en la ruta comunitaria; servidor y correo siguen siendo gastos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El autor la recomienda para uso personal y no productivo. Se mueve de motores de workflows a agendas y reservas |
| Coste | Sin pago a un modelo en la ruta básica. No requiere licencia Cal.com ni un LLM en la ruta comunitaria; servidor y correo siguen siendo gastos propios |
| Equipo | Preparación según la ruta elegida. Node.js y Yarn según el proyecto;  PostgreSQL;  Docker para el entorno de desarrollo |

El autor la recomienda para uso personal y no productivo. Se mueve de motores de workflows a agendas y reservas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js y Yarn según el proyecto
-  PostgreSQL
-  Docker para el entorno de desarrollo

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/calcom/cal.diy/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar cal.diy para mi objetivo y necesito pasos guiados. Lee https://github.com/calcom/cal.diy/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un evento personal de prueba y abre su página de reserva.

**Qué comprobar:** Puedes elegir una franja disponible y revisar la reserva creada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Experimentar con una agenda personal autoalojada
- Probar la duración y disponibilidad de distintos tipos de cita

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Experimentar con una agenda personal autoalojada; Probar la duración y disponibilidad de distintos tipos de cita | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El autor la recomienda para uso personal y no productivo. Se mueve de motores de workflows a agendas y reservas

## Stack y modelos

- **Stack:** Node.js y Yarn según el proyecto;  PostgreSQL;  Docker para el entorno de desarrollo
- **Etiquetas:** `motores` `next-auth` `nextjs` `open-source` `postgresql` `prisma` `t3-stack` `tailwindcss`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [calcom/cal.diy](https://github.com/calcom/cal.diy)
- 🌐 Web: <https://cal.diy>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría corregida en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/calcom/cal.diy/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
