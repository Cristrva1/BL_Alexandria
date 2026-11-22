[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 🎨 Open Code Review

> Revisa cambios de código con reglas y un informe guiado, usando su propio proveedor de IA o el asistente de programación que ya tienes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 55.3k | Apache-2.0 | Go | 2026-11-22 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

## ¿Qué es?

Una herramienta de revisión defensiva de código para cambios propios antes de fusionarlos.

## ¿Qué hace?

Revisa cambios de código con reglas y un informe guiado, usando su propio proveedor de IA o el asistente de programación que ya tienes.

## ¿Cómo lo hace?

El modo delegado organiza los archivos, las reglas y la cobertura; el análisis lo realiza Claude Code, Codex u otro cliente admitido.

Estado en GitHub: activo · último push 2026-11-22 · última versión publicada v1.14.1 (2026-11-22) · licencia declarada Apache-2.0 (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/alibaba/open-code-review/blob/284ff013f0705ae6cac4c8dfbffa2f2551886d56/README.md) · [2](https://github.com/alibaba/open-code-review/blob/284ff013f0705ae6cac4c8dfbffa2f2551886d56/skills/open-code-review-delegate/SKILL.md) · [3](https://github.com/alibaba/open-code-review/blob/284ff013f0705ae6cac4c8dfbffa2f2551886d56/pages/src/content/docs/en/telemetry.md) · [4](https://github.com/alibaba/open-code-review/blob/284ff013f0705ae6cac4c8dfbffa2f2551886d56/.github/SECURITY.md) · [5](https://github.com/alibaba/open-code-review/releases/tag/v1.14.1) · [6](https://github.com/alibaba/open-code-review/blob/main/LICENSE) · [7](https://github.com/alibaba/open-code-review/security/advisories/GHSA-wwg6-qfxw-xffj)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El modo delegado usa el acceso del asistente. Para el modo nativo se configura y autentica un proveedor aparte. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Integración no documentada |
| Modelos locales | Ejecución con modelos locales por confirmar. No se ha comprobado una ruta local completa; la ficha se limita al modo delegado. |
| Coste | El coste depende del proveedor o la ruta. En modo delegado consumes el acceso y los límites de Claude Code o Codex. En modo nativo se configura el proveedor de OCR y su facturación por separado. |
| Equipo | Preparación según la ruta elegida. Git 2.41 o superior, la CLI ocr y un cliente apropiado para la ruta delegada. |

La skill delegada está documentada para Claude Code y Codex; esto no otorga una credencial para el modo nativo de OCR.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Git 2.41 o superior, la CLI ocr y un cliente apropiado para la ruta delegada.

1. Prepara Git 2.41 o superior; elige la CLI del release v1.14.1 y sigue la instalación de la skill delegada para tu cliente.
2. Pide que revise un cambio ficticio de un proyecto propio, sin permitir escrituras ni cargar un repositorio de origen desconocido.
3. Comprueba el resultado: el informe nombra archivos, hallazgos y comprobaciones sin modificar el proyecto de ejemplo.

Consulta la guía vinculada y la versión revisada. No se ejecutó el proyecto.

[Instrucciones originales de instalación](https://github.com/alibaba/open-code-review/blob/284ff013f0705ae6cac4c8dfbffa2f2551886d56/skills/open-code-review-delegate/SKILL.md)

[Abrir la web o descarga indicada por el autor](https://github.com/alibaba/open-code-review/blob/284ff013f0705ae6cac4c8dfbffa2f2551886d56/skills/open-code-review-delegate/SKILL.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Open Code Review para mi objetivo y necesito pasos guiados. Lee https://github.com/alibaba/open-code-review/blob/284ff013f0705ae6cac4c8dfbffa2f2551886d56/skills/open-code-review-delegate/SKILL.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide que revise un cambio ficticio de un proyecto propio, sin permitir escrituras ni cargar un repositorio de origen desconocido..

**Qué comprobar:** El informe nombra archivos, hallazgos y comprobaciones sin modificar el proyecto de ejemplo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar condiciones de error en un cambio de ejemplo.
- Preparar una lista de comprobaciones para una PR de un proyecto propio.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar condiciones de error en un cambio de ejemplo.; Preparar una lista de comprobaciones para una PR de un proyecto propio. | no usas un agente compatible con skills |

**Limitaciones:** GHSA-wwg6-qfxw-xffj afecta versiones anteriores a 1.11.1; el tag 1.14.1 incluye la corrección. Usa solo repositorios propios o de confianza. Si el modelo es remoto, el cliente puede enviar fragmentos del código. El ajuste de telemetría de la CLI está apagado por defecto. La revisión no acredita ausencia de fallos ni una instalación probada.

## Stack y modelos

- **Stack:** Go, Makefile, go.mod, package.json
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [alibaba/open-code-review](https://github.com/alibaba/open-code-review)
- 🌐 Web: <https://open-codereview.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/alibaba/open-code-review/blob/284ff013f0705ae6cac4c8dfbffa2f2551886d56/README.md)
- [Fuente 2](https://github.com/alibaba/open-code-review/blob/284ff013f0705ae6cac4c8dfbffa2f2551886d56/skills/open-code-review-delegate/SKILL.md)
- [Fuente 3](https://github.com/alibaba/open-code-review/blob/284ff013f0705ae6cac4c8dfbffa2f2551886d56/pages/src/content/docs/en/telemetry.md)
- [Fuente 4](https://github.com/alibaba/open-code-review/blob/284ff013f0705ae6cac4c8dfbffa2f2551886d56/.github/SECURITY.md)
- [Fuente 5](https://github.com/alibaba/open-code-review/releases/tag/v1.14.1)
- [Fuente 6](https://github.com/alibaba/open-code-review/blob/main/LICENSE)
- [Fuente 7](https://github.com/alibaba/open-code-review/security/advisories/GHSA-wwg6-qfxw-xffj)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
