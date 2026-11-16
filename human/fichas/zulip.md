[🏠 Inicio](../README.md) › [🤖 WhatsApp, mensajería y chatbots](../categorias/17-mensajeria-chatbots.md) › Comunidades,chat y llamadas

# ⚙️ Zulip

> Chat de equipo open source con hilos por tema: combina lo mejor del email y del chat para trabajo remoto.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.2k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** hard

## ¿Qué es?

Team chat Apache-2.0 con topic threading.

## ¿Qué hace?

Mensajería organizada por streams y topics.

## ¿Cómo lo hace?

Installer/docs o cloud.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Synapse](synapse.md) | Matrix federado vs Zulip centralizado. | Elige modelo. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 13.2 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/zulip/zulip#readme) · [2](https://zulip.com)</sub>

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

[Instrucciones originales de instalación](https://github.com/zulip/zulip/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://zulip.com)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Zulip para mi objetivo y necesito pasos guiados. Lee https://github.com/zulip/zulip/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue https://zulip.readthedocs.io para un install de lab o usa Zulip Cloud de prueba..

**Qué comprobar:** Creas un stream y un topic..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- chat interno con hilos por ticket
- comunidad open source autoalojada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: chat interno con hilos por ticket; comunidad open source autoalojada | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, package.json, pyproject.toml
- **Etiquetas:** `chat` `self-hosted`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Mattermost](mattermost.md) | 39.6k | Plataforma de colaboración autoalojada y open core, alternativa a Slack: chat, automatización de flujos, llamadas, pantalla compartida e integración con IA. |
| [Rocket.Chat](rocket-chat.md) | 46.5k | Plataforma de comunicación autoalojable para equipos y atención al cliente, con chat, llamadas, federación, omnicanal y marketplace de apps. |

## Enlaces

- 🐙 GitHub: [zulip/zulip](https://github.com/zulip/zulip)
- 🌐 Web: <https://zulip.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/zulip/zulip/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
