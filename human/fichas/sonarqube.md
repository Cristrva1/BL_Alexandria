[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# ⚙️ SonarQube Community Build

> Plataforma de inspección continua de calidad y seguridad del código: análisis estático de bugs, vulnerabilidades y mantenibilidad en muchos lenguajes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.2k | LGPL-3.0 | Java | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Puntuación de calidad** 54/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Código de SonarQube Community Build, la edición gratuita y de código abierto (LGPL-3.0) de la plataforma de SonarSource. Proyecto muy maduro; las ediciones superiores son comerciales.

## ¿Qué hace?

Analiza el código con técnicas como ejecución simbólica y análisis de flujo de datos y control para encontrar bugs, vulnerabilidades, puntos críticos de seguridad y problemas de mantenibilidad, y aplica puertas de calidad en cada análisis. Importa también informes de herramientas externas.

## ¿Cómo lo hace?

Servidor en Java con PostgreSQL u otra base soportada; se despliega con la imagen Docker oficial o el archivo ZIP. Los análisis se lanzan con SonarScanner desde CI o local; SonarSource publica además un servidor MCP para agentes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ruff](ruff.md) | SonarQube puede importar informes de Ruff como problemas externos del análisis de Python. | Genera el informe de Ruff; después configura su importación en el escáner. |
| [Claude Code](claude-code.md) | SonarSource publica un servidor MCP de SonarQube para que los agentes consulten problemas y analicen fragmentos. | SonarQube en marcha con un token; después registra el servidor MCP en Claude Code. |
| [coolify](coolify.md) | La imagen Docker de SonarQube con su base de datos puede desplegarse y respaldarse desde Coolify (combinación por arquitectura). | Coolify primero; luego SonarQube con PostgreSQL y volúmenes persistentes. |

**Notas:** Alternativas (elige una): semgrep.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada 26.11.0.134175 (2026-11-04) · licencia declarada LGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/SonarSource/sonarqube/blob/master/README.md) · [2](https://github.com/SonarSource/sonarqube-mcp-server) · [3](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/importing-external-issues/external-analyzer-reports/)</sub>

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

[Instrucciones originales de instalación](https://github.com/SonarSource/sonarqube/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SonarQube Community Build para mi objetivo y necesito pasos guiados. Lee https://github.com/SonarSource/sonarqube/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca la imagen Docker oficial, crea un proyecto y analiza un repositorio pequeño con el escáner..

**Qué comprobar:** El panel muestra problemas, puntos críticos y la puerta de calidad del proyecto..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- vigilar la calidad y seguridad de un repositorio en cada PR
- revisar el código generado por IA con reglas consistentes antes de fusionarlo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: vigilar la calidad y seguridad de un repositorio en cada PR; revisar el código generado por IA con reglas consistentes antes de fusionarlo | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Este repositorio es la Community Build (LGPL-3.0); las ediciones Developer, Enterprise y Data Center son de pago.

## Stack y modelos

- **Stack:** Java, build.gradle
- **Etiquetas:** `code` `java` `security` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Semgrep](semgrep.md) | 17.7k | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. |

## Enlaces

- 🐙 GitHub: [SonarSource/sonarqube](https://github.com/SonarSource/sonarqube)
- 🌐 Web: <http://www.sonarqube.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/SonarSource/sonarqube/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
