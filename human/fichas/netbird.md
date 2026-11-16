[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Redes y transporte

# ⚙️ NetBird

> Red privada superpuesta basada en WireGuard con SSO, MFA y control de acceso granular, autoalojable o en la nube.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31k | BSD-3-Clause + AGPL-3.0 (management, signal, relay) | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de red de código abierto de NetBird GmbH. El repositorio es BSD-3-Clause salvo management/, signal/ y relay/, que son AGPL-3.0. Muy activa, con nube de pago.

## ¿Qué hace?

Conecta máquinas mediante túneles WireGuard cifrados sin abrir puertos, con descubrimiento automático de pares, SSO y MFA, grupos y reglas de acceso, rutas de red, DNS, comprobaciones de postura y panel de administración.

## ¿Cómo lo hace?

Escrito en Go; el cliente se instala en Linux, Windows, macOS, Android e iOS. El servidor se autoaloja con Docker Compose siguiendo la guía de inicio rápido (incluye proveedor de identidad y proxy).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Grafana](grafana.md) | Los servicios de NetBird exponen métricas que se pueden visualizar en Grafana (combinación por arquitectura). | Configura Prometheus para leer las métricas; después crea el panel. |
| [Uptime Kuma](uptime-kuma.md) | Uptime Kuma vigila los servicios de gestión y relay de NetBird (combinación por arquitectura). | Añade monitores HTTP y TCP para sus endpoints. |
| [coolify](coolify.md) | El servidor de NetBird se puede desplegar en contenedor desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con volúmenes persistentes. |

**Notas:** Alternativas (elige una): headscale.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.83.1 (2026-11-13) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/netbirdio/netbird/blob/main/README.md) · [2](https://docs.netbird.io/)</sub>

## Ver similares

Grupo **Redes privadas tipo mesh (WireGuard)**: NetBird ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Headscale](headscale.md) ⭐ recomendado | 69 | Si buscas esto: implementación abierta y autoalojada del servidor de control de Tailscale para crear tu propia red privada WireGuard con los clientes oficiales. |
| 2 | **NetBird** (esta ficha) | 63 | Si buscas esto: red privada superpuesta basada en WireGuard con SSO, MFA y control de acceso granular, autoalojable o en la nube. |

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

[Instrucciones originales de instalación](https://github.com/netbirdio/netbird/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar NetBird para mi objetivo y necesito pasos guiados. Lee https://github.com/netbirdio/netbird/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue la guía de autoalojamiento rápido de NetBird en un VPS y conecta dos dispositivos con el cliente..

**Qué comprobar:** Ambos dispositivos aparecen en el panel y se alcanzan por la red privada..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- conectar servidores y equipos remotos sin abrir puertos
- dar acceso a la red interna con SSO y políticas por grupo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: conectar servidores y equipos remotos sin abrir puertos; dar acceso a la red interna con SSO y políticas por grupo | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Los servicios de servidor (management, signal, relay) son AGPL-3.0; el resto, BSD-3-Clause.

## Stack y modelos

- **Stack:** Go, go.mod
- **Etiquetas:** `network` `go` `self-hosted` `vpn`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Headscale](headscale.md) | 45.8k | Implementación abierta y autoalojada del servidor de control de Tailscale para crear tu propia red privada WireGuard con los clientes oficiales. |

## Enlaces

- 🐙 GitHub: [netbirdio/netbird](https://github.com/netbirdio/netbird)
- 🌐 Web: <https://netbird.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/netbirdio/netbird/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
