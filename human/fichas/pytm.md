[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# 📚 OWASP pytm

> Modelado de amenazas como código en Python: describe el sistema y obtén diagramas de flujo, secuencia y un informe de amenazas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.2k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 58/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** MIT. Fuente: [LICENSE](https://github.com/OWASP/pytm/blob/master/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Proyecto OWASP para modelado de amenazas como código en Python.

## ¿Qué hace?

A partir de una descripción del sistema en Python, identifica amenazas de una base predefinida y genera diagramas y un informe.

## ¿Cómo lo hace?

Biblioteca Python con salida para Graphviz y PlantUML y plantillas de informe vía pandoc; licencia MIT en LICENSE pese a NOASSERTION en la API de GitHub.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OWASP ASVS](asvs.md) | ASVS aporta requisitos para mitigar las amenazas que pytm identifica. | Genera el informe; asigna requisitos ASVS. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.4.1 (2026-11-01) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OWASP/pytm#readme)</sub>

## Ver similares

Grupo **Modelado de amenazas**: OWASP pytm ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OWASP Threat Dragon](threat-dragon.md) ⭐ recomendado | 70 | Si prefieres dibujar el diagrama en una aplicación de escritorio o web. |
| 2 | **OWASP pytm** (esta ficha) | 58 | Si quieres el modelo como código Python versionado junto al proyecto y generado en CI. |

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

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/OWASP/pytm/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/OWASP/pytm#readme)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP pytm para mi objetivo y necesito pasos guiados. Lee https://github.com/OWASP/pytm/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el ejemplo tm.py del README en un entorno con las dependencias indicadas y genera el DFD..

**Qué comprobar:** Obtienes un diagrama de flujo de datos y la lista de amenazas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- versionar el modelo de amenazas junto al código de un servicio
- generar informes de amenazas en CI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: versionar el modelo de amenazas junto al código de un servicio; generar informes de amenazas en CI | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Python, Dockerfile, Makefile, pyproject.toml
- **Etiquetas:** `security` `threat-modeling` `python` `as-code`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OWASP Threat Dragon](threat-dragon.md) | 1.7k | Herramienta OWASP de modelado de amenazas: diagramas de flujo de datos con amenazas STRIDE, LINDDUN o CIA, en escritorio o web. |

## Enlaces

- 🐙 GitHub: [OWASP/pytm](https://github.com/OWASP/pytm)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OWASP/pytm/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
