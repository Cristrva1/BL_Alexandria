[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# ⚙️ Dependency-Track

> Plataforma OWASP que ingiere SBOM CycloneDX y vigila de forma continua vulnerabilidades, licencias y riesgo de los componentes de tus proyectos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.5k | Apache-2.0 | Java | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; varios servicios con Docker Compose

**Puntuación de calidad** 65/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto insignia de OWASP para análisis continuo de componentes (Component Analysis) a partir de listas de materiales de software (SBOM).

## ¿Qué hace?

Mantiene un inventario de componentes por proyecto y versión, lo cruza con fuentes de vulnerabilidades y aplica políticas de seguridad, licencias y operación con alertas.

## ¿Cómo lo hace?

Recibe SBOM CycloneDX por la API o la interfaz, los analiza contra NVD, GitHub Advisories, OSV, Sonatype OSS Index y Snyk (opcional), y expone resultados por API REST, webhooks e integraciones.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [cdxgen](cdxgen.md) | cdxgen genera el SBOM CycloneDX que Dependency-Track analiza de forma continua. | Primero Dependency-Track; después cdxgen en CI publicando el SBOM por la API. |
| [Syft](syft.md) | Syft produce SBOM CycloneDX de imágenes de contenedor para subirlos a Dependency-Track. | Dependency-Track en marcha; Syft en el pipeline de imágenes. |
| [DefectDojo](defectdojo.md) | DefectDojo consolida los hallazgos de Dependency-Track con los de SAST/DAST para su gestión y seguimiento. | Ambos servidores; configura la importación de Dependency-Track en DefectDojo. |
| [OWASP Dependency-Check](dependency-check.md) | Dependency-Check aporta un análisis SCA puntual en build; Dependency-Track lo hace continuo sobre el inventario. | Dependency-Check en CI; Dependency-Track como inventario central. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[OWASP dep-scan](dep-scan.md)

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 5.2.1 (2026-10-25) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/DependencyTrack/dependency-track#readme) · [2](https://docs.dependencytrack.org/getting-started/deploy-docker/)</sub>

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

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno.

**Entrada documentada (bash):**

```
curl -LO https://dependencytrack.org/docker-compose.yml
docker compose up -d
```

Comando copiado literalmente de la documentación oficial enlazada desde el README; revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://docs.dependencytrack.org/getting-started/deploy-docker/)

[Abrir la web o descarga indicada por el autor](https://docs.dependencytrack.org/getting-started/deploy-docker/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Dependency-Track para mi objetivo y necesito pasos guiados. Lee https://docs.dependencytrack.org/getting-started/deploy-docker/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega el stack de prueba con el docker-compose.yml de la documentación oficial y sube un SBOM CycloneDX de un proyecto propio..

**Qué comprobar:** Ves el inventario de componentes con vulnerabilidades y licencias detectadas en la interfaz web..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- subir el SBOM de cada build en CI y recibir avisos cuando aparece un CVE nuevo en una dependencia
- auditar licencias de componentes de toda la cartera de aplicaciones

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: subir el SBOM de cada build en CI y recibir avisos cuando aparece un CVE nuevo en una dependencia; auditar licencias de componentes de toda la cartera de aplicaciones | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Requiere al menos 4 GB de RAM para el servidor API según la documentación; la primera sincronización de fuentes de vulnerabilidades tarda.

## Stack y modelos

- **Stack:** Java, Makefile, pom.xml
- **Etiquetas:** `security` `sbom` `sca` `supply-chain` `cyclonedx` `java`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [DependencyTrack/dependency-track](https://github.com/DependencyTrack/dependency-track)
- 🌐 Web: <https://dependencytrack.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/DependencyTrack/dependency-track/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
