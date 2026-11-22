[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Creación, renderizado y animación 3D

# 🧩 Open Reality

> Convierte video propio en escenas 3D consultables y ofrece herramientas MCP para trabajar con la reconstrucción desde un asistente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 662 | BSD-2-Clause | Python | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 3 Avanzado — preparación media; se instala dentro de un agente (skill, plugin o MCP); necesita GPU

## ¿Qué es?

Convierte video propio en escenas 3D consultables y ofrece herramientas MCP para trabajar con la reconstrucción desde un asistente.

## ¿Qué hace?

Convierte video propio en escenas 3D consultables y ofrece herramientas MCP para trabajar con la reconstrucción desde un asistente.

## ¿Cómo lo hace?

Un motor de reconstrucción procesa video y el conector expone operaciones de consulta sobre la escena.

Estado en GitHub: activo · último push 2026-11-18 · última versión publicada v0.4.0 (2026-10-20) · licencia declarada BSD-2-Clause (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/reality-opened/openreality/blob/86f545d1ff1c9191cedc3e85dbae9b65fec29ced/README.md) · [2](https://open-reality.io/mcp) · [3](https://github.com/reality-opened/openreality/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El cliente MCP utiliza su modelo; el backend necesita cómputo para reconstruir la escena, que puede alojarse en equipo propio. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | El coste depende del proveedor o la ruta. La reconstrucción puede usar GPU propia o alquilada. El servicio alojado, el cliente y los pesos tienen condiciones independientes. |
| Equipo | Equipo normal; revisar dependencias. Node.js para el conector, datos propios y un servidor que pueda procesar el video; la ruta alojada y la GPU tienen requisitos aparte. |

Configura este servidor en un cliente MCP compatible, incluido Claude Code o Codex. Sus servicios y permisos se preparan aparte.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js para el conector, datos propios y un servidor que pueda procesar el video; la ruta alojada y la GPU tienen requisitos aparte.

1. Prepara el backend que describe la guía y configura solo un cliente MCP; para la primera prueba utiliza una escena sin personas ni datos reales.
2. Prueba primero un ejemplo de escena y distingue si lo procesa el servidor propio o el servicio alojado.
3. Comprueba el resultado: puedes abrir la escena o consultar un elemento sin compartir datos privados.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://open-reality.io/mcp)

[Abrir la web o descarga indicada por el autor](https://open-reality.io/mcp)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Open Reality para mi objetivo y necesito pasos guiados. Lee https://open-reality.io/mcp. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prueba primero un ejemplo de escena y distingue si lo procesa el servidor propio o el servicio alojado..

**Qué comprobar:** Puedes abrir la escena o consultar un elemento sin compartir datos privados..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar un objeto propio grabado desde varios ángulos.
- Comprobar la representación 3D de un elemento de una escena de ejemplo.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar un objeto propio grabado desde varios ángulos.; Comprobar la representación 3D de un elemento de una escena de ejemplo. | necesitas un producto autónomo y esta pieza requiere un cliente MCP |

**Limitaciones:** Los pesos mencionados pueden estar limitados a usos no comerciales. Alojamiento y cómputo GPU no están incluidos por instalar el conector. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [reality-opened/openreality](https://github.com/reality-opened/openreality)
- 🌐 Web: <https://open-reality.io/mcp>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/reality-opened/openreality/blob/86f545d1ff1c9191cedc3e85dbae9b65fec29ced/README.md)
- [Fuente 2](https://open-reality.io/mcp)
- [Fuente 3](https://github.com/reality-opened/openreality/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
