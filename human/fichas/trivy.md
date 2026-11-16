[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Nube, contenedores e IaC

# 🖥️ Trivy

> Escáner de seguridad versátil: busca CVE, configuraciones erróneas de IaC, secretos y licencias en imágenes, repositorios, Kubernetes y nube.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39.4k | Apache-2.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 79/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Escáner de seguridad de código abierto (Apache-2.0) de Aqua Security. Muy popular y maduro; Aqua ofrece una plataforma comercial aparte.

## ¿Qué hace?

Detecta paquetes y dependencias (SBOM), vulnerabilidades conocidas, problemas de IaC y configuración, secretos y licencias en imágenes de contenedor, sistemas de archivos, repositorios remotos, imágenes de VM y Kubernetes, con salidas para CI.

## ¿Cómo lo hace?

Se distribuye como binario Go (Homebrew, Docker `aquasec/trivy`, paquetes y GitHub Action). Descarga bases de vulnerabilidades al ejecutarse; ofrece un plugin oficial (trivy-mcp) que lo expone como servidor MCP.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | El plugin oficial trivy-mcp expone Trivy como servidor MCP para agentes. | Instala Trivy y el plugin mcp; después registra el servidor en Claude Code. |
| [Semgrep](semgrep.md) | Semgrep analiza el código propio y Trivy las dependencias, imágenes y la IaC; juntos cubren SAST y SCA (combinación por arquitectura). | Añade ambos escaneos al pipeline de CI. |
| [pre-commit](pre-commit.md) | Un hook local de pre-commit puede lanzar `trivy fs` o el escaneo de secretos antes de cada commit (combinación por arquitectura). | Instala Trivy; después define un hook local en .pre-commit-config.yaml. |
| [coolify](coolify.md) | Las imágenes que despliega Coolify se pueden escanear con Trivy antes de publicarlas (combinación por arquitectura). | Escanea la imagen con Trivy en CI; después despliega en Coolify. |
| [Wazuh](wazuh.md) | Combinación recíproca: Wazuh lo enlaza como «Trivy escanea imágenes antes del despliegue y Wazuh vigila vulnerabilidades en ejecución (combinación por arquitectura)». | Orden indicado desde Wazuh: Integra Trivy en CI; después despliega agentes de Wazuh en los hosts. |
| [Lynis](lynis.md) | Combinación recíproca: Lynis lo enlaza como «Trivy revisa imágenes y dependencias mientras Lynis audita el sistema anfitrión (combinación por arquitectura)». | Orden indicado desde Lynis: Audita el host con Lynis; escanea las imágenes con Trivy. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (8). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Checkov](checkov.md) · [Cosign](cosign.md) · [Falco](falco.md) · [kube-bench](kube-bench.md) · [OSV-Scanner](osv-scanner.md) · [Pacu](pacu.md) · [Prowler](prowler.md) · [Syft](syft.md)

**Notas:** La base de vulnerabilidades se descarga de registros públicos; en entornos aislados hay que preparar una réplica.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v0.76.2 (2026-11-05) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/aquasecurity/trivy/blob/main/README.md) · [2](https://trivy.dev) · [3](https://github.com/aquasecurity/trivy-mcp)</sub>

## Ver similares

Grupo **Escáneres de vulnerabilidades de contenedores**: Trivy ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Trivy** (esta ficha) ⭐ recomendado | 79 | Si buscas esto: escáner de seguridad versátil: busca CVE, configuraciones erróneas de IaC, secretos y licencias en imágenes, repositorios, Kubernetes y nube. |
| 2 | [Grype](grype.md) | 70 | Si buscas esto: escáner de vulnerabilidades para imágenes de contenedor y SBOMs: empareja paquetes con CVE y prioriza remediación. |

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
brew install trivy
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/aquasecurity/trivy/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Trivy para mi objetivo y necesito pasos guiados. Lee https://github.com/aquasecurity/trivy/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `brew install trivy` (o la imagen Docker) y ejecuta `trivy fs .` en un proyecto propio..

**Qué comprobar:** Obtienes una tabla de vulnerabilidades por paquete con severidad y versión corregida..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- escanear una imagen Docker antes de desplegarla
- generar un SBOM y revisar dependencias vulnerables de un proyecto en CI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: escanear una imagen Docker antes de desplegarla; generar un SBOM y revisar dependencias vulnerables de un proyecto en CI | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Go, Dockerfile, go.mod
- **Etiquetas:** `security` `go` `cli` `devops`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Grype](grype.md) | 13.3k | Escáner de vulnerabilidades para imágenes de contenedor y SBOMs: empareja paquetes con CVE y prioriza remediación. |

## Enlaces

- 🐙 GitHub: [aquasecurity/trivy](https://github.com/aquasecurity/trivy)
- 🌐 Web: <https://trivy.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/aquasecurity/trivy/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
