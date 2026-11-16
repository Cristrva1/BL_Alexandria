[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Agentes de investigación financiera

# 📚 daily_stock_analysis

> Sistema que analiza acciones de varios mercados con LLM y envía un tablero de decisiones diario.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 72.3k | MIT | Python | 2026-06-24 |

**Ejecución** ☁️ cloud/API · **Rol** 🖥️ app · **Setup** 🟡 medio

**Puntuación de calidad** 78/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Sistema de análisis inteligente de acciones con LLM (股票智能分析系统), de @ZhuLinsen. Licencia MIT. Es muy popular (~73k estrellas, v3.34.0) y su README, principalmente en chino, incluye patrocinios de proveedores de modelos.

## ¿Qué hace?

Analiza cada día una lista de acciones de los mercados A, Hong Kong, EE. UU., Japón, Corea y Taiwán y envía un «panel de decisión» por WeCom, Feishu, Telegram, Discord, Slack o email. Combina datos de mercado, noticias e indicadores con un LLM.

## ¿Cómo lo hace?

Se ejecuta con GitHub Actions (sin servidor), Docker, tareas programadas locales o un servicio FastAPI, instalando con `pip install -r requirements.txt`. Usa cualquier API compatible con OpenAI (DeepSeek, Qwen…) y Ollama para despliegues locales o en Docker.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Modelos locales recomendados para despliegues locales o Docker. | Arranca Ollama y configura su URL. |
| [activepieces](activepieces.md) | Encadenar el informe con otros flujos o avisos. (combinación por arquitectura) | Recibe el informe por webhook o email en Activepieces. |
| [litellm](litellm.md) | Centralizar proveedores compatibles con OpenAI. (combinación por arquitectura) | Apunta `OPENAI_API_KEY`/base URL al proxy LiteLLM. |

**Notas:** Sin alternativas declaradas. Riesgo financiero: no es asesoramiento de inversión.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v3.34.0 (2026-11-09) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Ollama sirve para despliegue local; Actions normalmente usa API Cloud; datos, modelos y notificaciones tienen condiciones propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El panel generado no verifica por sí solo la exactitud financiera; una ejecución programada necesita infraestructura aunque tenga cupo gratuito |
| Coste | El coste depende del proveedor o la ruta. Ollama sirve para despliegue local; Actions normalmente usa API Cloud; datos, modelos y notificaciones tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Python; proveedor LLM u Ollama; fuentes de datos; notificaciones solo si las configuras |

El panel generado no verifica por sí solo la exactitud financiera; una ejecución programada necesita infraestructura aunque tenga cupo gratuito

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- proveedor LLM u Ollama
- fuentes de datos
- notificaciones solo si las configuras

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# 克隆项目
git clone https://github.com/ZhuLinsen/daily_stock_analysis.git && cd daily_stock_analysis

# 安装依赖
pip install -r requirements.txt
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar daily_stock_analysis para mi objetivo y necesito pasos guiados. Lee https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Analiza un símbolo de ejemplo sin activar envíos y contrasta fechas y datos del informe.

**Qué comprobar:** Puedes separar precios observados, fuentes y texto generado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un resumen de investigación
- Comparar noticias y datos de una lista de seguimiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un resumen de investigación; Comparar noticias y datos de una lista de seguimiento | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El panel generado no verifica por sí solo la exactitud financiera; una ejecución programada necesita infraestructura aunque tenga cupo gratuito

## Stack y modelos

- **Stack:** Python; proveedor LLM u Ollama; fuentes de datos; notificaciones solo si las configuras
- **Etiquetas:** `analytics` `agents` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)
- 🌐 Web: <https://dsa.zhulinsen.tech>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
