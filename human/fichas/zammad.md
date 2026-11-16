[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › CRM, ERP y soporte al cliente

# ⚙️ Zammad

> Sistema de helpdesk y tickets autoalojado y omnicanal: correo, chat, teléfono y redes sociales en una sola interfaz web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.1k | AGPL-3.0 | Ruby | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Helpdesk de código abierto (AGPL-3.0) de la Zammad Foundation, con alojamiento y soporte de pago de Zammad GmbH. Muy maduro.

## ¿Qué hace?

Gestiona la comunicación con clientes por correo, chat, teléfono y redes sociales, con tickets, SLA, macros, disparadores, base de conocimiento, informes, búsqueda y API REST para integraciones.

## ¿Cómo lo hace?

Escrito en Ruby on Rails; se instala con Docker Compose, paquetes de Linux o Helm. Requiere PostgreSQL; Elasticsearch es recomendable para búsqueda e informes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | La API REST y los webhooks de Zammad permiten crear tickets o avisos desde flujos de Activepieces (combinación por arquitectura). | Crea un token de API en Zammad; después úsalo en Activepieces. |
| [Claude Code](claude-code.md) | Un agente de código puede escribir scripts contra la API de Zammad para migraciones o informes (combinación por arquitectura). | Usa una instancia de prueba; después pide el script al agente. |
| [coolify](coolify.md) | Zammad se puede desplegar en contenedor desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con volúmenes persistentes. |

**Notas:** Alternativas (elige una): freescout. Chatwoot cubre atención por chat y mensajería con otro enfoque.

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/zammad/zammad/blob/develop/README.md) · [2](https://docs.zammad.org/en/latest/install/docker-compose.html)</sub>

## Ver similares

Grupo **Help desk y tickets**: Zammad ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Zammad** (esta ficha) ⭐ recomendado | 58 | Si buscas esto: sistema de helpdesk y tickets autoalojado y omnicanal: correo, chat, teléfono y redes sociales en una sola interfaz web. |
| 2 | [FreeScout](freescout.md) | 56 | Si buscas esto: helpdesk y bandeja de entrada compartida muy ligera, alternativa abierta a Help Scout y Zendesk, en PHP y desplegable incluso en hosting compartido. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/zammad/zammad/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Zammad para mi objetivo y necesito pasos guiados. Lee https://github.com/zammad/zammad/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega Zammad con zammad-docker-compose, conecta una cuenta de correo de prueba y responde a un ticket..

**Qué comprobar:** El correo entra como ticket y la respuesta sale desde Zammad..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- centralizar el soporte por correo y chat de un equipo pequeño
- crear una base de conocimiento y métricas de atención

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: centralizar el soporte por correo y chat de un equipo pequeño; crear una base de conocimiento y métricas de atención | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Ruby, Dockerfile, Gemfile, package.json
- **Etiquetas:** `helpdesk` `ruby` `self-hosted` `server`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [FreeScout](freescout.md) | 4.7k | Helpdesk y bandeja de entrada compartida muy ligera, alternativa abierta a Help Scout y Zendesk, en PHP y desplegable incluso en hosting compartido. |

## Enlaces

- 🐙 GitHub: [zammad/zammad](https://github.com/zammad/zammad)
- 🌐 Web: <https://zammad.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/zammad/zammad/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
