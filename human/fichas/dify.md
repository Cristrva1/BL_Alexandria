[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Builders visuales y plataformas de agentes

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
| API de IA | Depende de la ruta elegida. Dify Cloud tiene planes y cupos; self-hosting paga infraestructura y modelos; su licencia añade condiciones a Apache-2.0 |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Genera y guarda el token de sandbox antes de arrancar; un modelo Ollama local necesita una dirección accesible desde Docker |
| Coste | El coste depende del proveedor o la ruta. Dify Cloud tiene planes y cupos; self-hosting paga infraestructura y modelos; su licencia añade condiciones a Apache-2.0 |
| Equipo | Preparación según la ruta elegida. Docker y Compose >=2.35; OpenSSL; 2 CPU y 4 GiB mínimos del servidor |

Genera y guarda el token de sandbox antes de arrancar; un modelo Ollama local necesita una dirección accesible desde Docker

## Qué puedes hacer con él

Plataforma integral para construir apps de IA con backend y UI listos.

## Por qué destaca

Usos propuestos: Crear un asistente sobre políticas; Diseñar un workflow visual de clasificación.

## Cómo funciona

Genera y guarda el token de sandbox antes de arrancar; un modelo Ollama local necesita una dirección accesible desde Docker

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker y Compose >=2.35
- OpenSSL
- 2 CPU y 4 GiB mínimos del servidor

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/langgenius/dify/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dify para mi objetivo y necesito pasos guiados. Lee https://github.com/langgenius/dify/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una app de preguntas sobre un documento ficticio tras configurar el proveedor y los embeddings.

**Qué comprobar:** La respuesta recupera un fragmento comprobable del documento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear un asistente sobre políticas
- Diseñar un workflow visual de clasificación

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear un asistente sobre políticas; Diseñar un workflow visual de clasificación | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Genera y guarda el token de sandbox antes de arrancar; un modelo Ollama local necesita una dirección accesible desde Docker

## Stack y modelos

- **Stack:** Docker y Compose >=2.35; OpenSSL; 2 CPU y 4 GiB mínimos del servidor
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

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/langgenius/dify/blob/main/README.md)
- [Fuente 2](https://marketplace.dify.ai/plugin/langgenius/ollama)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
