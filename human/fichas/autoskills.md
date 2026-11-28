[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🧠 autoskills

> CLI que detecta tecnologías de un proyecto y selecciona skills de IA desde un registro de referencia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7k | CC-BY-NC-4.0 | Ruby | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 39/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** CC-BY-NC-4.0. Solo uso no comercial. Fuente: [LICENSE](https://github.com/midudev/autoskills/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

CLI de midudev que detecta el stack de un proyecto e instala skills de agente seleccionadas. Licencia CC BY-NC 4.0, que no es de código abierto y prohíbe el uso comercial, y que GitHub marca como NOASSERTION. Activo (v0.4.1).

## ¿Qué hace?

Con `npx autoskills` analiza `package.json`, los archivos de Gradle y la configuración del proyecto, elige las skills más adecuadas de su registro auditado y solo descarga y verifica esas. Su modelo de seguridad evita descargar en vivo de repositorios de terceros: los mantenedores sincronizan las skills en un registro propio que revisa una IA en busca de inyección de prompts y ataques a la cadena de suministro.

## ¿Cómo lo hace?

Paquete npm con opciones `-y`, `--dry-run` y `-a/--agent` para instalar solo en ciertos agentes, como cursor o claude-code.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Destino soportado (`-a claude-code`). | Ejecuta primero con `--dry-run`. |
| [SkillSpector](skillspector.md) | Segunda auditoría de las skills instaladas, además de la revisión por IA del registro (combinación por arquitectura). | Audita después de instalar. |
| [Codex CLI](codex.md) | Agente compatible con skills estándar (combinación por arquitectura). | Consulta la lista de agentes de la opción `--agent`. |

**Notas:** La licencia CC BY-NC impide el uso comercial. Se quitó awesome-agent-skills porque no hay integración.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.4.1 (2026-10-14) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/midudev/autoskills/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La detección local del stack no necesita un modelo; la licencia CC BY-NC limita usos comerciales y el agente se paga aparte |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Se corrige la API inferida por menciones a tecnologías de autenticación y pagos: no son proveedores requeridos por el CLI |
| Coste | Sin pago a un modelo en la ruta básica. La detección local del stack no necesita un modelo; la licencia CC BY-NC limita usos comerciales y el agente se paga aparte |
| Equipo | Preparación según la ruta elegida. Node.js;  un proyecto con sus manifiestos de dependencias |

Se corrige la API inferida por menciones a tecnologías de autenticación y pagos: no son proveedores requeridos por el CLI

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
-  un proyecto con sus manifiestos de dependencias

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npx autoskills
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/midudev/autoskills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar autoskills para mi objetivo y necesito pasos guiados. Lee https://github.com/midudev/autoskills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Revisa la selección que propone para tu stack antes de permitir la instalación.

**Qué comprobar:** La lista corresponde a tus tecnologías y queda un registro de las skills instaladas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Encontrar skills adecuadas para un proyecto React existente
- Revisar qué archivos de skills se incorporarían sin descargarlos todos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Encontrar skills adecuadas para un proyecto React existente; Revisar qué archivos de skills se incorporarían sin descargarlos todos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Se corrige la API inferida por menciones a tecnologías de autenticación y pagos: no son proveedores requeridos por el CLI

## Stack y modelos

- **Stack:** Node.js;  un proyecto con sus manifiestos de dependencias
- **Etiquetas:** `catalogos` `ruby`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Skills CLI (Vercel Labs)](vercel-skills.md) | 41.2k | Instala, lista, actualiza y quita skills de agentes de código desde un repositorio o una carpeta propia, en Claude Code, Codex y otros agentes. |

## Enlaces

- 🐙 GitHub: [midudev/autoskills](https://github.com/midudev/autoskills)
- 🌐 Web: <https://autoskills.sh>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/midudev/autoskills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
