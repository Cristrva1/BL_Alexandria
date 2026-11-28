[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# 📚 OWASP Java Encoder

> Codificación contextual de salida para Java (HTML, JavaScript, CSS, XML, URI) que previene XSS, sin dependencias en tiempo de ejecución.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 552 | BSD-3-Clause | Java | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 55/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto OWASP: un codificador de salida contextual para Java.

## ¿Qué hace?

Codifica datos según el contexto de salida (HTML, atributos, JavaScript, CSS, URI, XML) para evitar inyecciones XSS.

## ¿Cómo lo hace?

Biblioteca Java 8+ sin dependencias, con etiquetas y funciones EL para JSP y Jakarta; licencia BSD-3-Clause.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OWASP Java HTML Sanitizer](java-html-sanitizer.md) | Java Encoder codifica la salida; el sanitizer cubre el caso de HTML enriquecido permitido. | Codifica toda salida; usa el sanitizer solo donde aceptes HTML. |
| [OWASP CheatSheet Series](cheatsheetseries.md) | La Cheat Sheet de prevención de XSS describe la codificación por contexto que aplica la biblioteca. | Consulta la hoja al elegir el método Encode.for* de cada contexto. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.6.0 (2026-10-18) · licencia declarada BSD-3-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OWASP/owasp-java-encoder#readme) · [2](https://owasp.org/www-project-java-encoder/)</sub>

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

[Instrucciones originales de instalación](https://github.com/OWASP/owasp-java-encoder/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://owasp.org/www-project-java-encoder/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP Java Encoder para mi objetivo y necesito pasos guiados. Lee https://github.com/OWASP/owasp-java-encoder/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade la dependencia Maven del README a un proyecto Java de prueba y usa Encode.forHtml..

**Qué comprobar:** La salida queda codificada para el contexto HTML..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- codificar datos de usuario al renderizar plantillas JSP
- escapar valores insertados en JavaScript en línea

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: codificar datos de usuario al renderizar plantillas JSP; escapar valores insertados en JavaScript en línea | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Java, pom.xml
- **Etiquetas:** `security` `xss` `encoding` `java`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OWASP/owasp-java-encoder](https://github.com/OWASP/owasp-java-encoder)
- 🌐 Web: <https://owasp.org/projects/java-encoder>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OWASP/owasp-java-encoder/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
