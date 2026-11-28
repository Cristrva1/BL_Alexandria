[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Skills de análisis y seguridad

# 🧠 security-audit-skill

> Skill de Cloudflare que organiza auditorías de código con búsqueda, validación independiente y hallazgos estructurados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 72.7k | MIT | JavaScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill de auditoría de seguridad para agentes de programación, de Cloudflare. Licencia MIT. Es muy popular (~73k estrellas, sin releases) y fue el germen del arnés de descubrimiento de vulnerabilidades que Cloudflare describe en su blog.

## ¿Qué hace?

Convierte al agente en auditor: orquesta agentes aislados en reconocimiento, búsqueda guiada por cobertura, validación de candidatos, salida estructurada y verificación independiente de cada hallazgo. Exige que la severidad dependa del impacto (probabilidad × impacto) y no de desviarse de una checklist. Los reemplazos importantes pasan por otro verificador independiente.

## ¿Cómo lo hace?

Se instala con `npx skills add https://github.com/cloudflare/security-audit-skill` eligiendo el agente. Requiere un agente con un modelo que soporte herramientas y subagentes en paralelo. Una auditoría completa consume muchos tokens.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente compatible con skills y subagentes en paralelo. | Instala la skill con `npx skills add` para Claude Code. |
| [Codex CLI](codex.md) | Agente compatible mediante el instalador `skills`. | Instala la skill seleccionando Codex. |
| [Semgrep](semgrep.md) | Partir de hallazgos estáticos para orientar la búsqueda. (combinación por arquitectura) | Ejecuta Semgrep y entrega el informe al agente. |

**Notas:** Sin alternativas declaradas. Úsalo solo contra sistemas propios o con autorización escrita.

Estado en GitHub: activo · último push 2026-09-14 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/cloudflare/security-audit-skill/blob/main/README.md) · [2](https://blog.cloudflare.com/build-your-own-vulnerability-harness)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La skill usa el agente y puede multiplicar llamadas al delegar; herramientas y servicios externos tienen costes propios |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. El formato Agent Skills es portable; el workflow completo requiere las capacidades de herramientas y subagentes indicadas por el autor |
| Coste | Consumo del agente que ya utilizas. La skill usa el agente y puede multiplicar llamadas al delegar; herramientas y servicios externos tienen costes propios |
| Equipo | Preparación según la ruta elegida. Agente con herramientas y subagentes paralelos; proyecto propio de prueba |

El formato Agent Skills es portable; el workflow completo requiere las capacidades de herramientas y subagentes indicadas por el autor

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente con herramientas y subagentes paralelos
- proyecto propio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add https://github.com/cloudflare/security-audit-skill \
  --skill security-audit
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/cloudflare/security-audit-skill/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar security-audit-skill para mi objetivo y necesito pasos guiados. Lee https://github.com/cloudflare/security-audit-skill/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Solicita una revisión de una app pequeña propia y separa candidatos de hallazgos validados.

**Qué comprobar:** Cada hallazgo tiene ubicación, evidencia, impacto y veredicto revisable.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar una revisión de código autorizada
- Evaluar la calidad de hallazgos generados por un agente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar una revisión de código autorizada; Evaluar la calidad de hallazgos generados por un agente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El formato Agent Skills es portable; el workflow completo requiere las capacidades de herramientas y subagentes indicadas por el autor

## Stack y modelos

- **Stack:** Agente con herramientas y subagentes paralelos; proyecto propio de prueba
- **Etiquetas:** `metodologia` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cloudflare/security-audit-skill/blob/main/README.md)
- [Fuente 2](https://github.com/vercel-labs/skills/blob/main/docs/agents.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
