[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Modelos y backtesting cuantitativo

# 📚 FinRL

> Biblioteca y ejemplos para investigar estrategias de trading mediante aprendizaje por refuerzo y simulaciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.1k | MIT | Jupyter Notebook | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🔴 pesado

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

FinRL, el framework open source de aprendizaje por refuerzo para finanzas, de AI4Finance Foundation. Licencia MIT; la marca FinRL pertenece a FinRL LLC. Es maduro (~17k estrellas, v0.3.8) y su sucesor orientado a producción es FinRL-X (repositorio FinRL-Trading).

## ¿Qué hace?

Ofrece un flujo educativo y de investigación completo: entornos de mercado, agentes de RL profundo (A2C, DDPG, PPO, TD3, SAC) y backtesting. Se apoya en librerías como Stable Baselines 3 y ElegantRL.

## ¿Cómo lo hace?

Se instala con `pip install -e .` desde el código. Para desarrollo nuevo o trading en vivo, el README recomienda FinRL-X.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [qlib](qlib.md) | Comparar con investigación cuantitativa basada en ML. (combinación por arquitectura) | Usa los mismos datos en ambos. |
| [machine-learning-for-trading](machine-learning-for-trading.md) | Base teórica y práctica complementaria. (combinación por arquitectura) | Estudia los capítulos de RL del libro. |
| [vectorbt](vectorbt.md) | Validar las políticas aprendidas con otro backtester. (combinación por arquitectura) | Exporta las señales a vectorbt. |

**Notas:** Sin alternativas declaradas. Uso académico: no es asesoramiento financiero.

Estado en GitHub: activo · último push 2026-11-03 · última versión publicada v0.3.8 (2026-03-20) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/AI4Finance-Foundation/FinRL/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El aprendizaje local no requiere API LLM; datos, entrenamiento y brokers tienen costes separados |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El autor enlaza FinRL-X como evolución; mantén versiones y documentación correspondientes a este repositorio |
| Coste | El coste depende del proveedor o la ruta. El aprendizaje local no requiere API LLM; datos, entrenamiento y brokers tienen costes separados |
| Equipo | Preparación según la ruta elegida. Python y dependencias de la guía; datos; entorno de entrenamiento |

El autor enlaza FinRL-X como evolución; mantén versiones y documentación correspondientes a este repositorio

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y dependencias de la guía
- datos
- entorno de entrenamiento

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/AI4Finance-Foundation/FinRL.git
cd FinRL

pip install -e .
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/AI4Finance-Foundation/FinRL/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FinRL para mi objetivo y necesito pasos guiados. Lee https://github.com/AI4Finance-Foundation/FinRL/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta un ejemplo pequeño de aprendizaje por refuerzo y evalúa en un periodo distinto.

**Qué comprobar:** Puedes contrastar recompensas, operaciones simuladas y datos de prueba.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar entornos de RL financiero
- Comparar políticas en simulación histórica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar entornos de RL financiero; Comparar políticas en simulación histórica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El autor enlaza FinRL-X como evolución; mantén versiones y documentación correspondientes a este repositorio

## Stack y modelos

- **Stack:** Python y dependencias de la guía; datos; entorno de entrenamiento
- **Etiquetas:** `cuant` `framework` `jupyter-notebook`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [AI4Finance-Foundation/FinRL](https://github.com/AI4Finance-Foundation/FinRL)
- 🌐 Web: <https://finrl.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/AI4Finance-Foundation/FinRL/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
