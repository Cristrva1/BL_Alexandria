[🏠 Inicio](../README.md) › [📄 Presentaciones, diagramas y explicación visual](../categorias/31-presentaciones-diagramas.md) › Diagramas y documentación

# 📄 archify

> Skill para convertir ideas, planes y bases de código en diagramas y visualizaciones HTML interactivas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 96.5k | Apache-2.0 | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## ¿Qué es?

Archify, skill que convierte ideas, preguntas o planes en visuales HTML interactivos, de @tt-a1i. Licencia Apache-2.0 (las concesiones MIT históricas siguen vigentes; servicios de terceros y planes de pago no son del proyecto). Creado en abril de 2026, tiene ~97k estrellas (v3.2.0), una cifra inusual.

## ¿Qué hace?

Describes lo que quieres entender o planificar (arquitecturas, mapas de aprendizaje, itinerarios) y el agente genera un HTML interactivo que se puede explorar, personalizar y compartir.

## ¿Cómo lo hace?

Funciona con Cursor, Claude Code, Codex CLI y OpenCode; en Claude.ai se sube `archify.zip` como skill (depende del acceso a Node.js en el sandbox).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente soportado. | Instala la skill. |
| [OpenCode](opencode.md) | Agente soportado. | Instala la skill. |
| [Mermaid](mermaid.md) | Diagramas textuales para documentación estática. (combinación por arquitectura) | Usa Mermaid en docs y Archify para explorar. |

**Notas:** Sin alternativas declaradas. Tiene un grupo funcional con diagram-design.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.2.0 (2026-10-19) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/tt-a1i/archify/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La skill usa el agente; los servicios de patrocinadores y planes externos no son parte incluida del proyecto |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | La función básica no necesita un modelo. Documenta Claude Code y Codex; la comprobación de actualizaciones puede hacer una petición de metadatos y no instala nuevas versiones automáticamente |
| Coste | Consumo del agente que ya utilizas. La skill usa el agente; los servicios de patrocinadores y planes externos no son parte incluida del proyecto |
| Equipo | Preparación según la ruta elegida. Agente con archivos y ejecución; idea o repositorio de prueba |

Documenta Claude Code y Codex; la comprobación de actualizaciones puede hacer una petición de metadatos y no instala nuevas versiones automáticamente

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente con archivos y ejecución
- idea o repositorio de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/tt-a1i/archify/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar archify para mi objetivo y necesito pasos guiados. Lee https://github.com/tt-a1i/archify/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Dibuja el flujo de una app pequeña y revisa que cada componente exista en la fuente.

**Qué comprobar:** Puedes contrastar nodos, enlaces y responsabilidades.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explicar una arquitectura
- Preparar un plan de trabajo visual

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explicar una arquitectura; Preparar un plan de trabajo visual | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code y Codex; la comprobación de actualizaciones puede hacer una petición de metadatos y no instala nuevas versiones automáticamente

## Stack y modelos

- **Stack:** Agente con archivos y ejecución; idea o repositorio de prueba
- **Etiquetas:** `diagramas` `agent-skills` `ai-agents` `architecture-diagram` `claude-code` `claude-skills` `codex` `coding-agents`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [tt-a1i/archify](https://github.com/tt-a1i/archify)
- 🌐 Web: <https://archify.si>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/tt-a1i/archify/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
