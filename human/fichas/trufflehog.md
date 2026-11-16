[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 🖥️ TruffleHog

> Busca, clasifica, verifica y analiza credenciales filtradas en git, chats, wikis, logs, almacenes de objetos y sistemas de archivos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 29.4k | AGPL-3.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de código abierto (AGPL-3.0) de Truffle Security, que financia el proyecto con una edición Enterprise de monitorización continua. Muy activa.

## ¿Qué hace?

Descubre secretos en Git, GitHub, GitLab, Docker, S3, GCS, Slack, Jira, Confluence, sistemas de archivos y más; los clasifica entre cientos de tipos, verifica si siguen siendo válidos y analiza los permisos de algunas credenciales.

## ¿Cómo lo hace?

Escrito en Go; se instala con Homebrew, Docker, script de instalación o desde el código. Se usa como CLI, hook de pre-commit o GitHub Action, con salida JSON.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [pre-commit](pre-commit.md) | TruffleHog se puede ejecutar como hook de pre-commit para escanear los cambios antes de confirmarlos. | Instala pre-commit; después añade el hook de TruffleHog según su documentación. |
| [Semgrep](semgrep.md) | Semgrep cubre el análisis estático y TruffleHog los secretos verificados en el mismo pipeline de seguridad (combinación por arquitectura). | Configura ambos pasos en CI y revisa sus informes. |
| [Claude Code](claude-code.md) | Un agente puede ejecutar TruffleHog sobre un repositorio y resumir qué credenciales están activas y deben rotarse (combinación por arquitectura). | Instala TruffleHog; después pide al agente el análisis sobre un repositorio autorizado. |

**Notas:** Alternativas (elige una): gitleaks.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.99.9 (2026-11-12) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/trufflesecurity/trufflehog/blob/main/README.md)</sub>

## Ver similares

Grupo **Detección de secretos en repos**: TruffleHog ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Gitleaks](gitleaks.md) ⭐ recomendado | 61 | Si buscas esto: detector de secretos (contraseñas, claves de API, tokens) en repositorios git, archivos y stdin, usable como hook o acción de CI. |
| 2 | **TruffleHog** (esta ficha) | 60 | Si buscas esto: busca, clasifica, verifica y analiza credenciales filtradas en git, chats, wikis, logs, almacenes de objetos y sistemas de archivos. |

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

**Entrada documentada (consulta la sintaxis original):**

```
brew install trufflehog
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/trufflesecurity/trufflehog/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar TruffleHog para mi objetivo y necesito pasos guiados. Lee https://github.com/trufflesecurity/trufflehog/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta la imagen Docker contra el repositorio de pruebas trufflesecurity/test_keys como indica el README..

**Qué comprobar:** El informe muestra las claves encontradas y si están verificadas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- auditar los repositorios de una organización en busca de claves activas
- revisar buckets o logs exportados antes de compartirlos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: auditar los repositorios de una organización en busca de claves activas; revisar buckets o logs exportados antes de compartirlos | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. La verificación hace peticiones reales a las APIs de los proveedores con las credenciales encontradas: úsalo solo sobre activos propios o autorizados.

## Stack y modelos

- **Stack:** Go, Dockerfile, go.mod
- **Etiquetas:** `security` `go` `cli` `code`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Gitleaks](gitleaks.md) | 31.1k | Detector de secretos (contraseñas, claves de API, tokens) en repositorios git, archivos y stdin, usable como hook o acción de CI. |

## Enlaces

- 🐙 GitHub: [trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog)
- 🌐 Web: <https://trufflesecurity.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/trufflesecurity/trufflehog/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
