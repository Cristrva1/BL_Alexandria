[🏠 Inicio](../README.md) › [🤖 Automatizar negocios y comunicación](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Ecosistema n8n

# 🔁 Self-hosted AI Starter Kit

> Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.4k | Apache-2.0 | — | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La ruta de inferencia o entrenamiento local no necesita una API de IA alojada. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible. |
| Coste | Sin pago a un modelo en la ruta básica. La receta incluye Ollama y servicios locales. Las integraciones añadidas a n8n pueden introducir cuentas o APIs externas. |
| Equipo | Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Kit oficial de n8n que levanta un entorno de IA privado: n8n para orquestar, Ollama para modelos, Qdrant como base vectorial y PostgreSQL. Útil para prototipar agentes y RAG sin enviar datos fuera.

## Por qué destaca

Mantenido por el equipo de n8n; resuelve en un comando el cableado entre las piezas.

## Cómo funciona

Un `docker-compose.yml` con perfiles para CPU y GPU arranca los servicios ya conectados entre sí.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker y recursos para los contenedores y el modelo que elijas.

1. Abre la configuración de Docker Compose y el perfil de CPU o GPU del README.
2. Prepara las variables del ejemplo y descarga un modelo compatible en Ollama.
3. Comprueba un flujo mínimo de n8n y sus conexiones antes de añadir servicios externos.

[Instrucciones originales de instalación](https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Self-hosted AI Starter Kit para mi objetivo y necesito pasos guiados. Lee https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Chat con tus documentos en local
- Agentes de n8n con modelos privados
- Demo de IA sin nube

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres un stack de IA local funcionando hoy con n8n | vas a producción con alta carga; arma tu propio despliegue |

**Limitaciones:** Es un punto de partida, no un despliegue endurecido para producción.

## Stack y modelos

- **Stack:** Docker Compose, n8n, Ollama, Qdrant, PostgreSQL
- **Etiquetas:** `automation` `local` `rag` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |
| [Qdrant](qdrant.md) | 35.6k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |

## Enlaces

- 🐙 GitHub: [n8n-io/self-hosted-ai-starter-kit](https://github.com/n8n-io/self-hosted-ai-starter-kit)
- 🌐 Web: <https://n8n.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
