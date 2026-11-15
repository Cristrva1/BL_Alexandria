[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 🛡️ Semgrep

> Análisis estático ligero para muchos lenguajes con reglas que se parecen al código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.7k | LGPL-2.1 | C | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Encuentra bugs y vulnerabilidades con miles de reglas comunitarias o propias. Muy usado en CI de seguridad.

## Por qué destaca

Reglas fáciles de escribir y gran catálogo de seguridad.

## Cómo funciona

Compara patrones contra el AST de cada archivo y reporta coincidencias con contexto.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

**Comando de entrada documentado:**

```shell
pip install semgrep
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/semgrep/semgrep/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Semgrep para mi objetivo y necesito pasos guiados. Lee https://github.com/semgrep/semgrep/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Escanear seguridad en CI
- Reglas internas de código
- Auditar código generado por IA

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres análisis de seguridad en CI | solo quieres refactors estructurales; mira `ast-grep` |

**Limitaciones:** Algunas funciones (análisis entre archivos, IA) son de la versión comercial.

## Stack y modelos

- **Stack:** OCaml, Python
- **Etiquetas:** `security` `code`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Defending Code Reference Harness](defending-code-reference-harness.md) | 7.8k | Arnés de referencia de Anthropic con skills para modelar amenazas, escanear, priorizar y parchear vulnerabilidades. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ast-grep](ast-grep.md) | 16.6k | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. |

## Enlaces

- 🐙 GitHub: [semgrep/semgrep](https://github.com/semgrep/semgrep)
- 🌐 Web: <https://semgrep.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/semgrep/semgrep/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
