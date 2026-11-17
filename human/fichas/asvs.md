[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Directorios y aprendizaje

# 📂 OWASP ASVS

> Estándar OWASP de verificación de seguridad de aplicaciones: requisitos verificables en tres niveles para diseñar, desarrollar y auditar.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.8k | CC-BY-SA-4.0 | HTML | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 56/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto insignia de OWASP: el estándar de verificación de seguridad de aplicaciones web.

## ¿Qué hace?

Define requisitos de seguridad verificables (autenticación, sesiones, control de acceso, validación, criptografía, API, configuración) en niveles L1 a L3.

## ¿Cómo lo hace?

Documento versionado en GitHub con identificadores estables y exportaciones en formatos legibles por máquina para integrarlo en herramientas y procesos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OWASP Web Security Testing Guide](wstg.md) | La WSTG explica cómo probar los requisitos de ASVS. | Fija los requisitos ASVS; prueba con la WSTG. |
| [OWASP CheatSheet Series](cheatsheetseries.md) | Las Cheat Sheets guían la implementación de cada requisito. | Requisito ASVS → Cheat Sheet correspondiente. |
| [OWASP Threat Dragon](threat-dragon.md) | El modelo de amenazas ayuda a elegir el nivel y los requisitos prioritarios. | Modela amenazas; selecciona requisitos ASVS como mitigaciones. |
| [OWASP Top 10](owasp-top10.md) | El Top 10 sensibiliza; ASVS concreta qué verificar. | Usa el Top 10 como introducción y ASVS como estándar. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[OWASP AISVS](aisvs.md) · [OWASP pytm](pytm.md)

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada latest (2026-10-26) · licencia declarada CC-BY-SA-4.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OWASP/ASVS#readme) · [2](https://owasp.org/www-project-application-security-verification-standard/)</sub>

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

[Instrucciones originales de instalación](https://github.com/OWASP/ASVS/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://owasp.org/www-project-application-security-verification-standard/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP ASVS para mi objetivo y necesito pasos guiados. Lee https://github.com/OWASP/ASVS/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga la última versión estable de ASVS desde el repositorio o el sitio de OWASP y elige el nivel 1 para un proyecto..

**Qué comprobar:** Obtienes la lista de requisitos aplicables con sus identificadores..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- definir los requisitos de seguridad de un proyecto según su nivel de riesgo
- usar los requisitos como lista de verificación en una auditoría

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: definir los requisitos de seguridad de un proyecto según su nivel de riesgo; usar los requisitos como lista de verificación en una auditoría | necesitas una aplicación lista para ejecutar en lugar de material de consulta |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Contenido CC BY-SA 4.0: puedes reutilizarlo citando a OWASP y compartiendo las obras derivadas con la misma licencia.

## Stack y modelos

- **Stack:** HTML, Makefile
- **Etiquetas:** `security` `standard` `requirements` `appsec`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OWASP/ASVS](https://github.com/OWASP/ASVS)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OWASP/ASVS/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
