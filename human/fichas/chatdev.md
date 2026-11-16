[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Frameworks de agentes en Python

# 🖥️ ChatDev

> Plataforma multiagente sin código de OpenBMB: configura equipos de agentes por roles; la versión 1.0 simulaba una empresa de software.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 34.8k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Proyecto de investigación y plataforma de OpenBMB (Tsinghua) bajo Apache-2.0. ChatDev 2.0 (DevAll), publicada en enero de 2026, es una plataforma multiagente sin código; la versión 1.x, la «empresa de software virtual», se conserva en una rama legacy.

## ¿Qué hace?

Permite construir y ejecutar sistemas multiagente personalizados mediante configuración: roles, flujos y herramientas para tareas de desarrollo, análisis o generación de contenidos, incluida generación 3D con Blender. Acompaña artículos sobre colaboración multiagente (MacNet, co-aprendizaje experiencial, orquestación evolutiva).

## ¿Cómo lo hace?

Backend en Python y frontend web (npm); se ejecuta en local o con `docker compose up --build`. Requiere credenciales de un proveedor de modelos. Los flujos de ejemplo documentan dependencias externas, como Blender y blender-mcp para escenas 3D.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [blender](blender.md) | El flujo de generación 3D de ChatDev requiere Blender instalado. | Instala Blender y blender-mcp; después ejecuta el flujo 3D. |
| [Blender MCP](blender-mcp.md) | ChatDev documenta blender-mcp como requisito de su flujo de construcción 3D. | Blender primero, luego blender-mcp, y por último el flujo de ChatDev. |
| [litellm](litellm.md) | Un proxy LiteLLM compatible con OpenAI permite usar otros proveedores o modelos locales con ChatDev (combinación por arquitectura). | LiteLLM en marcha; después configura su URL como endpoint del modelo. |

**Notas:** El código generado por agentes debe revisarse antes de usarse; ejecútalo en contenedores.

Estado en GitHub: activo · último push 2026-11-06 · última versión publicada v2.2.0 (2026-03-23) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OpenBMB/ChatDev/blob/main/README.md) · [2](https://arxiv.org/abs/2307.07924)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Consumo de APIs o servicios. Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (consulta la sintaxis original):**

```
docker compose up --build
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/OpenBMB/ChatDev/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ChatDev para mi objetivo y necesito pasos guiados. Lee https://github.com/OpenBMB/ChatDev/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca la aplicación con `docker compose up --build`, configura una clave de modelo y ejecuta un flujo de ejemplo..

**Qué comprobar:** El flujo termina y muestra los mensajes entre agentes y el artefacto generado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- prototipar una pequeña aplicación con agentes que actúan como roles de un equipo
- estudiar patrones de colaboración multiagente de los artículos del proyecto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: prototipar una pequeña aplicación con agentes que actúan como roles de un equipo; estudiar patrones de colaboración multiagente de los artículos del proyecto | necesitas una herramienta estable y auditada para datos sensibles |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Python, Dockerfile, package.json, pyproject.toml, requirements.txt
- **Etiquetas:** `agents` `python` `research`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev)
- 🌐 Web: <https://arxiv.org/abs/2307.07924>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OpenBMB/ChatDev/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
