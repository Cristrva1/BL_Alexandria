[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Blender MCP

> Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 34.5k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

MCP for Blender (antes blender-mcp), integración de terceros que conecta Blender con cualquier LLM, creada por @ahujasid. Licencia MIT. Es muy popular (~35k estrellas) y no está hecha por la Blender Foundation; el paquete PyPI pasó a llamarse `mcp-for-blender`.

## ¿Qué hace?

Permite que un asistente cree y modifique escenas, objetos, materiales e iluminación, inspeccione la escena y ejecute código Python de Blender directamente. Integra recursos de Poly Haven, Sketchfab y Poly Pizza, y modelos 3D generados con Meshy, Tripo, Hyper3D Rodin o Hunyuan3D. Incluye controles de telemetría (`disable_telemetry`).

## ¿Cómo lo hace?

Un comando instala el complemento de Blender y configura las apps de IA; también hay instalación manual con `uv` (`uvx mcp-for-blender`; `uvx blender-mcp` sigue funcionando). Requiere Blender y Python con uv. La ejecución de código arbitrario en Blender exige guardar el trabajo antes de usarlo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Controlar Blender desde un cliente MCP como Claude Code. | Ejecuta el setup y elige tu cliente. |
| [blender](blender.md) | Complemento que se instala dentro de Blender. | Instala Blender y activa el complemento. |
| [unity-mcp](unity-mcp.md) | Llevar a Unity los modelos creados en Blender, ambos controlados por agentes. (combinación por arquitectura) | Exporta desde Blender e importa en Unity con MCP for Unity. |
| [blender-skills](blender-skills.md) | Combinación recíproca: blender-skills lo enlaza como «Vía de ejecución de las skills en Blender». | Orden indicado desde blender-skills: Instala y conecta el MCP siguiendo `docs/BLENDER_MCP_SETUP.md`. |
| [dream-loop](dream-loop.md) | Combinación recíproca: dream-loop lo enlaza como «Vía preferida para que el agente controle Blender». | Orden indicado desde dream-loop: Blender abierto con el complemento del MCP antes de iniciar el bucle. |
| [ChatDev](chatdev.md) | Combinación recíproca: ChatDev lo enlaza como «ChatDev documenta blender-mcp como requisito de su flujo de construcción 3D». | Orden indicado desde ChatDev: Blender primero, luego blender-mcp, y por último el flujo de ChatDev. |

**Notas:** Sin alternativas declaradas. Revisa los ajustes de telemetría y el uso de servicios 3D de terceros.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ahujasid/mcp-for-blender/blob/main/README.md) · [2](https://pypi.org/project/mcp-for-blender/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El control básico no requiere API extra; generación premium y proveedores de modelos 3D tienen condiciones propias |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. El paquete actual es mcp-for-blender; plugin comunitario sin afiliación con Blender Foundation |
| Coste | El coste depende del proveedor o la ruta. El control básico no requiere API extra; generación premium y proveedores de modelos 3D tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Blender >=3; uv; cliente MCP; escena de prueba |

El paquete actual es mcp-for-blender; plugin comunitario sin afiliación con Blender Foundation

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Blender >=3
- uv
- cliente MCP
- escena de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (powershell):**

```
winget install --id=astral-sh.uv -e
uvx mcp-for-blender setup
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ahujasid/mcp-for-blender/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Blender MCP para mi objetivo y necesito pasos guiados. Lee https://github.com/ahujasid/mcp-for-blender/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un cubo y cambia su material en una escena vacía.

**Qué comprobar:** Puedes ver el objeto y el material en Blender.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Bocetar una escena 3D
- Automatizar ajustes de objetos y materiales

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Bocetar una escena 3D; Automatizar ajustes de objetos y materiales | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El paquete actual es mcp-for-blender; plugin comunitario sin afiliación con Blender Foundation

## Stack y modelos

- **Stack:** Blender >=3; uv; cliente MCP; escena de prueba
- **Etiquetas:** `mcp` `design` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender)
- 🌐 Web: <https://www.mcp-for-blender.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ahujasid/mcp-for-blender/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
