[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Directorios y aprendizaje

# 📂 OWASP Top 10

> Documento de concienciación de OWASP con los diez riesgos más críticos en aplicaciones web, con ejemplos, prevención y CWE asociados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.6k | CC-BY-SA-4.0 | HTML | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 56/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** CC-BY-SA-4.0. Fuente: [LICENSE](https://github.com/OWASP/Top10/blob/master/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Proyecto insignia de OWASP: el documento de referencia sobre los riesgos de seguridad más críticos en aplicaciones web.

## ¿Qué hace?

Clasifica y explica diez categorías de riesgo a partir de datos de la industria y una encuesta comunitaria, con ejemplos, prevención y referencias.

## ¿Cómo lo hace?

Contenido Markdown en GitHub publicado en owasp.org con traducciones; se actualiza por ediciones (2017, 2021 y siguientes).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OWASP ASVS](asvs.md) | ASVS convierte los riesgos del Top 10 en requisitos verificables. | Top 10 para concienciar; ASVS para verificar. |
| [OWASP CheatSheet Series](cheatsheetseries.md) | Las Cheat Sheets detallan la prevención de cada riesgo. | Consulta la hoja enlazada desde cada riesgo. |
| [OWASP Juice Shop](juice-shop.md) | Juice Shop permite practicar los riesgos del Top 10. | Lee el riesgo; practícalo en Juice Shop local. |
| [OWASP Threat Dragon](threat-dragon.md) | Combinación recíproca: OWASP Threat Dragon lo enlaza como «El Top 10 orienta qué riesgos priorizar en el modelo de una aplicación web». | Orden indicado desde OWASP Threat Dragon: Revisa el Top 10 antes de enumerar amenazas. |

Estado en GitHub: activo · último push 2026-09-24 · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OWASP/Top10#readme) · [2](https://owasp.org/Top10/)</sub>

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

[Instrucciones originales de instalación](https://github.com/OWASP/Top10/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://owasp.org/Top10/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP Top 10 para mi objetivo y necesito pasos guiados. Lee https://github.com/OWASP/Top10/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre la edición vigente en owasp.org/Top10 y lee la categoría de control de acceso roto..

**Qué comprobar:** Obtienes la descripción, ejemplos de ataque, prevención y CWE relacionados..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- formar a un equipo de desarrollo en los riesgos web más comunes
- priorizar una revisión de código por categorías de riesgo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: formar a un equipo de desarrollo en los riesgos web más comunes; priorizar una revisión de código por categorías de riesgo | necesitas una aplicación lista para ejecutar en lugar de material de consulta |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Contenido CC BY-SA 4.0: puedes reutilizarlo citando a OWASP y compartiendo las obras derivadas con la misma licencia. Licencia CC BY-SA 4.0 en LICENSE pese a NOASSERTION en la API de GitHub. No es un estándar de cumplimiento: para requisitos verificables usa ASVS.

## Stack y modelos

- **Stack:** HTML, Makefile, package.json, requirements.txt
- **Etiquetas:** `security` `awareness` `web` `standard`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OWASP/Top10](https://github.com/OWASP/Top10)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OWASP/Top10/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
