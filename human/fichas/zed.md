[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Editores y extensiones de código

# 🖥️ Zed

> Editor de código de alto rendimiento y multijugador, de los creadores de Atom y Tree-sitter, con IA integrada y agentes externos por ACP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 95.1k | GPL-3.0 (Apache-2.0 en componentes marcados) | Rust | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Editor de código abierto de Zed Industries. El código es principalmente GPL-3.0-or-later con componentes Apache-2.0 donde se indica. Muy activo; ofrece planes de pago para su IA alojada.

## ¿Qué hace?

Edita código con alto rendimiento, colaboración multijugador, Tree-sitter, LSP, depuración, terminal integrada y control de versiones, y ofrece un panel de agente con modelos configurables y agentes externos compatibles con ACP.

## ¿Cómo lo hace?

Escrito en Rust; se descarga para macOS, Linux y Windows o se instala con gestores de paquetes. Los agentes externos se integran mediante Agent Client Protocol.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Zed documenta el uso de Claude Code (Claude Agent) como agente externo por ACP. | Instala Claude Code; después añádelo como agente externo en Zed. |
| [Gemini CLI](gemini-cli.md) | Gemini CLI es uno de los agentes externos documentados en Zed. | Instala Gemini CLI; después actívalo en el panel de agentes. |
| [Codex CLI](codex.md) | Zed documenta Codex como agente externo. | Instala Codex; después configúralo en Zed. |
| [Qwen Code](qwen-code.md) | Qwen Code documenta su integración con Zed. | Instala Qwen Code; después configúralo como agente externo. |

**Notas:** No hay otro editor completo en el catálogo; cline y kilocode son extensiones para VS Code.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.28.1 (2026-11-11) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/zed-industries/zed/blob/main/README.md) · [2](https://zed.dev/docs/ai/external-agents)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La función básica y las funciones de IA se configuran por separado; activar un proveedor puede añadir credenciales y consumo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | El coste depende del proveedor o la ruta. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
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

[Instrucciones originales de instalación](https://github.com/zed-industries/zed/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Zed para mi objetivo y necesito pasos guiados. Lee https://github.com/zed-industries/zed/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga Zed para tu sistema, abre un proyecto y configura un agente externo como Gemini CLI..

**Qué comprobar:** El agente responde en el panel de Zed y propone cambios en el proyecto..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- editar código con un editor rápido y colaborar en tiempo real
- usar Claude Code, Gemini CLI o Codex dentro del editor por ACP

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: editar código con un editor rápido y colaborar en tiempo real; usar Claude Code, Gemini CLI o Codex dentro del editor por ACP | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Rust, Cargo.toml
- **Etiquetas:** `editor` `rust` `coding` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [zed-industries/zed](https://github.com/zed-industries/zed)
- 🌐 Web: <https://zed.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/zed-industries/zed/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
