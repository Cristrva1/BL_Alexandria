[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Modelos y backtesting cuantitativo

# 📊 qlib

> Plataforma de Microsoft para investigación cuantitativa con datos, modelos y evaluación de estrategias.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 50.3k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Qlib, plataforma de investigación cuantitativa orientada a IA de Microsoft. Licencia MIT. Es madura (~50k estrellas, v0.9.8).

## ¿Qué hace?

Cubre todo el flujo cuantitativo: datos, factores, modelos (desde GBDT hasta redes profundas y RL), backtesting y análisis, con un gestor de experimentos. Se complementa con RD-Agent, de Microsoft, para minar factores y optimizar modelos con LLM. La rama principal introduce un cambio incompatible que restringe la carga de artefactos guardados.

## ¿Cómo lo hace?

Se instala con `pip install pyqlib` o desde el código (requiere NumPy y Cython), y también con Docker. El gestor de experimentos usa MLflow. En Mac M1 puede requerir OpenMP para LightGBM.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [MLflow](mlflow.md) | El recorder de Qlib se basa en MLflow. | Configura el URI de MLflow para los experimentos. |
| [FinRL](finrl.md) | Comparar enfoques de aprendizaje por refuerzo. (combinación por arquitectura) | Usa ambos sobre los mismos datos. |
| [marimo](marimo.md) | Analizar resultados en notebooks. (combinación por arquitectura) | Carga los informes de Qlib en marimo. |
| [FinceptTerminal](finceptterminal.md) | Combinación recíproca: FinceptTerminal lo enlaza como «Investigación cuantitativa más profunda fuera del terminal. (combinación por arquitectura)». | Orden indicado desde FinceptTerminal: Exporta datos y modela con Qlib. |
| [machine-learning-for-trading](machine-learning-for-trading.md) | Combinación recíproca: machine-learning-for-trading lo enlaza como «Plataforma cuantitativa para aplicar lo aprendido. (combinación por arquitectura)». | Orden indicado desde machine-learning-for-trading: Reproduce un caso de estudio en Qlib. |

**Notas:** Sin alternativas declaradas. Revisa la guía de migración de artefactos antes de actualizar desde el código.

Estado en GitHub: activo · último push 2026-11-04 · última versión publicada v0.9.8 (2026-10-08) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/microsoft/qlib/blob/main/README.md) · [2](https://qlib.readthedocs.io/en/latest/component/recorder.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El núcleo ML no exige LLM; datos licenciados, cómputo y automatización externa pueden costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Los baselines no comparten siempre versiones de Python; los cambios recientes del recorder requieren revisar la migración |
| Coste | El coste depende del proveedor o la ruta. El núcleo ML no exige LLM; datos licenciados, cómputo y automatización externa pueden costar |
| Equipo | Preparación según la ruta elegida. Python compatible con baseline; datos históricos; dependencias del modelo |

Los baselines no comparten siempre versiones de Python; los cambios recientes del recorder requieren revisar la migración

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python compatible con baseline
- datos históricos
- dependencias del modelo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install pyqlib
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/microsoft/qlib/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar qlib para mi objetivo y necesito pasos guiados. Lee https://github.com/microsoft/qlib/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta una baseline pequeña sobre un periodo de prueba separado y revisa predicciones y evaluación.

**Qué comprobar:** Puedes reproducir resultados sin mezclar datos futuros.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comparar modelos sobre datos temporales
- Investigar un pipeline cuantitativo reproducible

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comparar modelos sobre datos temporales; Investigar un pipeline cuantitativo reproducible | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los baselines no comparten siempre versiones de Python; los cambios recientes del recorder requieren revisar la migración

## Stack y modelos

- **Stack:** Python compatible con baseline; datos históricos; dependencias del modelo
- **Etiquetas:** `finanzas` `algorithmic-trading` `auto-quant` `deep-learning` `finance` `fintech` `investment` `machine-learning`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [microsoft/qlib](https://github.com/microsoft/qlib)
- 🌐 Web: <https://qlib.readthedocs.io/en/latest/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/microsoft/qlib/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
