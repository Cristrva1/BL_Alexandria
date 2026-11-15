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
| API de IA | Sin clave propia de API de IA en la ruta básica. El gestor AGPL no necesita modelo; SMTP, entrega, servidor y dominio pueden costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. No incluye un servicio de entrega de correo gratuito por instalarlo; configura el proveedor y prueba con tu propio destinatario |
| Coste | El coste depende del proveedor o la ruta. El gestor AGPL no necesita modelo; SMTP, entrega, servidor y dominio pueden costar |
| Equipo | Preparación según la ruta elegida. Docker; PostgreSQL; SMTP de ensayo; lista ficticia |

No incluye un servicio de entrega de correo gratuito por instalarlo; configura el proveedor y prueba con tu propio destinatario

## Qué puedes hacer con él

Gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depender de un SaaS.

## Por qué destaca

Usos propuestos: Gestionar una newsletter propia; Evaluar segmentación de una lista de prueba.

## Cómo funciona

No incluye un servicio de entrega de correo gratuito por instalarlo; configura el proveedor y prueba con tu propio destinatario

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- PostgreSQL
- SMTP de ensayo
- lista ficticia

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (shell):**

```
# Download the compose file to the current directory.
curl -LO https://github.com/knadh/listmonk/raw/master/docker-compose.yml

# Run the services in the background.
docker compose up -d
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/knadh/listmonk/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar listmonk para mi objetivo y necesito pasos guiados. Lee https://github.com/knadh/listmonk/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una lista de prueba y revisa el preview de una campaña antes de un envío de ensayo propio.

**Qué comprobar:** Puedes comprobar plantilla, destinatario y estado del trabajo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Gestionar una newsletter propia
- Evaluar segmentación de una lista de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Gestionar una newsletter propia; Evaluar segmentación de una lista de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No incluye un servicio de entrega de correo gratuito por instalarlo; configura el proveedor y prueba con tu propio destinatario

## Stack y modelos

- **Stack:** Docker; PostgreSQL; SMTP de ensayo; lista ficticia
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

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/knadh/listmonk/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
