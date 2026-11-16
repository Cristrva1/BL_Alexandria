[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 👨‍💻 Open Interpreter

> Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con modelos locales o baratos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 68.9k | Apache-2.0 | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## ¿Qué es?

Open Interpreter, ahora reescrito en Rust a partir de Codex como agente de programación optimizado para modelos de bajo coste. Licencia Apache-2.0. Tiene ~69k estrellas (rust-v0.0.61); el proyecto Python original sigue como fork comunitario (endolith/open-interpreter).

## ¿Qué hace?

Ofrece una interfaz parecida a Codex con harness específicos por proveedor, por ejemplo una reimplementación del harness de Kimi Code para Kimi K3. Admite `exec`, MCP, ACP, skills, hooks, permisos y `AGENTS.md`.

## ¿Cómo lo hace?

Se instala con un script (`curl … | sh` o PowerShell). La versión Rust es muy reciente y cambia rápido.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Modelos locales baratos. (combinación por arquitectura) | Configura un proveedor local si está soportado. |
| [E2B](e2b.md) | Ejecutar código en sandboxes remotos. (combinación por arquitectura) | Usa un sandbox E2B para tareas arriesgadas. |
| [Context7](context7.md) | Documentación de librerías vía MCP. (combinación por arquitectura) | Añade el MCP de Context7. |

**Notas:** Alternativas (elige una): goose. La descripción antigua (intérprete Python local) ya no corresponde a este repo.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada rust-v0.0.61 (2026-11-11) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/openinterpreter/openinterpreter/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El proveedor elegido define autenticación y coste; llamar abierto a un modelo no acredita que la inferencia se haga localmente |
| Claude Code | Referencia para la herramienta; no es una integración |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La versión actual está escrita en Rust y deriva de Codex; su compatibilidad con el SDK mediante override no implica acceso al plan de Codex; la versión Python tiene otra continuación |
| Coste | El coste depende del proveedor o la ruta. El proveedor elegido define autenticación y coste; llamar abierto a un modelo no acredita que la inferencia se haga localmente |
| Equipo | Preparación según la ruta elegida. Terminal; instalador del sistema; proveedor configurado; carpeta de prueba |

La versión actual está escrita en Rust y deriva de Codex; su compatibilidad con el SDK mediante override no implica acceso al plan de Codex; la versión Python tiene otra continuación

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Terminal
- instalador del sistema
- proveedor configurado
- carpeta de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://www.openinterpreter.com/docs/terminal/install)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Open Interpreter para mi objetivo y necesito pasos guiados. Lee https://www.openinterpreter.com/docs/terminal/install. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca interpreter y revisa modelo y harness antes de pedir una explicación de código.

**Qué comprobar:** Puedes identificar proveedor y permisos sin ejecutar cambios.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un agente con distintos harnesses
- Reutilizar un cliente del SDK de Codex

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un agente con distintos harnesses; Reutilizar un cliente del SDK de Codex | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La versión actual está escrita en Rust y deriva de Codex; su compatibilidad con el SDK mediante override no implica acceso al plan de Codex; la versión Python tiene otra continuación

## Stack y modelos

- **Stack:** Terminal; instalador del sistema; proveedor configurado; carpeta de prueba
- **Etiquetas:** `coding-agent` `local` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [goose](goose.md) | 56.6k | Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM. |

## Enlaces

- 🐙 GitHub: [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter)
- 🌐 Web: <http://openinterpreter.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openinterpreter/openinterpreter/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
