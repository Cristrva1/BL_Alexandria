[🏠 Inicio](../README.md) › [🤖 CRM, ventas y marketing](../categorias/18-crm-ventas-marketing.md) › CRM, ERP y soporte al cliente

# ⚙️ FreeScout

> Helpdesk y bandeja de entrada compartida muy ligera, alternativa abierta a Help Scout y Zendesk, en PHP y desplegable incluso en hosting compartido.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.7k | AGPL-3.0 | PHP | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; varios servicios con Docker Compose

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Helpdesk de código abierto (AGPL-3.0) del proyecto FreeScout, financiado con la venta de módulos. Maduro y activo.

## ¿Qué hace?

Centraliza conversaciones de clientes en bandejas compartidas con asignación, notas, respuestas guardadas, flujos y seguimiento; con módulos, añade WhatsApp, Telegram, Facebook, Slack, chat en vivo y otras funciones.

## ¿Cómo lo hace?

Aplicación PHP/MySQL con Laravel; se instala en hosting compartido, servidor propio o Docker. El instalador web guía la configuración.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | La API de FreeScout (módulo) o el correo permiten crear conversaciones desde flujos de Activepieces (combinación por arquitectura). | Configura el acceso por API o correo; después crea el flujo. |
| [Claude Code](claude-code.md) | Un agente de código puede ayudar a escribir módulos o scripts de migración para FreeScout (combinación por arquitectura). | Usa un entorno de pruebas; después revisa el código generado. |
| [coolify](coolify.md) | FreeScout se puede desplegar en contenedor desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con volúmenes persistentes. |

**Notas:** Alternativas (elige una): zammad.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 1.8.251 (2026-11-14) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/freescout-help-desk/freescout/blob/dist/README.md) · [2](https://freescout.net/)</sub>

## Ver similares

Grupo **Help desk y tickets**: FreeScout ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **FreeScout** (esta ficha) ⭐ recomendado | 59 | Si buscas esto: helpdesk y bandeja de entrada compartida muy ligera, alternativa abierta a Help Scout y Zendesk, en PHP y desplegable incluso en hosting compartido. |
| 2 | [Zammad](zammad.md) | 58 | Si buscas esto: sistema de helpdesk y tickets autoalojado y omnicanal: correo, chat, teléfono y redes sociales en una sola interfaz web. |

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

**Entrada documentada (bash):**

```
docker compose up -d
```

Comando copiado literalmente de la documentación oficial enlazada desde el README (sección «Pull the new image and start»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://freescout.net/docker/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FreeScout para mi objetivo y necesito pasos guiados. Lee https://freescout.net/docker/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala FreeScout en un servidor PHP o con su imagen Docker, conecta un buzón de prueba y responde a una conversación..

**Qué comprobar:** El correo aparece como conversación y la respuesta se envía desde FreeScout..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- gestionar el correo de soporte de un equipo pequeño en un hosting barato
- unificar correo, WhatsApp o Telegram de clientes con módulos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: gestionar el correo de soporte de un equipo pequeño en un hosting barato; unificar correo, WhatsApp o Telegram de clientes con módulos | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Muchos canales y funciones avanzadas dependen de módulos de pago.

## Stack y modelos

- **Stack:** PHP, composer.json, package.json
- **Etiquetas:** `helpdesk` `php` `self-hosted` `server`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Zammad](zammad.md) | 6.1k | Sistema de helpdesk y tickets autoalojado y omnicanal: correo, chat, teléfono y redes sociales en una sola interfaz web. |

## Enlaces

- 🐙 GitHub: [freescout-help-desk/freescout](https://github.com/freescout-help-desk/freescout)
- 🌐 Web: <https://freescout.net>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/freescout-help-desk/freescout/blob/dist/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
