[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧭 Spec Kit

> Kit de GitHub para desarrollo guiado por especificaciones con agentes de código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 150k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## ¿Qué es?

Kit de código abierto de GitHub (MIT) que da a los agentes de código procesos estructurados, plantillas reutilizables y resultados documentados. Muy activo (v1.4.0).

## ¿Qué hace?

Ofrece desarrollo guiado por especificaciones (en el núcleo), corrección de errores y evaluación de ideas (como extensiones), además de primitivas para adaptar o crear procesos: integraciones, extensiones, overlays de flujos, paquetes por rol y catálogos autoalojados para trabajar sin conexión.

## ¿Cómo lo hace?

CLI en Python 3.11+ instalada con uv (`uv tool install specify-cli`, luego `specify init <proyecto> --integration <agente>`). Soporta decenas de agentes, entre ellos Claude Code (`claude`), Codex CLI (`codex`), Gemini CLI (`gemini`), GitHub Copilot, Cursor, opencode y Hermes. Las extensiones comunitarias deben revisarse antes de instalarlas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Integración `--integration claude`. | Instala el agente antes de `specify init`. |
| [Codex CLI](codex.md) | Integración `--integration codex`. | Igual que arriba. |
| [Gemini CLI](gemini-cli.md) | Integración `--integration gemini`. | Igual que arriba. |

**Notas:** Alternativas (elige una): bmad-method, claude-task-master.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v1.4.0 (2026-11-10) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/github/spec-kit/blob/main/README.md) · [2](https://github.github.io/spec-kit/integrations/index.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El CLI no incluye el modelo; los encargos consumen el acceso del agente elegido |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. La guía actual usa integration y claves claude, codex y agy; no reutilizar comandos de versiones antiguas sin comprobarlos |
| Coste | Consumo del agente que ya utilizas. El CLI no incluye el modelo; los encargos consumen el acceso del agente elegido |
| Equipo | Preparación según la ruta elegida. Python y uv según la guía;  un agente con integración soportada |

La guía actual usa integration y claves claude, codex y agy; no reutilizar comandos de versiones antiguas sin comprobarlos

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv según la guía
-  un agente con integración soportada

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.github.io/spec-kit/installation.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Spec Kit para mi objetivo y necesito pasos guiados. Lee https://github.github.io/spec-kit/installation.html. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Inicializa un proyecto de prueba y selecciona su integración antes de crear una especificación.

**Qué comprobar:** El proyecto contiene el scaffolding y los comandos o skills de ese agente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Especificar una función con requisitos y criterios de aceptación
- Mantener un flujo común en un equipo que usa agentes diferentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Especificar una función con requisitos y criterios de aceptación; Mantener un flujo común en un equipo que usa agentes diferentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La guía actual usa integration y claves claude, codex y agy; no reutilizar comandos de versiones antiguas sin comprobarlos

## Stack y modelos

- **Stack:** Python y uv según la guía;  un agente con integración soportada
- **Etiquetas:** `coding-agent` `skills` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [BMAD Method](bmad-method.md) | 55.4k | Metodología ágil con agentes especializados (analista, PM, arquitecto, dev) para desarrollar con IA. |
| [claude-task-master](claude-task-master.md) | 28.4k | Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP. |

## Enlaces

- 🐙 GitHub: [github/spec-kit](https://github.com/github/spec-kit)
- 🌐 Web: <https://github.github.com/spec-kit/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/github/spec-kit/blob/main/README.md)
- [Fuente 2](https://github.github.io/spec-kit/integrations/index.html)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
