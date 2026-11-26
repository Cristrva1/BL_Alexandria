[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🎨 book-to-skill

> Herramientas para convertir un libro técnico en PDF en una skill que un agente pueda consultar durante el trabajo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 37.9k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill de virgiliojr94 (MIT) que convierte libros técnicos, carpetas de documentos o colecciones de fuentes en una skill de agente unificada. Activa (v1.4.0).

## ¿Qué hace?

Con `/book-to-skill ./libro.pdf` destila el libro en marcos, reglas de decisión, antipatrones y un archivo por capítulo, es decir, estructura y no un resumen. Después el agente carga solo el capítulo pertinente al preguntar (`/mi-libro replicación`). El README declara entre 24 y 51 veces menos tokens que meter el libro entero en el contexto [DATO NO VERIFICADO: medición propia]. Acepta PDF, EPUB, DOCX, MD, HTML, RTF y más.

## ¿Cómo lo hace?

Combina un extractor determinista en Python (documento → texto limpio y metadatos) con un generador guiado por especificación que sigue el agente. Para PDF usa pdftotext (poppler) en textos y Docling para contenido técnico con tablas, código o fórmulas; `extract.py --check` muestra qué extractores hay. Se instala con `npx skills add virgiliojr94/book-to-skill` en Copilot CLI, Amp, Claude Code, Codex, Hermes Agent, OpenCode y otros.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Docling](docling.md) | Extractor recomendado para libros técnicos. | `pip3 install docling` antes de convertir PDF técnicos. |
| [Claude Code](claude-code.md) | Agente compatible. | Instala con npx skills. |
| [hermes-agent](hermes-agent.md) | Agente compatible citado. | Igual que arriba. |

**Notas:** Convierte solo libros cuyos derechos tengas: la skill generada contiene el contenido del libro.

Estado en GitHub: activo · último push 2026-11-08 · última versión publicada v1.4.0 (2026-08-10) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/virgiliojr94/book-to-skill/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El procesamiento y uso consumen el agente; OCR y dependencias se revisan según el documento |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. La portabilidad corresponde al estándar Agent Skills; empieza con material propio y revisa qué contenido puede redistribuirse |
| Coste | Consumo del agente que ya utilizas. El procesamiento y uso consumen el agente; OCR y dependencias se revisan según el documento |
| Equipo | Preparación según la ruta elegida. Agente con Agent Skills;  un documento propio o autorizado de pocas páginas |

La portabilidad corresponde al estándar Agent Skills; empieza con material propio y revisa qué contenido puede redistribuirse

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente con Agent Skills
-  un documento propio o autorizado de pocas páginas

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# One command, any host — via the cross-agent skills CLI:
npx skills add virgiliojr94/book-to-skill
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/virgiliojr94/book-to-skill/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar book-to-skill para mi objetivo y necesito pasos guiados. Lee https://github.com/virgiliojr94/book-to-skill/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Convierte un extracto técnico propio en una skill y revisa el SKILL.md generado.

**Qué comprobar:** La skill resume el ámbito, conserva referencias y responde una pregunta sobre ese extracto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una guía de consulta a partir de documentación interna
- Convertir notas técnicas propias en instrucciones reutilizables del agente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una guía de consulta a partir de documentación interna; Convertir notas técnicas propias en instrucciones reutilizables del agente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La portabilidad corresponde al estándar Agent Skills; empieza con material propio y revisa qué contenido puede redistribuirse

## Stack y modelos

- **Stack:** Agente con Agent Skills;  un documento propio o autorizado de pocas páginas
- **Etiquetas:** `metodologia` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/virgiliojr94/book-to-skill/blob/master/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
