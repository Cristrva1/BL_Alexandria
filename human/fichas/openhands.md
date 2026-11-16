[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes para issues y tareas de ingeniería

# 🙌 OpenHands

> Agent Canvas: centro de sesiones autoalojado para OpenHands, Claude Code, Codex y agentes ACP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 93.5k | MIT | TypeScript | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Puntuación de calidad** 74/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

OpenHands, cuyo repo principal es ahora Agent Canvas, centro de control autoalojado para agentes de programación y automatizaciones. Licencia MIT. Es muy activo (~94k estrellas, v1.40.0).

## ¿Qué hace?

Ejecuta OpenHands, Claude Code, Codex, Gemini, OpenCode o cualquier agente compatible con ACP en backends locales, remotos o en la nube, y automatiza tareas recurrentes. Se apoya en el OpenHands Agent Server y en el SDK `software-agent-sdk`.

## ¿Cómo lo hace?

Se instala con `npm install -g @openhands/agent-canvas` o con Docker. Por defecto corre en local y puede ejecutar agentes en contenedores, máquinas virtuales o la nube.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente soportado en Agent Canvas. | Configura Claude Code como agente ACP. |
| [Codex CLI](codex.md) | Agente soportado en Agent Canvas. | Configura Codex como agente. |
| [sandbox](sandbox.md) | Aislar la ejecución de los agentes. (combinación por arquitectura) | Ejecuta los agentes en un backend aislado. |
| [ECC](ecc.md) | Configuración de agentes reutilizable. (combinación por arquitectura) | Aplica la configuración a los agentes que lances. |
| [SWE-bench](swe-bench.md) | Combinación recíproca: SWE-bench lo enlaza como «Evaluar agentes de programación sobre SWE-bench. (combinación por arquitectura)». | Orden indicado desde SWE-bench: Genera predicciones con el agente y evalúalas con el arnés. |

**Notas:** Alternativas (elige una): open-swe.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.40.0 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OpenHands/OpenHands/blob/main/README.md) · [2](https://docs.openhands.dev)</sub>

## Ver similares

Grupo **Agentes que resuelven issues de software**: OpenHands ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **OpenHands** (esta ficha) ⭐ recomendado | 74 | Si buscas esto: agent Canvas: centro de sesiones autoalojado para OpenHands, Claude Code, Codex y agentes ACP. |
| 2 | [Open SWE](open-swe.md) | 61 | Si buscas esto: robin, fábrica de cambios sobre Deep Agents que despliega con Managed Deep Agents y entrega propuestas revisables. |
| 3 | [mini-swe-agent](mini-swe-agent.md) | 52 | Si buscas esto: agente de ingeniería de software mínimo (unas 100 líneas) del equipo de SWE-bench y SWE-agent: solo usa bash y rinde alto en SWE-bench. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Canvas usa el proveedor o plan del agente y la infraestructura elegida; ejecutar localmente la interfaz no elimina la facturación del modelo |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El README actual presenta Agent Canvas con OpenHands, Claude Code, Codex y agentes ACP; la receta de Docker limita el puerto al equipo local |
| Coste | El coste depende del proveedor o la ruta. Canvas usa el proveedor o plan del agente y la infraestructura elegida; ejecutar localmente la interfaz no elimina la facturación del modelo |
| Equipo | Preparación según la ruta elegida. Node 24 o posterior; uv; repositorio de prueba; agente autenticado; Docker según backend |

El README actual presenta Agent Canvas con OpenHands, Claude Code, Codex y agentes ACP; la receta de Docker limita el puerto al equipo local

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node 24 o posterior
- uv
- repositorio de prueba
- agente autenticado
- Docker según backend

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
npm install -g @openhands/agent-canvas
agent-canvas
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/OpenHands/OpenHands/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenHands para mi objetivo y necesito pasos guiados. Lee https://github.com/OpenHands/OpenHands/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca Agent Canvas y crea una sesión que solo examine un proyecto de ejemplo.

**Qué comprobar:** Puedes reconocer agente, backend y permisos de la sesión.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Centralizar sesiones de agentes
- Preparar una automatización de ingeniería

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Centralizar sesiones de agentes; Preparar una automatización de ingeniería | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README actual presenta Agent Canvas con OpenHands, Claude Code, Codex y agentes ACP; la receta de Docker limita el puerto al equipo local

## Stack y modelos

- **Stack:** Node 24 o posterior; uv; repositorio de prueba; agente autenticado; Docker según backend
- **Etiquetas:** `agents` `automation` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Open SWE](open-swe.md) | 11.2k | Robin, fábrica de cambios sobre Deep Agents que despliega con Managed Deep Agents y entrega propuestas revisables. |
| [mini-swe-agent](mini-swe-agent.md) | 9.6k | Agente de ingeniería de software mínimo (unas 100 líneas) del equipo de SWE-bench y SWE-agent: solo usa bash y rinde alto en SWE-bench. |

## Enlaces

- 🐙 GitHub: [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
- 🌐 Web: <https://openhands.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OpenHands/OpenHands/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
