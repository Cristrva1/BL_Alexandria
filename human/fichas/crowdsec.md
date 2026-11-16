[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Detección, SIEM e IDS

# ⚙️ CrowdSec

> IDS/IPS, WAF y detección de bots abiertos con lista de bloqueo colaborativa de IP maliciosas, para Linux, Windows, Docker y Kubernetes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.6k | MIT | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Solución de seguridad de código abierto (MIT) de CrowdSec SAS, con consola y listas premium de pago. Muy activa.

## ¿Qué hace?

Detecta comportamientos maliciosos en registros y peticiones HTTP, bloquea IP mediante componentes de remediación, incluye un WAF basado en Coraza compatible con OWASP CRS y comparte señales para alimentar una lista de bloqueo comunitaria.

## ¿Cómo lo hace?

Escrito en Go; se instala con paquetes, Docker o Helm. Las reglas y escenarios vienen del hub (MIT); los bouncers se integran con nftables/iptables, Nginx, Traefik, Cloudflare y otros. Expone métricas Prometheus.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Grafana](grafana.md) | CrowdSec expone métricas Prometheus y documenta paneles de Grafana para visualizarlas. | Habilita las métricas Prometheus; después importa el panel en Grafana. |
| [Wazuh](wazuh.md) | CrowdSec bloquea en el perímetro y Wazuh correlaciona alertas de los equipos (combinación por arquitectura). | Despliega CrowdSec; después reenvía sus registros a Wazuh. |
| [coolify](coolify.md) | Coolify usa Traefik como proxy, que puede protegerse con el bouncer de CrowdSec para Traefik (combinación por arquitectura). | CrowdSec en el servidor; después añade el bouncer como middleware de Traefik. |
| [Traefik Proxy](traefik.md) | Combinación recíproca: Traefik Proxy lo enlaza como «CrowdSec ofrece un bouncer para Traefik que bloquea IP maliciosas como middleware». | Orden indicado desde Traefik Proxy: CrowdSec en el servidor; después añade el bouncer como middleware de Traefik. |
| [Falco](falco.md) | Combinación recíproca: Falco lo enlaza como «CrowdSec bloquea IPs; Falco detecta abuso dentro del host». | Orden indicado desde Falco: Complementa red (CrowdSec) con runtime (Falco). |
| [Sigma](sigma.md) | Combinación recíproca: Sigma lo enlaza como «CrowdSec y Sigma cubren detección en red y logs». | Orden indicado desde Sigma: Despliega CrowdSec; aporta reglas Sigma al SIEM. |

**Notas:** Compartir señales con la red comunitaria es opcional; revisa qué datos se envían.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v1.8.2 (2026-10-26) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/crowdsecurity/crowdsec/blob/master/README.md) · [2](https://docs.crowdsec.net)</sub>

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
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/crowdsecurity/crowdsec/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar CrowdSec para mi objetivo y necesito pasos guiados. Lee https://github.com/crowdsecurity/crowdsec/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala CrowdSec en un servidor propio, añade la colección de SSH y un bouncer de cortafuegos, y consulta `cscli metrics`..

**Qué comprobar:** CrowdSec muestra los registros analizados y las decisiones de bloqueo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- bloquear ataques de fuerza bruta a SSH o paneles web de tu servidor
- proteger un proxy inverso con WAF y lista comunitaria de IP maliciosas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: bloquear ataques de fuerza bruta a SSH o paneles web de tu servidor; proteger un proxy inverso con WAF y lista comunitaria de IP maliciosas | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Go, go.mod
- **Etiquetas:** `security` `go` `server` `self-hosted`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [crowdsecurity/crowdsec](https://github.com/crowdsecurity/crowdsec)
- 🌐 Web: <https://docs.crowdsec.net>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/crowdsecurity/crowdsec/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
