[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Escritura y calidad de texto

# 🧑 Humanizer

> Skill para revisar estilo y claridad de texto conservando su sentido; no prueba autoría humana.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 69.1k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## ¿Qué es?

Skill de escritura de código abierto (MIT) de blader que hace que un texto escrito por IA suene a persona sin cambiar su contenido. Muy popular y activa (v4.0.0); el README lleva un patrocinio.

## ¿Qué hace?

Reescribe borradores eliminando las marcas de escritura de IA descritas en la guía «Signs of AI writing» de Wikipedia: entusiasmo vacío, emojis, fórmulas y estructuras repetidas. Se invoca con `/humanizer`. Edita para lectores humanos, no para burlar detectores de IA; según su README, en una prueba ciega los jueces prefirieron su versión 16 de 16 veces [DATO NO VERIFICADO: prueba del propio proyecto].

## ¿Cómo lo hace?

Es un conjunto de instrucciones para agentes (formato skill). Se instala como plugin de Claude Code (`/plugin marketplace add blader/humanizer`, requiere Claude Code 2.1.142+) o con `npx skills add blader/humanizer --global --agent claude-code` o `--agent codex`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin oficial y skill instalable. | Actualiza Claude Code a 2.1.142+ antes de instalar el plugin. |
| [Codex CLI](codex.md) | Instalación documentada con `npx skills add ... --agent codex`. | Codex instalado primero. |
| [Marketing Skills](marketingskills.md) | Pulir los textos de marketing que generan otras skills (combinación por arquitectura). | Genera con marketingskills y pasa el resultado por `/humanizer`. |
| [postiz-app](postiz-app.md) | Revisar publicaciones antes de programarlas (combinación por arquitectura). | Humaniza primero; programa después. |

**Notas:** Alternativa (elige una): stop-slop.

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada v4.0.0 (2026-11-10) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/blader/humanizer/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el modelo o plan del anfitrión; no necesita una API adicional por sí solo |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Documenta Claude Code, Codex y otros hosts de skills; mejorar estilo no demuestra autoría humana ni garantiza pasar detectores |
| Coste | Consumo del agente que ya utilizas. Usa el modelo o plan del anfitrión; no necesita una API adicional por sí solo |
| Equipo | Preparación según la ruta elegida. Agente con skills; texto propio breve |

Documenta Claude Code, Codex y otros hosts de skills; mejorar estilo no demuestra autoría humana ni garantiza pasar detectores

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente con skills
- texto propio breve

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add blader/humanizer --global --agent codex
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/blader/humanizer/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Humanizer para mi objetivo y necesito pasos guiados. Lee https://github.com/blader/humanizer/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Revisa un párrafo y compara la versión propuesta con los hechos y tono del original.

**Qué comprobar:** Puedes aceptar cambios de estilo sin alterar el contenido.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Mejorar claridad de un correo
- Revisar prosa repetitiva

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Mejorar claridad de un correo; Revisar prosa repetitiva | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta Claude Code, Codex y otros hosts de skills; mejorar estilo no demuestra autoría humana ni garantiza pasar detectores

## Stack y modelos

- **Stack:** Agente con skills; texto propio breve
- **Etiquetas:** `skills` `prompts` `docs`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Stop Slop](stop-slop.md) | 18.9k | Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad. |

## Enlaces

- 🐙 GitHub: [blader/humanizer](https://github.com/blader/humanizer)
- 🌐 Web: <https://skills.sh/blader/humanizer>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/blader/humanizer/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
