[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🖥️ OpenJarvis

> Crea un asistente personal con chat y flujos que pueden usar modelos locales, con conectores opcionales para tus servicios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.9k | Apache-2.0 | Python | 2026-11-22 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 58/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Crea un asistente personal con chat y flujos que pueden usar modelos locales, con conectores opcionales para tus servicios.

## ¿Qué hace?

Crea un asistente personal con chat y flujos que pueden usar modelos locales, con conectores opcionales para tus servicios.

## ¿Cómo lo hace?

El asistente combina motores de inferencia con perfiles de conversación y, si los habilitas, herramientas y memoria.

Estado en GitHub: activo · último push 2026-11-22 · última versión publicada desktop-v1.0.5 (2026-11-11) · licencia declarada Apache-2.0 (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/open-jarvis/OpenJarvis/blob/c05ebe99e524a269a08d017ce3730a436ab4c46b/README.md) · [2](https://github.com/open-jarvis/OpenJarvis/releases) · [3](https://github.com/open-jarvis/OpenJarvis/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ruta local o básica no necesita una clave de LLM alojado. Las modalidades remotas se configuran aparte. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. La guía del proyecto documenta componentes locales. Confirma qué parte corre en tu equipo y la licencia de los modelos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume equipo; proveedores, servicios alojados y bases remotas pueden cobrar. |
| Equipo | Equipo normal; revisar dependencias. Distribución oficial para tu sistema, memoria para el modelo inicial y espacio para pesos; Node.js 22+ si usas la interfaz desde el código. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Distribución oficial para tu sistema, memoria para el modelo inicial y espacio para pesos; Node.js 22+ si usas la interfaz desde el código.

1. Desde Releases elige la distribución para tu sistema y abre el chat básico; confirma motor y modelo antes de activar skills.
2. Elige una distribución oficial y empieza con el chat básico sin conectores.
3. Comprueba el resultado: el modelo configurado responde a una pregunta y puedes identificar si la ruta usada fue local.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/open-jarvis/OpenJarvis/releases)

[Abrir la web o descarga indicada por el autor](https://github.com/open-jarvis/OpenJarvis/releases)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenJarvis para mi objetivo y necesito pasos guiados. Lee https://github.com/open-jarvis/OpenJarvis/releases. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige una distribución oficial y empieza con el chat básico sin conectores..

**Qué comprobar:** El modelo configurado responde a una pregunta y puedes identificar si la ruta usada fue local..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Conversar con un modelo descargado sin conectar cuentas.
- Probar búsqueda sobre un pequeño conjunto de documentos ficticios.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Conversar con un modelo descargado sin conectar cuentas.; Probar búsqueda sobre un pequeño conjunto de documentos ficticios. | necesitas una herramienta estable y auditada para datos sensibles |

**Limitaciones:** Evita pegar instaladores remotos directamente en la terminal. Revisar por separado las funciones que leen cuentas o envían datos externos. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python, Makefile, pyproject.toml
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [open-jarvis/OpenJarvis](https://github.com/open-jarvis/OpenJarvis)
- 🌐 Web: <https://openjarvis.stanford.edu/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/open-jarvis/OpenJarvis/blob/c05ebe99e524a269a08d017ce3730a436ab4c46b/README.md)
- [Fuente 2](https://github.com/open-jarvis/OpenJarvis/releases)
- [Fuente 3](https://github.com/open-jarvis/OpenJarvis/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
