[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Blender MCP

> Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 34.5k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

## Qué puedes hacer con él

Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP.

## Por qué destaca

Usos propuestos: Bocetar una escena 3D; Automatizar ajustes de objetos y materiales.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |

## Enlaces

- 🐙 GitHub: [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender)
- 🌐 Web: <https://www.mcp-for-blender.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ahujasid/mcp-for-blender/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
