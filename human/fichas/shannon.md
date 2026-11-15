[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Análisis y pruebas con agentes

# 🖥️ shannon

> Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autorizado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 51.9k | AGPL-3.0 | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos. |
| Claude Code | Integración no documentada |
| Codex | Integración documentada por el proyecto |
| Modelos locales | Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. |
| Equipo | Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

El README documenta una ruta de autenticación de Codex. Comprueba la configuración y las limitaciones de esa ruta; otras funciones y proveedores se configuran aparte. La versión actual declara que no usa suscripciones de Claude Code; la documentación remite a 1.9.0 para la ruta antigua.

## Qué puedes hacer con él

Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autorizado.

## Cómo funciona

La aplicación coordina modelos y herramientas; el acceso de cada componente se configura antes de ejecutar sus tareas.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Prepara una aplicación propia de laboratorio y el alcance de prueba antes de configurar el agente.
2. Elige el proveedor: la versión actual documenta Codex, APIs y modelos locales; la ruta de suscripción de Claude Code corresponde a una versión antigua.
3. Ejecuta una comprobación pequeña en el laboratorio y revisa la evidencia y el consumo antes de ampliar el alcance.

[Instrucciones originales de instalación](https://github.com/KeygraphHQ/shannon/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar shannon para mi objetivo y necesito pasos guiados. Lee https://github.com/KeygraphHQ/shannon/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autorizado.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| buscas esta función: Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autorizado. | necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas y modificaciones requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, docker-compose.yml, package.json
- **Etiquetas:** `agentes` `agent` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon)
- 🌐 Web: <https://keygraph.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/KeygraphHQ/shannon/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
