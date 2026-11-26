[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Detección, SIEM e IDS

# ⚙️ Pi.Alert

> Lleva un inventario de dispositivos de una red propia y avisa cuando aparece uno nuevo o deja de responder uno conocido.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.4k | GPL-3.0 | PHP | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 47/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Monitor de dispositivos para una red propia que muestra cambios en su interfaz web.

## ¿Qué hace?

Lleva un inventario de dispositivos de una red propia y avisa cuando aparece uno nuevo o deja de responder uno conocido.

## ¿Cómo lo hace?

Usa métodos de descubrimiento de red como ARP y puede importar datos de otros servicios; guarda el inventario y los eventos en el servidor.

Estado en GitHub: activo · último push 2026-10-16 · última versión publicada v2026-10-16 (2026-10-16) · licencia declarada GPL-3.0 (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/leiweibau/Pi.Alert/blob/850e40a90871816161559e136e703cf68c1c994a/README.md) · [2](https://github.com/leiweibau/Pi.Alert/blob/850e40a90871816161559e136e703cf68c1c994a/docs/SECURITY.md) · [3](https://github.com/leiweibau/Pi.Alert/blob/850e40a90871816161559e136e703cf68c1c994a/install/pialert_install.sh) · [4](https://github.com/leiweibau/Pi.Alert/blob/850e40a90871816161559e136e703cf68c1c994a/docs/NETWORK_RELATIONSHIP.md) · [5](https://github.com/leiweibau/Pi.Alert/releases/tag/v2026-10-16) · [6](https://github.com/leiweibau/Pi.Alert/blob/main/LICENSE.txt) · [7](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-vmjp-664r-67rw) · [8](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-f58p-mp38-66qv) · [9](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-ff6r-j7j6-gfx8) · [10](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-vp5h-q268-p65m) · [11](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-66mg-wpcq-2phq) · [12](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-xg85-f8qw-7c5f) · [13](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-r59g-5wf9-f7vv) · [14](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-m929-j7w8-334j)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La primera prueba no llama a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función descrita no depende de un modelo de IA. |
| Coste | El coste depende del proveedor o la ruta. Código GPL-3.0 y sin API ni modelo de IA. Consume el equipo del monitor; los canales o servicios de aviso que conectes pueden tener costes propios. |
| Equipo | Preparación según la ruta elegida. Equipo Debian compatible en la red propia, acceso administrativo para preparar el servidor y un segmento de prueba. |

La ruta descrita no utiliza una suscripción de IA.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Equipo Debian compatible en la red propia, acceso administrativo para preparar el servidor y un segmento de prueba.

1. Revisa el instalador de la etiqueta v2026-10-16 y la guía de seguridad. Prepara un equipo Debian dedicado en una red de prueba.
2. Activa la protección de la interfaz y observa únicamente la llegada o salida de un equipo propio conocido.
3. Comprueba el resultado: el evento aparece en el inventario y la interfaz solo es accesible desde la red autorizada.

Consulta la guía vinculada y la versión revisada. No se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/leiweibau/Pi.Alert/blob/850e40a90871816161559e136e703cf68c1c994a/docs/SECURITY.md)

[Abrir la web o descarga indicada por el autor](https://github.com/leiweibau/Pi.Alert/blob/850e40a90871816161559e136e703cf68c1c994a/docs/SECURITY.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Pi.Alert para mi objetivo y necesito pasos guiados. Lee https://github.com/leiweibau/Pi.Alert/blob/850e40a90871816161559e136e703cf68c1c994a/docs/SECURITY.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Activa la protección de la interfaz y observa únicamente la llegada o salida de un equipo propio conocido..

**Qué comprobar:** El evento aparece en el inventario y la interfaz solo es accesible desde la red autorizada..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Identificar un dispositivo nuevo en una red de prueba.
- Verificar si se registra la desconexión de un dispositivo ya conocido.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Identificar un dispositivo nuevo en una red de prueba.; Verificar si se registra la desconexión de un dispositivo ya conocido. | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** El instalador modifica servicios del sistema y el escaneo usa permisos elevados. La corrección inicial de mayo fue incompleta; el seguimiento GHSA-66mg-wpcq-2phq fija v2026-08-14 como corregida. La etiqueta v2026-10-16 la incorpora. No publiques la interfaz en internet. La revisión no acredita ausencia de fallos ni una instalación probada.

## Stack y modelos

- **Stack:** PHP
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [leiweibau/Pi.Alert](https://github.com/leiweibau/Pi.Alert)
- 🌐 Web: <https://leiweibau.net>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/leiweibau/Pi.Alert/blob/850e40a90871816161559e136e703cf68c1c994a/README.md)
- [Fuente 2](https://github.com/leiweibau/Pi.Alert/blob/850e40a90871816161559e136e703cf68c1c994a/docs/SECURITY.md)
- [Fuente 3](https://github.com/leiweibau/Pi.Alert/blob/850e40a90871816161559e136e703cf68c1c994a/install/pialert_install.sh)
- [Fuente 4](https://github.com/leiweibau/Pi.Alert/blob/850e40a90871816161559e136e703cf68c1c994a/docs/NETWORK_RELATIONSHIP.md)
- [Fuente 5](https://github.com/leiweibau/Pi.Alert/releases/tag/v2026-10-16)
- [Fuente 6](https://github.com/leiweibau/Pi.Alert/blob/main/LICENSE.txt)
- [Fuente 7](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-vmjp-664r-67rw)
- [Fuente 8](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-f58p-mp38-66qv)
- [Fuente 9](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-ff6r-j7j6-gfx8)
- [Fuente 10](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-vp5h-q268-p65m)
- [Fuente 11](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-66mg-wpcq-2phq)
- [Fuente 12](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-xg85-f8qw-7c5f)
- [Fuente 13](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-r59g-5wf9-f7vv)
- [Fuente 14](https://github.com/leiweibau/Pi.Alert/security/advisories/GHSA-m929-j7w8-334j)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
