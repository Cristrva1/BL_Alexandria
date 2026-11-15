[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Figma Context MCP

> Servidor MCP que entrega a los agentes de código el layout de tus diseños de Figma para implementarlos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.2k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. El servidor expone herramientas; el modelo lo aporta el cliente MCP. La herramienta puede necesitar credenciales de otros servicios. |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Un servidor MCP no incluye un LLM; puede ser invocado por un agente con un modelo local si ese cliente lo soporta. |
| Coste | El coste depende del proveedor o la ruta. Requiere credenciales y acceso al archivo de Figma. La clave de Figma no es una clave de un LLM. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

Puede conectarse a un cliente con soporte MCP, incluido Claude Code o Codex. Debes configurar el servidor y sus permisos.

## Qué puedes hacer con él

Simplifica la respuesta de la API de Figma y da al agente solo lo relevante (estructura, estilos, medidas) para convertir un diseño en código.

## Por qué destaca

Muy usado con Cursor y Claude Code para pasar de Figma a código con fidelidad.

## Cómo funciona

Llama a la API de Figma con tu token y transforma el resultado en un resumen compacto para el modelo.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un cliente MCP compatible.
- Las credenciales del servicio conectado, si las pide el servidor.

1. Instala o configura el servidor según su README.
2. Añade su comando o URL en la configuración MCP de tu cliente.
3. Comprueba que aparecen las herramientas antes de asignar una tarea.

[Instrucciones originales de instalación](https://github.com/GLips/Figma-Context-MCP/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Figma Context MCP para mi objetivo y necesito pasos guiados. Lee https://github.com/GLips/Figma-Context-MCP/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Implementar pantallas desde Figma
- Mantener fidelidad de diseño
- Acelerar maquetación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| implementas diseños de Figma con un agente de código | no usas Figma |

## Stack y modelos

- **Stack:** TypeScript
- **Etiquetas:** `mcp` `design` `ui` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [ui](ui.md) | 128k | Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada. |
| [tailwindcss](tailwindcss.md) | 98.6k | Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado. |

## Enlaces

- 🐙 GitHub: [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)
- 🌐 Web: <https://www.framelink.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/GLips/Figma-Context-MCP/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
