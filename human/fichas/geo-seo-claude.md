[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de dominio: marketing, SEO y negocio

# 🌍 GEO-SEO Claude

> Skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO clásico, con citabilidad, schema, llms.txt e informes PDF.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.7k | MIT | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Puntuación de calidad** 49/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill para Claude Code de zubair-trabzada (MIT) que optimiza sitios para buscadores con IA (GEO) sin descuidar el SEO tradicional. Activa, sin releases.

## ¿Qué hace?

Comandos `/geo` para auditoría completa GEO+SEO con subagentes en paralelo, instantánea rápida, puntuación de «citabilidad», acceso de rastreadores de IA (robots.txt), análisis o generación de llms.txt, menciones de marca en plataformas citadas por IA, datos estructurados, SEO técnico, calidad de contenido (E-E-A-T) e informes para clientes, también en PDF con gráficos.

## ¿Cómo lo hace?

Se instala con un script (macOS/Linux o Git Bash en Windows) que copia la skill y crea un entorno virtual aislado en `~/.claude/skills/geo/.venv/`. Requiere Python 3.10+, Claude Code y Git; uv acelera la instalación y Playwright es opcional para capturas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Requisito: los comandos se ejecutan dentro de Claude Code. | Claude Code primero; luego el script de instalación. |
| [playwright](playwright.md) | Dependencia opcional para capturas de pantalla. | Instala Playwright y sus navegadores si quieres capturas en los informes. |
| [open-seo](open-seo.md) | Datos de palabras clave y backlinks como complemento a la auditoría (combinación por arquitectura). | Conecta el MCP de OpenSEO al mismo agente. |

**Notas:** Revisa el script antes de ejecutar `curl | bash`. Alternativa (elige una): claude-seo.

Estado en GitHub: activo · último push 2026-11-15 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/zubair-trabzada/geo-seo-claude/blob/main/README.md)</sub>

## Ver similares

Grupo **Skills de SEO para agentes**: GEO-SEO Claude ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [claude-seo](claude-seo.md) ⭐ recomendado | 70 | Si buscas esto: skills de Claude Code para revisar SEO técnico, contenido, presencia en buscadores de IA y otros aspectos de una web. |
| 2 | **GEO-SEO Claude** (esta ficha) | 49 | Si buscas esto: skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO clásico, con citabilidad, schema, llms.txt e informes PDF. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Usa el plan de Claude y dependencias locales; servicios o extensiones de datos pueden añadir costes |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Optimizar citabilidad no garantiza aparecer en resultados AI; la instalación Windows documentada usa Git Bash y no PowerShell |
| Coste | El coste depende del proveedor o la ruta. Usa el plan de Claude y dependencias locales; servicios o extensiones de datos pueden añadir costes |
| Equipo | Preparación según la ruta elegida. Claude Code; Python; Git Bash en Windows; web propia de prueba |

Optimizar citabilidad no garantiza aparecer en resultados AI; la instalación Windows documentada usa Git Bash y no PowerShell

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
- Python
- Git Bash en Windows
- web propia de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/zubair-trabzada/geo-seo-claude.git
cd geo-seo-claude
./install.sh
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/zubair-trabzada/geo-seo-claude/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GEO-SEO Claude para mi objetivo y necesito pasos guiados. Lee https://github.com/zubair-trabzada/geo-seo-claude/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta una revisión de una página propia y contrasta dos hallazgos con el HTML.

**Qué comprobar:** Puedes separar observación, heurística y propuesta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar schema de una web
- Preparar un informe GEO inicial

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar schema de una web; Preparar un informe GEO inicial | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Optimizar citabilidad no garantiza aparecer en resultados AI; la instalación Windows documentada usa Git Bash y no PowerShell

## Stack y modelos

- **Stack:** Claude Code; Python; Git Bash en Windows; web propia de prueba
- **Etiquetas:** `skills` `search` `pdf` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [claude-seo](claude-seo.md) | 29.4k | Skills de Claude Code para revisar SEO técnico, contenido, presencia en buscadores de IA y otros aspectos de una web. |

## Enlaces

- 🐙 GitHub: [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)
- 🌐 Web: <https://www.skool.com/aiworkshop>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/zubair-trabzada/geo-seo-claude/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
