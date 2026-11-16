[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧠 claude-token-efficient

> Instrucciones para reducir la verbosidad de Claude Code y medir el coste de respuestas y contexto.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.2k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Puntuación de calidad** 50/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Un archivo `CLAUDE.md` de drona23 (MIT) para que Claude responda de forma concisa y gaste menos tokens. Sin releases; último cambio en junio de 2026.

## ¿Qué hace?

Elimina aperturas y cierres de cortesía, guiones largos y caracteres Unicode que rompen parsers, la repetición de la pregunta, las sugerencias no pedidas, la sobreingeniería y el dar la razón ante afirmaciones incorrectas. Su prueba con 5 prompts mide un 63 % menos de palabras [DATO NO VERIFICADO: indicador direccional, no estadístico según el propio README].

## ¿Cómo lo hace?

Se pega una regla corta en el chat o se coloca el `CLAUDE.md` en el proyecto. El README advierte que los archivos de instrucciones añaden tokens de entrada en cada turno y solo se probó con Claude.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Formato CLAUDE.md. | Copia el archivo a la raíz del proyecto y mantenlo corto. |
| [andrej-karpathy-skills](andrej-karpathy-skills.md) | Principios compatibles contra la sobreingeniería (combinación por arquitectura). | Fusiona ambos en un único CLAUDE.md breve para no duplicar el coste de entrada. |
| [Claude-Code-Usage-Monitor](claude-code-usage-monitor.md) | Medir con el monitor de uso si el `CLAUDE.md` reduce de verdad el consumo; el propio README advierte que el archivo añade tokens de entrada en cada turno (combinación por arquitectura). | Registra una semana de uso sin el archivo y otra con él antes de dejarlo fijo. |

Estado en GitHub: activo · último push 2026-06-16 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/drona23/claude-token-efficient/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las instrucciones consumen el agente; menos texto no garantiza una reducción concreta de la factura |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Los resultados con modelos locales se declaran sin probar; no se presentan como compatibilidad validada |
| Coste | Consumo del agente que ya utilizas. Las instrucciones consumen el agente; menos texto no garantiza una reducción concreta de la factura |
| Equipo | Preparación según la ruta elegida. Claude Code;  copia revisable de las instrucciones del proyecto |

Los resultados con modelos locales se declaran sin probar; no se presentan como compatibilidad validada

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
-  copia revisable de las instrucciones del proyecto

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/drona23/claude-token-efficient
cp claude-token-efficient/profiles/CLAUDE.coding.md your-project/CLAUDE.md
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/drona23/claude-token-efficient/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar claude-token-efficient para mi objetivo y necesito pasos guiados. Lee https://github.com/drona23/claude-token-efficient/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Aplica un perfil en una carpeta de prueba y pide una respuesta breve con criterios concretos.

**Qué comprobar:** Puedes comparar extensión y claridad sin perder la información necesaria.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Reducir respuestas repetitivas en una sesión larga
- Mantener un estilo de comunicación conciso para tareas de código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Reducir respuestas repetitivas en una sesión larga; Mantener un estilo de comunicación conciso para tareas de código | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los resultados con modelos locales se declaran sin probar; no se presentan como compatibilidad validada

## Stack y modelos

- **Stack:** Claude Code;  copia revisable de las instrucciones del proyecto
- **Etiquetas:** `metodologia` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/drona23/claude-token-efficient/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
