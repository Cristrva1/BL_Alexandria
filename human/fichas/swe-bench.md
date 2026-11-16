[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Calidad, seguridad y benchmarks de código

# 🛡️ SWE-bench

> Benchmark para evaluar si los modelos resuelven issues reales de GitHub.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.2k | MIT | Python | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El harness no necesita llamar un modelo para evaluar predicciones; generar parches y levantar contenedores sí puede consumir modelos y cómputo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El benchmark no demuestra que un agente resuelva cualquier issue real; usa el conjunto y la versión de tareas correspondientes |
| Coste | El coste depende del proveedor o la ruta. El harness no necesita llamar un modelo para evaluar predicciones; generar parches y levantar contenedores sí puede consumir modelos y cómputo |
| Equipo | Preparación según la ruta elegida. Python; Docker para evaluación; predicciones y tareas elegidas |

El benchmark no demuestra que un agente resuelva cualquier issue real; usa el conjunto y la versión de tareas correspondientes

## Qué puedes hacer con él

Benchmark para evaluar si los modelos resuelven issues reales de GitHub.

## Por qué destaca

Usos propuestos: Comparar soluciones a issues reproducibles; Estudiar evaluación de agentes de programación.

## Cómo funciona

El benchmark no demuestra que un agente resuelva cualquier issue real; usa el conjunto y la versión de tareas correspondientes

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- Docker para evaluación
- predicciones y tareas elegidas

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone git@github.com:SWE-bench/SWE-bench.git
cd SWE-bench
pip install -e .
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SWE-bench para mi objetivo y necesito pasos guiados. Lee https://github.com/SWE-bench/SWE-bench/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Evalúa una predicción ya preparada sobre una tarea pequeña antes de generar nuevas soluciones.

**Qué comprobar:** El informe muestra si las pruebas del entorno aceptan el parche.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comparar soluciones a issues reproducibles
- Estudiar evaluación de agentes de programación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comparar soluciones a issues reproducibles; Estudiar evaluación de agentes de programación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El benchmark no demuestra que un agente resuelva cualquier issue real; usa el conjunto y la versión de tareas correspondientes

## Stack y modelos

- **Stack:** Python; Docker para evaluación; predicciones y tareas elegidas
- **Etiquetas:** `evaluation` `coding-agent` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [SWE-bench/SWE-bench](https://github.com/SWE-bench/SWE-bench)
- 🌐 Web: <https://www.swebench.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/SWE-bench/SWE-bench/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
