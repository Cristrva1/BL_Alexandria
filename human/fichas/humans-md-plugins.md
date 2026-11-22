[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🎨 HUMANS.md Plugins

> Carga preferencias de trabajo de un archivo HUMANS.md al iniciar una sesión en asistentes compatibles con el plugin.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3 | Apache-2.0 | JavaScript | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

## ¿Qué es?

Carga preferencias de trabajo de un archivo HUMANS.md al iniciar una sesión en asistentes compatibles con el plugin.

## ¿Qué hace?

Carga preferencias de trabajo de un archivo HUMANS.md al iniciar una sesión en asistentes compatibles con el plugin.

## ¿Cómo lo hace?

El plugin lee el archivo de preferencias y añade su contenido al contexto de una sesión.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v0.3.2 (2026-10-18) · licencia declarada Apache-2.0 (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/cmdai-hq/humans-md-plugins/blob/fab03e3c81544d418349b6c477049e31ab9bed1b/README.md) · [2](https://humansmd.dev/) · [3](https://github.com/cmdai-hq/humans-md-plugins/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El componente se usa dentro del agente. El modelo y los conectores externos se contratan por separado. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. El código o las instrucciones no incluyen el consumo del agente ni de los servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Node.js 22.18 o posterior según el README, un anfitrión compatible y perfil de prueba. |

Consume el acceso y los límites del agente donde lo configures. No incluye servicios externos de generación, datos o alojamiento.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js 22.18 o posterior según el README, un anfitrión compatible y perfil de prueba.

1. Crea un perfil de prueba desde el ejemplo y sigue la instalación de tu cliente. En Codex revisa el hook antes de confiar en él.
2. Crea un perfil con una sola preferencia ficticia y abre una nueva sesión.
3. Comprueba el resultado: el agente puede leer y explicar esa preferencia sin cargar notas reales.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://humansmd.dev/)

[Abrir la web o descarga indicada por el autor](https://humansmd.dev/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar HUMANS.md Plugins para mi objetivo y necesito pasos guiados. Lee https://humansmd.dev/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un perfil con una sola preferencia ficticia y abre una nueva sesión..

**Qué comprobar:** El agente puede leer y explicar esa preferencia sin cargar notas reales..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Pedir que el agente avise antes de modificar archivos de configuración.
- Reutilizar preferencias de comunicación entre dos clientes compatibles.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Pedir que el agente avise antes de modificar archivos de configuración.; Reutilizar preferencias de comunicación entre dos clientes compatibles. | no usas un agente compatible con skills |

**Limitaciones:** El autor indica pruebas solo en macOS. El proveedor del agente puede procesar el perfil; no guardes contraseñas ni datos sensibles. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** JavaScript, package.json
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [cmdai-hq/humans-md-plugins](https://github.com/cmdai-hq/humans-md-plugins)
- 🌐 Web: <https://humansmd.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cmdai-hq/humans-md-plugins/blob/fab03e3c81544d418349b6c477049e31ab9bed1b/README.md)
- [Fuente 2](https://humansmd.dev/)
- [Fuente 3](https://github.com/cmdai-hq/humans-md-plugins/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
