[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Ejemplos y aprendizaje

# 🖥️ pixel-hedge-fund

> Demostración de una oficina financiera en pixel art con interfaz de análisis y conexiones configurables a mercados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5 | — | Svelte | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Pixel Hedge Fund, «oficina viva» en pixel art de un fondo de los 90 hecha con SvelteKit, de @jaypolanco96. El repo no declara licencia. Es una demo muy pequeña (~5 estrellas).

## ¿Qué hace?

Representa una oficina de trading animada donde un escritorio de análisis técnico dirige el comportamiento de los personajes, con temas visuales y rutas que se conectan a la API de BloFin.

## ¿Cómo lo hace?

Se ejecuta con `npm install` y `npm run dev`. El README advierte de no exponer el servidor de desarrollo a la red si la máquina guarda `.env.local` o `.secrets/`, porque las rutas `/api/blofin/*` usan credenciales.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ccxt](ccxt.md) | Datos de mercado normalizados en lugar de una sola API. (combinación por arquitectura) | Sustituye las llamadas por CCXT. |
| [TradingAgents](tradingagents.md) | Lógica de decisión multiagente detrás de la escena. (combinación por arquitectura) | Conecta las decisiones a la oficina. |
| [Claude Code](claude-code.md) | Personalizar la demo con un agente. (combinación por arquitectura) | Pide cambios al agente en un entorno sin credenciales. |

**Notas:** Sin alternativas declaradas. Pregunta de pertenencia al catálogo: demo con adopción mínima y sin licencia.

Estado en GitHub: activo · último push 2026-10-08 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/jaypolanco96/pixel-hedge-fund/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita modelo para la interfaz; fuentes e infraestructura pueden tener costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La producción no usa el fallback SAMPLE de desarrollo; los errores o datos ausentes deben permanecer visibles |
| Coste | Sin pago a un modelo en la ruta básica. No necesita modelo para la interfaz; fuentes e infraestructura pueden tener costes |
| Equipo | Preparación según la ruta elegida. Node; SvelteKit; datos de prueba; conexión a fuentes si corresponde |

La producción no usa el fallback SAMPLE de desarrollo; los errores o datos ausentes deben permanecer visibles

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- SvelteKit
- datos de prueba
- conexión a fuentes si corresponde

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
cd pixel-hedge-fund   # repo root
npm install
npm run dev -- --port 5173
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/jaypolanco96/pixel-hedge-fund/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar pixel-hedge-fund para mi objetivo y necesito pasos guiados. Lee https://github.com/jaypolanco96/pixel-hedge-fund/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre la interfaz de desarrollo y comprueba si muestra SAMPLE o datos de un exchange.

**Qué comprobar:** Puedes reconocer el origen y la ausencia de datos sin confundirla con un precio cero.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar una interfaz financiera en pixel art
- Mostrar estados y movimientos de una simulación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar una interfaz financiera en pixel art; Mostrar estados y movimientos de una simulación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La producción no usa el fallback SAMPLE de desarrollo; los errores o datos ausentes deben permanecer visibles

## Stack y modelos

- **Stack:** Node; SvelteKit; datos de prueba; conexión a fuentes si corresponde
- **Etiquetas:** `aprender` `template` `svelte`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [jaypolanco96/pixel-hedge-fund](https://github.com/jaypolanco96/pixel-hedge-fund)
- 🌐 Web: <https://pixel-hf.vercel.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/jaypolanco96/pixel-hedge-fund/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
