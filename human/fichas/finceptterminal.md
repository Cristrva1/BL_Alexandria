[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Agentes de investigación financiera

# 📊 FinceptTerminal

> Terminal de análisis financiero que reúne datos, investigación, paneles y herramientas de agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 33.8k | AGPL-3.0 | C++ | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🔴 pesado

## ¿Qué es?

Fincept Terminal, terminal nativo de escritorio para investigación financiera, de Fincept Corporation. Licencia AGPL-3.0 o posterior, con una edición Enterprise propietaria de pago. Es popular (~34k estrellas, v4.5.2).

## ¿Qué hace?

Reúne datos de mercado, investigación, paneles, carteras, análisis cuantitativo y 37 agentes de IA (traders, economía, geopolítica) con tu propia clave (OpenAI, Anthropic, Gemini, Groq, DeepSeek, OpenRouter, Ollama). Incluye un editor visual de nodos, herramientas MCP y un laboratorio de quant (ML, factores, RL).

## ¿Cómo lo hace?

Es un binario C++20 con interfaz Qt6 y Python 3.11 embebido, sin Electron; se descarga desde las releases. Cada fuente de datos tiene sus propias condiciones, que normalmente limitan su uso al personal.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor local soportado para los agentes. | Configura Ollama en los ajustes de IA. |
| [qlib](qlib.md) | Investigación cuantitativa más profunda fuera del terminal. (combinación por arquitectura) | Exporta datos y modela con Qlib. |
| [ccxt](ccxt.md) | Datos de cripto adicionales. (combinación por arquitectura) | Usa CCXT para fuentes no integradas. |

**Notas:** Sin alternativas declaradas. El README se centra en vender la edición Enterprise. Riesgo financiero: no es asesoramiento de inversión.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v4.5.2 (2026-11-09) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Tiene planes, créditos y edición Enterprise; BYOK y Ollama son rutas distintas; el instalador no incluye todos los datos y modelos |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Verifica los módulos y límites de tu edición; la marca y ciertos derechos comerciales tienen condiciones adicionales |
| Coste | El coste depende del proveedor o la ruta. Tiene planes, créditos y edición Enterprise; BYOK y Ollama son rutas distintas; el instalador no incluye todos los datos y modelos |
| Equipo | Preparación según la ruta elegida. Instalador oficial para tu sistema; cuenta o claves según módulo; datos de prueba |

Verifica los módulos y límites de tu edición; la marca y ciertos derechos comerciales tienen condiciones adicionales

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Instalador oficial para tu sistema
- cuenta o claves según módulo
- datos de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FinceptTerminal para mi objetivo y necesito pasos guiados. Lee https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre un panel de investigación y comprueba proveedor y hora de sus datos antes de activar AI.

**Qué comprobar:** Puedes distinguir datos observados y análisis generado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar indicadores de varios mercados
- Comparar información económica de fuentes distintas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar indicadores de varios mercados; Comparar información económica de fuentes distintas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Verifica los módulos y límites de tu edición; la marca y ciertos derechos comerciales tienen condiciones adicionales

## Stack y modelos

- **Stack:** Instalador oficial para tu sistema; cuenta o claves según módulo; datos de prueba
- **Etiquetas:** `finanzas` `ai-agents` `algorithmic-trading` `bloomberg-terminal` `cpp` `finance` `financial-markets` `fintech`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal)
- 🌐 Web: <https://fincept.in>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
