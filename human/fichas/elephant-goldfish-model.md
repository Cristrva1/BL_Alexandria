[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🎨 elephant-goldfish-model

> Plugin con instrucciones para diseñar y revisar software con agentes mediante contextos y perspectivas complementarias.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.3k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

EGM, plugin de código abierto de Google (Apache 2.0) para asistentes de IA, que separa diseñar con contexto de revisar con ojos frescos. Muy reciente (v0.1.1).

## ¿Qué hace?

El «elefante» conserva el contexto del proyecto y redacta la especificación. Los revisores «pez dorado» examinan el borrador y las fuentes sin la conversación previa, para sacar a la luz supuestos implícitos y puntos ciegos. Sus comandos (`egm-brainstorm`, `egm-draft`, `egm-review`, `egm-resolve`, `egm-bootstrap`, `egm-drift`) sirven para especificaciones de software y, con `/egm-review-loop`, para otros documentos; también revisa documentos existentes contra el código vivo.

## ¿Cómo lo hace?

Se instala como plugin completo en Claude Code (`claude plugin marketplace add google/elephant-goldfish-model`), Codex CLI (`codex plugin marketplace add ...`), Antigravity (`agy plugin install ...`) y las apps de escritorio de ChatGPT y Codex. Tiene guías para Claude Cowork y ChatGPT Work.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Instalación documentada (`egm@egm`). | Instala y abre una sesión nueva. |
| [Codex CLI](codex.md) | Instalación documentada. | Igual que arriba. |
| [Spec Kit](spec-kit.md) | Revisar con ojos frescos las especificaciones que genera Spec Kit (combinación por arquitectura). | Genera la especificación y pásala por `egm-review`. |

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.1.1 (2026-11-06) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google/elephant-goldfish-model/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El plugin consume el agente anfitrión; no aporta un modelo ni una bolsa de créditos |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. El repositorio de Google declara que no es un producto con soporte oficial; cada host tiene una guía propia |
| Coste | Consumo del agente que ya utilizas. El plugin consume el agente anfitrión; no aporta un modelo ni una bolsa de créditos |
| Equipo | Preparación según la ruta elegida. Cliente compatible;  una propuesta o documento propio para revisar |

El repositorio de Google declara que no es un producto con soporte oficial; cada host tiene una guía propia

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cliente compatible
-  una propuesta o documento propio para revisar

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
claude plugin marketplace add google/elephant-goldfish-model
claude plugin install egm@egm
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/google/elephant-goldfish-model/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar elephant-goldfish-model para mi objetivo y necesito pasos guiados. Lee https://github.com/google/elephant-goldfish-model/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Plantea una decisión de diseño y pide una revisión con una perspectiva nueva.

**Qué comprobar:** Obtienes un brief y observaciones que puedes contrastar con el contexto inicial.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Documentar alternativas para una funcionalidad antes de elegir una
- Revisar una especificación con un contexto de lectura renovado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Documentar alternativas para una funcionalidad antes de elegir una; Revisar una especificación con un contexto de lectura renovado | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El repositorio de Google declara que no es un producto con soporte oficial; cada host tiene una guía propia

## Stack y modelos

- **Stack:** Cliente compatible;  una propuesta o documento propio para revisar
- **Etiquetas:** `metodologia` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)
- 🌐 Web: <https://egm.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google/elephant-goldfish-model/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
