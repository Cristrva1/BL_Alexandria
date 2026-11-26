[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 blender-skills

> Skills para guiar a un agente por modelado y preparación de escenas en Blender mediante herramientas y conexiones MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.3k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Paquete de 94 skills (MIT) de arjun988 para artistas de Blender, que se presenta como un equipo de arte técnico senior. Sin releases; su ficha en el marketplace de Anthropic estaba en revisión según el README.

## ¿Qué hace?

Cubre modelado, producción, técnica, pipeline, estilos artísticos, paquetes de terror, mundos, ambientes y jugabilidad, ejecutando las acciones en Blender a través de Blender MCP en lugar de dar tutoriales.

## ¿Cómo lo hace?

Skills en `.claude/skills` que se copian al proyecto para Claude Code, a `.cursor/skills` en Cursor, al directorio de Kiro o a la ruta de skills de Codex. La documentación completa está en su web en Vercel.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Blender MCP](blender-mcp.md) | Vía de ejecución de las skills en Blender. | Instala y conecta el MCP siguiendo `docs/BLENDER_MCP_SETUP.md`. |
| [blender](blender.md) | Aplicación sobre la que actúan. | Blender instalado y abierto con el complemento del MCP. |
| [Claude Code](claude-code.md) | Agente compatible documentado. | Copia las skills al `.claude/skills` del proyecto. |

Estado en GitHub: activo · último push 2026-11-06 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/arjun988/blender-skills/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las skills usan el plan del agente; Blender y servicios de assets adicionales tienen condiciones propias |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | La función básica no necesita un modelo. Documenta Claude Code y Codex; instalar instrucciones no instala ni autentica automáticamente el servidor Blender MCP |
| Coste | Consumo del agente que ya utilizas. Las skills usan el plan del agente; Blender y servicios de assets adicionales tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Blender; agente; conexión MCP o scripting; escena de prueba |

Documenta Claude Code y Codex; instalar instrucciones no instala ni autentica automáticamente el servidor Blender MCP

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Blender
- agente
- conexión MCP o scripting
- escena de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/arjun988/blender-skills.git
cp -r blender-skills/.claude/skills /path/to/your/project/.claude/skills/
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/arjun988/blender-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar blender-skills para mi objetivo y necesito pasos guiados. Lee https://github.com/arjun988/blender-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prueba un blockout sencillo y revisa objetos y escala antes de exportar.

**Qué comprobar:** Puedes abrir y editar la escena generada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un objeto para un juego
- Revisar un pipeline de assets 3D

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un objeto para un juego; Revisar un pipeline de assets 3D | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code y Codex; instalar instrucciones no instala ni autentica automáticamente el servidor Blender MCP

## Stack y modelos

- **Stack:** Blender; agente; conexión MCP o scripting; escena de prueba
- **Etiquetas:** `creacion-3d` `skill` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [arjun988/blender-skills](https://github.com/arjun988/blender-skills)
- 🌐 Web: <https://blender-skills.vercel.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/arjun988/blender-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
