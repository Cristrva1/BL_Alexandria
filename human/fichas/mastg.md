[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Directorios y aprendizaje

# 📂 OWASP MASTG

> Guía OWASP de pruebas de seguridad de apps móviles (Android e iOS): técnicas, herramientas y casos de prueba ligados a MASVS.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.3k | CC-BY-SA-4.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 69/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto insignia de OWASP: el manual de pruebas de seguridad y de ingeniería inversa de aplicaciones móviles.

## ¿Qué hace?

Explica cómo verificar los controles MASVS en Android e iOS con pruebas estáticas y dinámicas, técnicas de ingeniería inversa y herramientas recomendadas.

## ¿Cómo lo hace?

Contenido Markdown publicado como sitio MkDocs en mas.owasp.org, con identificadores estables de pruebas, técnicas y herramientas; licencia CC BY-SA 4.0.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OWASP MASVS](masvs.md) | MASVS define los controles que el MASTG enseña a probar. | Elige los controles MASVS; aplica las pruebas del MASTG. |
| [frida](frida.md) | Frida es la herramienta de instrumentación usada en muchas pruebas dinámicas del MASTG. | Instala Frida en un dispositivo de pruebas y sigue la técnica del MASTG. |
| [Apktool](apktool.md) | Apktool descompila APK para las pruebas estáticas de Android. | Descompila la APK propia con Apktool y revisa según el MASTG. |
| [jadx](jadx.md) | jadx decompila a Java para revisar la lógica de la app. | Abre la APK en jadx durante las pruebas estáticas. |

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada v2.0.0 (2026-06-30) · licencia declarada CC-BY-SA-4.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OWASP/mastg#readme) · [2](https://mas.owasp.org/MASTG/)</sub>

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

[Instrucciones originales de instalación](https://github.com/OWASP/mastg/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://mas.owasp.org/MASTG/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP MASTG para mi objetivo y necesito pasos guiados. Lee https://github.com/OWASP/mastg/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre mas.owasp.org, elige un control MASVS (por ejemplo MASVS-STORAGE) y sigue sus pruebas para Android..

**Qué comprobar:** Obtienes los pasos, las herramientas y la evidencia esperada para cada prueba..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- auditar el almacenamiento local y la red de una app Android propia
- preparar un plan de pruebas para una app iOS antes de publicarla

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: auditar el almacenamiento local y la red de una app Android propia; preparar un plan de pruebas para una app iOS antes de publicarla | necesitas una aplicación lista para ejecutar en lugar de material de consulta |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Contenido CC BY-SA 4.0: puedes reutilizarlo citando a OWASP y compartiendo las obras derivadas con la misma licencia. Las pruebas sobre apps de terceros requieren autorización.

## Stack y modelos

- **Stack:** Python, package.json
- **Etiquetas:** `security` `mobile` `android` `ios` `guide`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OWASP/mastg](https://github.com/OWASP/mastg)
- 🌐 Web: <http://mas.owasp.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OWASP/mastg/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
