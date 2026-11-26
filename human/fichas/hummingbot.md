[🏠 Inicio](../README.md) › [📈 Investigar finanzas y mercados](../categorias/14-investigar-finanzas-y-mercados.md) › Bots y conexiones a exchanges

# 🖥️ hummingbot

> Software para desarrollar y ejecutar bots de trading de criptomonedas mediante conectores y estrategias configurables.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 21.2k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 69/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Hummingbot, framework open source para diseñar y ejecutar bots de trading en exchanges centralizados y descentralizados. Licencia Apache-2.0. Es maduro (~21k estrellas, v2.17.0) y recibe patrocinio de exchanges mediante acuerdos de broker.

## ¿Qué hace?

Ofrece estrategias de market making, arbitraje y otras, con conectores para muchos CEX y DEX. Se controla con la CLI `hbot` (no interactiva, para automatizar) o la interfaz clásica, y se complementa con Condor, un arnés de IA para estrategias agénticas.

## ¿Cómo lo hace?

Se instala desde el código con Anaconda o Miniconda, o con Docker Compose. Está escrito en Python y Cython.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ccxt](ccxt.md) | Contrastar datos de exchanges no cubiertos por conectores propios. (combinación por arquitectura) | Usa CCXT en scripts de análisis aparte. |
| [Claude Code](claude-code.md) | Automatizar la operación con la CLI `hbot`, pensada para uso no interactivo. (combinación por arquitectura) | Permite al agente ejecutar `hbot` con límites. |
| [Grafana](grafana.md) | Monitorizar bots en ejecución. (combinación por arquitectura) | Exporta métricas y crea paneles. |

**Notas:** Sin alternativas declaradas. Riesgo financiero alto; los patrocinios de exchanges pueden sesgar la oferta de conectores.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v2.17.0 (2026-09-22) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/hummingbot/hummingbot/blob/master/README.md) · [2](https://hummingbot.org)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere LLM; datos, red, servidores y operaciones reales pueden cobrar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El CLI y Gateway tienen papeles distintos; instalar el código no deja preparada una estrategia segura ni verificada |
| Coste | El coste depende del proveedor o la ruta. No requiere LLM; datos, red, servidores y operaciones reales pueden cobrar |
| Equipo | Preparación según la ruta elegida. Conda o Docker; dependencias de compilación; conector y estrategia de prueba |

El CLI y Gateway tienen papeles distintos; instalar el código no deja preparada una estrategia segura ni verificada

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Conda o Docker
- dependencias de compilación
- conector y estrategia de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
# Clone the repository
git clone https://github.com/hummingbot/hummingbot.git
cd hummingbot

# Create the conda environment, build extensions, and expose the `hbot` CLI
make install

# Activate the environment
conda activate hummingbot
hbot --help
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/hummingbot/hummingbot/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar hummingbot para mi objetivo y necesito pasos guiados. Lee https://github.com/hummingbot/hummingbot/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Comprueba la instalación con ayuda del CLI y configura una estrategia en paper trade según su guía.

**Qué comprobar:** Puedes distinguir ejecución simulada y conexiones reales.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar un conector de exchange
- Evaluar un bot en un entorno de práctica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar un conector de exchange; Evaluar un bot en un entorno de práctica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El CLI y Gateway tienen papeles distintos; instalar el código no deja preparada una estrategia segura ni verificada

## Stack y modelos

- **Stack:** Conda o Docker; dependencias de compilación; conector y estrategia de prueba
- **Etiquetas:** `bots` `app` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [hummingbot/hummingbot](https://github.com/hummingbot/hummingbot)
- 🌐 Web: <https://hummingbot.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/hummingbot/hummingbot/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
