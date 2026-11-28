[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Modelos y backtesting cuantitativo

# 📚 nautilus_trader

> Motor de trading y backtesting con arquitectura orientada a eventos para investigar y desarrollar estrategias.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 31.5k | LGPL-3.0 | Rust | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 71/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

NautilusTrader, motor de trading y backtesting de alto rendimiento nativo en Rust con API de Python, de Nautech Systems. Licencia LGPL-3.0. Es muy activo (~32k estrellas, v1.231.0).

## ¿Qué hace?

Ofrece una arquitectura orientada a eventos con el mismo código para backtesting y trading en vivo, multi-activo y multi-venue. Se integra mediante adaptadores con exchanges cripto (CEX y DEX), brokers tradicionales y proveedores de datos. Las estrategias se pueden escribir en Python o íntegramente en Rust.

## ¿Cómo lo hace?

Se instala con `pip install -U nautilus_trader` (estable) o con `--pre` para la rama 2.0, también desde su índice propio de paquetes. El núcleo está en Rust con bindings para Python 3.13–3.15 y Rust 1.100+.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Polars](polars.md) | Preparar grandes volúmenes de datos de mercado. (combinación por arquitectura) | Transforma los datos con Polars y cárgalos en el catálogo. |
| [marimo](marimo.md) | Analizar resultados de backtests en notebooks. (combinación por arquitectura) | Carga los informes en marimo. |
| [ccxt](ccxt.md) | Se pueden comparar fuentes de datos. La documentación revisada no acredita un adaptador CCXT directo para esa versión y mercado. | Contrasta versiones y fuentes de datos antes de reutilizar resultados. |
| [py-sdk](py-sdk.md) | Combinación recíproca: py-sdk lo enlaza como «NautilusTrader documenta una integración con Polymarket para backtesting y ejecución; usa los clientes de Polymarket, no necesariamente este SDK. (combinación por arquitectura)». | Orden indicado desde py-sdk: Elige uno como capa de ejecución; prueba primero en modo simulado. |

**Notas:** Sin alternativas declaradas. Curva de aprendizaje alta; la rama 2.0 aún es prerelease.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.231.0 (2026-08-02) · licencia declarada LGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/nautechsystems/nautilus_trader/blob/develop/README.md) · [2](https://nautilustrader.io/docs/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita LLM; datos, infraestructura y conectores tienen costes separados |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La rama y docs revisadas son v2 RC y piden --pre; sin él se instala v1 con otra API; el autor desaconseja RC para capital real |
| Coste | Sin pago a un modelo en la ruta básica. No necesita LLM; datos, infraestructura y conectores tienen costes separados |
| Equipo | Preparación según la ruta elegida. CPython 3.13–3.15 para wheels v2 revisadas; entorno virtual; datos de prueba |

La rama y docs revisadas son v2 RC y piden --pre; sin él se instala v1 con otra API; el autor desaconseja RC para capital real

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- CPython 3.13–3.15 para wheels v2 revisadas
- entorno virtual
- datos de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
pip install -U nautilus_trader --pre
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/nautechsystems/nautilus_trader/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar nautilus_trader para mi objetivo y necesito pasos guiados. Lee https://github.com/nautechsystems/nautilus_trader/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta un ejemplo de backtest de la misma versión v2 y revisa su secuencia de eventos.

**Qué comprobar:** Puedes reproducir órdenes y fills simulados con configuración fija.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar un motor orientado a eventos
- Comparar simulaciones con datos registrados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar un motor orientado a eventos; Comparar simulaciones con datos registrados | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La rama y docs revisadas son v2 RC y piden --pre; sin él se instala v1 con otra API; el autor desaconseja RC para capital real

## Stack y modelos

- **Stack:** CPython 3.13–3.15 para wheels v2 revisadas; entorno virtual; datos de prueba
- **Etiquetas:** `cuant` `framework` `rust`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [nautechsystems/nautilus_trader](https://github.com/nautechsystems/nautilus_trader)
- 🌐 Web: <https://nautilustrader.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/nautechsystems/nautilus_trader/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
