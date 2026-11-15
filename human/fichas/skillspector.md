[🏠 Inicio](../README.md) › [🧠 Mejorar tu agente: skills y prompts](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🛡️ SkillSpector

> Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.1k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | Consumo de APIs o servicios. El escaneo con LLM documenta proveedores con API key. Una propuesta de añadir Ollama no demuestra soporte local implementado. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve el riesgo de ejecutar skills de terceros sin revisión.

## Por qué destaca

Aporta una capa de seguridad muy necesaria sobre catálogos enormes de skills de terceros, y proviene de NVIDIA, lo que le da respaldo institucional. Es agnóstica al asistente, así que sirve para skills de Claude Code, Codex, Cursor, etc.

## Cómo funciona

Analiza los archivos de la skill en busca de comandos shell peligrosos, llamadas de red sospechosas o instrucciones ocultas, y reporta los hallazgos en un resumen accionable sin ejecutar nada.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/NVIDIA/SkillSpector/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SkillSpector para mi objetivo y necesito pasos guiados. Lee https://github.com/NVIDIA/SkillSpector/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `skills` `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Agentic Awesome Skills](antigravity-awesome-skills.md) | 49.7k | Biblioteca comunitaria de más de 2.800 skills SKILL.md para Claude Code, Codex, Cursor y Gemini CLI, con instalador npx y MCP local. |

## Enlaces

- 🐙 GitHub: [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)
- 🌐 Web: <https://docs.nvidia.com/skills/scanning-agent-skills>
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/NVIDIA/SkillSpector/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
