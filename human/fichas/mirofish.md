[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Simulación, evolución y debate entre modelos

# 🐟 MiroFish

> Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 85.6k | AGPL-3.0 | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

Motor de 'inteligencia colectiva' (AGPL-3.0) de 666ghj para predecir escenarios simulando sociedades de agentes. Su motor de simulación es OASIS, de CAMEL-AI. Es experimental (v0.1.2 de marzo de 2026; último push en octubre de 2026), pese a sus ~86k estrellas.

## ¿Qué hace?

Parte de material semilla (noticias, borradores de políticas, señales financieras o incluso novelas) y de una petición en lenguaje natural. Construye un grafo de conocimiento (GraphRAG) con memoria individual y colectiva, genera miles de agentes con personalidad y simula su interacción. Devuelve un informe de predicción y un 'mundo digital' con el que se puede interactuar. La validez predictiva de estas simulaciones no está demostrada [DATO NO VERIFICADO: no se encontró evaluación independiente].

## ¿Cómo lo hace?

El backend está en Python (3.11–3.12, con uv) y el frontend en Node.js 18+. También hay despliegue con Docker. Necesita una API de LLM compatible con el SDK de OpenAI (recomiendan qwen-plus de Alibaba Bailian) y una clave de Zep Cloud para la memoria en grafo. Las simulaciones grandes consumen muchas llamadas al LLM, así que conviene vigilar el coste.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Graphiti](graphiti.md) | Motor open source de grafos temporales de Zep; podría sustituir o complementar Zep Cloud para no depender del servicio. (combinación por arquitectura: MiroFish solo documenta Zep Cloud) | Requiere adaptar el código; evalúalo solo si necesitas autoalojar la memoria. |
| [litellm](litellm.md) | Proxy compatible con OpenAI para usar cualquier proveedor o modelo local mediante `LLM_BASE_URL`. (combinación por arquitectura) | Arranca el proxy de LiteLLM y apunta las variables LLM_* de MiroFish a él. |
| [Ollama](ollama.md) | Modelos locales para reducir el coste de simulaciones masivas vía endpoint compatible con OpenAI. (combinación por arquitectura; la calidad con modelos pequeños no está verificada) | Instala Ollama y apunta LLM_BASE_URL a su API /v1. |

**Notas:** Sin alternativas declaradas. Combinación anterior con openevolve eliminada: sin relación técnica documentada. Licencia AGPL-3.0: ofrecerlo como servicio en red obliga a publicar las modificaciones.

Estado en GitHub: activo · último push 2026-10-16 · última versión publicada v0.1.2 (2026-03-07) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/666ghj/MiroFish/blob/main/README.md) · [2](https://github.com/camel-ai/oasis)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta documentada usa API compatible OpenAI y Zep; muchas rondas multiplican consumo; los cupos gratuitos pueden cambiar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Son simulaciones generadas, no predicciones validadas del mercado ni evidencia de cómo actuarán personas reales |
| Coste | Consumo de APIs o servicios. La ruta documentada usa API compatible OpenAI y Zep; muchas rondas multiplican consumo; los cupos gratuitos pueden cambiar |
| Equipo | Preparación según la ruta elegida. Docker o Node 18+ y Python 3.11–3.12; clave LLM; Zep Cloud |

Son simulaciones generadas, no predicciones validadas del mercado ni evidencia de cómo actuarán personas reales

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o Node 18+ y Python 3.11–3.12
- clave LLM
- Zep Cloud

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# 1. Configure environment variables (same as source deployment)
cp .env.example .env

# 2. Pull image and start
docker compose up -d
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/666ghj/MiroFish/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MiroFish para mi objetivo y necesito pasos guiados. Lee https://github.com/666ghj/MiroFish/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga un escenario ficticio y realiza una simulación corta con menos de 40 rondas.

**Qué comprobar:** Puedes inspeccionar los agentes simulados y el informe del escenario.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar reacciones hipotéticas a un anuncio
- Comparar escenarios narrativos antes de investigar datos reales

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar reacciones hipotéticas a un anuncio; Comparar escenarios narrativos antes de investigar datos reales | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Son simulaciones generadas, no predicciones validadas del mercado ni evidencia de cómo actuarán personas reales

## Stack y modelos

- **Stack:** Docker o Node 18+ y Python 3.11–3.12; clave LLM; Zep Cloud
- **Etiquetas:** `agents` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [666ghj/MiroFish](https://github.com/666ghj/MiroFish)
- 🌐 Web: <https://mirofish.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/666ghj/MiroFish/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
