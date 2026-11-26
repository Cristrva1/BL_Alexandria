[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# 🖥️ cdxgen

> Generador de SBOM CycloneDX del ecosistema OWASP para código fuente, contenedores y binarios en decenas de lenguajes y gestores de paquetes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.1k | Apache-2.0 | JavaScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 63/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta del proyecto OWASP CycloneDX para generar listas de materiales de software (SBOM) y otras BOM.

## ¿Qué hace?

Produce SBOM, SaaSBOM, CBOM y otros BOM CycloneDX de código, contenedores y entornos, con análisis de evidencia y alcanzabilidad opcionales.

## ¿Cómo lo hace?

CLI Node.js que llama a los gestores de paquetes de cada lenguaje o lee lockfiles; se distribuye por npm, Homebrew e imágenes de contenedor.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Dependency-Track](dependency-track.md) | Dependency-Track ingiere el SBOM generado por cdxgen. | cdxgen en CI; publica el BOM en Dependency-Track. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[OWASP dep-scan](dep-scan.md)

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v13.8.0 (2026-11-14) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/cdxgen/cdxgen#readme) · [2](https://cdxgen.github.io/cdxgen/)</sub>

## Ver similares

Grupo **Generadores de SBOM**: cdxgen ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Syft](syft.md) ⭐ recomendado | 71 | Si tu prioridad son imágenes de contenedor y sistemas de archivos, con salida SPDX o CycloneDX. |
| 2 | **cdxgen** (esta ficha) | 63 | Si necesitas BOM CycloneDX de código fuente en muchos lenguajes, con evidencia y alcanzabilidad. |

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
npm install -g @cdxgen/cdxgen --omit=optional --ignore-scripts --min-release-age=2
```

Comando copiado literalmente de el README (sección «npm and JavaScript package managers»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/cdxgen/cdxgen/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://cdxgen.github.io/cdxgen/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar cdxgen para mi objetivo y necesito pasos guiados. Lee https://github.com/cdxgen/cdxgen/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con npm como indica el README y ejecuta cdxgen en el directorio de un proyecto propio..

**Qué comprobar:** Obtienes un archivo bom.json en formato CycloneDX..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- generar el SBOM de cada release en CI
- inventariar componentes de una imagen Docker propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: generar el SBOM de cada release en CI; inventariar componentes de una imagen Docker propia | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** JavaScript, docker-compose.yml, package.json, pyproject.toml
- **Etiquetas:** `security` `sbom` `cyclonedx` `supply-chain` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Syft](syft.md) | 9.9k | Genera SBOMs (Software Bill of Materials) de imágenes, directorios y remotes para alimentar Grype u otros scanners. |

## Enlaces

- 🐙 GitHub: [cdxgen/cdxgen](https://github.com/cdxgen/cdxgen)
- 🌐 Web: <https://cdxgen.github.io/cdxgen/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cdxgen/cdxgen/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
