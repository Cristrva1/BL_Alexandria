[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Catálogos y marketplaces de skills

# 🧠 autoskills

> CLI que detecta tecnologías de un proyecto y selecciona skills de IA desde un registro de referencia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7k | NOASSERTION | Ruby | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

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

## Qué puedes hacer con él

CLI que detecta tecnologías de un proyecto y selecciona skills de IA desde un registro de referencia.

## Por qué destaca

Usos propuestos: Encontrar skills adecuadas para un proyecto React existente; Revisar qué archivos de skills se incorporarían sin descargarlos todos.

## Cómo funciona

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

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Awesome Agent Skills](awesome-agent-skills.md) | 37.2k | Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comunidad, para varios agentes. |

## Enlaces

- 🐙 GitHub: [midudev/autoskills](https://github.com/midudev/autoskills)
- 🌐 Web: <https://autoskills.sh>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/midudev/autoskills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
