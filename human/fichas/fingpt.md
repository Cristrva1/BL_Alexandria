[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Agentes de investigación financiera

# 🧩 FinGPT

> Proyecto de LLM financieros abiertos de AI4Finance: modelos ajustados con LoRA, datos y recetas para análisis de sentimiento y tareas financieras.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 21.6k | MIT | Jupyter Notebook | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

**Puntuación de calidad** 54/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto de código abierto (MIT) de la AI4Finance Foundation, ligado a investigación académica. Activo, aunque gran parte del contenido son cuadernos y recetas.

## ¿Qué hace?

Ofrece LLM financieros ajustados (sentimiento, clasificación de titulares, reconocimiento de entidades, pronóstico), conjuntos de datos y benchmarks, y guías para entrenar con LoRA a bajo coste. Permite usar los modelos en local con GPU o mediante APIs en la nube.

## ¿Cómo lo hace?

Código en Python y cuadernos Jupyter; se instala con `pip install -r requirements.txt` o `pip install -e .` siguiendo SETUP.md. Usa Transformers y PEFT; la inferencia local requiere GPU según el modelo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Transformers](transformers.md) | Los modelos FinGPT se cargan y ajustan con Hugging Face Transformers. | Instala transformers y descarga el modelo base y el adaptador del Hub. |
| [PEFT](peft.md) | FinGPT entrena sus variantes con LoRA mediante PEFT. | Instala peft; después carga el adaptador LoRA de FinGPT sobre el modelo base. |
| [PyTorch](pytorch.md) | El entrenamiento y la inferencia local de FinGPT se ejecutan sobre PyTorch con GPU. | Instala PyTorch con CUDA; después las dependencias del proyecto. |

**Notas:** Los resultados de benchmarks del README corresponden a configuraciones concretas; verifica antes de usar en decisiones.

Estado en GitHub: activo · último push 2026-10-25 · última versión publicada v1.0.0 (2026-04-08) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/AI4Finance-Foundation/FinGPT/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos. |
| Coste | El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista. |
| Equipo | Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida.

1. Elige un ejemplo de consulta de datos, backtesting o simulación que no envíe órdenes reales.
2. Prepara datos de prueba y, si el proveedor lo requiere, una cuenta y credenciales de solo lectura; revisa sus cuotas por separado.
3. Comprueba los resultados y el coste observado. La ejecución con fondos es otra configuración y no se activa como parte de esta primera prueba.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/AI4Finance-Foundation/FinGPT/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FinGPT para mi objetivo y necesito pasos guiados. Lee https://github.com/AI4Finance-Foundation/FinGPT/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el SETUP del repositorio y ejecuta el ejemplo de análisis de sentimiento con la ruta por API o un modelo local pequeño..

**Qué comprobar:** El script devuelve etiquetas de sentimiento para frases financieras de ejemplo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- clasificar el sentimiento de noticias financieras con un modelo ajustado
- reproducir un ajuste LoRA barato sobre datos financieros para investigación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: clasificar el sentimiento de noticias financieras con un modelo ajustado; reproducir un ajuste LoRA barato sobre datos financieros para investigación | no tienes el hardware o no aceptas la licencia de los pesos |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. No se verificó rentabilidad ni operación con fondos. Herramienta de investigación: no constituye asesoramiento financiero ni garantiza resultados. Los modelos base tienen licencias propias.

## Stack y modelos

- **Stack:** Jupyter Notebook, requirements.txt, setup.py
- **Etiquetas:** `finanzas` `python` `model` `training`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [AI4Finance-Foundation/FinGPT](https://github.com/AI4Finance-Foundation/FinGPT)
- 🌐 Web: <https://fingpt.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/AI4Finance-Foundation/FinGPT/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
