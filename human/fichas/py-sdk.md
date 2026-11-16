[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Bots y conexiones a exchanges

# 📚 py-sdk

> SDK Python de Polymarket para integrar funciones de su plataforma mediante las APIs y credenciales correspondientes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 154 | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 54/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

SDK oficial de Polymarket para Python (`polymarket-client`). Licencia MIT. Es reciente y pequeño (~150 estrellas, polymarket-client-v0.18.0).

## ¿Qué hace?

Ofrece una interfaz unificada para datos públicos, cuenta autenticada, trading, atribución de builders y operaciones de wallet en Polymarket, con clientes síncrono y asíncrono.

## ¿Cómo lo hace?

Se instala con `uv add polymarket-client` o `pip install polymarket-client`. Operar requiere wallet y credenciales; revisa si Polymarket está permitido en tu jurisdicción.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ccxt](ccxt.md) | CCXT también cubre mercados de predicción. (combinación por arquitectura) | Compara cobertura antes de elegir. |
| [nautilus_trader](nautilus-trader.md) | NautilusTrader documenta una integración con Polymarket para backtesting y ejecución; usa los clientes de Polymarket, no necesariamente este SDK. (combinación por arquitectura) | Elige uno como capa de ejecución; prueba primero en modo simulado. |
| [activepieces](activepieces.md) | Avisos de mercados o posiciones desde un flujo que llame a tu script. (combinación por arquitectura) | Levanta ambos servicios y crea el flujo en Activepieces con la pieza HTTP o un disparador Webhook. |

**Notas:** Sin alternativas declaradas. Riesgo financiero: no es asesoramiento de inversión.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada polymarket-client-v0.18.0 (2026-11-09) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Polymarket/py-sdk/blob/main/README.md) · [2](https://nautilustrader.io/docs/latest/integrations/polymarket/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita LLM; cuentas, red y operaciones de la plataforma tienen condiciones y posibles costes propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El paquete se llama polymarket-client; datos públicos y funciones autenticadas de cuenta o wallet tienen requisitos separados |
| Coste | El coste depende del proveedor o la ruta. No necesita LLM; cuentas, red y operaciones de la plataforma tienen condiciones y posibles costes propios |
| Equipo | Preparación según la ruta elegida. Python y uv o pip; API y permisos según función; consulta de datos públicos |

El paquete se llama polymarket-client; datos públicos y funciones autenticadas de cuenta o wallet tienen requisitos separados

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y uv o pip
- API y permisos según función
- consulta de datos públicos

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
uv add polymarket-client
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Polymarket/py-sdk/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar py-sdk para mi objetivo y necesito pasos guiados. Lee https://github.com/Polymarket/py-sdk/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Enumera datos públicos de un mercado y revisa su esquema sin autenticar una wallet.

**Qué comprobar:** Puedes contrastar identificadores y datos con la fuente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar la API pública de Polymarket
- Preparar una migración desde el cliente antiguo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar la API pública de Polymarket; Preparar una migración desde el cliente antiguo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El paquete se llama polymarket-client; datos públicos y funciones autenticadas de cuenta o wallet tienen requisitos separados

## Stack y modelos

- **Stack:** Python y uv o pip; API y permisos según función; consulta de datos públicos
- **Etiquetas:** `bots` `library` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Polymarket/py-sdk](https://github.com/Polymarket/py-sdk)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Polymarket/py-sdk/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
