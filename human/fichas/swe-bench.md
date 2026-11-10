[🏠 Inicio](../README.md) › [🧑‍💻 Inteligencia de Código, Datos & Entrenamiento](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 🛡️ SWE-bench

> Benchmark para evaluar si los modelos resuelven issues reales de GitHub.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 6.2k | MIT | Python | 2026-09-18 | 📦 Sí |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🔴 pesado

## Qué es

Da al modelo un repositorio y un issue y comprueba si su parche pasa las pruebas. Es la referencia para medir agentes de código.

## Por qué destaca

Estándar de la industria para comparar agentes de programación.

## Cómo funciona

Ejecuta cada tarea en contenedores Docker y aplica los tests del repositorio al parche generado.

## Instalación rápida

`pip install swebench` (requiere Docker y mucho espacio en disco).

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
- **Modelos / API:** El modelo que evalúes.
- **Etiquetas:** `evaluation` `coding-agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SWE-agent](swe-agent.md) | 20.8k | Agente de Princeton y Stanford que toma un issue de GitHub e intenta resolverlo solo. |

## Enlaces

- 🐙 GitHub: [SWE-bench/SWE-bench](https://github.com/SWE-bench/SWE-bench)
- 🌐 Web: <https://www.swebench.com>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
