[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Inteligencia de fuentes abiertas y mapas

# 🖥️ Recon-ng

> Framework modular de reconocimiento web OSINT con espacios de trabajo, base de datos y módulos al estilo de Metasploit.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6k | GPL-3.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Framework de reconocimiento de código abierto (GPL-3.0) creado por Tim Tomes (lanmaster53). Maduro, con ritmo de cambios bajo (último push en octubre de 2026).

## ¿Qué hace?

Ofrece un entorno para hacer reconocimiento basado en fuentes abiertas de forma rápida y ordenada: módulos de descubrimiento, reconocimiento, informes e importación, espacios de trabajo con base de datos, claves de API centralizadas e informes.

## ¿Cómo lo hace?

Escrito en Python; se instala clonando el repositorio y sus requisitos. Los módulos se instalan desde un marketplace aparte; la interfaz recuerda a Metasploit y tiene también una interfaz web para informes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [theHarvester](theharvester.md) | theHarvester aporta correos y subdominios que se pueden importar como semillas en un espacio de trabajo de Recon-ng (combinación por arquitectura). | Ejecuta theHarvester; después importa los resultados en Recon-ng. |
| [DuckDB](duckdb.md) | La base SQLite de cada espacio de trabajo se puede consultar con DuckDB para cruzar resultados (combinación por arquitectura). | Localiza la base del espacio de trabajo; después ábrela en DuckDB en solo lectura. |
| [Claude Code](claude-code.md) | Un agente puede escribir módulos nuevos en Python siguiendo la guía de desarrollo del framework (combinación por arquitectura). | Lee la guía de desarrollo; después pide al agente el módulo y pruébalo en un espacio de trabajo aislado. |

**Notas:** Ritmo de mantenimiento bajo: comprueba que los módulos que necesitas siguen funcionando.

Estado en GitHub: activo · último push 2026-10-05 · licencia declarada GPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/lanmaster53/recon-ng/blob/master/README.md) · [2](https://github.com/lanmaster53/recon-ng/wiki)</sub>

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

[Instrucciones originales de instalación](https://github.com/lanmaster53/recon-ng/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Recon-ng para mi objetivo y necesito pasos guiados. Lee https://github.com/lanmaster53/recon-ng/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala las dependencias del README, crea un espacio de trabajo e instala un módulo pasivo del marketplace..

**Qué comprobar:** El módulo se ejecuta y sus resultados aparecen en la tabla correspondiente del espacio de trabajo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- organizar un reconocimiento OSINT autorizado en espacios de trabajo reproducibles
- automatizar consultas a varias fuentes con módulos y claves de API

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: organizar un reconocimiento OSINT autorizado en espacios de trabajo reproducibles; automatizar consultas a varias fuentes con módulos y claves de API | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Úsalo solo sobre objetivos propios o con autorización; muchos módulos requieren claves de API de terceros.

## Stack y modelos

- **Stack:** Python, Dockerfile, docker-compose.yml
- **Etiquetas:** `osint` `python` `security` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [lanmaster53/recon-ng](https://github.com/lanmaster53/recon-ng)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/lanmaster53/recon-ng/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
