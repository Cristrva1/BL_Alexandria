[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Alojamiento y backend

# ⚙️ Traefik Proxy

> Proxy inverso y balanceador de carga dinámico para contenedores y microservicios que se configura automáticamente desde Docker, Kubernetes y otros.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 65.6k | MIT | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proxy inverso de código abierto (MIT) de Traefik Labs, que vende productos comerciales aparte. Muy maduro.

## ¿Qué hace?

Enruta tráfico a servicios descubiertos automáticamente, con HTTPS por Let's Encrypt (incluidos comodines), balanceo, reintentos, cortacircuitos, middlewares, panel web y métricas (Prometheus, Datadog, StatsD, InfluxDB) y trazas.

## ¿Cómo lo hace?

Escrito en Go; un binario o imagen Docker oficial. La configuración estática se define en archivo o argumentos y la dinámica llega de los proveedores, por ejemplo etiquetas de Docker.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [coolify](coolify.md) | Coolify usa Traefik como proxy por defecto para sus despliegues. | Viene configurado al instalar Coolify; ajusta dominios desde el panel. |
| [Dokploy](dokploy.md) | Dokploy integra Traefik automáticamente para enrutamiento y balanceo. | Viene configurado por el instalador de Dokploy. |
| [CrowdSec](crowdsec.md) | CrowdSec ofrece un bouncer para Traefik que bloquea IP maliciosas como middleware. | CrowdSec en el servidor; después añade el bouncer como middleware de Traefik. |
| [Grafana](grafana.md) | Las métricas Prometheus de Traefik se visualizan en Grafana. | Habilita las métricas Prometheus; después crea el panel en Grafana. |
| [Portainer CE](portainer.md) | Combinación recíproca: Portainer CE lo enlaza como «Los stacks gestionados con Portainer pueden publicarse con etiquetas de Traefik (combinación por arquitectura)». | Orden indicado desde Portainer CE: Despliega Traefik; después añade las etiquetas en los stacks desde Portainer. |

**Notas:** Alternativas (elige una): caddy.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v3.7.19 (2026-11-13) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/traefik/traefik/blob/master/README.md) · [2](https://doc.traefik.io/traefik/) · [3](https://docs.crowdsec.net/u/bouncers/traefik)</sub>

## Ver similares

Grupo **Proxies inversos con HTTPS automático**: Traefik Proxy ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Caddy](caddy.md) ⭐ recomendado | 70 | Si buscas esto: servidor web y proxy inverso extensible con HTTPS automático por defecto, configurable con Caddyfile o JSON y API. |
| 2 | **Traefik Proxy** (esta ficha) | 70 | Si buscas esto: proxy inverso y balanceador de carga dinámico para contenedores y microservicios que se configura automáticamente desde Docker, Kubernetes y otros. |

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
git clone https://github.com/traefik/traefik
```

Comando copiado literalmente de el README (sección «Download»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/traefik/traefik/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Traefik Proxy para mi objetivo y necesito pasos guiados. Lee https://github.com/traefik/traefik/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca Traefik con Docker y el proveedor de Docker activado, y lanza un contenedor whoami con etiquetas de ruta..

**Qué comprobar:** El servicio responde en el dominio configurado sin reiniciar Traefik..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- publicar contenedores Docker con dominios y HTTPS mediante etiquetas
- balancear tráfico entre servicios en Kubernetes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: publicar contenedores Docker con dominios y HTTPS mediante etiquetas; balancear tráfico entre servicios en Kubernetes | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Go, Dockerfile, go.mod
- **Etiquetas:** `network` `go` `self-hosted` `server`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Caddy](caddy.md) | 79.1k | Servidor web y proxy inverso extensible con HTTPS automático por defecto, configurable con Caddyfile o JSON y API. |

## Enlaces

- 🐙 GitHub: [traefik/traefik](https://github.com/traefik/traefik)
- 🌐 Web: <https://traefik.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/traefik/traefik/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
