[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Agentes de investigación financiera

# 🖥️ Vibe-Trading

> Agente de investigación y trabajo con estrategias de trading que utiliza modelos y componentes configurables.

## Cuándo elegir esta ficha

Conservar por research, replay/paper documentado y tareas de cuenta. Dexter cubre research y vectorbt simulación histórica por señales. Ambos pierden el flujo unificado. HEAD y release instalable pueden divergir.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/HKUDS/Vibe-Trading/blob/HEAD/README.md) · [Fuente 2](https://github.com/HKUDS/Vibe-Trading/commit/a7ea2328337ee435fc7c25c0378d130dd038b63b)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.2k | MIT | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Vibe-Trading, agente personal de investigación de trading de la organización HKUDS. Licencia MIT. Es muy activo (~38k estrellas, v0.1.19).

## ¿Qué hace?

Da a tu agente capacidades de investigación y trading: datos de mercado, skills de análisis, backtesting con costes y pruebas fuera de muestra, laboratorio de investigación, paper trading (incluidas sesiones de acciones A en pasos de cinco minutos) y una «cuenta sombra». Ofrece web, CLI, API y servidor MCP.

## ¿Cómo lo hace?

Se instala con `pip install vibe-trading-ai`, que incluye CLI, API y el servidor MCP `vibe-trading-mcp`. Hay app de escritorio con actualizaciones firmadas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Servidor MCP por stdio (`vibe-trading-mcp`). | Añade el servidor MCP y llama a `list_skills`. |
| [OpenClaw](openclaw.md) | Documentación de pruebas MCP con OpenClaw. | Configura el MCP en OpenClaw. |
| [vectorbt](vectorbt.md) | Contrastar los backtests con otro motor. (combinación por arquitectura) | Reproduce la estrategia en vectorbt. |

**Notas:** Sin alternativas declaradas. Riesgo financiero: no es asesoramiento de inversión.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.1.19 (2026-11-05) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/HKUDS/Vibe-Trading/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Modelos, fuentes y herramientas tienen costes por ruta; el paquete incluye MCP stdio; una ruta local requiere configuración adicional |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Las referencias Codex OAuth no garantizan todas las funciones de cada cuenta; usa la guía de proveedores y límites de la versión |
| Coste | El coste depende del proveedor o la ruta. Modelos, fuentes y herramientas tienen costes por ruta; el paquete incluye MCP stdio; una ruta local requiere configuración adicional |
| Equipo | Preparación según la ruta elegida. Python; proveedor o modelo local; fuente de datos; entorno de investigación |

Las referencias Codex OAuth no garantizan todas las funciones de cada cuenta; usa la guía de proveedores y límites de la versión

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- proveedor o modelo local
- fuente de datos
- entorno de investigación

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install vibe-trading-ai
vibe-trading init
vibe-trading
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/HKUDS/Vibe-Trading/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Vibe-Trading para mi objetivo y necesito pasos guiados. Lee https://github.com/HKUDS/Vibe-Trading/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Guarda una investigación histórica y repítela variando solo comisiones y deslizamiento.

**Qué comprobar:** Puedes comparar supuestos y resultados sin cambiar los datos de entrada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar sensibilidad de una estrategia
- Organizar artefactos de investigación reproducibles

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar sensibilidad de una estrategia; Organizar artefactos de investigación reproducibles | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las referencias Codex OAuth no garantizan todas las funciones de cada cuenta; usa la guía de proveedores y límites de la versión

## Stack y modelos

- **Stack:** Python; proveedor o modelo local; fuente de datos; entorno de investigación
- **Etiquetas:** `agentes` `agent` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading)
- 🌐 Web: <https://vibetrading.wiki/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/HKUDS/Vibe-Trading/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
