[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 📦 skills

> Skills de ingeniería de Matt Pocock para trabajar sobre requisitos, diseño, implementación y revisión, con plugins para Claude Code y Codex.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 325k | MIT | Shell | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skills de agente de Matt Pocock (MIT) para «ingeniería real, no vibe coding»: pequeñas, adaptables y combinables. Activas (v1.3.2).

## ¿Qué hace?

Incluye skills para preguntar qué flujo conviene (`ask-matt`), sesiones de interrogatorio que generan documentación, triaje de incidencias, mejora de arquitectura, convertir conversaciones en especificaciones y tickets, implementar especificaciones, planificar trabajos grandes, retrospectivas y prototipos desechables. El autor las presenta como alternativa a procesos más rígidos como GSD, BMAD o Spec-Kit.

## ¿Cómo lo hace?

Se instalan como plugin con actualización automática en Claude Code (`claude plugin install mattpocock-skills@claude-plugins-official`), Codex y GitHub Copilot (CLI y VS Code), o como archivos editables con `npx skills@latest add mattpocock/skills -a <agente>`. Recomienda elegir un solo método por agente e incluir `setup-matt-pocock-skills`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin oficial. | No combines el plugin con skills.sh en el mismo agente: duplicarías las skills. |
| [Claude Code Plugins Directory](claude-plugins-official.md) | Marketplace desde el que se instala en Claude Code. | Igual que arriba. |
| [Codex CLI](codex.md) | Marketplace propio para Codex. | `codex plugin marketplace add mattpocock/skills`. |
| [plugins](plugins.md) | Combinación recíproca: plugins lo enlaza como «Skills de ingeniería instalables también en Cursor (combinación por arquitectura)». | Orden indicado desde plugins: `npx skills add mattpocock/skills -a cursor`. |

**Notas:** Se quitó awesome-agent-skills: es un catálogo, no una integración.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v1.3.2 (2026-10-29) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mattpocock/skills/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las skills consumen el agente; no suministran un modelo ni créditos de API |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El README actual ya documenta plugins para Claude Code y Codex; se corrige la ficha que los dejaba sin documentar |
| Coste | Consumo del agente que ya utilizas. Las skills consumen el agente; no suministran un modelo ni créditos de API |
| Equipo | Preparación según la ruta elegida. Claude Code o Codex;  carpeta de prueba para la primera skill |

El README actual ya documenta plugins para Claude Code y Codex; se corrige la ficha que los dejaba sin documentar

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code o Codex
-  carpeta de prueba para la primera skill

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
claude plugin install mattpocock-skills@claude-plugins-official
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mattpocock/skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar skills para mi objetivo y necesito pasos guiados. Lee https://github.com/mattpocock/skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige una skill de ingeniería e invócala sobre una tarea acotada.

**Qué comprobar:** El agente aplica la skill y produce el artefacto que esa tarea pide.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar requisitos de una función antes de implementarla
- Organizar una refactorización pequeña con un plan revisable

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar requisitos de una función antes de implementarla; Organizar una refactorización pequeña con un plan revisable | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README actual ya documenta plugins para Claude Code y Codex; se corrige la ficha que los dejaba sin documentar

## Stack y modelos

- **Stack:** Claude Code o Codex;  carpeta de prueba para la primera skill
- **Etiquetas:** `skills` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [mattpocock/skills](https://github.com/mattpocock/skills)
- 🌐 Web: <https://aihero.dev/skills>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mattpocock/skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
