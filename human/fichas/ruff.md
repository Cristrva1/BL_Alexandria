[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 🖥️ Ruff

> Linter y formateador de Python extremadamente rápido escrito en Rust, compatible con Flake8, isort y Black, con más de 800 reglas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 51.3k | MIT | Rust | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Linter y formateador de código abierto (MIT) desarrollado por Astral, la empresa de uv. Estándar de facto en el ecosistema Python, usado por proyectos como FastAPI, pandas o Apache Airflow.

## ¿Qué hace?

Analiza código Python con más de 800 reglas (equivalentes a Flake8 y muchos de sus plugins, isort, pyupgrade y otros), corrige automáticamente y formatea con paridad práctica con Black, entre 10 y 100 veces más rápido según el proyecto. Soporta cuadernos Jupyter y monorepos.

## ¿Cómo lo hace?

Escrito en Rust; se instala con `pip install ruff`, el instalador de Astral, `uvx ruff` o gestores de paquetes. Se configura en `pyproject.toml` o `ruff.toml` y se integra en editores (servidor de lenguaje), pre-commit y CI.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [pre-commit](pre-commit.md) | Astral mantiene el hook oficial ruff-pre-commit para ejecutar lint y formato antes de cada commit. | Instala pre-commit; después añade el repositorio ruff-pre-commit a .pre-commit-config.yaml. |
| [SonarQube Community Build](sonarqube.md) | El analizador Python de SonarQube puede importar informes de Ruff como problemas externos. | Genera el informe de Ruff en el formato admitido; después configura la propiedad de importación en el análisis de SonarQube. |
| [Claude Code](claude-code.md) | Un agente de código puede ejecutar `ruff check --fix` y `ruff format` tras cada cambio para mantener el estilo (combinación por arquitectura). | Instala Ruff en el proyecto; después indícale al agente que lo ejecute antes de terminar. |

**Notas:** Ruff no hace comprobación de tipos: combínalo con un verificador de tipos si lo necesitas.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 0.17.5 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/astral-sh/ruff/blob/main/README.md) · [2](https://docs.astral.sh/ruff/) · [3](https://github.com/astral-sh/ruff-pre-commit) · [4](https://docs.sonarsource.com/sonarqube-server/latest/analyzing-source-code/importing-external-issues/external-analyzer-reports/)</sub>

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
pip install ruff
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/astral-sh/ruff/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Ruff para mi objetivo y necesito pasos guiados. Lee https://github.com/astral-sh/ruff/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta `uvx ruff check` y `uvx ruff format` en un proyecto Python de prueba..

**Qué comprobar:** Ruff informa de los problemas en segundos y el formateo deja un diff limpio..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- sustituir Flake8, isort y Black por una sola herramienta en un proyecto
- revisar y corregir el código que genera un agente antes de cada commit

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: sustituir Flake8, isort y Black por una sola herramienta en un proyecto; revisar y corregir el código que genera un agente antes de cada commit | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Rust, Cargo.toml, Dockerfile, pyproject.toml
- **Etiquetas:** `code` `python` `rust` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [astral-sh/ruff](https://github.com/astral-sh/ruff)
- 🌐 Web: <https://docs.astral.sh/ruff>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/astral-sh/ruff/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
