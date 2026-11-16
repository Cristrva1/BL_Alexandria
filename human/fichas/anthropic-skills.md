[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🗂️ Anthropic Skills

> Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especificación Agent Skills.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 195k | — | Python | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## ¿Qué es?

Repositorio oficial de Anthropic con su implementación de skills para Claude: carpetas de instrucciones, scripts y recursos que Claude carga bajo demanda. Muy activo y sin releases. GitHub no detecta una licencia de repositorio, pero el README dice que muchas skills son Apache 2.0, incluidas las de documentos.

## ¿Qué hace?

Reúne skills de ejemplo que van de lo creativo (arte, música, diseño) a lo técnico (probar aplicaciones web, generar servidores MCP) y lo empresarial. Incluye las skills de documentos (docx, pdf, pptx, xlsx) que usa Claude para crear archivos, como referencia de skills complejas. Sirve de inspiración y como guía de patrones; el estándar abierto está en agentskills.io.

## ¿Cómo lo hace?

Cada skill es una carpeta con `SKILL.md` (instrucciones y metadatos) y recursos. Se instala como marketplace en Claude Code (`/plugin marketplace add anthropics/skills`, luego `document-skills` o `example-skills`). Las skills ya están disponibles en los planes de pago de Claude.ai y pueden usarse mediante la API de Claude.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Instalación oficial como marketplace de plugins. | Añade el marketplace e instala solo los paquetes que necesites. |
| [SkillSpector](skillspector.md) | Auditar skills (scripts incluidos) antes de instalarlas (combinación por arquitectura). | Pasa SkillSpector sobre las carpetas antes de habilitarlas. |
| [claude-agent-sdk-python](claude-agent-sdk-python.md) | Usar las skills dentro de agentes propios (combinación por arquitectura). | Copia las skills al directorio que cargue tu agente. |

**Notas:** Se quitaron claude-plugins-official y superpowers porque no hay integración documentada.

Estado en GitHub: activo · último push 2026-11-14 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/anthropics/skills/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El agente consume su acceso habitual; cada skill puede necesitar programas adicionales y recursos de cómputo |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La implementación es para Claude; el estándar abierto no demuestra que todos sus scripts funcionen en otros clientes |
| Coste | Consumo del agente que ya utilizas. El agente consume su acceso habitual; cada skill puede necesitar programas adicionales y recursos de cómputo |
| Equipo | Preparación según la ruta elegida. Claude Code activo;  dependencias de la skill de documentos elegida |

La implementación es para Claude; el estándar abierto no demuestra que todos sus scripts funcionen en otros clientes

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code activo
-  dependencias de la skill de documentos elegida

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
/plugin marketplace add anthropics/skills

/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/anthropics/skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Anthropic Skills para mi objetivo y necesito pasos guiados. Lee https://github.com/anthropics/skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide a la skill PDF identificar campos de un formulario de prueba.

**Qué comprobar:** El agente identifica la skill y entrega la lista de campos del PDF.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Extraer campos de un formulario PDF propio
- Crear una presentación usando las instrucciones de la skill de diapositivas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Extraer campos de un formulario PDF propio; Crear una presentación usando las instrucciones de la skill de diapositivas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La implementación es para Claude; el estándar abierto no demuestra que todos sus scripts funcionen en otros clientes

## Stack y modelos

- **Stack:** Claude Code activo;  dependencias de la skill de documentos elegida
- **Etiquetas:** `skills` `docs` `pdf` `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [anthropics/skills](https://github.com/anthropics/skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/anthropics/skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
