[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 🖥️ Gitleaks

> Detector de secretos (contraseñas, claves de API, tokens) en repositorios git, archivos y stdin, usable como hook o acción de CI.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.1k | MIT | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de detección de secretos de código abierto (MIT) creada por Zachary Rice. Muy usada; el README indica que está completa en funciones y que las versiones futuras serán solo parches de seguridad, mientras el autor se centra en Betterleaks.

## ¿Qué hace?

Detecta secretos como contraseñas, claves de API y tokens en repositorios git (historial completo o rangos de commits), directorios, archivos y entrada estándar. Genera informes en JSON, CSV, SARIF y otros, y admite listas de excepciones y una línea base.

## ¿Cómo lo hace?

Escrito en Go; se instala con Homebrew, Docker, Go o binarios. Se usa como CLI, como hook de pre-commit o como GitHub Action (Gitleaks-Action); las reglas se configuran en TOML.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [pre-commit](pre-commit.md) | El README documenta Gitleaks como hook de pre-commit para frenar secretos antes de cada commit. | Instala pre-commit; después añade el hook de Gitleaks a .pre-commit-config.yaml. |
| [Semgrep](semgrep.md) | Semgrep cubre análisis estático de vulnerabilidades y Gitleaks los secretos: juntos forman una revisión de seguridad básica en CI (combinación por arquitectura). | Configura ambos en el mismo pipeline de CI y revisa sus informes SARIF. |
| [Claude Code](claude-code.md) | Ejecutar Gitleaks sobre los cambios de un agente antes de publicarlos evita filtrar claves que haya escrito en el código (combinación por arquitectura). | Instala Gitleaks; después añádelo como paso obligatorio antes del commit. |

**Notas:** Alternativas (elige una): trufflehog. Sucesor declarado por el autor: Betterleaks.

Estado en GitHub: activo · último push 2026-10-28 · última versión publicada v8.30.1 (2026-03-21) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/gitleaks/gitleaks/blob/master/README.md) · [2](https://github.com/betterleaks/betterleaks)</sub>

## Ver similares

Grupo **Detección de secretos en repos**: Gitleaks ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Gitleaks** (esta ficha) ⭐ recomendado | 61 | Si buscas esto: detector de secretos (contraseñas, claves de API, tokens) en repositorios git, archivos y stdin, usable como hook o acción de CI. |
| 2 | [TruffleHog](trufflehog.md) | 60 | Si buscas esto: busca, clasifica, verifica y analiza credenciales filtradas en git, chats, wikis, logs, almacenes de objetos y sistemas de archivos. |

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
brew install gitleaks
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/gitleaks/gitleaks/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Gitleaks para mi objetivo y necesito pasos guiados. Lee https://github.com/gitleaks/gitleaks/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Gitleaks y ejecútalo sobre un repositorio de prueba con una clave falsa en un commit..

**Qué comprobar:** El informe señala el archivo, la línea y el commit de la clave falsa..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- revisar el historial de un repositorio antes de hacerlo público
- bloquear commits que contengan claves con un hook pre-commit

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: revisar el historial de un repositorio antes de hacerlo público; bloquear commits que contengan claves con un hook pre-commit | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. El autor declara Gitleaks completo en funciones: solo publicará parches de seguridad y centra su trabajo en Betterleaks.

## Stack y modelos

- **Stack:** Go, Dockerfile, go.mod
- **Etiquetas:** `security` `go` `cli` `code`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [TruffleHog](trufflehog.md) | 29.4k | Busca, clasifica, verifica y analiza credenciales filtradas en git, chats, wikis, logs, almacenes de objetos y sistemas de archivos. |

## Enlaces

- 🐙 GitHub: [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)
- 🌐 Web: <https://gitleaks.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/gitleaks/gitleaks/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
