[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Nube, contenedores e IaC

# 🖥️ Grype

> Escáner de vulnerabilidades para imágenes de contenedor y SBOMs: empareja paquetes con CVE y prioriza remediación.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.3k | Apache-2.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 71/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Escáner de vulnerabilidades open source de Anchore, pareja natural de Syft y alternativa/complemento de Trivy.

## ¿Qué hace?

Analiza imágenes o SBOMs y reporta CVE conocidos contra las bases de datos que mantiene.

## ¿Cómo lo hace?

Binario instalable con el script oficial; salida tabular/JSON para CI.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Falco](falco.md) | Grype endurece la imagen; Falco vigila el runtime. | Grype en CI; Falco en el nodo. |
| [Semgrep](semgrep.md) | Semgrep encuentra bugs de código; Grype, CVE de dependencias de imagen. | Usa ambos en el pipeline. |
| [Checkov](checkov.md) | Checkov endurece IaC; Grype la imagen resultante. | Checkov → build → Grype. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[OSV-Scanner](osv-scanner.md) · [Syft](syft.md)

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.121.3 (2026-11-09) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/anchore/grype#readme)</sub>

## Ver similares

Grupo **Escáneres de vulnerabilidades de contenedores**: Grype ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Trivy](trivy.md) ⭐ recomendado | 79 | Si buscas esto: escáner de seguridad versátil: busca CVE, configuraciones erróneas de IaC, secretos y licencias en imágenes, repositorios, Kubernetes y nube. |
| 2 | **Grype** (esta ficha) | 71 | Si buscas esto: escáner de vulnerabilidades para imágenes de contenedor y SBOMs: empareja paquetes con CVE y prioriza remediación. |

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

**Entrada documentada (consulta la sintaxis original):**

```
curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/anchore/grype/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Grype para mi objetivo y necesito pasos guiados. Lee https://github.com/anchore/grype/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `curl -sSfL https://get.anchore.io/grype | sudo sh -s -- -b /usr/local/bin` y ejecuta `grype <imagen>`..

**Qué comprobar:** Obtienes CVE por paquete con severidad..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- escanear una imagen Docker propia antes de publicarla
- evaluar un SBOM generado en CI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: escanear una imagen Docker propia antes de publicarla; evaluar un SBOM generado en CI | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Go, Dockerfile, Makefile, go.mod
- **Etiquetas:** `security` `containers` `sbom`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Trivy](trivy.md) | 39.4k | Escáner de seguridad versátil: busca CVE, configuraciones erróneas de IaC, secretos y licencias en imágenes, repositorios, Kubernetes y nube. |

## Enlaces

- 🐙 GitHub: [anchore/grype](https://github.com/anchore/grype)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/anchore/grype/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
