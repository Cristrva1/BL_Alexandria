[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 🖥️ pre-commit

> Framework para gestionar y ejecutar hooks de git multilenguaje antes de cada commit: linters, formateadores y escáneres declarados en YAML.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.7k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de hooks de git de código abierto (MIT) mantenido por Anthony Sottile y la comunidad pre-commit desde 2014. Muy maduro y ampliamente adoptado.

## ¿Qué hace?

Gestiona hooks de pre-commit en muchos lenguajes: descarga cada herramienta en la versión fijada, la aísla en su propio entorno y la ejecuta solo sobre los archivos afectados. Sirve para formateo, lint, escaneo de secretos y otras comprobaciones; existe el servicio pre-commit.ci para ejecutarlo en PR.

## ¿Cómo lo hace?

Escrito en Python; se instala con pip o gestores de paquetes y se activa con `pre-commit install`. La configuración es un archivo YAML con repositorios de hooks y revisiones fijadas; `pre-commit autoupdate` actualiza versiones.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ruff](ruff.md) | ruff-pre-commit es el hook oficial de Ruff para pre-commit. | pre-commit instalado; después añade ruff-pre-commit al YAML. |
| [Gitleaks](gitleaks.md) | Gitleaks documenta su uso como hook de pre-commit. | pre-commit instalado; después añade el hook de Gitleaks. |
| [TruffleHog](trufflehog.md) | TruffleHog se puede ejecutar como hook para escanear cambios antes del commit. | pre-commit instalado; después añade el hook de TruffleHog. |
| [Biome](biome.md) | Biome publica hooks oficiales para pre-commit. | pre-commit instalado; después añade los hooks de Biome. |
| [Semgrep](semgrep.md) | Semgrep ofrece un hook de pre-commit para analizar los archivos modificados. | pre-commit instalado; después añade el hook de Semgrep con su configuración. |
| [Trivy](trivy.md) | Combinación recíproca: Trivy lo enlaza como «Un hook local de pre-commit puede lanzar `trivy fs` o el escaneo de secretos antes de cada commit (combinación por arquitectura)». | Orden indicado desde Trivy: Instala Trivy; después define un hook local en .pre-commit-config.yaml. |

**Notas:** Los hooks se descargan de repositorios externos: fija revisiones y revisa su origen.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada v4.7.0 (2026-10-13) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/pre-commit/pre-commit/blob/main/README.md) · [2](https://pre-commit.com/)</sub>

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

[Instrucciones originales de instalación](https://github.com/pre-commit/pre-commit/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar pre-commit para mi objetivo y necesito pasos guiados. Lee https://github.com/pre-commit/pre-commit/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala pre-commit, crea un .pre-commit-config.yaml con un hook de formato y ejecuta `pre-commit run --all-files`..

**Qué comprobar:** El hook se instala solo y formatea o señala los archivos del repositorio..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- obligar a pasar formato, lint y escaneo de secretos antes de cada commit
- aplicar las mismas comprobaciones en local y en CI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: obligar a pasar formato, lint y escaneo de secretos antes de cada commit; aplicar las mismas comprobaciones en local y en CI | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, setup.py
- **Etiquetas:** `code` `python` `cli` `git`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [pre-commit/pre-commit](https://github.com/pre-commit/pre-commit)
- 🌐 Web: <https://pre-commit.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pre-commit/pre-commit/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
