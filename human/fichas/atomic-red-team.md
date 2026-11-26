[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Explotación, C2 y post-explotación

# 📂 Atomic Red Team

> Biblioteca de pruebas ATT&CK pequeñas y documentadas para validar detecciones y controles en un laboratorio propio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.9k | MIT | C | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟡 medio

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Biblioteca open source de Red Canary con pruebas ATT&CK atómicas para emulación de adversario.

## ¿Qué hace?

Cada atomic describe precondiciones, comandos y criterios de éxito de una técnica ATT&CK concreta.

## ¿Cómo lo hace?

Se clona el repositorio; las pruebas se lanzan con Invoke-AtomicRedTeam u otros runners documentados.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Wazuh](wazuh.md) | Los atomics generan telemetría que Wazuh debe detectar. | Configura Wazuh; ejecuta el atomic y revisa alertas. |
| [Sigma](sigma.md) | Convierte hallazgos en reglas Sigma tras validar el atomic. | Ejecuta el atomic; escribe/ajusta la regla Sigma. |
| [CALDERA](caldera.md) | Caldera puede orquestar atomics en campañas automatizadas. | Ten Caldera listo; importa o lanza atomics según la guía. |
| [Evilginx2](evilginx2.md) | Combinación recíproca: Evilginx2 lo enlaza como «Complementa con atomics de phishing/inicial access». | Orden indicado desde Evilginx2: Atomic + Evilginx2 en purple team. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[SET](social-engineer-toolkit.md)

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/redcanaryco/atomic-red-team#readme) · [2](https://github.com/redcanaryco/invoke-atomicredteam)</sub>

## Ver similares

Grupo **Emulación de adversarios**: Atomic Red Team ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [CALDERA](caldera.md) ⭐ recomendado | 64 | Si buscas esto: framework Apache de emulación de adversario automatizado: agentes, adversarios ATT&CK y operaciones controladas desde web. |
| 2 | **Atomic Red Team** (esta ficha) | 62 | Si buscas esto: biblioteca de pruebas ATT&CK pequeñas y documentadas para validar detecciones y controles en un laboratorio propio. |

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

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/redcanaryco/atomic-red-team/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/redcanaryco/atomic-red-team)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Atomic Red Team para mi objetivo y necesito pasos guiados. Lee https://github.com/redcanaryco/atomic-red-team/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona el repo y ejecuta un atomic con Invoke-AtomicRedTeam sobre una VM de laboratorio..

**Qué comprobar:** Observas el artefacto/comportamiento esperado y contrastas con tus alertas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- validar una regla de detección con un atomic concreto
- entrenar al SOC con técnicas ATT&CK controladas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: validar una regla de detección con un atomic concreto; entrenar al SOC con técnicas ATT&CK controladas | necesitas una aplicación lista para ejecutar en lugar de material de consulta |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** C, Gemfile, pyproject.toml
- **Etiquetas:** `security` `attack` `purple`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [redcanaryco/atomic-red-team](https://github.com/redcanaryco/atomic-red-team)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/redcanaryco/atomic-red-team/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
