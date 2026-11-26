[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Alojamiento y backend

# ⚙️ Uptime Kuma

> Monitor de disponibilidad autoalojado y fácil de usar: comprueba webs y servicios, envía alertas a más de 90 canales y publica páginas de estado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 94.5k | MIT | JavaScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 76/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de monitorización de código abierto (MIT) creada por Louis Lam. Uno de los proyectos autoalojados más populares; activa.

## ¿Qué hace?

Monitoriza HTTP(S), palabras clave, JSON, TCP, ping, DNS, Docker, bases de datos y más, con intervalos de hasta 20 segundos, notificaciones por Telegram, Discord, Slack, correo y más de 90 servicios, páginas de estado con dominio propio, certificados y 2FA.

## ¿Cómo lo hace?

Escrito en JavaScript/Node.js; se despliega con `docker run` o Docker Compose, o en local con Node.js. Expone métricas Prometheus.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Grafana](grafana.md) | Uptime Kuma expone métricas Prometheus que se pueden visualizar en Grafana. | Configura Prometheus para leer /metrics; después crea el panel en Grafana. |
| [coolify](coolify.md) | Uptime Kuma se puede desplegar en contenedor desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con volúmenes persistentes. |
| [Caddy](caddy.md) | Caddy publica la interfaz y las páginas de estado de Uptime Kuma con HTTPS automático (combinación por arquitectura). | Uptime Kuma en el puerto local; después configura un reverse_proxy en Caddy. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (6). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Dokploy](dokploy.md) · [frp](frp.md) · [Headscale](headscale.md) · [NetBird](netbird.md) · [Portainer CE](portainer.md) · [signal-cli](signal-cli.md)

**Notas:** No sustituye a una monitorización completa de métricas y registros.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 2.5.11 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/louislam/uptime-kuma/blob/master/README.md) · [2](https://github.com/louislam/uptime-kuma/wiki/Prometheus-Integration)</sub>

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
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2
```

Comando copiado literalmente de el README (sección «🐳 Docker Command»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/louislam/uptime-kuma/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Uptime Kuma para mi objetivo y necesito pasos guiados. Lee https://github.com/louislam/uptime-kuma/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca Uptime Kuma con el `docker run` del README, añade un monitor HTTP para una web propia y configura una notificación..

**Qué comprobar:** El panel muestra el monitor en verde y el historial de tiempos de respuesta..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- recibir un aviso en Telegram cuando tu web o servidor cae
- publicar una página de estado de tus servicios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: recibir un aviso en Telegram cuando tu web o servidor cae; publicar una página de estado de tus servicios | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** JavaScript, compose.yaml, package.json
- **Etiquetas:** `monitoring` `self-hosted` `javascript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma)
- 🌐 Web: <https://uptime.kuma.pet>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/louislam/uptime-kuma/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
