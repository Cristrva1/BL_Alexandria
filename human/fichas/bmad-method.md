[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧭 BMAD Method

> Metodología ágil con agentes especializados (analista, PM, arquitecto, dev) para desarrollar con IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 55.4k | NOASSERTION | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

BMad Method es un marco de «desarrollo ágil dirigido por IA» de bmad-code-org. El README declara licencia MIT, aunque GitHub la marca como NOASSERTION. Tiene dos líneas: la v6.12 estable, congelada salvo correcciones (release v6.12.4), y la V7 en alfa de vista previa, que cambia a menudo.

## ¿Qué hace?

Lleva una idea o petición de cambio hasta software funcionando sin delegar el razonamiento: qué construir, cómo encaja y cómo evoluciona. Las decisiones quedan explícitas y el contexto se conserva en briefs, especificaciones y documentos de arquitectura, que también pueden llevarse a un flujo de entrega existente. Incluye módulos con roles, por ejemplo un fabricante de skills y un asesor de fundadores.

## ¿Cómo lo hace?

La v6.12 se instala con `npx bmad-method install` y requiere Node.js 20.12+ y Python 3.10+. La V7 se instala con `npx skills add bmad-code-org/BMAD-METHOD/skills/<módulo>` y requiere Node, npm y Git. Desde la herramienta de IA se invocan `bmad-build` para cambiar algo y `bmad-help` para orientarse.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Herramienta de código compatible con sus skills (combinación por arquitectura: el README habla de «tu herramienta de IA» sin lista cerrada). | Instala BMad en la raíz del proyecto y abre el proyecto en el agente. |
| [Codex CLI](codex.md) | Igual: es compatible con skills estándar mediante `npx skills` (combinación por arquitectura). | Igual que arriba. |
| [SkillSpector](skillspector.md) | Revisar con SkillSpector los módulos de la V7, que se instalan como skills (`npx skills add …`), antes de dárselos al agente (combinación por arquitectura). | Escanea la carpeta del módulo con SkillSpector; instala en el agente solo lo que pase la revisión. |

**Notas:** Alternativa (elige una): spec-kit. Usa la v6.12 si necesitas estabilidad.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v6.12.4 (2026-10-14) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md)</sub>

## Ver similares

Grupo **Desarrollo guiado por especificaciones**: BMAD Method ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Spec Kit](spec-kit.md) ⭐ recomendado | 76 | Si buscas esto: kit de GitHub para desarrollo guiado por especificaciones con agentes de código. |
| 2 | **BMAD Method** (esta ficha) | 60 | Si buscas esto: metodología ágil con agentes especializados (analista, PM, arquitecto, dev) para desarrollar con IA. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El método es abierto; cada agente y sus modelos conservan su forma de pago |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. El README distingue la versión estable del preview V7. Los comandos seleccionados son del preview: pueden cambiar y no deben mezclarse con la guía estable |
| Coste | Consumo del agente que ya utilizas. El método es abierto; cada agente y sus modelos conservan su forma de pago |
| Equipo | Preparación según la ruta elegida. Node.js, Git y uv;  cliente compatible con Agent Skills |

El README distingue la versión estable del preview V7. Los comandos seleccionados son del preview: pueden cambiar y no deben mezclarse con la guía estable

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js, Git y uv
-  cliente compatible con Agent Skills

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add bmad-code-org/BMAD-METHOD/skills/core-tools --skill '*'
npx skills add bmad-code-org/BMAD-METHOD/skills/method --skill '*'
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar BMAD Method para mi objetivo y necesito pasos guiados. Lee https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala los módulos de la ruta elegida y pide configurar una primera mejora pequeña.

**Qué comprobar:** El agente identifica el método y deja un plan o artefacto de trabajo revisable.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Convertir una idea de producto en un primer cambio acotado
- Revisar requisitos y decisiones antes de implementar una función

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Convertir una idea de producto en un primer cambio acotado; Revisar requisitos y decisiones antes de implementar una función | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README distingue la versión estable del preview V7. Los comandos seleccionados son del preview: pueden cambiar y no deben mezclarse con la guía estable

## Stack y modelos

- **Stack:** Node.js, Git y uv;  cliente compatible con Agent Skills
- **Etiquetas:** `coding-agent` `skills` `agents`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Spec Kit](spec-kit.md) | 150k | Kit de GitHub para desarrollo guiado por especificaciones con agentes de código. |

## Enlaces

- 🐙 GitHub: [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
