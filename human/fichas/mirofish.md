[🏠 Inicio](../README.md) › [🕸️ Frameworks & Orquestación de Agentes](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Simulación, evolución y debate entre modelos

# 🐟 MiroFish

> Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios.

| ⭐ Estrellas | Licencia | Lenguaje | Última actividad | En tu biblioteca local |
|---|---|---|---|---|
| 85.1k | AGPL-3.0 | Python | 2026-10-16 | 📦 Sí |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Qué es

Permite simular dinámicas sociales en un "sandbox". Proyecto de nicho.

## Por qué destaca

Simula futuros con agentes que tienen personalidad, memoria y lógica que evolucionan, ofreciendo una "vista de dios" del escenario. El enfoque de simulación multiagente lo distingue de los frameworks orientados a tareas.

## Cómo funciona

Según lo descrito, instancia muchos agentes con perfiles y memoria que interactúan en un mundo simulado para estimar resultados; pila Python/web con persistencia.

## Instalación rápida

Consulta el README del repo (`git clone` y ejecución en Python). Requiere claves de LLM para los agentes y cómputo no trivial para simulaciones grandes (de ahí el setup 🔴).

## Casos de uso

- Simular impacto de una noticia/política
- Predecir tendencias en un "sandbox" social
- What-if sobre escenarios con muchos actores

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| simulas futuros/escenarios con muchos actores | necesitas tareas deterministas o resultados reproducibles |

**Limitaciones:** Proyecto de nicho, coste de LLM alto por la cantidad de agentes y resultados no deterministas.

## Stack y modelos

- **Stack:** Python/web, Docker, PostgreSQL
- **Modelos / API:** Múltiples; agnóstico vía variables de entorno.
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [openevolve](openevolve.md) | 7.8k | Agente de codificación evolutivo que optimiza algoritmos por simulación genética. |

## Enlaces

- 🐙 GitHub: [666ghj/MiroFish](https://github.com/666ghj/MiroFish)
- 🌐 Web: <https://mirofish.ai>

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
