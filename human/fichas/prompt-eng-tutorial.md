[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Prompts y prompt engineering

# 💡 Anthropic's Prompt Engineering Tutorial

> Tutorial interactivo oficial de Anthropic para aprender ingeniería de prompts con ejercicios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39.3k | — | Jupyter Notebook | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 38/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Tutorial interactivo oficial de Anthropic para aprender ingeniería de prompts con Claude. El repositorio no tiene archivo de licencia, así que no hay permiso explícito de reutilización. Último push en agosto de 2026; los ejemplos usan Claude 3 Haiku, un modelo ya antiguo.

## ¿Qué hace?

Enseña en 9 capítulos con ejercicios y un apéndice la estructura de un buen prompt, los fallos habituales y las técnicas '80/20' para corregirlos, las fortalezas y debilidades de Claude, y a construir prompts desde cero para casos comunes. Cada lección tiene un 'Example Playground' para experimentar.

## ¿Cómo lo hace?

Notebooks Jupyter en dos versiones: API de Anthropic (carpeta 'Anthropic 1P') y Amazon Bedrock. También existe una versión en Google Sheets con la extensión Claude for Sheets. Requiere una clave de API de Anthropic o acceso a Bedrock, y cada ejercicio consume tokens.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Cookbooks](claude-cookbooks.md) | Pasar de la teoría de prompts a recetas de código (herramientas, RAG, evaluación) del mismo proveedor. (combinación por arquitectura) | Termina el tutorial y continúa con las recetas que necesites. |
| [promptfoo](promptfoo.md) | Convertir los ejercicios en pruebas automáticas y comparar variantes de prompt. (combinación por arquitectura) | Usa los prompts del tutorial como casos base. |
| [marimo](marimo.md) | Ejecutar los notebooks en un entorno reactivo y reproducible en lugar de Jupyter clásico. (combinación por arquitectura) (requiere convertirlos) | Convierte el notebook con la herramienta de importación de marimo. |

**Notas:** Alternativas (elige una): prompt-engineering-guide. Sin archivo de licencia. Combinación anterior con claude-cookbooks conservada como complemento de aprendizaje.

Estado en GitHub: activo · último push 2026-08-28 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/anthropics/prompt-eng-interactive-tutorial/blob/master/README.md)</sub>

## Ver similares

Grupo **Guías de ingeniería de prompts**: Anthropic's Prompt Engineering Tutorial ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Prompt Engineering Guide](prompt-engineering-guide.md) ⭐ recomendado | 62 | Si buscas esto: guía de referencia de DAIR.AI sobre prompts, ingeniería de contexto, RAG y agentes. |
| 2 | **Anthropic's Prompt Engineering Tutorial** (esta ficha) | 38 | Si buscas esto: tutorial interactivo oficial de Anthropic para aprender ingeniería de prompts con ejercicios. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Leer es gratuito; los ejercicios en notebooks o Claude for Sheets pueden requerir API y consumo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Las referencias a Claude 3 Haiku y modelos superiores son históricas del tutorial; consulta disponibilidad actual antes de ejecutar |
| Coste | El coste depende del proveedor o la ruta. Leer es gratuito; los ejercicios en notebooks o Claude for Sheets pueden requerir API y consumo |
| Equipo | Preparación según la ruta elegida. Navegador; cuenta y acceso al modelo para ejecutar ejercicios |

Las referencias a Claude 3 Haiku y modelos superiores son históricas del tutorial; consulta disponibilidad actual antes de ejecutar

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- cuenta y acceso al modelo para ejecutar ejercicios

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/anthropics/prompt-eng-interactive-tutorial/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Anthropic's Prompt Engineering Tutorial para mi objetivo y necesito pasos guiados. Lee https://github.com/anthropics/prompt-eng-interactive-tutorial/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Completa Basic Prompt Structure y compara una respuesta ambigua con otra que pide un formato concreto.

**Qué comprobar:** Puedes reconocer la diferencia entre instrucción y contenido.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Practicar instrucciones claras
- Aprender a separar datos y órdenes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Practicar instrucciones claras; Aprender a separar datos y órdenes | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las referencias a Claude 3 Haiku y modelos superiores son históricas del tutorial; consulta disponibilidad actual antes de ejecutar

## Stack y modelos

- **Stack:** Navegador; cuenta y acceso al modelo para ejecutar ejercicios
- **Etiquetas:** `learning` `prompts` `notebooks`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Prompt Engineering Guide](prompt-engineering-guide.md) | 80.1k | Guía de referencia de DAIR.AI sobre prompts, ingeniería de contexto, RAG y agentes. |

## Enlaces

- 🐙 GitHub: [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/anthropics/prompt-eng-interactive-tutorial/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
