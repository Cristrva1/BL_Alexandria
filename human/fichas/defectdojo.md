[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# ⚙️ DefectDojo

> Gestor OWASP de vulnerabilidades y DevSecOps: importa resultados de más de 200 escáneres, deduplica hallazgos y sigue su corrección.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.2k | BSD-3-Clause | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; varios servicios con Docker Compose

**Puntuación de calidad** 70/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto insignia de OWASP para gestión unificada de vulnerabilidades y seguridad de aplicaciones (ASPM), con edición comunitaria de código abierto.

## ¿Qué hace?

Importa y normaliza informes de escáneres, deduplica hallazgos, asigna responsables, gestiona aceptación de riesgos y genera métricas e informes.

## ¿Cómo lo hace?

Servidor Django con PostgreSQL, Celery y Redis desplegado con Docker Compose; parsers por herramienta, API REST v2 e integraciones con Jira y CI.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Semgrep](semgrep.md) | Los resultados SAST de Semgrep se importan en DefectDojo para su triaje. | DefectDojo primero; exporta Semgrep en un formato soportado e impórtalo. |
| [ZAP (Zed Attack Proxy)](zaproxy.md) | Los informes DAST de ZAP alimentan DefectDojo junto con otros hallazgos. | Ejecuta ZAP en un objetivo autorizado y sube el informe XML/JSON. |
| [Trivy](trivy.md) | Trivy aporta vulnerabilidades de contenedores e IaC al mismo tablero. | Trivy en CI con salida JSON; importación en DefectDojo. |
| [Nuclei](nuclei.md) | Los hallazgos de plantillas de Nuclei se consolidan y deduplican en DefectDojo. | Nuclei con salida JSON; importa en una prueba de DefectDojo. |
| [Dependency-Track](dependency-track.md) | Combinación recíproca: Dependency-Track lo enlaza como «DefectDojo consolida los hallazgos de Dependency-Track con los de SAST/DAST para su gestión y seguimiento». | Orden indicado desde Dependency-Track: Ambos servidores; configura la importación de Dependency-Track en DefectDojo. |
| [OWASP Dependency-Check](dependency-check.md) | Combinación recíproca: OWASP Dependency-Check lo enlaza como «DefectDojo importa el informe XML de Dependency-Check para su seguimiento». | Orden indicado desde OWASP Dependency-Check: Genera el informe XML e impórtalo en DefectDojo. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (7). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Bandit](bandit.md) · [Brakeman](brakeman.md) · [CodeQL](codeql.md) · [gosec](gosec.md) · [MobSF (Mobile Security Framework)](mobsf.md) · [OWASP Nettacker](nettacker.md) · [OWASP secureCodeBox](securecodebox.md)

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 3.5.200 (2026-11-16) · licencia declarada BSD-3-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/DefectDojo/django-DefectDojo#readme) · [2](https://docs.defectdojo.com)</sub>

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
git clone https://github.com/DefectDojo/django-DefectDojo && cd django-DefectDojo && docker compose up
```

Comando copiado literalmente de el README (sección «Quick Start for Docker Compose»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/DefectDojo/django-DefectDojo/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://docs.defectdojo.com)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar DefectDojo para mi objetivo y necesito pasos guiados. Lee https://github.com/DefectDojo/django-DefectDojo/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona el repo y levanta la versión de prueba con Docker Compose como indica el README; importa un informe de un escáner propio..

**Qué comprobar:** Ves los hallazgos deduplicados asociados a un producto y a una prueba..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- centralizar los informes de Semgrep, ZAP y Trivy de un equipo en un único tablero
- medir el tiempo de corrección de hallazgos críticos por producto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: centralizar los informes de Semgrep, ZAP y Trivy de un equipo en un único tablero; medir el tiempo de corrección de hallazgos críticos por producto | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Existe una edición comercial (DefectDojo Pro) con funciones adicionales; la edición comunitaria es BSD-3-Clause.

## Stack y modelos

- **Stack:** Python, docker-compose.yml, requirements.txt
- **Etiquetas:** `security` `vulnerability-management` `devsecops` `aspm` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [DefectDojo/django-DefectDojo](https://github.com/DefectDojo/django-DefectDojo)
- 🌐 Web: <https://defectdojo.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/DefectDojo/django-DefectDojo/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
