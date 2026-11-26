[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🧩 Home Assistant MCP

> Conecta Home Assistant con un asistente mediante MCP para consultar entidades y trabajar con automatizaciones de domótica.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.1k | MIT | Python | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 68/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Conecta Home Assistant con un asistente mediante MCP para consultar entidades y trabajar con automatizaciones de domótica.

## ¿Qué hace?

Conecta Home Assistant con un asistente mediante MCP para consultar entidades y trabajar con automatizaciones de domótica.

## ¿Cómo lo hace?

El conector presenta entidades y acciones como herramientas MCP con el alcance de la conexión.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Home Assistant](home-assistant.md) | Expone entidades de esa instalación mediante MCP. | — |

Estado en GitHub: activo · último push 2026-11-22 · última versión publicada v9.2.0 (2026-11-11) · licencia declarada MIT (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/homeassistant-ai/ha-mcp/blob/d068d1218983a369d8082ec923c14445cd462393/README.md) · [2](https://homeassistant-ai.github.io/ha-mcp/) · [3](https://github.com/advisories/GHSA-q855-8rh5-jfgq) · [4](https://github.com/homeassistant-ai/ha-mcp/blob/master/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El servidor MCP no llama a un LLM por sí solo. Usa un cliente compatible, con modelo local o remoto, para controlarlo. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El README describe clientes conectados a modelos locales; la calidad depende del modelo y del contexto. |
| Coste | El coste depende del proveedor o la ruta. El acceso al cliente y el coste del backend, datos o cómputo se evalúan por separado. |
| Equipo | Equipo normal; revisar dependencias. Home Assistant compatible o el demo oficial, y un cliente MCP de prueba. |

Configura este servidor en un cliente MCP compatible, incluido Claude Code o Codex. Sus servicios y permisos se preparan aparte.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Home Assistant compatible o el demo oficial, y un cliente MCP de prueba.

1. Abre la guía Get Started y elige su servidor demo antes de cambiar la instalación real de Home Assistant.
2. Inicia con el demo y pide una consulta sin cambios sobre una entidad ficticia.
3. Comprueba el resultado: la herramienta devuelve el estado de la entidad sin accionar dispositivos.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://homeassistant-ai.github.io/ha-mcp/)

[Abrir la web o descarga indicada por el autor](https://homeassistant-ai.github.io/ha-mcp/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Home Assistant MCP para mi objetivo y necesito pasos guiados. Lee https://homeassistant-ai.github.io/ha-mcp/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Inicia con el demo y pide una consulta sin cambios sobre una entidad ficticia..

**Qué comprobar:** La herramienta devuelve el estado de la entidad sin accionar dispositivos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar qué sensores aparecen en el demo.
- Revisar como borrador la automatización de una luz virtual.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar qué sensores aparecen en el demo.; Revisar como borrador la automatización de una luz virtual. | necesitas un producto autónomo y esta pieza requiere un cliente MCP |

**Limitaciones:** Hay avisos públicos: el release revisado v9.2.0 es posterior a los pisos publicados para el paquete. Mantén endpoint y token privados y prueba con permisos mínimos. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python, Dockerfile, docker-compose.yml, pyproject.toml
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp)
- 🌐 Web: <https://homeassistant-ai.github.io/ha-mcp/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/homeassistant-ai/ha-mcp/blob/d068d1218983a369d8082ec923c14445cd462393/README.md)
- [Fuente 2](https://homeassistant-ai.github.io/ha-mcp/)
- [Fuente 3](https://github.com/advisories/GHSA-q855-8rh5-jfgq)
- [Fuente 4](https://github.com/homeassistant-ai/ha-mcp/blob/master/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
