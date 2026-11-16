[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧠 SuperClaude_Framework

> Framework de configuración que añade comandos, roles y metodologías de trabajo a Claude Code.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.9k | MIT | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Puntuación de calidad** 49/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Marco de «metaprogramación» de configuración para Claude Code (MIT) de SuperClaude-Org, no afiliado a Anthropic. Versión v4.3.0; último cambio en septiembre de 2026.

## ¿Qué hace?

Convierte Claude Code en una plataforma de desarrollo estructurada mediante inyección de instrucciones de comportamiento: 30 comandos `/sc:*` que cubren de la lluvia de ideas al despliegue, 20 agentes especializados, 7 modos de comportamiento y 8 integraciones MCP. Por ejemplo, `/sc:research` hace investigación web profunda con Tavily.

## ¿Cómo lo hace?

Se instala con pipx (`pipx install superclaude`), que despliega los componentes en Claude Code. `superclaude mcp` instala servidores MCP opcionales (Serena, Sequential, Tavily, Context7, Mindbase) mediante airis-mcp-gateway, con mejoras de velocidad y tokens declaradas por el proyecto [DATO NO VERIFICADO]. El instalador como plugin está previsto para la v5.0.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plataforma que configura. | Claude Code primero; luego `pipx install superclaude` y su instalador. |
| [Context7](context7.md) | MCP opcional para consultar documentación oficial. | `superclaude mcp --servers context7`. |
| [Serena](serena.md) | MCP opcional de comprensión de código. | Mediante airis-mcp-gateway. |

**Notas:** Alternativas (elige una): superpowers, ecc, gstack. Inyecta muchas instrucciones, así que no conviene instalarlo junto a otro de estos marcos.

Estado en GitHub: activo · último push 2026-09-27 · última versión publicada v4.3.0 (2026-03-22) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/master/README.md)</sub>

## Ver similares

Grupo **Metodologías y harness para agentes de código**: SuperClaude_Framework ocupa la posición 5 de 5 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ECC](ecc.md) ⭐ recomendado | 72 | Si quieres un sistema completo de skills, hooks y configuración adaptable a varios agentes. |
| 2 | [gstack](gstack.md) | 66 | Si quieres el flujo de planificar, implementar, revisar y probar que usa Garry Tan con Claude Code. |
| 3 | [Agent Skills (Addy Osmani)](agent-skills.md) | 63 | Si quieres skills de ingeniería portables en el formato Agent Skills. |
| 4 | [superpowers](superpowers.md) | 62 | Si quieres que el agente siga TDD, planificación y revisión de forma disciplinada. |
| 5 | **SuperClaude_Framework** (esta ficha) | 49 | Si quieres comandos y personas para Claude Code organizados por fase. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El núcleo usa tu acceso a Claude; servidores opcionales como Tavily y otras integraciones pueden cobrar aparte |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Se limita el comando inicial al núcleo; las opciones MCP del ejemplo son pasos separados, no requisitos para todos |
| Coste | El coste depende del proveedor o la ruta. El núcleo usa tu acceso a Claude; servidores opcionales como Tavily y otras integraciones pueden cobrar aparte |
| Equipo | Preparación según la ruta elegida. Claude Code;  Python y pipx según la guía;  copia de configuración revisable |

Se limita el comando inicial al núcleo; las opciones MCP del ejemplo son pasos separados, no requisitos para todos

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
-  Python y pipx según la guía
-  copia de configuración revisable

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# Install from PyPI
pipx install superclaude

# Install commands (installs all 30 slash commands)
superclaude install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SuperClaude_Framework para mi objetivo y necesito pasos guiados. Lee https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala la configuración básica y consulta la lista de comandos antes de añadir MCP opcionales.

**Qué comprobar:** Puedes identificar qué comandos se incorporaron y ejecutar el diagnóstico del proyecto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Usar un rol especializado para revisar una decisión de arquitectura
- Organizar un flujo de desarrollo con comandos de trabajo coherentes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Usar un rol especializado para revisar una decisión de arquitectura; Organizar un flujo de desarrollo con comandos de trabajo coherentes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Se limita el comando inicial al núcleo; las opciones MCP del ejemplo son pasos separados, no requisitos para todos

## Stack y modelos

- **Stack:** Claude Code;  Python y pipx según la guía;  copia de configuración revisable
- **Etiquetas:** `metodologia` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [superpowers](superpowers.md) | 318k | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |
| [ECC](ecc.md) | 303k | Sistema de skills, hooks y configuración para agentes de código, con rutas nativas y adaptadores cuya capacidad varía según el cliente. |
| [gstack](gstack.md) | 142k | Conjunto de skills y herramientas para organizar planificación, implementación, revisión y pruebas con Claude Code. |

## Enlaces

- 🐙 GitHub: [SuperClaude-Org/SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)
- 🌐 Web: <https://superclaude.netlify.app/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/SuperClaude-Org/SuperClaude_Framework/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
