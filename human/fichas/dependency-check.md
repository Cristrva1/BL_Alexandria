[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# 🖥️ OWASP Dependency-Check

> Análisis de composición de software (SCA) de OWASP: detecta dependencias con CVE publicados en Java, .NET, JavaScript, Python y más.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.8k | Apache-2.0 | Java | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 63/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta OWASP de análisis de composición de software que busca vulnerabilidades conocidas en las dependencias de un proyecto.

## ¿Qué hace?

Identifica las bibliotecas usadas, les asigna identificadores CPE y emite informes HTML, JSON, XML o SARIF con los CVE encontrados.

## ¿Cómo lo hace?

Descarga y mantiene en caché la NVD (se recomienda una clave de API de NVD) y otros analizadores; se ejecuta como CLI, plugin de build o contenedor.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Dependency-Track](dependency-track.md) | Dependency-Check cubre el análisis en build; Dependency-Track mantiene el inventario continuo. | Dependency-Check en CI; Dependency-Track como servidor central. |
| [DefectDojo](defectdojo.md) | DefectDojo importa el informe XML de Dependency-Check para su seguimiento. | Genera el informe XML e impórtalo en DefectDojo. |
| [OSV-Scanner](osv-scanner.md) | OSV-Scanner contrasta resultados con la base OSV y reduce falsos negativos. | Ejecuta ambos en CI y compara hallazgos. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v13.0.0 (2026-08-03) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/dependency-check/DependencyCheck#readme) · [2](https://dependency-check.github.io/DependencyCheck/)</sub>

## Ver similares

Grupo **Análisis de dependencias vulnerables (SCA)**: OWASP Dependency-Check ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OSV-Scanner](osv-scanner.md) ⭐ recomendado | 79 | Si quieres consultar la base OSV desde lockfiles con una CLI ligera en Go. |
| 2 | **OWASP Dependency-Check** (esta ficha) | 63 | Si trabajas con Java/.NET y quieres plugins de Maven, Gradle o Jenkins. |
| 3 | [OWASP dep-scan](dep-scan.md) | 59 | Si quieres auditoría de riesgo con SBOM, alcanzabilidad y VEX en una sola CLI. |

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
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (bash):**

```
brew update && brew install dependency-check
```

Comando copiado literalmente de el README (sección «Command Line»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/dependency-check/DependencyCheck/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://dependency-check.github.io/DependencyCheck/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP Dependency-Check para mi objetivo y necesito pasos guiados. Lee https://github.com/dependency-check/DependencyCheck/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala la CLI con Homebrew como indica el README y analiza el directorio de un proyecto propio..

**Qué comprobar:** Obtienes un informe HTML con las dependencias y los CVE asociados..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- romper el build de Maven cuando aparece una dependencia con CVSS alto
- generar un informe HTML de dependencias vulnerables para una auditoría

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: romper el build de Maven cuando aparece una dependencia con CVSS alto; generar un informe HTML de dependencias vulnerables para una auditoría | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. La identificación por CPE produce falsos positivos y negativos; la descarga inicial de la NVD es lenta sin clave de API.

## Stack y modelos

- **Stack:** Java, Dockerfile, pom.xml
- **Etiquetas:** `security` `sca` `dependencies` `cve` `java`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [dependency-check/DependencyCheck](https://github.com/dependency-check/DependencyCheck)
- 🌐 Web: <https://owasp.org/www-project-dependency-check/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/dependency-check/DependencyCheck/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
