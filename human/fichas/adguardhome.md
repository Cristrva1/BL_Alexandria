[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Credenciales y privacidad

# ⚙️ AdGuardHome

> Servidor DNS para filtrar anuncios y rastreadores de los dispositivos de una red desde una configuración central.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.5k | GPL-3.0 | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

Servidor DNS de bloqueo de anuncios y rastreadores para toda la red, de AdGuard. Licencia GPL-3.0. Es muy maduro (~38k estrellas, v0.107.80) y sigue en la serie 0.107 desde hace años.

## ¿Qué hace?

Actúa como servidor DNS de la red y bloquea dominios de anuncios, rastreo y malware para todos los dispositivos sin instalar nada en ellos. Admite listas de bloqueo, reglas propias, control parental, búsqueda segura y estadísticas por cliente. Ofrece DNS cifrado (DNS-over-HTTPS, DNS-over-TLS, DNSCrypt), reescrituras DNS locales y servidor DHCP opcional.

## ¿Cómo lo hace?

Es un binario único en Go con interfaz web (TypeScript). Se instala con el script oficial, con Docker (`adguard/adguardhome`), con Snap o descargando el binario; después un asistente web configura los puertos. Requiere que los dispositivos o el router usen su IP como DNS, y expone una API HTTP documentada en OpenAPI.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Home Assistant](home-assistant.md) | Ver estadísticas y activar o desactivar filtros desde Home Assistant con la integración oficial de AdGuard Home. | Instala AdGuard Home y añade la integración con su URL y credenciales. |
| [activepieces](activepieces.md) | Automatizar tareas (pausar el filtrado, añadir reglas) llamando a la API HTTP de AdGuard Home. (combinación por arquitectura) | Crea un usuario de AdGuard Home y usa la pieza HTTP de Activepieces contra su API. |
| [vaultwarden](vaultwarden.md) | Dar un nombre local (p. ej. `vault.casa`) a los servicios autoalojados con las reescrituras DNS de AdGuard Home. (combinación por arquitectura) | Configura la reescritura DNS hacia el proxy inverso que publica Vaultwarden con HTTPS. |
| [CasaOS](casaos.md) | Combinación recíproca: CasaOS lo enlaza como «DNS con bloqueo de anuncios para la red de casa. (combinación por arquitectura)». | Orden indicado desde CasaOS: Instálalo como app. |
| [cleanyourtv](cleanyourtv.md) | Combinación recíproca: cleanyourtv lo enlaza como «Bloquear por DNS los dominios de telemetría y anuncios que queden activos. (combinación por arquitectura)». | Orden indicado desde cleanyourtv: Pon AdGuard Home como DNS de la red antes o después de limpiar el televisor. |
| [optimizerDuck](optimizerduck.md) | Combinación recíproca: optimizerDuck lo enlaza como «Bloqueo de telemetría a nivel de red que complementa los ajustes locales. (combinación por arquitectura)». | Orden indicado desde optimizerDuck: Configura AdGuard Home como DNS y luego aplica los ajustes de privacidad en Windows. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[universal-android-debloater-next-generation](universal-android-debloater-next-generation.md)

**Notas:** Sin alternativas declaradas en el catálogo (Pi-hole no está catalogado). Bloquear por DNS no sustituye a un bloqueador en el navegador.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v0.107.80 (2026-11-03) · licencia declarada GPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/AdguardTeam/AdGuardHome/blob/master/README.md) · [2](https://adguard-dns.io/kb/adguard-home/getting-started/) · [3](https://github.com/AdguardTeam/AdGuardHome/wiki/Getting-Started) · [4](https://github.com/AdguardTeam/AdGuardHome/tree/master/openapi) · [5](https://www.home-assistant.io/integrations/adguard/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere modelo; servidor, DNS externos y recursos de red tienen condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El filtrado DNS no bloquea todo anuncio ni sustituye otras protecciones; no cambies toda la red para la primera prueba |
| Coste | Sin pago a un modelo en la ruta básica. No requiere modelo; servidor, DNS externos y recursos de red tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Equipo servidor; acceso de configuración DNS; cliente de prueba |

El filtrado DNS no bloquea todo anuncio ni sustituye otras protecciones; no cambies toda la red para la primera prueba

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Equipo servidor
- acceso de configuración DNS
- cliente de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/AdguardTeam/AdGuardHome/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AdGuardHome para mi objetivo y necesito pasos guiados. Lee https://github.com/AdguardTeam/AdGuardHome/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un único dispositivo de prueba y revisa una consulta en el registro DNS.

**Qué comprobar:** Puedes identificar si el dominio se permitió o bloqueó y por qué regla.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Filtrar dominios en una red propia
- Estudiar consultas y reglas DNS

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Filtrar dominios en una red propia; Estudiar consultas y reglas DNS | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El filtrado DNS no bloquea todo anuncio ni sustituye otras protecciones; no cambies toda la red para la primera prueba

## Stack y modelos

- **Stack:** Equipo servidor; acceso de configuración DNS; cliente de prueba
- **Etiquetas:** `privacidad` `server` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [AdguardTeam/AdGuardHome](https://github.com/AdguardTeam/AdGuardHome)
- 🌐 Web: <https://adguard.com/adguard-home/overview.html>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/AdguardTeam/AdGuardHome/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
