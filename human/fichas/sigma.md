[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Detección, SIEM e IDS

# 📂 Sigma

> Formato y reglas de detección SIEM multi-vendor: escribe una vez, convierte a Elastic, Splunk, QRadar, etc.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.5k | NOASSERTION | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Estándar abierto de reglas de detección; especificación en dominio público y reglas bajo Detection Rule License 1.1.

## ¿Qué hace?

Describe búsquedas de log de forma abstracta y se traduce al lenguaje de cada SIEM.

## ¿Cómo lo hace?

Se clonan las reglas y se convierten con las herramientas pySigma documentadas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Wazuh](wazuh.md) | Convierte reglas Sigma a decoders/rules de Wazuh. | Selecciona reglas; convierte e importa. |
| [Atomic Red Team](atomic-red-team.md) | Valida una regla Sigma ejecutando el atomic relacionado. | Atomic → telemetría → regla Sigma. |
| [CrowdSec](crowdsec.md) | CrowdSec y Sigma cubren detección en red y logs. | Despliega CrowdSec; aporta reglas Sigma al SIEM. |
| [OpenCTI](opencti.md) | Combinación recíproca: OpenCTI lo enlaza como «Reglas Sigma se gestionan junto al intel en el SOC». | Orden indicado desde OpenCTI: Vincula detecciones Sigma a CTI en OpenCTI. |
| [osquery](osquery.md) | Combinación recíproca: osquery lo enlaza como «Traduce ideas Sigma a queries osquery». | Orden indicado desde osquery: Diseña la query y despliega el pack. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Elastic detection-rules](detection-rules.md) · [Hayabusa](hayabusa.md)

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada r2026-07-01 (2026-07-09) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/SigmaHQ/sigma#readme) · [2](https://sigmahq.io/)</sub>

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

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Abre el material original y localiza la sección relacionada con tu tarea.
2. Elige una referencia o ejemplo; revisa sus requisitos y su procedencia antes de instalar nada.
3. Conserva solo las piezas que necesitas y consulta la ficha de cada proyecto enlazado.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/SigmaHQ/sigma/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://sigmahq.io/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Sigma para mi objetivo y necesito pasos guiados. Lee https://github.com/SigmaHQ/sigma/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona SigmaHQ/sigma y convierte una regla con pySigma hacia tu SIEM de lab..

**Qué comprobar:** La regla convertida se carga y dispara con telemetría de prueba..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- portar una detección a varios SIEM sin reescribirla
- cubrir técnicas ATT&CK con reglas comunitarias

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: portar una detección a varios SIEM sin reescribirla; cubrir técnicas ATT&CK con reglas comunitarias | necesitas una aplicación lista para ejecutar en lugar de material de consulta |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `security` `detection` `siem`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [SigmaHQ/sigma](https://github.com/SigmaHQ/sigma)
- 🌐 Web: <https://sigmahq.io/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/SigmaHQ/sigma/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
