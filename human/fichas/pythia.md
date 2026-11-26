[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Inteligencia de fuentes abiertas y mapas

# 📊 Pythia

> Plataforma local que reúne fuentes de actualidad y genera escenarios con motores de inteligencia y predicción.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.2k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado · **MCP** 🔌 sí

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 47/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

PYTHIA, plataforma local de predicción geopolítica de @jangles-byte que fusiona MiroFish (motor de predicción por inteligencia de enjambre) y Osiris (panel de inteligencia global). Licencia MIT. Es muy reciente (creado en junio de 2026, ~1.2k estrellas, sin releases).

## ¿Qué hace?

Vigila fuentes abiertas (conflictos, desastres naturales, mercados, desplazamientos, salud pública, sanciones, ciberseguridad) y genera escenarios con un enjambre de personas simuladas por LLM. Cada predicción queda registrada y un LLM juez la califica al vencer su horizonte. Expone una API y un servidor MCP para agentes.

## ¿Cómo lo hace?

Requiere Python 3.11+ con uv, Ollama con un modelo descargado y una copia de Osiris con el overlay de PYTHIA. Corre en local sin claves de API. Se añade a Claude Code con `claude mcp add pythia -- uv … run python -m engine.mcp`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [osiris](osiris.md) | Requisito: aporta el globo y las fuentes en vivo. | Instala Osiris y aplica el overlay de integración. |
| [MiroFish](mirofish.md) | Motor de predicción por enjambre integrado. | Viene integrado en PYTHIA. |
| [Ollama](ollama.md) | Modelos locales para cada persona del enjambre. | Arranca Ollama y descarga un modelo de chat. |
| [Claude Code](claude-code.md) | Servidor MCP documentado en el README. | Ejecuta `claude mcp add pythia …`. |
| [gods-eye-view](gods-eye-view.md) | Combinación recíproca: gods-eye-view lo enlaza como «Contrastar las predicciones de PYTHIA con las capas en vivo. (combinación por arquitectura)». | Orden indicado desde gods-eye-view: Usa ambos sobre la misma región. |

**Notas:** Sin alternativas declaradas. Las predicciones de LLM no son análisis de inteligencia verificados.

Estado en GitHub: activo · último push 2026-09-06 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/jangles-byte/Pythia/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El autor ofrece feeds sin claves y modelo local; eso consume hardware y depende de disponibilidad de fuentes |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. Las predicciones son resultados generados y no probabilidades verificadas; MCP stdio permite consultar el motor desde los clientes |
| Coste | Sin pago a un modelo en la ruta básica. El autor ofrece feeds sin claves y modelo local; eso consume hardware y depende de disponibilidad de fuentes |
| Equipo | Preparación según la ruta elegida. Ollama con modelo descargado; Python y uv; checkout Osiris; dependencias del script |

Las predicciones son resultados generados y no probabilidades verificadas; MCP stdio permite consultar el motor desde los clientes

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Ollama con modelo descargado
- Python y uv
- checkout Osiris
- dependencias del script

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/jangles-byte/Pythia && cd Pythia
cp .env.example .env          # sensible defaults — no keys needed
./run-all.sh                  # starts Osiris + the engine and opens the UI
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/jangles-byte/Pythia/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Pythia para mi objetivo y necesito pasos guiados. Lee https://github.com/jangles-byte/Pythia/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Consulta un resumen del estado observado y separa los eventos de los escenarios generados.

**Qué comprobar:** Cada evento tiene origen y los escenarios se identifican como hipótesis.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Resumir fuentes públicas con un LLM local
- Comparar escenarios sobre un conjunto de eventos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Resumir fuentes públicas con un LLM local; Comparar escenarios sobre un conjunto de eventos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las predicciones son resultados generados y no probabilidades verificadas; MCP stdio permite consultar el motor desde los clientes

## Stack y modelos

- **Stack:** Ollama con modelo descargado; Python y uv; checkout Osiris; dependencias del script
- **Etiquetas:** `osint` `typescript`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [jangles-byte/Pythia](https://github.com/jangles-byte/Pythia)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/jangles-byte/Pythia/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
