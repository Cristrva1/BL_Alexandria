[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 📐 design.md

> Especificación y CLI para documentar identidad visual en DESIGN.md,validar tokens y comparar versiones.

## Cuándo elegir esta ficha

La ficha compacta marca ejecución cloud, mientras el upstream ofrece especificación, validador y exportador ejecutables en Node. Conservar composición y linter. Quitar el formato pierde reglas de identidad versionables. Design DNA conserva parte de la información con otro esquema.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/google-labs-code/design.md) · [Fuente 2](https://github.com/zanwei/design-dna) · [Fuente 3](https://github.com/google-labs-code/design.md/commit/db977b3c1d1f309269f43d5d17ae828d54bd6ae3)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 28.9k | Apache-2.0 | TypeScript | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 65/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Especificación de formato de Google Labs (Apache 2.0) para describir una identidad visual a agentes de código, con CLI de validación. Versión 0.4.0; el campo de versión de la especificación es aún «alpha».

## ¿Qué hace?

Un archivo DESIGN.md combina tokens de diseño legibles por máquina (YAML) con la justificación del diseño en Markdown, de modo que el agente conoce los valores exactos y su porqué. La CLI valida el archivo contra la especificación, detecta referencias de tokens rotas, comprueba el contraste WCAG, compara versiones y exporta a Tailwind v3/v4 o DTCG.

## ¿Cómo lo hace?

Paquete npm `@google/design.md` usado con `npx` (`lint`, `diff`, `export`), con salida JSON pensada para que actúen los agentes. La especificación completa está en `docs/spec.md`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [tailwindcss](tailwindcss.md) | Exporta temas para Tailwind v3 y v4. | Valida el DESIGN.md antes de exportar. |
| [impeccable](impeccable.md) | Su comando `document` genera un DESIGN.md (combinación por arquitectura). | Genera con impeccable y valida con la CLI. |
| [Claude Code](claude-code.md) | El agente lee el DESIGN.md como contexto persistente (combinación por arquitectura). | Coloca el archivo en la raíz del repositorio. |
| [design-dna](design-dna.md) | Los formatos son distintos. Valida el documento después de redactar y mapear el perfil manualmente. | Redacta el documento a partir del perfil y valida una copia de prueba. |
| [open-design](open-design.md) | Combinación recíproca: open-design lo enlaza como «Formato `DESIGN.md` para describir el sistema de diseño que el agente sigue. (combinación por arquitectura) (OpenDesign usa archivos DESIGN.md; la compatibilidad exacta con la especificación de Google no está verificada)». | Orden indicado desde open-design: Redacta el DESIGN.md antes de generar prototipos. |
| [Stitch SDK](stitch-sdk.md) | Combinación recíproca: Stitch SDK lo enlaza como «Especificación de sistema de diseño de Google Labs para guiar la generación. (combinación por arquitectura)». | Orden indicado desde Stitch SDK: Redacta el DESIGN.md e inclúyelo en los prompts. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[ui-ux-pro-max-skill](ui-ux-pro-max-skill.md)

**Notas:** La especificación sigue en alpha y puede cambiar.

Estado en GitHub: activo · último push 2026-11-06 · última versión publicada 0.4.0 (2026-07-27) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google-labs-code/design.md/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La especificación y CLI básicos no requieren modelo ni API; usar un agente consume su plan |
| Claude Code | Referencia para la herramienta; no es una integración |
| Codex | Referencia para la herramienta; no es una integración |
| Antigravity | Referencia para la herramienta; no es una integración |
| Modelos locales | La función básica no necesita un modelo. Es un formato y conjunto de utilidades, no un skill específico de Claude Code, Codex o Antigravity; debe cargarse como contexto según el agente |
| Coste | Sin pago a un modelo en la ruta básica. La especificación y CLI básicos no requieren modelo ni API; usar un agente consume su plan |
| Equipo | Preparación según la ruta elegida. Node para CLI; archivo DESIGN.md de prueba |

Es un formato y conjunto de utilidades, no un skill específico de Claude Code, Codex o Antigravity; debe cargarse como contexto según el agente

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node para CLI
- archivo DESIGN.md de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npx @google/design.md lint DESIGN.md
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/google-labs-code/design.md/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar design.md para mi objetivo y necesito pasos guiados. Lee https://github.com/google-labs-code/design.md/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Valida un archivo de identidad y corrige una referencia de token rota.

**Qué comprobar:** Puedes revisar el JSON de hallazgos y repetir la validación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Documentar una identidad visual
- Comparar dos versiones de tokens

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Documentar una identidad visual; Comparar dos versiones de tokens | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un formato y conjunto de utilidades, no un skill específico de Claude Code, Codex o Antigravity; debe cargarse como contexto según el agente

## Stack y modelos

- **Stack:** Node para CLI; archivo DESIGN.md de prueba
- **Etiquetas:** `skills` `design` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [google-labs-code/design.md](https://github.com/google-labs-code/design.md)
- 🌐 Web: <https://stitch.withgoogle.com/docs/design-md/specification>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google-labs-code/design.md/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
