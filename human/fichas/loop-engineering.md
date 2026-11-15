[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 🎓 Loop Engineering

> Patrones, plantillas y CLI para diseñar bucles de trabajo con agentes de código en vez de prompts sueltos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.8k | MIT | TypeScript | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Las plantillas usan el modelo o plan del agente; las estimaciones de coste no son facturas ni tarifas garantizadas |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La primera semana se plantea solo con informes; Claude y Codex están documentados y Antigravity no figura como adaptador |
| Coste | Consumo del agente que ya utilizas. Las plantillas usan el modelo o plan del agente; las estimaciones de coste no son facturas ni tarifas garantizadas |
| Equipo | Preparación según la ruta elegida. Node; proyecto de prueba; Claude Code o Codex configurado |

La primera semana se plantea solo con informes; Claude y Codex están documentados y Antigravity no figura como adaptador

## Qué puedes hacer con él

Patrones, plantillas y CLI para diseñar bucles de trabajo con agentes de código en vez de prompts sueltos.

## Por qué destaca

Usos propuestos: Diseñar un ciclo de revisión de issues; Estimar el coste de un bucle antes de automatizarlo.

## Cómo funciona

La primera semana se plantea solo con informes; Claude y Codex están documentados y Antigravity no figura como adaptador

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- proyecto de prueba
- Claude Code o Codex configurado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx @cobusgreyling/loop init . --pattern daily-triage --tool claude
npx @cobusgreyling/loop doctor .
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/cobusgreyling/loop-engineering/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Loop Engineering para mi objetivo y necesito pasos guiados. Lee https://github.com/cobusgreyling/loop-engineering/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera la plantilla de daily-triage en una carpeta de prueba y ejecuta doctor antes de activar acciones.

**Qué comprobar:** Puedes revisar la configuración y los avisos del diagnóstico.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Diseñar un ciclo de revisión de issues
- Estimar el coste de un bucle antes de automatizarlo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Diseñar un ciclo de revisión de issues; Estimar el coste de un bucle antes de automatizarlo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La primera semana se plantea solo con informes; Claude y Codex están documentados y Antigravity no figura como adaptador

## Stack y modelos

- **Stack:** Node; proyecto de prueba; Claude Code o Codex configurado
- **Etiquetas:** `coding-agent` `skills` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Claude Code](claude-code.md) | 156k | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. |
| [Codex CLI](codex.md) | 135k | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. |
| [superpowers](superpowers.md) | 318k | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |

## Enlaces

- 🐙 GitHub: [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)
- 🌐 Web: <https://cobusgreyling.github.io/loop-engineering/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cobusgreyling/loop-engineering/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
