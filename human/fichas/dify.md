[🏠 Inicio](../README.md) › [🕸️ Crear y usar agentes de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Builders visuales y plataformas de agentes

# 🧱 dify

> Plataforma integral para construir apps de IA con backend y UI listos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 161k | NOASSERTION | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Combina orquestación de prompts, RAG, agentes, workflows y observabilidad en un mismo producto autoalojable.

## Por qué destaca

Todo-en-uno muy popular para llevar apps de IA a producción sin ensamblar piezas sueltas. Cubre desde el chatbot con RAG hasta workflows visuales y agentes, con gestión de usuarios y API propia.

## Cómo funciona

Define apps (chatbot, agente, workflow) desde un panel web; el backend en Python orquesta modelos y herramientas sobre PostgreSQL/Redis, y se despliega con Docker Compose.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/langgenius/dify/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dify para mi objetivo y necesito pasos guiados. Lee https://github.com/langgenius/dify/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Desplegar un chatbot/asistente con RAG
- Apps IA para clientes
- Workflows visuales con herramientas propias

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres una app IA completa autoalojada | solo necesitas una librería o un prototipo puntual |

## Stack y modelos

- **Stack:** Python/TS, React, PostgreSQL, Redis, Docker
- **Etiquetas:** `automation` `agents` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langflow](langflow.md) | 157k | Constructor visual de flujos LLM/agentes construido sobre LangChain. |
| [Flowise](flowise.md) | 55.6k | Constructor visual para diseñar aplicaciones de IA conectando modelos, herramientas, memoria y fuentes de datos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Sim](sim.md) | 30.1k | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. |
| [RAGFlow](ragflow.md) | 94.2k | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. |

## Enlaces

- 🐙 GitHub: [langgenius/dify](https://github.com/langgenius/dify)
- 🌐 Web: <https://dify.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/langgenius/dify/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
