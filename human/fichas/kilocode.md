[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Editores y extensiones de código

# 🖥️ Kilo Code

> Agente de código abierto para VS Code, JetBrains y la terminal, con más de 500 modelos, modos de trabajo y marketplace de agentes, skills y MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 28k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere clave de API

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Agente de código de código abierto (MIT) de Kilo Code, Inc., con servicio en la nube y pasarela de modelos de pago por uso. Muy activo. La extensión nació a partir de Roo Code y Cline; según el README, la CLI actual es un fork de OpenCode.

## ¿Qué hace?

Planifica, escribe y revisa código en VS Code, JetBrains o la terminal, con cambio de modelo a mitad de tarea, modos especializados, marketplace para instalar agentes, skills, servidores MCP y plugins, y ejecución en la nube desde app.kilo.ai.

## ¿Cómo lo hace?

Escrito en TypeScript; se instala como extensión del marketplace de VS Code, plugin de JetBrains o CLI. Requiere cuenta de Kilo o claves de proveedor; el coste depende del modelo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Context7](context7.md) | Context7 se instala como servidor MCP para que el agente consulte documentación actualizada de bibliotecas (combinación por arquitectura). | Añade el servidor MCP de Context7 desde el marketplace o la configuración. |
| [Playwright MCP](playwright-mcp.md) | Playwright MCP permite al agente abrir y probar la aplicación en un navegador (combinación por arquitectura). | Registra Playwright MCP en la configuración de servidores MCP. |
| [GitHub MCP Server](github-mcp-server.md) | El servidor MCP de GitHub da al agente acceso a issues y pull requests (combinación por arquitectura). | Crea un token de GitHub; después registra el servidor MCP. |

**Notas:** Alternativas (elige una): cline. Revisa los cambios antes de aceptarlos y controla el gasto en la pasarela.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v7.8.27 (2026-11-05) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Kilo-Org/kilocode/blob/main/README.md) · [2](https://kilo.ai/)</sub>

## Ver similares

Grupo **Agentes de código en el editor**: Kilo Code ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Cline](cline.md) ⭐ recomendado | 66 | Si buscas esto: agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. |
| 2 | **Kilo Code** (esta ficha) | 60 | Si buscas esto: agente de código abierto para VS Code, JetBrains y la terminal, con más de 500 modelos, modos de trabajo y marketplace de agentes, skills y MCP. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Consumo de APIs o servicios. Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Kilo-Org/kilocode/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Kilo Code para mi objetivo y necesito pasos guiados. Lee https://github.com/Kilo-Org/kilocode/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala la extensión desde el VS Code Marketplace, conecta un modelo y pídele que explique un archivo de tu proyecto..

**Qué comprobar:** El agente responde y propone cambios que puedes aceptar o rechazar..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- delegar en el editor una tarea de refactorización con revisión de cambios
- usar el mismo agente en VS Code y en la terminal con distintos modelos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: delegar en el editor una tarea de refactorización con revisión de cambios; usar el mismo agente en VS Code y en la terminal con distintos modelos | necesitas una herramienta estable y auditada para datos sensibles |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `coding` `agent` `typescript` `vscode`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Cline](cline.md) | 71.6k | Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. |

## Enlaces

- 🐙 GitHub: [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode)
- 🌐 Web: <https://kilo.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Kilo-Org/kilocode/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
