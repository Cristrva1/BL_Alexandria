[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 🖥️ ccusage

> Resume los tokens y estima el coste de tus sesiones de asistentes a partir de los registros locales de sus terminales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.5k | MIT | Rust | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 71/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Una utilidad de terminal para medir el uso registrado por asistentes de programación.

## ¿Qué hace?

Resume los tokens y estima el coste de tus sesiones de asistentes a partir de los registros locales de sus terminales.

## ¿Cómo lo hace?

Lee archivos locales de sesiones, agrupa tokens por asistente y periodo, y les aplica precios de referencia para estimar importes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Lee los registros de sesión que genera este asistente. | — |

Estado en GitHub: activo · último push 2026-11-22 · última versión publicada v20.0.51 (2026-11-14) · licencia declarada MIT (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ccusage/ccusage/blob/8fd41cd10e595cd4231a5627427d1725112ad718/README.md) · [2](https://ccusage.com/guide/installation) · [3](https://ccusage.com/guide/) · [4](https://www.npmjs.com/package/ccusage/v/20.0.51) · [5](https://github.com/ccusage/ccusage/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El informe usa registros existentes y no llama a un LLM. Puede consultar precios si no usas el modo offline. |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración documentada por el proyecto |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. El paquete es MIT. La estimación por tarifas no representa la factura, el saldo ni los límites de tu plan. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Compatibilidad como lector de registros locales de los tres clientes; no inicia sesión ni ejecuta modelos con su suscripción.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js y npm compatibles con la versión que elijas, u otro ejecutor indicado en la guía.
- Registros locales de al menos un cliente compatible; el modo offline requiere precios disponibles en caché.

1. Comprueba que el cliente que quieres medir ya generó sesiones y que la guía lo reconoce como fuente.
2. Elige el paquete oficial en la guía. Para la primera revisión limita el informe a un cliente y usa datos de precios en caché si quieres trabajar sin red.
3. Compara tokens por día y valida facturación o cuotas en el proveedor, no en la estimación de ccusage.

**Entrada documentada (consulta la sintaxis original):**

```
npx ccusage@latest
```

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://ccusage.com/guide/installation)

[Abrir la web o descarga indicada por el autor](https://ccusage.com/guide/installation)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ccusage para mi objetivo y necesito pasos guiados. Lee https://ccusage.com/guide/installation. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Usa la ruta oficial de instalación, abre el informe diario de un cliente con actividad previa y fíjate en el periodo..

**Qué comprobar:** Aparece una tabla de tokens por día para ese cliente; la cifra de coste es una estimación..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Identificar el día con más tokens en Claude Code.
- Comparar sesiones registradas por Codex y Antigravity sin confundir la estimación con cargos del plan.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Identificar el día con más tokens en Claude Code.; Comparar sesiones registradas por Codex y Antigravity sin confundir la estimación con cargos del plan. | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Puede leer registros de sesión. Usa un perfil de prueba para una primera revisión, un paquete de versión identificada y no publiques los registros. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Rust, package.json
- **Etiquetas:** `consumo` `tokens` `costos`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ccusage/ccusage](https://github.com/ccusage/ccusage)
- 🌐 Web: <https://ccusage.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ccusage/ccusage/blob/8fd41cd10e595cd4231a5627427d1725112ad718/README.md)
- [Fuente 2](https://ccusage.com/guide/installation)
- [Fuente 3](https://ccusage.com/guide/)
- [Fuente 4](https://www.npmjs.com/package/ccusage/v/20.0.51)
- [Fuente 5](https://github.com/ccusage/ccusage/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
