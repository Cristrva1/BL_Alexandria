[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › SDKs y frameworks para crear MCP

# 🧰 MCP Inspector

> Herramienta oficial para probar y depurar servidores MCP desde una interfaz web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.3k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La inspección no requiere modelo; una herramienta conectada puede llamar servicios de pago |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Las instrucciones CLAUDE.md del repositorio sirven para contribuir al código; no hacen del Inspector un plugin de Claude Code |
| Coste | Sin pago a un modelo en la ruta básica. La inspección no requiere modelo; una herramienta conectada puede llamar servicios de pago |
| Equipo | Preparación según la ruta elegida. Node ^22.23.4 o ^24.22.1 o >=26.12.1; servidor MCP de prueba |

Las instrucciones CLAUDE.md del repositorio sirven para contribuir al código; no hacen del Inspector un plugin de Claude Code

## Qué puedes hacer con él

Herramienta oficial para probar y depurar servidores MCP desde una interfaz web.

## Por qué destaca

Usos propuestos: Depurar un esquema MCP; Reproducir un fallo de una herramienta.

## Cómo funciona

Las instrucciones CLAUDE.md del repositorio sirven para contribuir al código; no hacen del Inspector un plugin de Claude Code

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node ^22.23.4 o ^24.22.1 o >=26.12.1
- servidor MCP de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npx @modelcontextprotocol/inspector                   # web UI (default)
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/modelcontextprotocol/inspector/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MCP Inspector para mi objetivo y necesito pasos guiados. Lee https://github.com/modelcontextprotocol/inspector/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta un servidor local, lista herramientas y llama una con datos ficticios.

**Qué comprobar:** Puedes inspeccionar argumentos, respuesta y errores sin un agente de IA.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Depurar un esquema MCP
- Reproducir un fallo de una herramienta

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Depurar un esquema MCP; Reproducir un fallo de una herramienta | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las instrucciones CLAUDE.md del repositorio sirven para contribuir al código; no hacen del Inspector un plugin de Claude Code

## Stack y modelos

- **Stack:** Node ^22.23.4 o ^24.22.1 o >=26.12.1; servidor MCP de prueba
- **Etiquetas:** `mcp` `evaluation` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [FastMCP](fastmcp.md) | 28.5k | La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas. |
| [MCP TypeScript SDK](mcp-typescript-sdk.md) | 13.8k | SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol. |

## Enlaces

- 🐙 GitHub: [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)
- 🌐 Web: <https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector>
- 🧪 Receta: [Construir una app o servidor MCP](../playbooks/construir-una-appservidor-mcp.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/modelcontextprotocol/inspector/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
