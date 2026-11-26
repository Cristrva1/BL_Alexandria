[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Alojamiento y backend

# ⚙️ Portainer CE

> Interfaz web ligera para gestionar contenedores en Docker, Swarm, Podman, Kubernetes y ACI (Community Edition).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.8k | Zlib | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 71/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Gestor de contenedores de código abierto (zlib) de Portainer.io. La Community Edition es gratuita y la Business Edition añade funciones de pago sobre la misma base. Muy maduro.

## ¿Qué hace?

Gestiona contenedores, imágenes, redes, volúmenes, stacks de Compose y recursos de Kubernetes con interfaz gráfica, plantillas de aplicaciones, registros, consola y control de acceso básico.

## ¿Cómo lo hace?

Escrito en Go con frontend web; se instala como contenedor con acceso al socket de Docker o con agentes y Helm para Kubernetes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Traefik Proxy](traefik.md) | Los stacks gestionados con Portainer pueden publicarse con etiquetas de Traefik (combinación por arquitectura). | Despliega Traefik; después añade las etiquetas en los stacks desde Portainer. |
| [Uptime Kuma](uptime-kuma.md) | Uptime Kuma, desplegado como stack desde Portainer, vigila los servicios del host (combinación por arquitectura). | Crea el stack de Uptime Kuma en Portainer; después añade monitores. |
| [WireGuard Easy](wg-easy.md) | wg-easy se despliega y actualiza como stack desde Portainer (combinación por arquitectura). | Crea el stack con el Compose de wg-easy. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Dagger](dagger.md)

**Notas:** Dar a Portainer acceso al socket de Docker equivale a acceso de administrador al host.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 2.45.3 (2026-10-21) · licencia declarada Zlib (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/portainer/portainer/blob/release/2.45/README.md) · [2](https://docs.portainer.io/start/install-ce)</sub>

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

[Instrucciones originales de instalación](https://github.com/portainer/portainer/blob/release/2.45/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Portainer CE para mi objetivo y necesito pasos guiados. Lee https://github.com/portainer/portainer/blob/release/2.45/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega Portainer CE con Docker según su guía, crea el usuario administrador y revisa los contenedores locales..

**Qué comprobar:** El panel lista los contenedores con su estado y registros..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- administrar los contenedores de tu homelab desde el navegador
- desplegar stacks de Docker Compose con interfaz gráfica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: administrar los contenedores de tu homelab desde el navegador; desplegar stacks de Docker Compose con interfaz gráfica | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Community Edition gratuita; RBAC avanzado, GitOps, edge, auditoría y SSO forman parte de Business Edition (de pago).

## Stack y modelos

- **Stack:** TypeScript, go.mod, package.json
- **Etiquetas:** `containers` `go` `self-hosted` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [portainer/portainer](https://github.com/portainer/portainer)
- 🌐 Web: <https://www.portainer.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/portainer/portainer/blob/release/2.45/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
