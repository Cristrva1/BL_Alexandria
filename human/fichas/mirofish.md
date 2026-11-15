[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Simulación, evolución y debate entre modelos

# 🐟 MiroFish

> Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 85.6k | AGPL-3.0 | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Permite simular dinámicas sociales en un "sandbox". Proyecto de nicho.

## Por qué destaca

Simula futuros con agentes que tienen personalidad, memoria y lógica que evolucionan, ofreciendo una "vista de dios" del escenario. El enfoque de simulación multiagente lo distingue de los frameworks orientados a tareas.

## Cómo funciona

Según lo descrito, instancia muchos agentes con perfiles y memoria que interactúan en un mundo simulado para estimar resultados; pila Python/web con persistencia.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/666ghj/MiroFish/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MiroFish para mi objetivo y necesito pasos guiados. Lee https://github.com/666ghj/MiroFish/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

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
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [openevolve](openevolve.md) | 7.8k | Agente de codificación evolutivo que optimiza algoritmos por simulación genética. |

## Enlaces

- 🐙 GitHub: [666ghj/MiroFish](https://github.com/666ghj/MiroFish)
- 🌐 Web: <https://mirofish.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/666ghj/MiroFish/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
