[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Directorios, clientes y aprendizaje

# 📚 MCP for Beginners

> Curso abierto de Microsoft para aprender MCP con ejemplos en .NET, Java, TypeScript, JavaScript y Python.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.7k | MIT | Jupyter Notebook | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Curso de Microsoft para aprender Model Context Protocol con ejemplos prácticos en C#, Java, JavaScript, Rust, Python y TypeScript. Licencia MIT. Es popular (~18k estrellas, sin releases) y tiene más de 50 traducciones automáticas.

## ¿Qué hace?

Recorre desde los conceptos básicos de MCP hasta la construcción de servidores y clientes, seguridad, despliegue y casos reales, con lecciones y código por lenguaje. Mantiene las traducciones con Co-op Translator.

## ¿Cómo lo hace?

Se clona el repo (el README recomienda un clon parcial sin traducciones porque pesan mucho) y se siguen las lecciones. Cada ejemplo usa el SDK oficial del lenguaje correspondiente.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [MCP Python SDK](mcp-python-sdk.md) | SDK oficial usado en los ejemplos de Python. | Instala `mcp[cli]` para seguir las lecciones de Python. |
| [FastMCP](fastmcp.md) | Framework popular para practicar servidores Python tras el curso. (combinación por arquitectura) | Rehaz un ejercicio con FastMCP para comparar. |
| [MCP Inspector](mcp-inspector.md) | Probar los servidores de los ejercicios. (combinación por arquitectura) | Lanza el Inspector contra cada servidor que construyas. |
| [AI Agents for Beginners](ai-agents-for-beginners.md) | Combinación recíproca: AI Agents for Beginners lo enlaza como «Profundizar en MCP, que el curso trata en la lección de protocolos agénticos (enlazado en el README)». | Orden indicado desde AI Agents for Beginners: Tómalo después de la lección 11. |
| [Generative AI for Beginners](generative-ai-for-beginners.md) | Combinación recíproca: Generative AI for Beginners lo enlaza como «Curso complementario sobre Model Context Protocol (enlazado en el README)». | Orden indicado desde Generative AI for Beginners: Tómalo cuando llegues a la parte de herramientas y agentes. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-13 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/microsoft/mcp-for-beginners/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El curso se lee sin API; los ejercicios concretos pueden usar modelos, nube o servicios de pago |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. No necesitas ejecutar todos los lenguajes ni desplegar todos los ejemplos para empezar |
| Coste | Sin pago a un modelo en la ruta básica. El curso se lee sin API; los ejercicios concretos pueden usar modelos, nube o servicios de pago |
| Equipo | Preparación según la ruta elegida. Navegador; lenguaje elegido para los ejercicios |

No necesitas ejecutar todos los lenguajes ni desplegar todos los ejemplos para empezar

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- lenguaje elegido para los ejercicios

1. Lee la introducción y completa un ejercicio de herramienta con entrada y salida pequeñas.
2. Comprueba: Puedes explicar el papel del host, cliente y servidor.

**Entrada documentada (bash):**

```
git clone https://github.com/microsoft/mcp-for-beginners.git
```

Comando copiado literalmente de el README; revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/microsoft/mcp-for-beginners/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MCP for Beginners para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/mcp-for-beginners/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee la introducción y completa un ejercicio de herramienta con entrada y salida pequeñas.

**Qué comprobar:** Puedes explicar el papel del host, cliente y servidor.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender conceptos MCP desde cero
- Comparar un servidor Python con otro TypeScript

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender conceptos MCP desde cero; Comparar un servidor Python con otro TypeScript | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No necesitas ejecutar todos los lenguajes ni desplegar todos los ejemplos para empezar

## Stack y modelos

- **Stack:** Navegador; lenguaje elegido para los ejercicios
- **Etiquetas:** `mcp` `learning`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/mcp-for-beginners/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
