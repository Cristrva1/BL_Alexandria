[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧠 codex-plugin-cc

> Plugin oficial de OpenAI para usar Codex desde Claude Code en revisiones y tareas delegadas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 35.1k | Apache-2.0 | JavaScript | 2026-11-14 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Claude Code y Codex tienen accesos y límites propios; Codex admite sesión del plan o API según su configuración |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. No es una skill que se instala dentro de Codex: es un puente desde Claude Code hacia el CLI de Codex |
| Coste | El coste depende del proveedor o la ruta. Claude Code y Codex tienen accesos y límites propios; Codex admite sesión del plan o API según su configuración |
| Equipo | Preparación según la ruta elegida. Claude Code;  Codex CLI autenticado y acceso a su cuenta |

No es una skill que se instala dentro de Codex: es un puente desde Claude Code hacia el CLI de Codex

## Qué puedes hacer con él

Plugin oficial de OpenAI para usar Codex desde Claude Code en revisiones y tareas delegadas.

## Por qué destaca

Usos propuestos: Pedir una segunda revisión de un cambio desde Claude Code; Delegar una tarea acotada a Codex manteniendo el contexto principal.

## Cómo funciona

No es una skill que se instala dentro de Codex: es un puente desde Claude Code hacia el CLI de Codex

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
-  Codex CLI autenticado y acceso a su cuenta

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
/plugin marketplace add openai/codex-plugin-cc

/plugin install codex@openai-codex
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/openai/codex-plugin-cc/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar codex-plugin-cc para mi objetivo y necesito pasos guiados. Lee https://github.com/openai/codex-plugin-cc/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide revisar un diff pequeño mediante el comando del plugin y examina su informe.

**Qué comprobar:** La delegación devuelve una revisión atribuible al proceso de Codex.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Pedir una segunda revisión de un cambio desde Claude Code
- Delegar una tarea acotada a Codex manteniendo el contexto principal

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Pedir una segunda revisión de un cambio desde Claude Code; Delegar una tarea acotada a Codex manteniendo el contexto principal | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No es una skill que se instala dentro de Codex: es un puente desde Claude Code hacia el CLI de Codex

## Stack y modelos

- **Stack:** Claude Code;  Codex CLI autenticado y acceso a su cuenta
- **Etiquetas:** `metodologia` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openai/codex-plugin-cc/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
