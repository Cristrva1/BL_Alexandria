[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Ahorro de contexto y tokens

# 🗜️ headroom

> Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 79.7k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Headroom, capa de compresión de contexto para agentes y LLM de Headroom Labs (paquete `headroom-ai` en PyPI y npm). Licencia Apache-2.0. Es muy activo (~80k estrellas, v0.44.0).

## ¿Qué hace?

Comprime salidas de herramientas, logs, fragmentos de RAG, archivos e historial antes de que lleguen al modelo. Según su propia medición ahorra entre un 21 y un 57 % de tokens de entrada en escenarios de agentes y más del 90 % en JSON y logs repetitivos, con poco efecto en prosa. Ofrece SDK, proxy, envoltura de agentes de programación, memoria compartida entre agentes y servidor MCP.

## ¿Cómo lo hace?

Se instala con `pip install headroom-ai` (o con extras `[proxy]`/`[all]`) y se usa con `compress(...)` en código, con `headroom proxy --port 8787` o con `headroom wrap claude|codex|cursor|…`. La compresión corre en local; `HEADROOM_OFFLINE=1` evita cualquier llamada de red.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Envoltura nativa: `headroom wrap claude`. | Instala headroom-ai[all] y envuelve el agente. |
| [litellm](litellm.md) | Integración citada en el README para apps que llaman a LiteLLM. | Comprime los mensajes antes de enviarlos por LiteLLM. |
| [Context-Engineering](context-engineering.md) | Aplicar técnicas de ingeniería de contexto junto a la compresión. (combinación por arquitectura) | Diseña el contexto y comprime después lo voluminoso. |
| [codegraph](codegraph.md) | Reducir lecturas de código con un índice semántico. (combinación por arquitectura) | Usa codegraph para localizar y Headroom para comprimir. |
| [Claude-Code-Usage-Monitor](claude-code-usage-monitor.md) | Combinación recíproca: Claude-Code-Usage-Monitor lo enlaza como «Medir el ahorro de compresión de contexto. (combinación por arquitectura)». | Orden indicado desde Claude-Code-Usage-Monitor: Compara el consumo con y sin `headroom wrap claude`. |
| [MiMo-Code](mimo-code.md) | Combinación recíproca: MiMo-Code lo enlaza como «Comprimir el contexto en sesiones largas. (combinación por arquitectura)». | Orden indicado desde MiMo-Code: Envuelve el agente con Headroom si es compatible. |

**Notas:** Alternativas (elige una): rtk. El número de estrellas crece de forma inusual para un proyecto tan joven; los ahorros son mediciones del propio proyecto.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.44.0 (2026-11-10) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/headroomlabs-ai/headroom/blob/main/README.md) · [2](https://docs.headroomlabs.ai/docs)</sub>

## Ver similares

Grupo **Compactar contexto y tokens**: headroom ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [rtk](rtk.md) ⭐ recomendado | 69 | Si buscas esto: proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código. |
| 2 | **headroom** (esta ficha) | 60 | Si buscas esto: utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La compresión básica no pide clave ni descargar modelo; el agente y funciones opcionales pueden usar otros recursos |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Documenta wrap para Claude y Codex y MCP para cualquier cliente compatible; los ahorros de benchmarks no garantizan iguales respuestas en toda tarea |
| Coste | El coste depende del proveedor o la ruta. La compresión básica no pide clave ni descargar modelo; el agente y funciones opcionales pueden usar otros recursos |
| Equipo | Preparación según la ruta elegida. Python compatible; contenido de prueba; agente o cliente MCP si lo conectas |

Documenta wrap para Claude y Codex y MCP para cualquier cliente compatible; los ahorros de benchmarks no garantizan iguales respuestas en toda tarea

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python compatible
- contenido de prueba
- agente o cliente MCP si lo conectas

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install headroom-ai
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/headroomlabs-ai/headroom/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar headroom para mi objetivo y necesito pasos guiados. Lee https://github.com/headroomlabs-ai/headroom/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Comprime una salida JSON pequeña y compara el resultado con el original antes de envolver un agente.

**Qué comprobar:** Puedes identificar qué se conservó y recuperar el original cuando corresponda.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Reducir salidas extensas de herramientas
- Comparar una sesión con y sin compresión

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Reducir salidas extensas de herramientas; Comparar una sesión con y sin compresión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta wrap para Claude y Codex y MCP para cualquier cliente compatible; los ahorros de benchmarks no garantizan iguales respuestas en toda tarea

## Stack y modelos

- **Stack:** Python compatible; contenido de prueba; agente o cliente MCP si lo conectas
- **Etiquetas:** `automation` `llmops` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [rtk](rtk.md) | 86.6k | Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código. |

## Enlaces

- 🐙 GitHub: [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)
- 🌐 Web: <https://docs.headroomlabs.ai/docs>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/headroomlabs-ai/headroom/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
