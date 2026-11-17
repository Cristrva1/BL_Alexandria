[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Directorios y aprendizaje

# 📂 OWASP AISVS

> Estándar OWASP de verificación de seguridad para sistemas de IA: requisitos verificables para datos, modelos, agentes e infraestructura.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 590 | CC-BY-SA-4.0 | — | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 54/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto OWASP: el estándar de verificación de seguridad para sistemas de inteligencia artificial.

## ¿Qué hace?

Define requisitos verificables sobre gobierno de datos de entrenamiento, validación de entradas, seguridad del modelo, agentes autónomos, privacidad e infraestructura.

## ¿Cómo lo hace?

Documento versionado en GitHub con capítulos numerados; sigue el formato de ASVS. Licencia CC BY-SA 4.0.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OWASP ASVS](asvs.md) | ASVS cubre la aplicación web; AISVS añade los requisitos propios de IA. | Aplica ASVS a la app y AISVS a los componentes de IA. |

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada v1.01 (2026-10-16) · licencia declarada CC-BY-SA-4.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OWASP/AISVS#readme)</sub>

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

[Instrucciones originales de instalación](https://github.com/OWASP/AISVS/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/OWASP/AISVS#readme)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP AISVS para mi objetivo y necesito pasos guiados. Lee https://github.com/OWASP/AISVS/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre el repositorio y revisa los capítulos de AISVS aplicables a un proyecto con LLM..

**Qué comprobar:** Obtienes una lista de requisitos con identificadores para verificar..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- definir requisitos de seguridad para una aplicación con LLM y agentes
- auditar controles de un pipeline de ML

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: definir requisitos de seguridad para una aplicación con LLM y agentes; auditar controles de un pipeline de ML | necesitas una aplicación lista para ejecutar en lugar de material de consulta |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Contenido CC BY-SA 4.0: puedes reutilizarlo citando a OWASP y compartiendo las obras derivadas con la misma licencia.

## Stack y modelos

- **Etiquetas:** `security` `ai` `standard` `requirements`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OWASP/AISVS](https://github.com/OWASP/AISVS)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OWASP/AISVS/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
