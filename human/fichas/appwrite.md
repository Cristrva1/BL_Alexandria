[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Alojamiento y backend

# ⚙️ Appwrite

> Plataforma de backend abierta orientada a agentes y desarrolladores: autenticación, bases de datos, almacenamiento, funciones, mensajería, tiempo real y hosting, con MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 58.1k | BSD-3-Clause | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de backend de código abierto (BSD-3-Clause) de Appwrite, que ofrece también una nube gestionada. Muy popular y activa.

## ¿Qué hace?

Proporciona autenticación, bases de datos (propias o PostgreSQL/MySQL gestionados), almacenamiento, funciones serverless, mensajería, tiempo real, hosting de frontends (Sites) y un servidor MCP para que los agentes de código operen proyectos vivos.

## ¿Cómo lo hace?

Se autoaloja con Docker (un `docker run` que instala la pila de contenedores) o se usa en Appwrite Cloud. Ofrece SDK cliente y servidor para web, móvil y backend.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Appwrite incluye un servidor MCP para conectar agentes como Claude Code a un proyecto vivo. | Crea el proyecto y una clave; después registra el servidor MCP en Claude Code. |
| [Codex CLI](codex.md) | El README cita Codex entre los agentes que se conectan por el servidor MCP de Appwrite. | Configura el servidor MCP de Appwrite en Codex. |
| [coolify](coolify.md) | Appwrite se puede desplegar en contenedor desde Coolify (combinación por arquitectura). | Coolify primero; después crea el servicio con volúmenes persistentes. |

**Notas:** Alternativas (elige una): supabase.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 2.7.2 (2026-11-12) · licencia declarada BSD-3-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/appwrite/appwrite/blob/main/README.md) · [2](https://appwrite.io/docs)</sub>

## Ver similares

Grupo **Backends como servicio auto-hospedados**: Appwrite ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [supabase](supabase.md) ⭐ recomendado | 76 | Si buscas esto: plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones. |
| 2 | **Appwrite** (esta ficha) | 72 | Si buscas esto: plataforma de backend abierta orientada a agentes y desarrolladores: autenticación, bases de datos, almacenamiento, funciones, mensajería, tiempo real y hosting, con MCP. |

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
docker run -it --rm --publish 127.0.0.1:20080:20080 --volume /var/run/docker.sock:/var/run/docker.sock --volume "$(pwd)"/appwrite:/usr/src/code/appwrite:rw --entrypoint="install" appwrite/appwrite:2.7.2
```

Comando copiado literalmente de el README (sección «Unix»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/appwrite/appwrite/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Appwrite para mi objetivo y necesito pasos guiados. Lee https://github.com/appwrite/appwrite/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lanza Appwrite con el `docker run` del README, crea un proyecto y un usuario de prueba..

**Qué comprobar:** El panel muestra el proyecto con autenticación y base de datos listas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- dar backend completo a una app web o móvil sin escribir servidor
- dejar que un agente de código opere un proyecto de backend vía MCP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: dar backend completo a una app web o móvil sin escribir servidor; dejar que un agente de código opere un proyecto de backend vía MCP | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, Cargo.toml, Dockerfile, composer.json, docker-compose.yml, package.json
- **Etiquetas:** `backend` `self-hosted` `docker` `mcp`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [supabase](supabase.md) | 115k | Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones. |

## Enlaces

- 🐙 GitHub: [appwrite/appwrite](https://github.com/appwrite/appwrite)
- 🌐 Web: <https://appwrite.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/appwrite/appwrite/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
