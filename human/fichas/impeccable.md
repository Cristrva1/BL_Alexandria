[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 💎 impeccable

> Vocabulario y playbooks de diseño para agentes, con detector determinista y hooks según herramienta.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 110k | Apache-2.0 | Rust | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

«Vocabulario de diseño» para agentes de código, de Paul Bakaus, con licencia Apache 2.0. Muy popular y activo (CLI v4.9.2).

## ¿Qué hace?

Ofrece comandos para dirigir el diseño (`polish`, `bolder`), revisarlo (`critique` puntúa con heurísticas de usabilidad; `audit` revisa accesibilidad) y planificarlo (`shape`, `init` escribe PRODUCT.md, `document` escribe DESIGN.md). Incluye un detector determinista con 62 reglas, sin LLM, para los tics típicos de la IA: Inter en todo, degradados morado-azul, tarjetas anidadas.

## ¿Cómo lo hace?

Se instala con `npx impeccable install` en la raíz del proyecto y se inicia con `/impeccable init`. Funciona con Claude Code, Cursor, Codex CLI, Copilot, Gemini CLI, OpenCode, Kiro y muchos otros. `npx impeccable detect` analiza directorios o páginas renderizadas (usa Chrome o Edge) y emite JSON o anotaciones de GitHub Actions; guarda su estado en `.impeccable/`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente compatible documentado. | Instala y ejecuta `/impeccable init` una vez por proyecto. |
| [Codex CLI](codex.md) | Agente compatible (`$impeccable init`). | Igual que arriba. |
| [design.md](design-md.md) | El comando `document` escribe un DESIGN.md que puede validarse con la herramienta de Google (combinación por arquitectura; [DATO NO VERIFICADO: plena conformidad con la especificación de Google]). | Genera con impeccable y valida con `npx @google/design.md lint`. |

**Notas:** Alternativas (elige una): ui-ux-pro-max-skill, taste-skill, hallmark.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada cli-v4.9.2 (2026-11-16) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/pbakaus/impeccable/blob/main/README.md)</sub>

## Ver similares

Grupo **Skills de diseño de interfaces para agentes**: impeccable ocupa la posición 3 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ui-ux-pro-max-skill](ui-ux-pro-max-skill.md) ⭐ recomendado | 73 | Si quieres una skill con bases de estilos, paletas y tipografías para generar UI. |
| 2 | [taste-skill](taste-skill.md) | 70 | Si quieres que el agente evite el aspecto genérico en las interfaces. |
| 3 | **impeccable** (esta ficha) | 63 | Si quieres vocabulario y playbooks de diseño con detector y hooks. |
| 4 | [hallmark](hallmark.md) | 50 | Si quieres decisiones visuales más concretas y coherentes al construir interfaces. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El detector no requiere LLM ni API; los cambios guiados usan el plan del agente |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Hooks y descarga del motor tienen efectos propios fuera del permiso de cada llamada del modelo; Antigravity puede cargar skills sin compartir todos los hooks de Claude o Codex |
| Coste | El coste depende del proveedor o la ruta. El detector no requiere LLM ni API; los cambios guiados usan el plan del agente |
| Equipo | Preparación según la ruta elegida. Node para instalador; agente; Chrome o Edge para revisión de página |

Hooks y descarga del motor tienen efectos propios fuera del permiso de cada llamada del modelo; Antigravity puede cargar skills sin compartir todos los hooks de Claude o Codex

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node para instalador
- agente
- Chrome o Edge para revisión de página

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx impeccable install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/pbakaus/impeccable/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar impeccable para mi objetivo y necesito pasos guiados. Lee https://github.com/pbakaus/impeccable/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala para un proyecto de prueba y revisa hallazgos del detector antes de pedir cambios.

**Qué comprobar:** Puedes distinguir reglas deterministas de recomendaciones del modelo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Auditar una interfaz
- Pulir un componente concreto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Auditar una interfaz; Pulir un componente concreto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Hooks y descarga del motor tienen efectos propios fuera del permiso de cada llamada del modelo; Antigravity puede cargar skills sin compartir todos los hooks de Claude o Codex

## Stack y modelos

- **Stack:** Node para instalador; agente; Chrome o Edge para revisión de página
- **Etiquetas:** `skills` `design` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ui-ux-pro-max-skill](ui-ux-pro-max-skill.md) | 150k | Conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para que las interfaces que genera dejen de verse a "plantilla". |
| [taste-skill](taste-skill.md) | 116k | Skill design-taste-frontend para dirección visual y revisión de sitios; otros skills del pack antiguo se movieron a repos propios. |
| [hallmark](hallmark.md) | 55.1k | Skill de diseño para agentes que ayuda a construir interfaces con decisiones visuales más específicas y coherentes. |

## Enlaces

- 🐙 GitHub: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
- 🌐 Web: <https://impeccable.style>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pbakaus/impeccable/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
