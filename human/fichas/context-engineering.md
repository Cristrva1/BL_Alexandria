[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 🧩 Context-Engineering

> Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.3k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 44/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Guía y curso en construcción (MIT) sobre 'ingeniería de contexto', inspirada en la definición de Andrej Karpathy. El repositorio cambió de dueño, de davidkimai/Context-Engineering a jasontang-ai/Context-Engineering, y el README todavía enlaza al nombre antiguo. Último push en febrero de 2026.

## ¿Qué hace?

Propone un recorrido desde primeros principios: prompts atómicos, few-shot, memoria, sistemas multiagente, 'campos' cognitivos y protocolos. Incluye plantillas, ejemplos y referencias a investigación reciente, como un survey de más de 1.400 artículos. Parte del marco teórico (campos neuronales, 'residuo simbólico') es especulativo y poco contrastado [DATO NO VERIFICADO].

## ¿Cómo lo hace?

Contenido en Markdown y notebooks Python, más plantillas reutilizables; no se instala. El curso '00_COURSE' está marcado como en construcción. Enlaza recursos externos como DeepWiki y NotebookLM.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [12-Factor Agents](12-factor-agents.md) | Visión práctica e ingenieril del mismo tema (factor 3). (combinación por arquitectura) | Empieza por el factor 3 para una base concreta y usa esta guía para profundizar. |
| [Prompt Engineering Guide](prompt-engineering-guide.md) | Base de prompting previa a la ingeniería de contexto. (combinación por arquitectura) | Lee primero los fundamentos de prompts. |
| [headroom](headroom.md) | Herramienta de compresión de contexto para aplicar en la práctica la gestión de la ventana. (combinación por arquitectura) | Úsala cuando el problema de contexto sea de tamaño y coste. |

**Notas:** Sin alternativas declaradas. Hallazgo: el catálogo debería documentar el cambio de dueño (davidkimai → jasontang-ai). Combinación anterior con andrej-karpathy-skills eliminada: sin relación documentada.

Estado en GitHub: activo · último push 2026-02-27 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/jasontang-ai/Context-Engineering/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El material es abierto; ejecutar comandos o experimentos usa recursos del agente o proveedor |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El curso está en construcción y declara comandos para Claude Code y Codex; los resultados de artículos citados no validan por sí solos todas sus propuestas |
| Coste | Consumo del agente que ya utilizas. El material es abierto; ejecutar comandos o experimentos usa recursos del agente o proveedor |
| Equipo | Preparación según la ruta elegida. Navegador; agente si utilizas los comandos |

El curso está en construcción y declara comandos para Claude Code y Codex; los resultados de artículos citados no validan por sí solos todas sus propuestas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- agente si utilizas los comandos

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/jasontang-ai/Context-Engineering/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Context-Engineering para mi objetivo y necesito pasos guiados. Lee https://github.com/jasontang-ai/Context-Engineering/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee el mapa de contexto y reduce un encargo a objetivo, datos pertinentes y límites.

**Qué comprobar:** Puedes justificar qué datos incluyes y cuáles omites.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar contexto para una tarea larga
- Estudiar memoria y recuperación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar contexto para una tarea larga; Estudiar memoria y recuperación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El curso está en construcción y declara comandos para Claude Code y Codex; los resultados de artículos citados no validan por sí solos todas sus propuestas

## Stack y modelos

- **Stack:** Navegador; agente si utilizas los comandos
- **Etiquetas:** `learning` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [jasontang-ai/Context-Engineering](https://github.com/jasontang-ai/Context-Engineering)
- 🌐 Web: <https://deepwiki.com/davidkimai/Context-Engineering>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/jasontang-ai/Context-Engineering/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
