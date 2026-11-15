[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Simulación, evolución y debate entre modelos

# 🧬 openevolve

> Agente de codificación evolutivo que optimiza algoritmos por simulación genética.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.8k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Admite APIs y los CLI de Claude Code o Codex; cada ruta mantiene sus límites; la búsqueda repetida puede acumular consumo |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Es una implementación independiente de AlphaEvolve; una puntuación mejor solo vale para el evaluador definido |
| Coste | El coste depende del proveedor o la ruta. Admite APIs y los CLI de Claude Code o Codex; cada ruta mantiene sus límites; la búsqueda repetida puede acumular consumo |
| Equipo | Preparación según la ruta elegida. Python 3.10+; evaluador de calidad; API o CLI compatible autenticado |

Es una implementación independiente de AlphaEvolve; una puntuación mejor solo vale para el evaluador definido

## Qué puedes hacer con él

Agente de codificación evolutivo que optimiza algoritmos por simulación genética.

## Por qué destaca

Usos propuestos: Optimizar una función medible; Buscar mejores reglas de ordenación.

## Cómo funciona

Es una implementación independiente de AlphaEvolve; una puntuación mejor solo vale para el evaluador definido

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10+
- evaluador de calidad
- API o CLI compatible autenticado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/algorithmicsuperintelligence/openevolve.git
cd openevolve
pip install -e .
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/algorithmicsuperintelligence/openevolve/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar openevolve para mi objetivo y necesito pasos guiados. Lee https://github.com/algorithmicsuperintelligence/openevolve/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prueba la minimización de una función con pocas iteraciones y revisa cada candidato.

**Qué comprobar:** El evaluador permite comparar la puntuación inicial y la final.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Optimizar una función medible
- Buscar mejores reglas de ordenación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Optimizar una función medible; Buscar mejores reglas de ordenación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una implementación independiente de AlphaEvolve; una puntuación mejor solo vale para el evaluador definido

## Stack y modelos

- **Stack:** Python 3.10+; evaluador de calidad; API o CLI compatible autenticado
- **Etiquetas:** `automation` `agents` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [llm-council](llm-council.md) | 26.5k | "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. |

## Enlaces

- 🐙 GitHub: [algorithmicsuperintelligence/openevolve](https://github.com/algorithmicsuperintelligence/openevolve)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/algorithmicsuperintelligence/openevolve/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
