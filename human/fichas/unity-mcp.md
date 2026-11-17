[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🧩 unity-mcp

> Servidor MCP que permite a un asistente operar escenas, scripts y recursos dentro de un proyecto del editor Unity.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16k | MIT | C# | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

MCP for Unity, puente entre asistentes de IA y el editor de Unity, de Coplay (patrocinado y mantenido por Aura). Licencia MIT. Es activo (~16k estrellas, v10.3.0).

## ¿Qué hace?

Permite que Claude, Codex, VS Code, modelos locales y otros clientes creen y modifiquen escenas, GameObjects, scripts, assets y configuraciones del editor de Unity. Expone herramientas de gestión de escena, scripts y consola para iterar con el agente.

## ¿Cómo lo hace?

Se instala en Unity desde el Package Manager con la URL de git y requiere Python 3.10+ con uv. Funciona con Unity 2021.3 LTS hasta 6.x y con cualquier cliente MCP; el paquete configura los clientes habituales.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Cliente MCP soportado según el README. | Instala el paquete en Unity y configura Claude Code desde su ventana. |
| [Codex CLI](codex.md) | Cliente MCP soportado según el README. | Configura Codex desde la ventana de MCP for Unity. |
| [blender](blender.md) | Crear modelos en Blender y llevarlos a Unity. (combinación por arquitectura) | Exporta FBX/GLB desde Blender e impórtalos en Unity. |
| [Blender MCP](blender-mcp.md) | Combinación recíproca: Blender MCP lo enlaza como «Llevar a Unity los modelos creados en Blender, ambos controlados por agentes. (combinación por arquitectura)». | Orden indicado desde Blender MCP: Exporta desde Blender e importa en Unity con MCP for Unity. |

**Notas:** Sin alternativas declaradas. Usa control de versiones: el agente puede modificar escenas y scripts.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v10.3.0 (2026-10-04) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/CoplayDev/unity-mcp/blob/beta/README.md) · [2](https://coplaydev.github.io/unity-mcp/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El conector es MIT; el agente o LLM local y la licencia Unity mantienen sus condiciones |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Instala el paquete desde Package Manager y configura el cliente; guarda una copia del proyecto antes de automatizar ediciones |
| Coste | Consumo del agente que ya utilizas. El conector es MIT; el agente o LLM local y la licencia Unity mantienen sus condiciones |
| Equipo | Preparación según la ruta elegida. Unity 2021.3 LTS a 6.x; Python 3.10+ mediante uv; cliente MCP |

Instala el paquete desde Package Manager y configura el cliente; guarda una copia del proyecto antes de automatizar ediciones

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Unity 2021.3 LTS a 6.x
- Python 3.10+ mediante uv
- cliente MCP

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/CoplayDev/unity-mcp/blob/beta/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar unity-mcp para mi objetivo y necesito pasos guiados. Lee https://github.com/CoplayDev/unity-mcp/blob/beta/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En un proyecto vacío pide crear un cubo en el origen con un Rigidbody.

**Qué comprobar:** El cubo aparece y puedes inspeccionar el componente en Unity.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Bocetar escenas de una demo
- Ejecutar pruebas del proyecto desde un agente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Bocetar escenas de una demo; Ejecutar pruebas del proyecto desde un agente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Instala el paquete desde Package Manager y configura el cliente; guarda una copia del proyecto antes de automatizar ediciones

## Stack y modelos

- **Stack:** Unity 2021.3 LTS a 6.x; Python 3.10+ mediante uv; cliente MCP
- **Etiquetas:** `servidores` `mcp` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp)
- 🌐 Web: <https://coplaydev.github.io/unity-mcp/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/CoplayDev/unity-mcp/blob/beta/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
