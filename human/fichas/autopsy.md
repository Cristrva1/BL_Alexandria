[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Respuesta a incidentes y forense

# 🖥️ Autopsy

> GUI forense sobre The Sleuth Kit: casos, timelines e ingest modules para investigar discos en laboratorio.

## Cuándo elegir esta ficha

Interfaz gráfica forense que usa The Sleuth Kit. Úsala para explorar una imagen de ejemplo propia o autorizada.

Revisión documental del 2026-11-27. [Fuente 1](https://www.autopsy.com/download/) · [Fuente 2](https://github.com/sleuthkit/autopsy/commit/cb3dacdcad67abe7cf863c74f10dcdb8e25a5c21) · [Fuente 3](https://sleuthkit.org/autopsy/)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.5k | — | Java | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; dominio especializado

**Puntuación de calidad** 38/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

GUI forense (Apache-2.0 en LICENSE-2.0.txt; API sin SPDX).

## ¿Qué hace?

Orquesta TSK y módulos de ingest en una UI.

## ¿Cómo lo hace?

Instalador / build.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Hayabusa](hayabusa.md) | Hayabusa tria evtx; Autopsy el disco. | Complementarios en DFIR. |
| [Wazuh](wazuh.md) | Tras el análisis forense, correlaciona con alertas Wazuh. | Autopsy + Wazuh. |
| [The Sleuth Kit](sleuthkit.md) | Autopsy utiliza el motor forense The Sleuth Kit y añade la interfaz gráfica. | Consulta los componentes incluidos en la distribución oficial. |

Estado en GitHub: activo · último push 2026-06-20 · última versión publicada autopsy-4.23.1 (2026-05-07) (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/sleuthkit/autopsy#readme) · [2](http://www.sleuthkit.org/autopsy/)</sub>

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

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/sleuthkit/autopsy/blob/develop/README.txt)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Autopsy para mi objetivo y necesito pasos guiados. Lee https://github.com/sleuthkit/autopsy/blob/develop/README.txt. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala el paquete Windows desde el sitio oficial o sigue README.txt y abre un caso de lab..

**Qué comprobar:** UI de Autopsy con el disco cargado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- abrir un caso forense de lab
- generar timeline de un disco de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: abrir un caso forense de lab; generar timeline de un disco de prueba | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Java
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [sleuthkit/autopsy](https://github.com/sleuthkit/autopsy)
- 🌐 Web: <http://www.sleuthkit.org/autopsy/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/sleuthkit/autopsy/blob/develop/README.txt)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
