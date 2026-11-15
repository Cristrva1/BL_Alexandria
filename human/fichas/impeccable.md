[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces](../categorias/09-dise-o-ui-frontend.md) › Skills de diseño para agentes

# 💎 impeccable

> Guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" de UI por IA) que empuja al agente hacia frontends con criterio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 110k | Apache-2.0 | Rust | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Ataca el patrón repetitivo de interfaces que "huelen" a IA.

## Por qué destaca

Ataca de forma deliberada el "AI slop" visual con reglas deterministas, un enfoque diferenciado frente a prompts genéricos de diseño. Su autor (pbakaus, ex Google) le da peso en la comunidad de diseño para agentes.

## Cómo funciona

Se instala como skill que añade comandos y detectores; itera la UI en el navegador y señala patrones delatores (Inter omnipresente, gradientes morados, sombras genéricas, etc.).

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y acceso activo a su modelo.

1. Elige el agente indicado en Acceso y costes.
2. Sigue la instalación para ese agente en el README; un catálogo puede contener varias skills independientes.
3. Prueba una tarea pequeña y revisa si activa conectores externos.

**Comando de entrada documentado:**

```shell
npx impeccable
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/pbakaus/impeccable/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar impeccable para mi objetivo y necesito pasos guiados. Lee https://github.com/pbakaus/impeccable/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Evitar Inter+gradientes morados en todo
- Iterar diseño en vivo en el navegador
- Auditar una UI generada antes de entregarla

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres frontends que no parezcan generados por IA | no generas UI con agentes |

## Stack y modelos

- **Stack:** Node (`npx impeccable`)
- **Etiquetas:** `skills` `design` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [taste-skill](taste-skill.md) | 116k | Skills "anti-slop" para producir frontends premium (layout, tipografía, motion y espaciado) más skills de generación de imagen para crear mood boards de referencia. |
| [ui-ux-pro-max-skill](ui-ux-pro-max-skill.md) | 150k | Conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para que las interfaces que genera dejen de verse a "plantilla". |

## Enlaces

- 🐙 GitHub: [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
- 🌐 Web: <https://impeccable.style>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/pbakaus/impeccable/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
