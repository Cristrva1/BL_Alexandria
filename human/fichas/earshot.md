[🏠 Inicio](../README.md) › [🎬 Audio, transcripción, voz y música](../categorias/29-audio-voz-musica.md) › Procesamiento y limpieza de audio

# 🧩 earshot

> Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.8k | MIT | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La herramienta opcional llm_critique utiliza GEMINI_API_KEY; las herramientas locales de audio no implican ese consumo. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. El análisis de audio se ejecuta con modelos locales en CPU. La crítica con LLM es una función opcional separada. |
| Coste | El coste depende del proveedor o la ruta. Los modelos de audio locales consumen CPU, memoria y disco. La crítica opcional mediante Gemini tiene el acceso y las cuotas de ese proveedor. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Configura este servidor en un cliente MCP compatible, incluido Claude Code o Codex. Sus servicios y permisos se preparan aparte.

## Qué puedes hacer con él

Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP.

## Cómo funciona

Un cliente MCP invoca las herramientas del servidor para trabajar con el programa o servicio conectado.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible y el programa o servicio que va a controlar la herramienta.

1. Prepara el servidor y sus dependencias siguiendo la configuración del README.
2. Añade el comando o la URL en el cliente MCP y configura los permisos y credenciales de los servicios conectados.
3. Comprueba que aparecen sus herramientas y prueba una consulta pequeña antes de permitir modificaciones.

[Instrucciones originales de instalación](https://github.com/Leonxlnx/earshot/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar earshot para mi objetivo y necesito pasos guiados. Lee https://github.com/Leonxlnx/earshot/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| buscas esta función: Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP. | necesitas un producto autónomo y esta pieza requiere un anfitrión compatible |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `edicion` `mcp` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Leonxlnx/earshot](https://github.com/Leonxlnx/earshot)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/Leonxlnx/earshot/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
