[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Directorios y aprendizaje

# 📂 OWASP Web Security Testing Guide

> Guía OWASP de referencia para probar la seguridad de aplicaciones web: metodología y casos de prueba con identificadores WSTG.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.3k | CC-BY-SA-4.0 | CSS | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 71/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto insignia de OWASP: la guía de pruebas de seguridad para aplicaciones y servicios web.

## ¿Qué hace?

Describe la metodología de prueba y cientos de casos (configuración, identidad, autenticación, sesiones, validación de entradas, lógica de negocio, API) con identificadores estables.

## ¿Cómo lo hace?

Contenido Markdown versionado en GitHub, publicado en owasp.org con versiones estables y la rama en desarrollo; licencia CC BY-SA 4.0.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ZAP (Zed Attack Proxy)](zaproxy.md) | ZAP ejecuta muchas de las pruebas que describe la guía. | Lee el caso WSTG; reprodúcelo con ZAP en un objetivo autorizado. |
| [OWASP Juice Shop](juice-shop.md) | Juice Shop permite practicar los casos de prueba sin riesgo. | Juice Shop en local; sigue los casos de la guía. |
| [OWASP CheatSheet Series](cheatsheetseries.md) | Las Cheat Sheets explican cómo corregir lo que la guía detecta. | Prueba con la WSTG; corrige con la Cheat Sheet correspondiente. |
| [OWASP ASVS](asvs.md) | ASVS define los requisitos que las pruebas de la WSTG verifican. | Fija el nivel ASVS; selecciona los casos WSTG asociados. |
| [WebGoat](webgoat.md) | Combinación recíproca: WebGoat lo enlaza como «La WSTG explica la metodología de prueba detrás de cada lección». | Orden indicado desde WebGoat: Lee la sección de la WSTG antes de cada lección. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[OWASP OWTF](owtf.md)

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v4.2 (2020-12-03) · licencia declarada CC-BY-SA-4.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OWASP/wstg#readme) · [2](https://owasp.org/www-project-web-security-testing-guide/)</sub>

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

[Instrucciones originales de instalación](https://github.com/OWASP/wstg/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://owasp.org/www-project-web-security-testing-guide/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP Web Security Testing Guide para mi objetivo y necesito pasos guiados. Lee https://github.com/OWASP/wstg/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre la versión estable de la guía en el sitio de OWASP y elige una categoría, por ejemplo pruebas de autenticación..

**Qué comprobar:** Obtienes los casos de prueba, sus objetivos y cómo verificarlos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- planificar un pentest web con una lista de casos WSTG
- citar identificadores WSTG en un informe de hallazgos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: planificar un pentest web con una lista de casos WSTG; citar identificadores WSTG en un informe de hallazgos | necesitas una aplicación lista para ejecutar en lugar de material de consulta |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Contenido CC BY-SA 4.0: puedes reutilizarlo citando a OWASP y compartiendo las obras derivadas con la misma licencia.

## Stack y modelos

- **Stack:** CSS
- **Etiquetas:** `security` `testing` `guide` `web`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OWASP/wstg](https://github.com/OWASP/wstg)
- 🌐 Web: <https://owasp.org/www-project-web-security-testing-guide/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OWASP/wstg/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
