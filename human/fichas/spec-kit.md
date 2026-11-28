[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧭 Spec Kit

> Kit de GitHub para desarrollo guiado por especificaciones con agentes de código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 150k | MIT | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 76/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

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
| [Awesome GitHub Copilot](awesome-copilot.md) | Combinación recíproca: Awesome GitHub Copilot lo enlaza como «Proceso de desarrollo guiado por especificaciones con integración para Copilot». | Orden indicado desde Awesome GitHub Copilot: `specify init <proyecto> --integration copilot`. |
| [elephant-goldfish-model](elephant-goldfish-model.md) | Combinación recíproca: elephant-goldfish-model lo enlaza como «Revisar con ojos frescos las especificaciones que genera Spec Kit (combinación por arquitectura)». | Orden indicado desde elephant-goldfish-model: Genera la especificación y pásala por `egm-review`. |

**Notas:** Alternativas (elige una): bmad-method, claude-task-master.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v1.4.0 (2026-11-10) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/github/spec-kit/blob/main/README.md) · [2](https://github.github.io/spec-kit/integrations/index.html)</sub>

## Ver similares

Grupo **Desarrollo guiado por especificaciones**: Spec Kit ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Spec Kit** (esta ficha) ⭐ recomendado | 76 | Si buscas esto: kit de GitHub para desarrollo guiado por especificaciones con agentes de código. |
| 2 | [BMAD Method](bmad-method.md) | 57 | Si buscas esto: metodología ágil con agentes especializados (analista, PM, arquitecto, dev) para desarrollar con IA. |

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
- un agente con integración soportada

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/github/spec-kit.git
```

Comando copiado literalmente de la documentación oficial enlazada desde el README (sección «Step 1: Build the wheel on a connected machine»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.github.io/spec-kit/install/air-gapped.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Spec Kit para mi objetivo y necesito pasos guiados. Lee https://github.github.io/spec-kit/install/air-gapped.html. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
