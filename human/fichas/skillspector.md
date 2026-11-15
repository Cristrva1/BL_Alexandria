[🏠 Inicio](../README.md) › [🧠 Skills, Prompts & Guías de Agente](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🛡️ SkillSpector

> Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 25.2k | Apache-2.0 | Python | 2026-11-10 | 📦 Sí |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Qué es

Resuelve el riesgo de ejecutar skills de terceros sin revisión.

## Por qué destaca

Aporta una capa de seguridad muy necesaria sobre catálogos enormes de skills de terceros, y proviene de NVIDIA, lo que le da respaldo institucional. Es agnóstica al asistente, así que sirve para skills de Claude Code, Codex, Cursor, etc.

## Cómo funciona

Analiza los archivos de la skill en busca de comandos shell peligrosos, llamadas de red sospechosas o instrucciones ocultas, y reporta los hallazgos en un resumen accionable sin ejecutar nada.

## Instalación rápida

Clona el repo e instala sus dependencias (Python/Node) según el README; ejecútalo apuntando al directorio de skills que quieras auditar. Requiere Python y/o Node según el modo de escaneo.

## Casos de uso

- Auditar skills de terceros antes de instalarlas
- Detectar comandos peligrosos o exfiltración
- Revisar catálogos descargados en lote

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| instalas skills externas o curas catálogos | solo usas skills propias de confianza |

## Stack y modelos

- **Stack:** Python/Node, Docker
- **Modelos / API:** Agnóstico; no invoca LLMs, solo analiza archivos.
- **Etiquetas:** `skills` `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Agentic Awesome Skills](antigravity-awesome-skills.md) | 49.5k | Biblioteca comunitaria de más de 2.800 skills SKILL.md para Claude Code, Codex, Cursor y Gemini CLI, con instalador npx y MCP local. |

## Enlaces

- 🐙 GitHub: [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)
- 🌐 Web: <https://docs.nvidia.com/skills/scanning-agent-skills>
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
