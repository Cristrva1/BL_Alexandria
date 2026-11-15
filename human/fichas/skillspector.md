[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Skills de análisis y seguridad

# 🛡️ SkillSpector

> Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.1k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

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

## Qué puedes hacer con él

Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos.

## Por qué destaca

Usos propuestos: Examinar una skill antes de incorporarla al agente; Añadir un escaneo de skills a una revisión de cambios.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Agentic Awesome Skills (AAS)](antigravity-awesome-skills.md) | 49.7k | Biblioteca de skills para varios agentes con selección revisable y distribución desde GitHub; antes llamada Antigravity Awesome Skills. |

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
