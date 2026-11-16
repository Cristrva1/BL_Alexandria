[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 modern-web-guidance

> Herramienta y skill para que un agente consulte documentación actual sobre prácticas y APIs de desarrollo web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.6k | Apache-2.0 | — | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## ¿Qué es?

Conjunto de skills (Apache 2.0) de Google Chrome, mantenido junto con los equipos de Microsoft Edge, Mozilla Firefox y MDN, que lleva al agente de código pautas de la plataforma web y datos de compatibilidad. Versión v1.0.0.

## ¿Qué hace?

Evita que los agentes generen JavaScript pesado o patrones antiguos cuando existe una solución nativa moderna: devuelve pautas seleccionadas por expertos para tareas concretas (por ejemplo, animar el fondo de un diálogo), con datos de compatibilidad de navegadores, y detecta código heredado en un proyecto.

## ¿Cómo lo hace?

CLI npm (`npx modern-web-guidance@latest install`, con asistente interactivo) con comandos `search`, `retrieve` y `legacy-scan`. Se integra como skill en GitHub Copilot CLI, como plugin de Claude Code y en OpenAI Codex, entre otros.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin documentado. | Ejecuta el asistente de instalación. |
| [Codex CLI](codex.md) | Instalación documentada. | Igual que arriba. |
| [Front-End-Checklist](front-end-checklist.md) | Lista de calidad para verificar el resultado (combinación por arquitectura). | Independientes. |

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada v1.0.0 (2026-11-10) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/GoogleChrome/modern-web-guidance/blob/main/README.md) · [2](https://developer.chrome.com/docs/modern-web-guidance)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La búsqueda usa embeddings locales sin API; el agente consume su plan y npx puede descargar actualizaciones |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelos locales documentados. Documenta Claude Code, Codex y Antigravity; el modelo local es el buscador de documentación y no un sustituto completo del agente de código |
| Coste | El coste depende del proveedor o la ruta. La búsqueda usa embeddings locales sin API; el agente consume su plan y npx puede descargar actualizaciones |
| Equipo | Preparación según la ruta elegida. Node; agente compatible; pregunta concreta de plataforma web |

Documenta Claude Code, Codex y Antigravity; el modelo local es el buscador de documentación y no un sustituto completo del agente de código

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- agente compatible
- pregunta concreta de plataforma web

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
npx modern-web-guidance@latest install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/GoogleChrome/modern-web-guidance/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar modern-web-guidance para mi objetivo y necesito pasos guiados. Lee https://github.com/GoogleChrome/modern-web-guidance/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Busca una guía sobre formularios y recupera su contenido antes de proponer una implementación.

**Qué comprobar:** Puedes identificar recomendación, compatibilidad y patrón aplicable.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar APIs web actuales
- Revisar patrones heredados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar APIs web actuales; Revisar patrones heredados | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code, Codex y Antigravity; el modelo local es el buscador de documentación y no un sustituto completo del agente de código

## Stack y modelos

- **Stack:** Node; agente compatible; pregunta concreta de plataforma web
- **Etiquetas:** `skills` `skill` `reference`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance)
- 🌐 Web: <https://goo.gle/modern-web-guidance>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/GoogleChrome/modern-web-guidance/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
