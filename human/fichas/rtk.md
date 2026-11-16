[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Ahorro de contexto y tokens

# 🧬 rtk

> Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 86.6k | Apache-2.0 | Rust | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

RTK (Rust Token Killer), filtro de salidas de terminal para agentes de programación, de rtk-ai. El binario por defecto combina Apache-2.0 y BUSL-1.1, y la edición `rtk-oss` es solo Apache-2.0. Es muy popular (~87k estrellas, v1.2.0) y tiene una versión comercial (RTK Pro).

## ¿Qué hace?

Comprime la salida de más de 100 comandos (tests, diffs, logs, builds) antes de que el agente la lea, con hasta un 90 % menos de texto según el proyecto y menos de 25 ms por comando. `rtk gain` muestra lo ahorrado. Las pipelines (motor bajo BUSL) delegan lecturas pesadas a modelos más baratos y comprimen más fuentes.

## ¿Cómo lo hace?

Se instala con `brew install rtk`, `winget` o un script `curl … | sh`, y se registra en el agente con `rtk init -g` (Claude Code) o variantes para Cursor, Gemini CLI y Codex. Es un binario Rust que reescribe comandos mediante hooks. La telemetría está desactivada por defecto.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Hook nativo con `rtk init -g`. | Instala rtk y ejecuta `rtk init -g`. |
| [Codex CLI](codex.md) | Hook nativo con `rtk init -g --codex`. | Registra el hook para Codex. |
| [Gemini CLI](gemini-cli.md) | Hook nativo con `rtk init -g --gemini`. | Registra el hook para Gemini CLI. |

**Notas:** Alternativas (elige una): headroom. Si quieres solo código Apache-2.0, instala `rtk-oss`.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.2.0 (2026-11-08) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/rtk-ai/rtk/blob/develop/README.md) · [2](https://www.rtk-ai.app/docs/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La compresión básica no necesita API; pipelines con otros modelos y el servicio Pro tienen costes separados |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Claude y Codex tienen hooks documentados; Antigravity usa un archivo de reglas y no la misma automatización; las cifras de ahorro dependen de la tarea |
| Coste | El coste depende del proveedor o la ruta. La compresión básica no necesita API; pipelines con otros modelos y el servicio Pro tienen costes separados |
| Equipo | Preparación según la ruta elegida. Binario para tu sistema; agente y proyecto de prueba; configuración por agente |

Claude y Codex tienen hooks documentados; Antigravity usa un archivo de reglas y no la misma automatización; las cifras de ahorro dependen de la tarea

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Binario para tu sistema
- agente y proyecto de prueba
- configuración por agente

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
winget install rtk-ai.rtk
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/rtk-ai/rtk/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar rtk para mi objetivo y necesito pasos guiados. Lee https://github.com/rtk-ai/rtk/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prueba un comando RTK y compara su salida con la versión sin comprimir antes de activar hooks.

**Qué comprobar:** Puedes comprobar datos omitidos y contadores de ahorro.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Reducir salida repetitiva de comandos
- Estudiar consumo de contexto por tarea

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Reducir salida repetitiva de comandos; Estudiar consumo de contexto por tarea | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Claude y Codex tienen hooks documentados; Antigravity usa un archivo de reglas y no la misma automatización; las cifras de ahorro dependen de la tarea

## Stack y modelos

- **Stack:** Binario para tu sistema; agente y proyecto de prueba; configuración por agente
- **Etiquetas:** `tokens` `agentic-coding` `ai-coding` `anthropic` `claude-code` `cli` `command-line-tool` `cost-reduction`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [headroom](headroom.md) | 79.7k | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. |

## Enlaces

- 🐙 GitHub: [rtk-ai/rtk](https://github.com/rtk-ai/rtk)
- 🌐 Web: <https://www.rtk-ai.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/rtk-ai/rtk/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
