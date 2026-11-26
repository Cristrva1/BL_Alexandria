[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# 🖥️ OWASP Threat Dragon

> Herramienta OWASP de modelado de amenazas: diagramas de flujo de datos con amenazas STRIDE, LINDDUN o CIA, en escritorio o web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.7k | Apache-2.0 | JavaScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 70/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto OWASP de código abierto para modelado de amenazas con diagramas.

## ¿Qué hace?

Permite dibujar diagramas de flujo de datos, asignar amenazas por metodología (STRIDE, LINDDUN, CIA, PLOT4ai) y registrar mitigaciones e informes.

## ¿Cómo lo hace?

Aplicación de escritorio Electron o servidor web; los modelos se guardan como JSON local o en repositorios Git remotos mediante OAuth.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OWASP ASVS](asvs.md) | ASVS aporta requisitos verificables para las mitigaciones del modelo. | Modela primero; después enlaza controles de ASVS a cada amenaza. |
| [OWASP CheatSheet Series](cheatsheetseries.md) | Las Cheat Sheets de OWASP detallan cómo aplicar cada mitigación. | Consulta la hoja correspondiente al implementar la mitigación. |
| [OWASP Top 10](owasp-top10.md) | El Top 10 orienta qué riesgos priorizar en el modelo de una aplicación web. | Revisa el Top 10 antes de enumerar amenazas. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.6.2 (2026-05-10) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OWASP/threat-dragon#readme) · [2](https://www.threatdragon.com/docs/)</sub>

## Ver similares

Grupo **Modelado de amenazas**: OWASP Threat Dragon ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **OWASP Threat Dragon** (esta ficha) ⭐ recomendado | 70 | Si prefieres dibujar el diagrama en una aplicación de escritorio o web. |
| 2 | [OWASP pytm](pytm.md) | 58 | Si quieres el modelo como código Python versionado junto al proyecto y generado en CI. |

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
docker pull threatdragon/owasp-threat-dragon:stable
```

Comando copiado literalmente de el README (sección «Docker (from dockerhub)»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/OWASP/threat-dragon/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://www.threatdragon.com/docs/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP Threat Dragon para mi objetivo y necesito pasos guiados. Lee https://github.com/OWASP/threat-dragon/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga el instalador de escritorio desde las releases oficiales o la imagen Docker del README y crea un modelo de ejemplo..

**Qué comprobar:** Obtienes un diagrama con amenazas asociadas y un informe exportable..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- modelar las amenazas de una API nueva durante el diseño
- documentar mitigaciones STRIDE para una revisión de arquitectura

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: modelar las amenazas de una API nueva durante el diseño; documentar mitigaciones STRIDE para una revisión de arquitectura | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** JavaScript, Dockerfile, package.json
- **Etiquetas:** `security` `threat-modeling` `stride` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OWASP pytm](pytm.md) | 1.2k | Modelado de amenazas como código en Python: describe el sistema y obtén diagramas de flujo, secuencia y un informe de amenazas. |

## Enlaces

- 🐙 GitHub: [OWASP/threat-dragon](https://github.com/OWASP/threat-dragon)
- 🌐 Web: <https://owasp.org/projects/threat-dragon>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OWASP/threat-dragon/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
