[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Directorios y aprendizaje

# 📂 OWASP MASVS

> Estándar OWASP de verificación de seguridad de aplicaciones móviles: controles para almacenamiento, criptografía, red, plataforma y resiliencia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.5k | CC-BY-SA-4.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 56/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto insignia de OWASP: el estándar de seguridad para aplicaciones móviles.

## ¿Qué hace?

Agrupa controles de seguridad (STORAGE, CRYPTO, AUTH, NETWORK, PLATFORM, CODE, RESILIENCE, PRIVACY) que una app móvil debe cumplir.

## ¿Cómo lo hace?

Documento versionado en GitHub y publicado en mas.owasp.org, enlazado a las pruebas del MASTG; licencia CC BY-SA 4.0.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OWASP MASTG](mastg.md) | El MASTG enseña a probar cada control MASVS. | Controles MASVS → pruebas MASTG. |

Estado en GitHub: activo · último push 2026-09-21 · última versión publicada v2.1.0 (2024-01-18) · licencia declarada CC-BY-SA-4.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OWASP/masvs#readme) · [2](https://mas.owasp.org/MASVS/)</sub>

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

[Instrucciones originales de instalación](https://github.com/OWASP/masvs/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://mas.owasp.org/MASVS/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP MASVS para mi objetivo y necesito pasos guiados. Lee https://github.com/OWASP/masvs/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre mas.owasp.org/MASVS y revisa el grupo MASVS-STORAGE..

**Qué comprobar:** Obtienes los controles y enlaces a sus pruebas en el MASTG..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- fijar requisitos de seguridad para una app móvil nueva
- estructurar una auditoría móvil por grupos de control

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: fijar requisitos de seguridad para una app móvil nueva; estructurar una auditoría móvil por grupos de control | necesitas una aplicación lista para ejecutar en lugar de material de consulta |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Contenido CC BY-SA 4.0: puedes reutilizarlo citando a OWASP y compartiendo las obras derivadas con la misma licencia.

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `security` `mobile` `standard`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OWASP/masvs](https://github.com/OWASP/masvs)
- 🌐 Web: <https://mas.owasp.org/MASVS>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OWASP/masvs/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
