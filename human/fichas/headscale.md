[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Redes y transporte

# ⚙️ Headscale

> Implementación abierta y autoalojada del servidor de control de Tailscale para crear tu propia red privada WireGuard con los clientes oficiales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 45.8k | BSD-3-Clause | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Servidor de control de código abierto (BSD-3-Clause) mantenido por la comunidad (Juan Font, Kristoffer Dalby y otros). Maduro; alcance deliberadamente acotado a una sola tailnet para uso personal o pequeñas organizaciones.

## ¿Qué hace?

Reemplaza el servidor de coordinación de Tailscale: registra nodos, distribuye claves y rutas, gestiona usuarios, ACL, DNS (MagicDNS), nodos de salida y rutas de subred, con autenticación OIDC opcional.

## ¿Cómo lo hace?

Escrito en Go; se instala con paquetes, binario o contenedor y se configura con YAML. Los clientes son los de Tailscale (código abierto salvo las GUI de Windows, macOS e iOS). Expone métricas Prometheus.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Caddy](caddy.md) | La documentación de Headscale incluye ejemplos para ejecutarlo detrás de Caddy como proxy inverso. | Headscale en local; después configura Caddy con el bloque de proxy documentado. |
| [Grafana](grafana.md) | Headscale expone métricas Prometheus que se pueden visualizar en Grafana. | Habilita metrics_listen_addr; después configura Prometheus y Grafana. |
| [Uptime Kuma](uptime-kuma.md) | Uptime Kuma vigila la disponibilidad del servidor de control (combinación por arquitectura). | Añade un monitor HTTP del endpoint de Headscale. |

**Notas:** Alternativas (elige una): netbird. No es un producto oficial de Tailscale.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.29.7 (2026-10-30) · licencia declarada BSD-3-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/juanfont/headscale/blob/main/README.md) · [2](https://headscale.net/stable/ref/integration/reverse-proxy/) · [3](https://headscale.net/stable/ref/configuration/)</sub>

## Ver similares

Grupo **Redes privadas tipo mesh (WireGuard)**: Headscale ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Headscale** (esta ficha) ⭐ recomendado | 67 | Si buscas esto: implementación abierta y autoalojada del servidor de control de Tailscale para crear tu propia red privada WireGuard con los clientes oficiales. |
| 2 | [NetBird](netbird.md) | 63 | Si buscas esto: red privada superpuesta basada en WireGuard con SSO, MFA y control de acceso granular, autoalojable o en la nube. |

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

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/juanfont/headscale/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Headscale para mi objetivo y necesito pasos guiados. Lee https://github.com/juanfont/headscale/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Headscale en un servidor siguiendo su documentación, crea un usuario y registra un cliente de Tailscale con `--login-server`..

**Qué comprobar:** El dispositivo aparece en `headscale nodes list` y alcanza a otros nodos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- conectar tus equipos y servidores en una red privada sin depender del servicio de Tailscale
- dar acceso remoto a una red doméstica o de laboratorio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: conectar tus equipos y servidores en una red privada sin depender del servicio de Tailscale; dar acceso remoto a una red doméstica o de laboratorio | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Go, go.mod
- **Etiquetas:** `network` `go` `self-hosted` `vpn`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [NetBird](netbird.md) | 31k | Red privada superpuesta basada en WireGuard con SSO, MFA y control de acceso granular, autoalojable o en la nube. |

## Enlaces

- 🐙 GitHub: [juanfont/headscale](https://github.com/juanfont/headscale)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/juanfont/headscale/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
