[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Navegadores y servidores de ejecución

# 🧩 Kitesurf

> Explora un motor experimental para renderizar páginas en Workers y obtener capturas desde código o herramientas compatibles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.6k | Apache-2.0 | TypeScript | 2026-11-22 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 57/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Explora un motor experimental para renderizar páginas en Workers y obtener capturas desde código o herramientas compatibles.

## ¿Qué hace?

Explora un motor experimental para renderizar páginas en Workers y obtener capturas desde código o herramientas compatibles.

## ¿Cómo lo hace?

El motor renderiza páginas en un entorno experimental, con rutas separadas para la prueba local y Workers.

Estado en GitHub: activo · último push 2026-11-22 · licencia declarada Apache-2.0 (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/cloudflare/kitesurf/blob/9295cc263b0a74fb17048462504c16bdcf363589/README.md) · [2](https://kitesurf.dev/) · [3](https://github.com/cloudflare/kitesurf/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La primera prueba descrita no llama a un modelo generativo ni exige una clave de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso. |
| Coste | El coste depende del proveedor o la ruta. La demo local consume equipo; el uso hospedado de Dynamic Workers depende de Cloudflare Workers Paid. |
| Equipo | Memoria y GPU según el modelo. Contenedor local para el ejemplo o Cloudflare Workers con los servicios que indique su guía. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Contenedor local para el ejemplo o Cloudflare Workers con los servicios que indique su guía.

1. Elige la sección Run with Docker de la guía para una prueba solo local y conserva la dirección de escucha en loopback.
2. Usa el ejemplo local enlazado y abre una página de prueba sin cuentas ni cookies.
3. Comprueba el resultado: se obtiene una captura o HTML del ejemplo y puedes compararlo con tu navegador.

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://kitesurf.dev/)

[Abrir la web o descarga indicada por el autor](https://kitesurf.dev/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Kitesurf para mi objetivo y necesito pasos guiados. Lee https://kitesurf.dev/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Usa el ejemplo local enlazado y abre una página de prueba sin cuentas ni cookies..

**Qué comprobar:** Se obtiene una captura o HTML del ejemplo y puedes compararlo con tu navegador..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Capturar una página estática de prueba.
- Comparar cómo se renderiza un componente en un entorno aislado.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Capturar una página estática de prueba.; Comparar cómo se renderiza un componente en un entorno aislado. | no quieres preparar modelos, dependencias y hardware propios |

**Limitaciones:** El motor es experimental. Workers y Dynamic Workers pueden requerir planes de Cloudflare; la demo local no exige cuenta. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** TypeScript, Cargo.toml, package.json
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [cloudflare/kitesurf](https://github.com/cloudflare/kitesurf)
- 🌐 Web: <https://kitesurf.dev/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cloudflare/kitesurf/blob/9295cc263b0a74fb17048462504c16bdcf363589/README.md)
- [Fuente 2](https://kitesurf.dev/)
- [Fuente 3](https://github.com/cloudflare/kitesurf/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
