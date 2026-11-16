[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 📂 plugins

> Especificación y colección oficial de plugins de Cursor para estudiar e instalar extensiones de ese agente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.3k | — | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Repositorio oficial de Cursor con plugins para herramientas de desarrollo, frameworks y productos SaaS. Muy activo; GitHub no detecta licencia de repositorio.

## ¿Qué hace?

Contiene unos 130 plugins: propios de Cursor (teaching, continual-learning para actualizar AGENTS.md, cursor-team-kit, thermos para revisiones profundas de ramas, create-plugin, ralph-loop, agent-compatibility…) e integraciones de terceros como Ashby o Workable, organizados por categoría.

## ¿Cómo lo hace?

Cada plugin es un directorio con su manifiesto `.cursor-plugin/plugin.json` que aparece en el marketplace de Cursor.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [skills](skills.md) | Skills de ingeniería instalables también en Cursor (combinación por arquitectura). | `npx skills add mattpocock/skills -a cursor`. |
| [Agent Skills (Addy Osmani)](agent-skills.md) | Skills de ingeniería con guía de instalación para Cursor. | Sigue la sección de Cursor. |
| [wshobson/agents](wshobson-agents.md) | Catálogo de plugins con marketplace para Cursor. | Instala desde su marketplace. |

**Notas:** Sin licencia declarada en la raíz; revisa la de cada plugin de terceros.

Estado en GitHub: activo · último push 2026-11-15 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/cursor/plugins/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Consultar el repositorio es libre; Cursor y los servicios conectados tienen sus planes y tarifas |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El manifiesto es de Cursor. No se afirma que todo el plugin pueda copiarse directamente a Claude Code, Codex o Antigravity |
| Coste | El coste depende del proveedor o la ruta. Consultar el repositorio es libre; Cursor y los servicios conectados tienen sus planes y tarifas |
| Equipo | Preparación según la ruta elegida. Cursor;  revisar el plugin concreto y sus credenciales |

El manifiesto es de Cursor. No se afirma que todo el plugin pueda copiarse directamente a Claude Code, Codex o Antigravity

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cursor
-  revisar el plugin concreto y sus credenciales

1. Abre un plugin del catálogo y lee su manifiesto y guía de conexión.
2. Comprueba: Puedes distinguir sus skills, reglas, servidor MCP y servicios externos.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/cursor/plugins/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar plugins para mi objetivo y necesito pasos guiados. Lee https://github.com/cursor/plugins/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre un plugin del catálogo y lee su manifiesto y guía de conexión.

**Qué comprobar:** Puedes distinguir sus skills, reglas, servidor MCP y servicios externos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Encontrar una integración de un servicio que ya utiliza tu equipo
- Estudiar cómo empaquetar reglas y skills para Cursor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Encontrar una integración de un servicio que ya utiliza tu equipo; Estudiar cómo empaquetar reglas y skills para Cursor | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El manifiesto es de Cursor. No se afirma que todo el plugin pueda copiarse directamente a Claude Code, Codex o Antigravity

## Stack y modelos

- **Stack:** Cursor;  revisar el plugin concreto y sus credenciales
- **Etiquetas:** `catalogos` `reference` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [cursor/plugins](https://github.com/cursor/plugins)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cursor/plugins/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
