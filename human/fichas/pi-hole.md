[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Credenciales y privacidad

# ⚙️ Pi-hole

> Sumidero DNS para bloquear anuncios y rastreadores en toda la red sin instalar nada en los dispositivos, con panel web y DHCP opcional.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 62k | EUPL-1.2 | Shell | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Bloqueador de anuncios por DNS de código abierto (EUPL-1.2 según su archivo de licencia) mantenido por Pi-hole LLC y la comunidad desde 2014. Muy maduro.

## ¿Qué hace?

Actúa como DNS de la red y descarta las peticiones a dominios de anuncios y rastreo, incluido en apps y TV donde no hay extensiones; acelera la navegación con caché, ofrece panel web con estadísticas, CLI, DHCP opcional e IPv4/IPv6.

## ¿Cómo lo hace?

Se instala con `curl -sSL https://install.pi-hole.net | bash` en Linux (Raspberry Pi incluido) o con la imagen Docker oficial. Requisitos mínimos de hardware; se configura con listas de bloqueo y listas de permitidos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Home Assistant](home-assistant.md) | Home Assistant tiene una integración oficial de Pi-hole para ver estadísticas y activar o desactivar el bloqueo. | Pi-hole en marcha con su clave de API; después añade la integración en Home Assistant. |
| [Grafana](grafana.md) | Las estadísticas de Pi-hole se pueden exportar a Prometheus con un exportador de la comunidad y verse en Grafana (combinación por arquitectura). | Configura un exportador de métricas de Pi-hole; después añade la fuente y el panel en Grafana. |
| [coolify](coolify.md) | La imagen Docker de Pi-hole se puede desplegar desde Coolify en un servidor de la red local (combinación por arquitectura). | Coolify primero; después despliega Pi-hole exponiendo el puerto DNS. |
| [WireGuard Easy](wg-easy.md) | Combinación recíproca: WireGuard Easy lo enlaza como «Los clientes de la VPN pueden usar Pi-hole como DNS para bloquear anuncios fuera de casa (combinación por arquitectura)». | Orden indicado desde WireGuard Easy: Pi-hole en la red; después define su IP como DNS de los clientes en wg-easy. |

**Notas:** Alternativas (elige una): adguardhome. Instalar con `curl | bash` ejecuta un script remoto: revísalo antes.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v6.6 (2026-11-11) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/pi-hole/pi-hole/blob/master/README.md) · [2](https://docs.pi-hole.net/) · [3](https://www.home-assistant.io/integrations/pi_hole/)</sub>

## Ver similares

Grupo **Bloqueo de anuncios por DNS**: Pi-hole ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Pi-hole** (esta ficha) ⭐ recomendado | 68 | Si buscas esto: sumidero DNS para bloquear anuncios y rastreadores en toda la red sin instalar nada en los dispositivos, con panel web y DHCP opcional. |
| 2 | [AdGuardHome](adguardhome.md) | 59 | Si buscas esto: servidor DNS para filtrar anuncios y rastreadores de los dispositivos de una red desde una configuración central. |

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
curl -sSL https://install.pi-hole.net | bash
```

Comando copiado literalmente de el README (sección «One-Step Automated Install»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/pi-hole/pi-hole/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Pi-hole para mi objetivo y necesito pasos guiados. Lee https://github.com/pi-hole/pi-hole/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Pi-hole en una máquina Linux de prueba o contenedor y apunta el DNS de un equipo a ella..

**Qué comprobar:** El panel muestra consultas bloqueadas y las webs cargan sin anuncios..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- bloquear anuncios en smart TV y apps móviles de toda la casa
- ver qué dominios consultan los dispositivos de tu red

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: bloquear anuncios en smart TV y apps móviles de toda la casa; ver qué dominios consultan los dispositivos de tu red | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Shell
- **Etiquetas:** `privacy` `self-hosted` `shell` `server`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [AdGuardHome](adguardhome.md) | 38.5k | Servidor DNS para filtrar anuncios y rastreadores de los dispositivos de una red desde una configuración central. |

## Enlaces

- 🐙 GitHub: [pi-hole/pi-hole](https://github.com/pi-hole/pi-hole)
- 🌐 Web: <https://pi-hole.net>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pi-hole/pi-hole/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
