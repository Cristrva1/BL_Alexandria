[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Skills de análisis y seguridad

# 🛡️ SkillSpector

> Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.1k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Escáner de seguridad para skills de agentes de IA, de NVIDIA. Licencia Apache-2.0. Es activo (~26k estrellas, v2.13.4) y forma parte de la canalización NVIDIA Verified Skills.

## ¿Qué hace?

Detecta vulnerabilidades, patrones maliciosos y riesgos en skills antes de instalarlas: 71 patrones en 17 categorías, como inyección de prompts, exfiltración de datos, escalada de privilegios, cadena de suministro y agencia excesiva. Combina un análisis estático rápido con una evaluación semántica opcional por LLM. El README cita un estudio en el que el 26,1 % de 31.132 skills analizadas tenían vulnerabilidades.

## ¿Cómo lo hace?

Es una herramienta Python que se instala con `uv tool install` desde el repo (con el extra `[mcp]` si quieres `skillspector mcp`) o se ejecuta con Docker (`docker run … skillspector scan ./skill --no-llm`). El análisis por LLM requiere credenciales de un proveedor (p. ej. Anthropic) en un `.env`. Avisa de que descarga e instala software de terceros con sus propias licencias.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Escanear skills desde el agente con el servidor MCP integrado (`skillspector mcp`). | Instala SkillSpector con el extra `[mcp]` y regístralo como servidor MCP. |
| [Agentic Awesome Skills (AAS)](antigravity-awesome-skills.md) | Revisar skills de colecciones grandes antes de instalarlas. (combinación por arquitectura) | Clona la colección y ejecuta `skillspector scan` sobre cada skill elegida. |
| [Cybersecurity Skills (comunidad)](cybersecurity-skills.md) | Revisar una biblioteca de skills ofensivas y de doble uso antes de dársela a un agente. (combinación por arquitectura) | Escanea las skills que vayas a instalar con `--no-llm` primero. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (7). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[agent-toolkit](agent-toolkit.md) · [Anthropic Skills](anthropic-skills.md) · [autoskills](autoskills.md) · [Awesome Agent Skills](awesome-agent-skills.md) · [Awesome Claude Code](awesome-claude-code.md) · [Awesome Claude Skills](awesome-claude-skills.md) · [BMAD Method](bmad-method.md)

**Notas:** Sin alternativas declaradas. Un escaneo limpio no garantiza que una skill sea segura.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v2.13.4 (2026-11-04) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/NVIDIA/SkillSpector/blob/main/README.md) · [2](https://docs.nvidia.com/skills/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ruta estática no requiere LLM; el análisis semántico puede usar Ollama, un CLI admitido o APIs con consumo |
| Claude Code | Integración documentada por el proyecto |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Se corrige API obligatoria y se mueve a seguridad. codex_cli está deshabilitado como proveedor; Codex como cliente MCP es otra ruta. El README señala una incidencia de stdio |
| Coste | El coste depende del proveedor o la ruta. La ruta estática no requiere LLM; el análisis semántico puede usar Ollama, un CLI admitido o APIs con consumo |
| Equipo | Preparación según la ruta elegida. Python, Git, uv y Make;  entorno Bash compatible para la ruta seleccionada |

Se corrige API obligatoria y se mueve a seguridad. codex_cli está deshabilitado como proveedor; Codex como cliente MCP es otra ruta. El README señala una incidencia de stdio

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python, Git, uv y Make
-  entorno Bash compatible para la ruta seleccionada

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Clone the repository
git clone https://github.com/NVIDIA/skillspector.git
cd skillspector

# Create and activate virtual environment
uv venv .venv && source .venv/bin/activate
# or: python3 -m venv .venv && source .venv/bin/activate

# Install for production use
make install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/NVIDIA/SkillSpector/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SkillSpector para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA/SkillSpector/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Escanea una carpeta de skill de prueba con la opción no-llm.

**Qué comprobar:** Se genera un informe que enumera comprobaciones, hallazgos y cobertura.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Examinar una skill antes de incorporarla al agente
- Añadir un escaneo de skills a una revisión de cambios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Examinar una skill antes de incorporarla al agente; Añadir un escaneo de skills a una revisión de cambios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Se corrige API obligatoria y se mueve a seguridad. codex_cli está deshabilitado como proveedor; Codex como cliente MCP es otra ruta. El README señala una incidencia de stdio

## Stack y modelos

- **Stack:** Python, Git, uv y Make;  entorno Bash compatible para la ruta seleccionada
- **Etiquetas:** `skills` `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)
- 🌐 Web: <https://docs.nvidia.com/skills/scanning-agent-skills>
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría corregida en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/NVIDIA/SkillSpector/blob/main/README.md)
- [Fuente 2](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
