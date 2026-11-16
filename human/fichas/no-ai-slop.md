[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Escritura y calidad de texto

# 🎨 no-ai-slop

> Skill para revisar escritura y eliminar patrones repetitivos o frases poco específicas en textos generados con IA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.5k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Puntuación de calidad** 55/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill de escritura de código abierto (MIT) de Peter Yang. Activa (v1.0.6).

## ¿Qué hace?

Quita más de 20 patrones de «slop» de IA (como «No es X. Es Y.» o «Lo que nadie te cuenta…») sin aplanar tu voz personal, y lista lo que cambió. También detecta y cita patrones sin juzgar si lo escribió una IA, y genera «slop» exagerado como sátira.

## ¿Cómo lo hace?

Skill instalable pidiéndoselo a ChatGPT, Claude Code o Codex, o con `npx skills add petergyang/no-ai-slop --skill no-ai-slop --global --yes`; se usa con `/no-ai-slop`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente compatible documentado. | Instala con npx skills de forma global. |
| [Codex CLI](codex.md) | Agente compatible documentado. | Igual que arriba. |
| [Marketing Skills](marketingskills.md) | Revisar los textos de marketing generados (combinación por arquitectura). | Genera primero y revisa después. |

**Notas:** Alternativas (elige una): humanizer, stop-slop.

Estado en GitHub: activo · último push 2026-09-02 · última versión publicada v1.0.6 (2026-08-01) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/petergyang/no-ai-slop/blob/main/README.md)</sub>

## Ver similares

Grupo **Skills para quitar el tono de IA a los textos**: no-ai-slop ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Humanizer](humanizer.md) ⭐ recomendado | 72 | Si buscas esto: skill para revisar estilo y claridad de texto conservando su sentido; no prueba autoría humana. |
| 2 | **no-ai-slop** (esta ficha) | 55 | Si buscas esto: skill para revisar escritura y eliminar patrones repetitivos o frases poco específicas en textos generados con IA. |
| 3 | [Stop Slop](stop-slop.md) | 43 | Si buscas esto: skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el modelo del anfitrión; no necesita una segunda API por sí solo |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Tiene metadatos de plugins para ChatGPT y Codex y formato de skill portable; no garantiza detección o invisibilidad de escritura AI |
| Coste | Consumo del agente que ya utilizas. Usa el modelo del anfitrión; no necesita una segunda API por sí solo |
| Equipo | Preparación según la ruta elegida. Agente compatible; texto propio |

Tiene metadatos de plugins para ChatGPT y Codex y formato de skill portable; no garantiza detección o invisibilidad de escritura AI

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
- texto propio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
npx skills add petergyang/no-ai-slop --skill no-ai-slop --global --yes
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/petergyang/no-ai-slop/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar no-ai-slop para mi objetivo y necesito pasos guiados. Lee https://github.com/petergyang/no-ai-slop/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Revisa un texto corto y contrasta cada cambio con el sentido y voz originales.

**Qué comprobar:** Puedes aceptar correcciones concretas sin perder información.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Editar una publicación
- Mejorar claridad de un informe

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Editar una publicación; Mejorar claridad de un informe | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Tiene metadatos de plugins para ChatGPT y Codex y formato de skill portable; no garantiza detección o invisibilidad de escritura AI

## Stack y modelos

- **Stack:** Agente compatible; texto propio
- **Etiquetas:** `escritura` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Humanizer](humanizer.md) | 69.1k | Skill para revisar estilo y claridad de texto conservando su sentido; no prueba autoría humana. |
| [Stop Slop](stop-slop.md) | 18.9k | Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbrica de calidad. |

## Enlaces

- 🐙 GitHub: [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)
- 🌐 Web: <https://creatoreconomy.so/p/use-my-no-ai-slop-skill-to-remove-20-ai-slop-patterns>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/petergyang/no-ai-slop/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
