[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de dominio: marketing, SEO y negocio

# 🎨 scientific-agent-skills

> Colección de skills y recursos para que agentes realicen tareas de investigación científica con herramientas de dominio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 57.2k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 71/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Colección MIT de 177 skills científicas y de investigación de K-Dense (antes Claude Scientific Skills), compatible con cualquier agente que siga el estándar Agent Skills. Muy activa (v2.72.0); K-Dense ofrece además un «co-científico» de escritorio de código abierto basado en ellas.

## ¿Qué hace?

Cubre biología, química, medicina, física, ingeniería, ciencias de la Tierra, datos y finanzas: búsqueda en más de 100 bases de datos científicas y financieras, integraciones con Benchling, DNAnexus, LatchBio, OMERO, Protocols.io, Open Notebook, Ginkgo Cloud Lab, LabArchives y Opentrons, análisis y generación de documentos e imágenes.

## ¿Cómo lo hace?

Skills en Markdown con scripts de apoyo; incluye las skills de documentos docx, pdf, pptx y xlsx copiadas de anthropics/skills bajo su licencia, y la generación de imágenes usa la API de OpenRouter. Se instala en el agente compatible según el README.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente compatible principal. | Instala solo las categorías que necesites. |
| [open-notebook](open-notebook.md) | Skill de integración explícita con Open Notebook. | Open Notebook en marcha y con API accesible antes de usar la skill. |
| [Anthropic Skills](anthropic-skills.md) | Sus skills de documentos provienen de anthropics/skills. | No dupliques las mismas skills de documentos desde ambos repositorios. |

**Notas:** Las integraciones de laboratorio requieren cuentas propias en cada plataforma.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada v2.72.0 (2026-10-01) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El agente, las bases de datos, servicios y cómputo de cada workflow tienen condiciones propias |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. Ahora se llama Scientific Agent Skills y admite Claude Code, Codex y Antigravity; la biblioteca no valida por sí sola conclusiones científicas ni autoriza operar equipos físicos |
| Coste | El coste depende del proveedor o la ruta. El agente, las bases de datos, servicios y cómputo de cada workflow tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Agente compatible; herramienta y skill elegidas; datos no sensibles de muestra |

Ahora se llama Scientific Agent Skills y admite Claude Code, Codex y Antigravity; la biblioteca no valida por sí sola conclusiones científicas ni autoriza operar equipos físicos

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
- herramienta y skill elegidas
- datos no sensibles de muestra

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add K-Dense-AI/scientific-agent-skills
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar scientific-agent-skills para mi objetivo y necesito pasos guiados. Lee https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige una skill de análisis y verifica dependencias y fuentes con un dataset educativo.

**Qué comprobar:** Puedes reproducir un resultado pequeño y revisar las referencias.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar un dataset científico
- Preparar una revisión bibliográfica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar un dataset científico; Preparar una revisión bibliográfica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ahora se llama Scientific Agent Skills y admite Claude Code, Codex y Antigravity; la biblioteca no valida por sí sola conclusiones científicas ni autoriza operar equipos físicos

## Stack y modelos

- **Stack:** Agente compatible; herramienta y skill elegidas; datos no sensibles de muestra
- **Etiquetas:** `dominio` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)
- 🌐 Web: <https://arxiv.org/abs/2609.00065>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
