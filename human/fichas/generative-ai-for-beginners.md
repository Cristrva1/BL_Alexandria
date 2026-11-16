[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Guías, cursos y cookbooks

# 🎓 Generative AI for Beginners

> Curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificial generativa.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 124k | MIT | Jupyter Notebook | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## ¿Qué es?

Curso gratuito de Microsoft (MIT) para aprender a construir aplicaciones de IA generativa, ahora en su versión 3. Es muy popular (~124k estrellas), se mantiene activo y está traducido a más de 50 idiomas mediante Co-op Translator.

## ¿Qué hace?

Ofrece 21 lecciones que combinan conceptos ('Learn') y código ('Build'): prompts, chat, búsqueda, generación de imágenes, RAG, agentes, fine-tuning, seguridad y más. Cada lección incluye vídeo, texto y ejercicios. Enlaza otros cursos de la serie, como agentes y MCP para principiantes.

## ¿Cómo lo hace?

Los ejemplos están en Python y TypeScript y funcionan con Azure OpenAI, Microsoft Foundry Models y la API de OpenAI. GitHub Models se retira a finales de julio de 2026, según el README. Una lección de configuración prepara el entorno, por ejemplo con Codespaces. El repositorio pesa mucho por las traducciones, así que el README recomienda un sparse checkout.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [AI Agents for Beginners](ai-agents-for-beginners.md) | Siguiente curso de la serie, centrado en agentes (enlazado en el README). | Haz primero este curso y continúa con el de agentes. |
| [MCP for Beginners](mcp-for-beginners.md) | Curso complementario sobre Model Context Protocol (enlazado en el README). | Tómalo cuando llegues a la parte de herramientas y agentes. |
| [OpenAI Cookbook](openai-cookbook.md) | Recetas más avanzadas para quienes usan la API de OpenAI en los ejercicios. (combinación por arquitectura) | Úsalo como siguiente paso práctico tras las lecciones 'Build'. |

**Notas:** Alternativas (elige una): llm-course. Aviso: algunas lecciones dependen de GitHub Models, que se retira; usa Foundry o la API de OpenAI.

Estado en GitHub: activo · último push 2026-11-12 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/microsoft/generative-ai-for-beginners/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Curso abierto; nube y APIs pueden cobrar por uso; Foundry Local ofrece una ruta offline con requisitos de equipo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. No todas las lecciones comparten dependencias ni admiten el mismo proveedor; la ruta local documentada no convierte todos los ejemplos a local |
| Coste | El coste depende del proveedor o la ruta. Curso abierto; nube y APIs pueden cobrar por uso; Foundry Local ofrece una ruta offline con requisitos de equipo |
| Equipo | Preparación según la ruta elegida. Navegador; Python para los laboratorios; proveedor o Foundry Local según lección |

No todas las lecciones comparten dependencias ni admiten el mismo proveedor; la ruta local documentada no convierte todos los ejemplos a local

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador
- Python para los laboratorios
- proveedor o Foundry Local según lección

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/microsoft/generative-ai-for-beginners/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Generative AI for Beginners para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/generative-ai-for-beginners/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Lee la introducción y elige un ejemplo de generación de texto antes de preparar su entorno específico.

**Qué comprobar:** Puedes distinguir modelo, aplicación y proveedor y localizar las dependencias de ese ejemplo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Empezar a construir una app generativa
- Comparar nube con Foundry Local

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Empezar a construir una app generativa; Comparar nube con Foundry Local | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No todas las lecciones comparten dependencias ni admiten el mismo proveedor; la ruta local documentada no convierte todos los ejemplos a local

## Stack y modelos

- **Stack:** Navegador; Python para los laboratorios; proveedor o Foundry Local según lección
- **Etiquetas:** `learning` `prompts` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LLM Course](llm-course.md) | 85.1k | Curso gratuito de Maxime Labonne con rutas y notebooks de Colab para aprender LLM de cero a producción. |

## Enlaces

- 🐙 GitHub: [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/generative-ai-for-beginners/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
