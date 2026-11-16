[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Escritura y calidad de texto

# 🧹 Stop Slop

> Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.9k | MIT | — | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 43/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill de código abierto (MIT) de Hardik Pandya para eliminar marcas de IA en la prosa. Sin releases y con último cambio en marzo de 2026.

## ¿Qué hace?

Enseña a Claude o a cualquier LLM a detectar y quitar frases vetadas (aperturas de relleno, muletillas de énfasis, jerga empresarial, adverbios, metacomentarios), clichés estructurales (contrastes binarios, fragmentación dramática, voz pasiva) y reglas por frase (sin guiones largos, sin inicios con interrogativos, voz activa). Puntúa el texto del 1 al 10 en cinco dimensiones y pide revisar por debajo de 35/50.

## ¿Cómo lo hace?

Una carpeta con `SKILL.md` y archivos de referencia (frases, estructuras) que se cargan bajo demanda. Se añade como skill en Claude Code, se sube a un Proyecto de Claude, se copian sus reglas a instrucciones personalizadas o se incluye en el prompt de sistema por API.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Se añade la carpeta como skill. | Copia la carpeta al directorio de skills. |
| [Marketing Skills](marketingskills.md) | Limpiar textos generados por las skills de marketing (combinación por arquitectura). | Genera primero y revisa después. |
| [postiz-app](postiz-app.md) | Revisar publicaciones antes de programarlas (combinación por arquitectura). | Igual que arriba. |

**Notas:** Alternativas (elige una): no-ai-slop, humanizer. Sus reglas son estrictas (por ejemplo, elimina todos los adverbios) y pueden aplanar el estilo.

Estado en GitHub: activo · último push 2026-03-17 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/hardikpandya/stop-slop/blob/main/README.md)</sub>

## Ver similares

Grupo **Skills para quitar el tono de IA a los textos**: Stop Slop ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Humanizer](humanizer.md) ⭐ recomendado | 72 | Si buscas esto: skill para revisar estilo y claridad de texto conservando su sentido; no prueba autoría humana. |
| 2 | [no-ai-slop](no-ai-slop.md) | 55 | Si buscas esto: skill para revisar escritura y eliminar patrones repetitivos o frases poco específicas en textos generados con IA. |
| 3 | **Stop Slop** (esta ficha) | 43 | Si buscas esto: skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el modelo elegido; las reglas no aportan créditos ni acceso a servicios |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Referencia para la herramienta; no es una integración |
| Antigravity | Referencia para la herramienta; no es una integración |
| Modelos locales | La función básica no necesita un modelo. Documenta instalación en Claude Code y uso de instrucciones en otros LLM; no acredita plugins específicos para Codex o Antigravity |
| Coste | Consumo del agente que ya utilizas. Usa el modelo elegido; las reglas no aportan créditos ni acceso a servicios |
| Equipo | Preparación según la ruta elegida. Claude con skills o instrucciones pegadas en otro modelo; texto propio |

Documenta instalación en Claude Code y uso de instrucciones en otros LLM; no acredita plugins específicos para Codex o Antigravity

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude con skills o instrucciones pegadas en otro modelo
- texto propio

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/hardikpandya/stop-slop/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Stop Slop para mi objetivo y necesito pasos guiados. Lee https://github.com/hardikpandya/stop-slop/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Aplica la lista de frases a un párrafo y conserva cualquier término técnico necesario.

**Qué comprobar:** Puedes justificar cada cambio de redacción.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Reducir frases vagas
- Revisar un borrador antes de publicarlo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Reducir frases vagas; Revisar un borrador antes de publicarlo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Documenta instalación en Claude Code y uso de instrucciones en otros LLM; no acredita plugins específicos para Codex o Antigravity

## Stack y modelos

- **Stack:** Claude con skills o instrucciones pegadas en otro modelo; texto propio
- **Etiquetas:** `skills` `prompts` `docs`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Humanizer](humanizer.md) | 69.1k | Skill para revisar estilo y claridad de texto conservando su sentido; no prueba autoría humana. |
| [no-ai-slop](no-ai-slop.md) | 13.5k | Skill para revisar escritura y eliminar patrones repetitivos o frases poco específicas en textos generados con IA. |

## Enlaces

- 🐙 GitHub: [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/hardikpandya/stop-slop/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
