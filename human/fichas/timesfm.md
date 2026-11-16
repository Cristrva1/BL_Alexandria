[🏠 Inicio](../README.md) › [🧑‍💻 Modelos abiertos y entrenamiento](../categorias/24-modelos-entrenamiento.md) › Modelos abiertos y fundacionales

# 🧠 TimesFM

> Modelos preentrenados de Google para pronóstico de series temporales; las licencias de los pesos cambian por versión.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 35.5k | Apache-2.0 | Python | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

TimesFM, modelo fundacional preentrenado de Google Research para pronóstico de series temporales (artículo en ICML 2024). El código es Apache-2.0 y la licencia de los pesos cambia por versión. Tiene ~36k estrellas y su versión actual es TimesFM 3.0; el README aclara que esta versión abierta no es un producto oficial de Google.

## ¿Qué hace?

Hace pronósticos zero-shot de series temporales; TimesFM 3 añade pronóstico multivariante. Google también lo ofrece en BigQuery ML, Google Sheets (Connected Sheets) y Vertex Model Garden.

## ¿Cómo lo hace?

Se instala con pip y carga checkpoints desde Hugging Face (`google/timesfm-3.0-pytorch`; las versiones hasta 2.5 están en la colección). Funciona con PyTorch.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Polars](polars.md) | Preparar series antes de pronosticar. (combinación por arquitectura) | Carga y limpia los datos con Polars. |
| [DuckDB](duckdb.md) | Consultar históricos en SQL antes de pronosticar. (combinación por arquitectura) | Extrae las series con DuckDB. |
| [PyTorch](pytorch.md) | Backend del checkpoint PyTorch. | Instala PyTorch. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v3.0.0 (2026-08-28) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/google-research/timesfm/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Inferencia propia consume hardware; Cloud cobra por servicio; pesos 3.0 tienen restricciones no comerciales y no productivas |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Código y pesos hasta 2.5 son Apache; pesos 3.0 autoalojados no permiten uso comercial o productivo, que sí se ofrece mediante servicios Google autorizados |
| Coste | El coste depende del proveedor o la ruta. Inferencia propia consume hardware; Cloud cobra por servicio; pesos 3.0 tienen restricciones no comerciales y no productivas |
| Equipo | Preparación según la ruta elegida. Python; serie numérica ordenada; backend PyTorch o MLX; pesos permitidos |

Código y pesos hasta 2.5 son Apache; pesos 3.0 autoalojados no permiten uso comercial o productivo, que sí se ofrece mediante servicios Google autorizados

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python
- serie numérica ordenada
- backend PyTorch o MLX
- pesos permitidos

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
# Install TimesFM with PyTorch
pip install timesfm[torch]
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/google-research/timesfm/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar TimesFM para mi objetivo y necesito pasos guiados. Lee https://github.com/google-research/timesfm/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pronostica un tramo reservado de una serie de ejemplo y compáralo con datos que no diste al modelo.

**Qué comprobar:** Puedes medir error fuera de la muestra.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar demanda con series temporales
- Comparar un baseline de pronóstico

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar demanda con series temporales; Comparar un baseline de pronóstico | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Código y pesos hasta 2.5 son Apache; pesos 3.0 autoalojados no permiten uso comercial o productivo, que sí se ofrece mediante servicios Google autorizados

## Stack y modelos

- **Stack:** Python; serie numérica ordenada; backend PyTorch o MLX; pesos permitidos
- **Etiquetas:** `data` `analytics` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [google-research/timesfm](https://github.com/google-research/timesfm)
- 🌐 Web: <https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/google-research/timesfm/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
