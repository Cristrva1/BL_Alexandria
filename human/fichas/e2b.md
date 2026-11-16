[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 🛠️ E2B

> Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.9k | Apache-2.0 | Python | 2026-11-10 |

**Ejecución** ☁️ cloud/API · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## ¿Qué es?

E2B, infraestructura open source para ejecutar código generado por IA en sandboxes aislados en la nube. Licencia Apache-2.0. Es maduro y activo (~15k estrellas).

## ¿Qué hace?

Crea sandboxes desde el SDK, ejecuta comandos y código (Code Interpreter) y ofrece escritorios virtuales para agentes de uso de ordenador (`e2b-desktop`).

## ¿Cómo lo hace?

Se instala con `npm i e2b` o `pip install e2b` y requiere `E2B_API_KEY` del servicio alojado. La infraestructura se puede autoalojar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [smolagents](smolagents.md) | Ejecutor remoto E2B soportado. | Configura el ejecutor E2B en el agente. |
| [Open SWE](open-swe.md) | Proveedor de sandbox posible. (combinación por arquitectura) | Configúralo como sandbox si tu despliegue lo admite. |
| [Gemini Computer Use (preview)](computer-use-preview.md) | Escritorio aislado para agentes de uso de ordenador. (combinación por arquitectura) | Ejecuta el navegador en `e2b-desktop`. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (4). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[claude-agent-sdk-python](claude-agent-sdk-python.md) · [claude-quickstarts](claude-quickstarts.md) · [MetaGPT](metagpt.md) · [Open Interpreter](open-interpreter.md)

**Notas:** Alternativas (elige una): sandbox.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada @e2b/cli@2.24.0 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/e2b-dev/E2B/blob/main/README.md) · [2](https://e2b.dev/docs/code-interpreting)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita API de IA para crear el entorno pero sí clave del servicio E2B; cómputo y tiempo del sandbox se facturan según plan |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Instalar el SDK no aloja todo E2B en tu equipo ni incluye un modelo de IA |
| Coste | Consumo de APIs o servicios. No necesita API de IA para crear el entorno pero sí clave del servicio E2B; cómputo y tiempo del sandbox se facturan según plan |
| Equipo | Preparación según la ruta elegida. Node o Python; cuenta E2B y clave; presupuesto de sandbox |

Instalar el SDK no aloja todo E2B en tu equipo ni incluye un modelo de IA

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node o Python
- cuenta E2B y clave
- presupuesto de sandbox

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (consulta la sintaxis original):**

```
npm i e2b
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/e2b-dev/E2B/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar E2B para mi objetivo y necesito pasos guiados. Lee https://github.com/e2b-dev/E2B/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un sandbox de prueba, ejecuta una operación de texto inocua y ciérralo.

**Qué comprobar:** Puedes revisar resultado y ciclo de vida del sandbox.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Ejecutar código aislado de una app
- Preparar un entorno temporal para un agente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Ejecutar código aislado de una app; Preparar un entorno temporal para un agente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Instalar el SDK no aloja todo E2B en tu equipo ni incluye un modelo de IA

## Stack y modelos

- **Stack:** Node o Python; cuenta E2B y clave; presupuesto de sandbox
- **Etiquetas:** `agents` `security` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [sandbox](sandbox.md) | 6.3k | Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. |

## Enlaces

- 🐙 GitHub: [e2b-dev/E2B](https://github.com/e2b-dev/E2B)
- 🌐 Web: <https://docs.e2b.dev/?utm_source=github&utm_medium=referral&utm_campaign=repo_website&utm_content=e2b>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/e2b-dev/E2B/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
