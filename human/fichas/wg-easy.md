[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Redes y transporte

# ⚙️ WireGuard Easy

> La forma más sencilla de ejecutar WireGuard VPN con interfaz web para gestionar clientes, códigos QR, estadísticas y 2FA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.5k | AGPL-3.0 | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; varios servicios con Docker Compose

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto de código abierto (AGPL-3.0) de la comunidad wg-easy. Maduro y activo; no está afiliado a WireGuard.

## ¿Qué hace?

Ejecuta un servidor WireGuard y ofrece una interfaz web para listar, crear, editar, activar y eliminar clientes, mostrar códigos QR, descargar configuraciones, ver estadísticas de tráfico, 2FA y métricas Prometheus.

## ¿Cómo lo hace?

Se despliega con Docker o Podman (Compose recomendado); necesita un puerto UDP accesible desde internet y, para HTTPS, un proxy inverso.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Grafana](grafana.md) | wg-easy expone métricas Prometheus que se pueden visualizar en Grafana. | Habilita las métricas; después configura Prometheus y Grafana. |
| [Caddy](caddy.md) | Caddy publica la interfaz web de wg-easy con HTTPS (combinación por arquitectura). | wg-easy en local; después configura reverse_proxy en Caddy. |
| [Pi-hole](pi-hole.md) | Los clientes de la VPN pueden usar Pi-hole como DNS para bloquear anuncios fuera de casa (combinación por arquitectura). | Pi-hole en la red; después define su IP como DNS de los clientes en wg-easy. |
| [Portainer CE](portainer.md) | Combinación recíproca: Portainer CE lo enlaza como «wg-easy se despliega y actualiza como stack desde Portainer (combinación por arquitectura)». | Orden indicado desde Portainer CE: Crea el stack con el Compose de wg-easy. |

**Notas:** Para redes malladas con muchos nodos, headscale o netbird encajan mejor.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada v15.5.0 (2026-10-24) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/wg-easy/wg-easy/blob/master/README.md) · [2](https://wg-easy.github.io/wg-easy/latest/)</sub>

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
sudo docker compose up / down
```

Comando copiado literalmente de la documentación del repositorio (sección «Follow tutorials»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/wg-easy/wg-easy/blob/master/docs/content/getting-started.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar WireGuard Easy para mi objetivo y necesito pasos guiados. Lee https://github.com/wg-easy/wg-easy/blob/master/docs/content/getting-started.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega wg-easy con Docker Compose según su documentación, crea un cliente y escanea el QR con la app de WireGuard..

**Qué comprobar:** El cliente se conecta y aparece activo en el panel..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- montar una VPN para acceder a tu red de casa desde el móvil
- gestionar clientes de WireGuard sin editar archivos a mano

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: montar una VPN para acceder a tu red de casa desde el móvil; gestionar clientes de WireGuard sin editar archivos a mano | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, docker-compose.yml, package.json
- **Etiquetas:** `network` `self-hosted` `docker` `vpn`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [wg-easy/wg-easy](https://github.com/wg-easy/wg-easy)
- 🌐 Web: <https://wg-easy.github.io/wg-easy/latest/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/wg-easy/wg-easy/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
