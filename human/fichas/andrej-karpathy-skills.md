[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧠 andrej-karpathy-skills

> Instrucciones para declarar supuestos, simplificar cambios y comprobar objetivos al programar, inspiradas en observaciones de Karpathy.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 233k | — | — | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El archivo de instrucciones consume el agente; no añade un proveedor de modelos |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Son principios inspirados en observaciones de Karpathy, no un proyecto publicado por él ni una garantía de calidad |
| Coste | Consumo del agente que ya utilizas. El archivo de instrucciones consume el agente; no añade un proveedor de modelos |
| Equipo | Preparación según la ruta elegida. Claude Code;  revisar las instrucciones que ya existen en el proyecto |

Son principios inspirados en observaciones de Karpathy, no un proyecto publicado por él ni una garantía de calidad

## Qué puedes hacer con él

Instrucciones para declarar supuestos, simplificar cambios y comprobar objetivos al programar, inspiradas en observaciones de Karpathy.

## Por qué destaca

Usos propuestos: Evitar una refactorización amplia para corregir un fallo pequeño; Hacer explícitas dudas y criterios de éxito antes de programar.

## Cómo funciona

Son principios inspirados en observaciones de Karpathy, no un proyecto publicado por él ni una garantía de calidad

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
-  revisar las instrucciones que ya existen en el proyecto

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
/plugin marketplace add forrestchang/andrej-karpathy-skills

/plugin install andrej-karpathy-skills@karpathy-skills
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar andrej-karpathy-skills para mi objetivo y necesito pasos guiados. Lee https://github.com/multica-ai/andrej-karpathy-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide un cambio pequeño y observa si declara supuestos y limita el alcance.

**Qué comprobar:** La propuesta identifica lo que cambiará y cómo comprobar el resultado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Evitar una refactorización amplia para corregir un fallo pequeño
- Hacer explícitas dudas y criterios de éxito antes de programar

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Evitar una refactorización amplia para corregir un fallo pequeño; Hacer explícitas dudas y criterios de éxito antes de programar | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Son principios inspirados en observaciones de Karpathy, no un proyecto publicado por él ni una garantía de calidad

## Stack y modelos

- **Stack:** Claude Code;  revisar las instrucciones que ya existen en el proyecto
- **Etiquetas:** `skills` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Awesome Claude Code](awesome-claude-code.md) | 58k | Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alternativos y guías. |
| [Context-Engineering](context-engineering.md) | 9.3k | Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso. |

## Enlaces

- 🐙 GitHub: [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
