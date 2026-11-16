[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 👨‍💻 Aider

> Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 50.1k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## ¿Qué es?

Aider, programación en pareja con IA en la terminal, de Aider-AI. Licencia Apache-2.0. Es maduro (~50k estrellas, v0.86.0), pero su último cambio es de mayo de 2026.

## ¿Qué hace?

Edita el repositorio a partir de instrucciones, con un mapa del código para proyectos grandes, soporte para más de 100 lenguajes, commits automáticos en git, lint y tests, voz e imágenes. Funciona con modelos en la nube y locales.

## ¿Cómo lo hace?

Se instala con `python -m pip install aider-install` y `aider-install`. Conecta con casi cualquier LLM mediante LiteLLM y construye el mapa del repo con Tree-sitter.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | Capa de conexión con proveedores de modelos. | Viene incluida; configura las claves del proveedor. |
| [Ollama](ollama.md) | Modelos locales documentados. | Ejecuta aider con un modelo `ollama/...`. |
| [tree-sitter](tree-sitter.md) | Mapa del repositorio basado en Tree-sitter. | No requiere instalación aparte. |
| [ast-grep](ast-grep.md) | Combinación recíproca: ast-grep lo enlaza como «Aplicar refactorizaciones masivas deterministas junto a la edición con IA. (combinación por arquitectura)». | Orden indicado desde ast-grep: Usa ast-grep para el cambio mecánico y Aider para el resto. |
| [openidea](openidea.md) | Combinación recíproca: openidea lo enlaza como «Pareja de programación con git en la terminal integrada. (combinación por arquitectura)». | Orden indicado desde openidea: Ejecuta aider dentro del proyecto. |
| [SWE-bench](swe-bench.md) | Combinación recíproca: SWE-bench lo enlaza como «Comparar el rendimiento de distintos modelos en Aider. (combinación por arquitectura)». | Orden indicado desde SWE-bench: Exporta los parches como predicciones. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[lazygit](lazygit.md)

**Notas:** Alternativas (elige una): opencode, cline. Actividad reciente baja.

Estado en GitHub: activo · último push 2026-05-22 · última versión publicada v0.86.0 (2025-08-09) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Aider-AI/aider/blob/main/README.md) · [2](https://aider.chat/docs/llms.html) · [3](https://aider.chat/docs/repomap.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. APIs remotas por consumo o modelos locales según configuración; no aporta créditos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Sus modelos de ejemplo incluyen versiones antiguas; la presencia de Claude en la lista no implica una suscripción Claude Code |
| Coste | El coste depende del proveedor o la ruta. APIs remotas por consumo o modelos locales según configuración; no aporta créditos |
| Equipo | Preparación según la ruta elegida. Python; Git; proveedor o modelo local; repositorio de prueba |

Sus modelos de ejemplo incluyen versiones antiguas; la presencia de Claude en la lista no implica una suscripción Claude Code

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- Git
- proveedor o modelo local
- repositorio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
python -m pip install aider-install
aider-install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Aider-AI/aider/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Aider para mi objetivo y necesito pasos guiados. Lee https://github.com/Aider-AI/aider/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una copia de un proyecto y pide una explicación antes de aceptar cambios y commits.

**Qué comprobar:** Puedes revisar archivos incluidos y cualquier diff propuesto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Corregir una función pequeña
- Programar en pareja desde terminal

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Corregir una función pequeña; Programar en pareja desde terminal | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Sus modelos de ejemplo incluyen versiones antiguas; la presencia de Claude en la lista no implica una suscripción Claude Code

## Stack y modelos

- **Stack:** Python; Git; proveedor o modelo local; repositorio de prueba
- **Etiquetas:** `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenCode](opencode.md) | 227k | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. |
| [Cline](cline.md) | 71.6k | Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. |

## Enlaces

- 🐙 GitHub: [Aider-AI/aider](https://github.com/Aider-AI/aider)
- 🌐 Web: <https://aider.chat/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Aider-AI/aider/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
