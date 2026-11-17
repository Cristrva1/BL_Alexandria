[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Respuesta a incidentes y forense

# 📚 The Sleuth Kit

> Toolkit forense de sistemas de archivos: recupera y analiza particiones, ficheros borrados y metadatos en evidencias de disco.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.2k | — | C | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; requiere programar con él; dominio especializado

**Puntuación de calidad** 41/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

TSK: toolkit forense de FS (licencias mixtas).

## ¿Qué hace?

Analiza volúmenes y recupera artefactos de disco.

## ¿Cómo lo hace?

Build desde fuente / paquetes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Velociraptor](velociraptor.md) | Velociraptor adquiere; TSK analiza discos. | Adquisición → TSK. |
| [Volatility 3](volatility3.md) | Memoria con Volatility; disco con TSK. | Complementarios. |

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada sleuthkit-4.15.0 (2026-04-15) (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/sleuthkit/sleuthkit#readme) · [2](https://www.sleuthkit.org/sleuthkit/)</sub>

## Ver similares

Grupo **Análisis forense de discos**: The Sleuth Kit ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Autopsy](autopsy.md) ⭐ recomendado | 46 | Si buscas esto: gUI forense sobre The Sleuth Kit: casos, timelines e ingest modules para investigar discos en laboratorio. |
| 2 | **The Sleuth Kit** (esta ficha) | 41 | Si buscas esto: toolkit forense de sistemas de archivos: recupera y analiza particiones, ficheros borrados y metadatos en evidencias de disco. |

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

[Instrucciones originales de instalación](https://github.com/sleuthkit/sleuthkit/blob/develop-4.1x/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar The Sleuth Kit para mi objetivo y necesito pasos guiados. Lee https://github.com/sleuthkit/sleuthkit/blob/develop-4.1x/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Compila/instala según INSTALL.txt y ejecuta `fls` sobre una imagen de laboratorio..

**Qué comprobar:** Listas inodos/nombres de fichero..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- listar ficheros de una imagen E01/raw de lab
- recuperar un fichero borrado de un volume de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: listar ficheros de una imagen E01/raw de lab; recuperar un fichero borrado de un volume de prueba | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** C
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Autopsy](autopsy.md) | 3.5k | GUI forense sobre The Sleuth Kit: casos, timelines e ingest modules para investigar discos en laboratorio. |

## Enlaces

- 🐙 GitHub: [sleuthkit/sleuthkit](https://github.com/sleuthkit/sleuthkit)
- 🌐 Web: <http://www.sleuthkit.org/sleuthkit/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/sleuthkit/sleuthkit/blob/develop-4.1x/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
