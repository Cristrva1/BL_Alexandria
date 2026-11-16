[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Alojamiento y backend

# ⚙️ CasaOS

> Entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 37.6k | Apache-2.0 | Go | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

CasaOS, sistema para nube personal sobre Docker, de IceWhaleTech (ZimaSpace). Licencia Apache-2.0. Tiene ~38k estrellas, pero su última release es v0.4.15 (diciembre de 2024), aunque el repo sigue recibiendo cambios.

## ¿Qué hace?

Ofrece un panel web para gestionar un servidor doméstico, archivos y una tienda de apps con instalación en un clic, además de acceso a miles de apps del ecosistema Docker. Funciona en ZimaBoard, NUC, Raspberry Pi o equipos viejos.

## ¿Cómo lo hace?

Se instala con un script en Debian, Ubuntu, Raspberry Pi OS y similares, y requiere Docker.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [server](nextcloud-server.md) | Nube de archivos como app. (combinación por arquitectura) | Instala Nextcloud desde la tienda o como contenedor. |
| [AdGuardHome](adguardhome.md) | DNS con bloqueo de anuncios para la red de casa. (combinación por arquitectura) | Instálalo como app. |
| [activepieces](activepieces.md) | Automatizaciones en el servidor doméstico. (combinación por arquitectura) | Instálalo como contenedor. |

**Notas:** Alternativa (elige una): coolify. Ritmo de releases lento.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada v0.4.15 (2024-12-19) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/IceWhaleTech/CasaOS/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita API de IA; equipo, discos y energía se pagan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La instalación modifica el servidor y debe seguir requisitos del autor; las apps de su catálogo tienen condiciones independientes |
| Coste | Sin pago a un modelo en la ruta básica. No necesita API de IA; equipo, discos y energía se pagan aparte |
| Equipo | Preparación según la ruta elegida. Servidor Linux compatible; disco y red; respaldo del equipo antes de instalar |

La instalación modifica el servidor y debe seguir requisitos del autor; las apps de su catálogo tienen condiciones independientes

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Servidor Linux compatible
- disco y red
- respaldo del equipo antes de instalar

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/IceWhaleTech/CasaOS/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar CasaOS para mi objetivo y necesito pasos guiados. Lee https://github.com/IceWhaleTech/CasaOS/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Consulta compatibilidad y prueba el panel en un equipo de laboratorio antes de instalar apps.

**Qué comprobar:** Puedes identificar almacenamiento y una app de prueba.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar servicios domésticos
- Explorar un servidor personal

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar servicios domésticos; Explorar un servidor personal | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La instalación modifica el servidor y debe seguir requisitos del autor; las apps de su catálogo tienen condiciones independientes

## Stack y modelos

- **Stack:** Servidor Linux compatible; disco y red; respaldo del equipo antes de instalar
- **Etiquetas:** `infraestructura` `server` `go`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [coolify](coolify.md) | 66.1k | Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios. |

## Enlaces

- 🐙 GitHub: [IceWhaleTech/CasaOS](https://github.com/IceWhaleTech/CasaOS)
- 🌐 Web: <https://casaos.zimaspace.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/IceWhaleTech/CasaOS/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
