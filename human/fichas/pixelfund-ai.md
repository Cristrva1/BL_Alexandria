[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Ejemplos y aprendizaje

# 🖥️ PixelFund-AI

> Aplicación de simulación bursátil con agentes e interfaz en pixel art para explorar carteras y operaciones virtuales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6 | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

PixelFund AI, simulador bursátil en pixel art con agentes de IA especializados, de @kyjwang. Licencia MIT. Es una demo muy pequeña (~6 estrellas) con último cambio en junio de 2026.

## ¿Qué hace?

Ofrece una oficina pixel art, cotizaciones en tiempo real, cuentas de simulación aisladas por navegador y operaciones con cartera virtual asistidas por agentes.

## ¿Cómo lo hace?

Es una app web Node con API separada que requiere PostgreSQL y Redis (con Docker o en local).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [TradingAgents](tradingagents.md) | Lógica de análisis multiagente más completa. (combinación por arquitectura) | Integra sus decisiones en el simulador. |
| [dexter](dexter.md) | Investigación financiera para los agentes. (combinación por arquitectura) | Usa Dexter como fuente de análisis. |
| [Ollama](ollama.md) | Modelos locales para los agentes. (combinación por arquitectura) | Configura un endpoint local si la app lo permite. |

**Notas:** Sin alternativas declaradas. Pregunta de pertenencia al catálogo: demo con adopción mínima.

Estado en GitHub: activo · último push 2026-06-15 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/kyjwang/PixelFund-AI/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La interfaz no obliga a modelo; análisis necesita proveedor AI y datos Finnhub para ciertas funciones; consumo y cupos son externos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La guía y env.example distinguen proveedor AI y claves; no se confirma modelo local; autenticación de producción sigue entre tareas de endurecimiento |
| Coste | El coste depende del proveedor o la ruta. La interfaz no obliga a modelo; análisis necesita proveedor AI y datos Finnhub para ciertas funciones; consumo y cupos son externos |
| Equipo | Preparación según la ruta elegida. Node >=20; npm >=10; Docker o PostgreSQL y Redis; claves opcionales según función |

La guía y env.example distinguen proveedor AI y claves; no se confirma modelo local; autenticación de producción sigue entre tareas de endurecimiento

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node >=20
- npm >=10
- Docker o PostgreSQL y Redis
- claves opcionales según función

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
cp .env.example .env
npm install
npm run dev:all
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/kyjwang/PixelFund-AI/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PixelFund-AI para mi objetivo y necesito pasos guiados. Lee https://github.com/kyjwang/PixelFund-AI/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre System Console tras iniciar la app y revisa disponibilidad de base, Redis, datos y AI.

**Qué comprobar:** Puedes ver qué componentes están listos y cuáles impiden análisis u operaciones virtuales.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar una cartera virtual con ciclo de órdenes
- Prototipar una interfaz de comité de inversión

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar una cartera virtual con ciclo de órdenes; Prototipar una interfaz de comité de inversión | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La guía y env.example distinguen proveedor AI y claves; no se confirma modelo local; autenticación de producción sigue entre tareas de endurecimiento

## Stack y modelos

- **Stack:** Node >=20; npm >=10; Docker o PostgreSQL y Redis; claves opcionales según función
- **Etiquetas:** `aprender` `template` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [kyjwang/PixelFund-AI](https://github.com/kyjwang/PixelFund-AI)
- 🌐 Web: <https://pixelfund-ai.vercel.app>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/kyjwang/PixelFund-AI/blob/main/README.md)
- [Fuente 2](https://github.com/kyjwang/PixelFund-AI/blob/main/docs/SETUP.md)
- [Fuente 3](https://github.com/kyjwang/PixelFund-AI/blob/main/.env.example)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
