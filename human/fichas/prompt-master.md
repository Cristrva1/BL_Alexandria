[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Prompts y prompt engineering

# 🎯 prompt-master

> Skill de Claude que ayuda a formular encargos para distintas herramientas de IA; no garantiza ahorro de tokens.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16k | MIT | — | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill para Claude (MIT) de nidhinjs que redacta prompts optimizados para otras herramientas de IA. Es un proyecto individual y reciente (último push en octubre de 2026), sin releases. Promete ahorrar créditos y tokens [DATO NO VERIFICADO: sin medición independiente].

## ¿Qué hace?

A partir de lo que el usuario quiere, pregunta lo que falta y genera un prompt adaptado a la herramienta de destino: ChatGPT, Claude Code, Cursor, Midjourney, ComfyUI, Ollama y otras. Aplica reglas por tipo de herramienta (por ejemplo, incluir system prompt para un Modelfile de Ollama) para evitar ciclos de re-prompting.

## ¿Cómo lo hace?

Es un SKILL.md con referencias. La instalación recomendada es subir el ZIP en claude.ai (Customize → Skills); la alternativa es clonarlo en `~/.claude/skills/prompt-master` para Claude Code, opción que el propio autor desaconseja. No ejecuta código ni requiere claves adicionales.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Cliente donde se puede cargar la skill desde `~/.claude/skills`. | Instala Claude Code y clona la skill en el directorio de skills. |
| [Prompt Engineering Guide](prompt-engineering-guide.md) | Entender las técnicas que la skill aplica automáticamente. (combinación por arquitectura) | Consulta la guía para revisar críticamente los prompts generados. |
| [Anthropic Skills](anthropic-skills.md) | Referencia oficial del formato de skills, útil para adaptar o auditar esta skill. (combinación por arquitectura) | Compara la estructura con los ejemplos oficiales antes de modificarla. |

**Notas:** Sin alternativas declaradas. Combinación anterior con andrej-karpathy-skills eliminada: sin relación documentada.

Estado en GitHub: activo · último push 2026-10-22 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/nidhinjs/prompt-master/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El skill no trae créditos; lo ejecuta el modelo del anfitrión y los destinos tienen sus propios costes |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Referencia para la herramienta; no es una integración |
| Antigravity | Referencia para la herramienta; no es una integración |
| Modelos locales | La función básica no necesita un modelo. La instalación documentada es para Claude y Claude Code; Codex y Antigravity aparecen como destinos del prompt generado y no prueban instalación nativa en ellos; cero desperdicio es una afirmación promocional |
| Coste | Consumo del agente que ya utilizas. El skill no trae créditos; lo ejecuta el modelo del anfitrión y los destinos tienen sus propios costes |
| Equipo | Preparación según la ruta elegida. Claude con skills o Claude Code; descripción de una tarea |

La instalación documentada es para Claude y Claude Code; Codex y Antigravity aparecen como destinos del prompt generado y no prueban instalación nativa en ellos; cero desperdicio es una afirmación promocional

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude con skills o Claude Code
- descripción de una tarea

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
mkdir -p ~/.claude/skills
git clone https://github.com/nidhinjs/prompt-master.git ~/.claude/skills/prompt-master
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/nidhinjs/prompt-master/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar prompt-master para mi objetivo y necesito pasos guiados. Lee https://github.com/nidhinjs/prompt-master/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide al skill que formule preguntas para redactar un prompt de una página de reservas.

**Qué comprobar:** El prompt especifica objetivo, contexto, restricciones y criterio de aceptación.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Redactar un encargo de programación
- Preparar un prompt de imagen con requisitos concretos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Redactar un encargo de programación; Preparar un prompt de imagen con requisitos concretos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La instalación documentada es para Claude y Claude Code; Codex y Antigravity aparecen como destinos del prompt generado y no prueban instalación nativa en ellos; cero desperdicio es una afirmación promocional

## Stack y modelos

- **Stack:** Claude con skills o Claude Code; descripción de una tarea
- **Etiquetas:** `skills` `prompts`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/nidhinjs/prompt-master/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
