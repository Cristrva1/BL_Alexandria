[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 🎓 Loop Engineering

> Patrones, plantillas y CLI para diseñar bucles de trabajo con agentes de código en vez de prompts sueltos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.8k | MIT | TypeScript | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## ¿Qué es?

Biblioteca de patrones (MIT) de Cobus Greyling para operar agentes de programación alrededor de un repositorio mediante 'bucles' en lugar de prompts sueltos. Es activa (v1.6.0) y reciente.

## ¿Qué hace?

Ofrece patrones y plantillas: triaje diario de issues, CI y dependencias, vigilancia de PRs, refactorizaciones y otros. Cada patrón descubre trabajo, lo delega en agentes, verifica resultados con una puntuación y persiste el estado (`STATE.md`). La primera semana funciona en modo 'solo informe' para limitar riesgos. Incluye un selector de patrones y un starter mínimo como GitHub Action.

## ¿Cómo lo hace?

CLI npm (`npx @cobusgreyling/loop init . --pattern daily-triage --tool claude`) con comandos `doctor` y `cost` para estimar gasto. El agente por defecto es Claude Code, y también admite Grok, Codex y opencode. Requiere tener instalado y autenticado el agente elegido. Los bucles automatizados pueden generar costes recurrentes, así que conviene revisar `cost` antes de activarlos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente por defecto de los bucles (`--tool claude`). | Instala y autentica Claude Code antes de `loop init`. |
| [Codex CLI](codex.md) | Agente alternativo soportado (`--tool codex`). | Instala Codex CLI y elige `--tool codex` al iniciar. |
| [OpenCode](opencode.md) | Agente open source soportado (`--tool opencode`). | Instala opencode y elige `--tool opencode`. |

**Notas:** Sin alternativas declaradas. claude-code, codex y opencode son alternativas entre sí: elige uno por bucle. Combinación anterior con superpowers eliminada: sin integración documentada.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.6.0 (2026-07-20) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/cobusgreyling/loop-engineering/blob/main/README.md)</sub>

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

## Enlaces

- 🐙 GitHub: [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)
- 🌐 Web: <https://cobusgreyling.github.io/loop-engineering/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cobusgreyling/loop-engineering/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
