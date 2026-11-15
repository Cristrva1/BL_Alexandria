[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 🛡️ SWE-bench

> Benchmark para evaluar si los modelos resuelven issues reales de GitHub.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.2k | MIT | Python | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo. |
| Coste | Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Da al modelo un repositorio y un issue y comprueba si su parche pasa las pruebas. Es la referencia para medir agentes de código.

## Por qué destaca

Estándar de la industria para comparar agentes de programación.

## Cómo funciona

Ejecuta cada tarea en contenedores Docker y aplica los tests del repositorio al parche generado.

## Cómo empezar

Material para leer. [Entender los términos](../vocabulario.md).

1. Abre el material original y elige un capítulo o ejemplo.
2. Revisa los requisitos de ese ejemplo antes de instalar dependencias.
3. Usa las alternativas y recetas para situarlo dentro de tu proyecto.

[Instrucciones originales de instalación](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SWE-bench para mi objetivo y necesito pasos guiados. Lee https://github.com/SWE-bench/SWE-bench/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Evaluar un agente de código propio
- Comparar modelos
- Investigación en agentes de software

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| necesitas medir agentes de código con un estándar | solo quieres usar un agente |

## Stack y modelos

- **Stack:** Python, Docker
- **Etiquetas:** `evaluation` `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SWE-agent](swe-agent.md) | 20.8k | Agente de Princeton y Stanford que toma un issue de GitHub e intenta resolverlo solo. |

## Enlaces

- 🐙 GitHub: [SWE-bench/SWE-bench](https://github.com/SWE-bench/SWE-bench)
- 🌐 Web: <https://www.swebench.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
