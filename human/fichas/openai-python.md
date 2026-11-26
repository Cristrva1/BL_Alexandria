[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › CLIs y SDKs de desarrollo

# 🐍 openai-python

> SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 32.2k | Apache-2.0 | Python | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él; requiere clave de API

**Puntuación de calidad** 75/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

SDK oficial de OpenAI para Python. Licencia Apache-2.0. Es madura y muy activa (~32k estrellas, v3.51.0) y se genera a partir de la especificación OpenAPI de OpenAI.

## ¿Qué hace?

Da acceso tipado a la API REST de OpenAI (Responses, Chat Completions, embeddings, imágenes, audio, archivos, Realtime, etc.) con clientes síncronos y asíncronos. Incluye streaming, paginación automática, reintentos, timeouts y webhooks. También admite Azure OpenAI y Bedrock mediante extras.

## ¿Cómo lo hace?

Se instala con `pip install openai` y requiere Python 3.10+. Usa HTTPX2 por defecto y `aiohttp` opcionalmente (`openai[aiohttp]`). Se configura con `OPENAI_API_KEY` y puede apuntar a otro endpoint compatible con `base_url`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [litellm](litellm.md) | El proxy LiteLLM se consume con el SDK de OpenAI cambiando `base_url`. | Arranca el proxy y crea el cliente con su URL y clave. |
| [vLLM](vllm.md) | vLLM expone un servidor compatible con OpenAI que se usa con este SDK. | Lanza `vllm serve` y apunta `base_url` a `/v1`. |
| [langchain](langchain.md) | `langchain-openai` se construye sobre este SDK. | Instala `langchain-openai` y configura la clave. |
| [OpenAI Agents SDK](openai-agents-python.md) | Combinación recíproca: OpenAI Agents SDK lo enlaza como «Cliente oficial de OpenAI que usa el SDK». | Orden indicado desde OpenAI Agents SDK: Se instala como dependencia. |
| [OpenAI Cookbook](openai-cookbook.md) | Combinación recíproca: OpenAI Cookbook lo enlaza como «SDK oficial usado por casi todos los notebooks». | Orden indicado desde OpenAI Cookbook: Instala `openai` en el entorno antes de ejecutar los ejemplos. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v3.51.0 (2026-11-13) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/openai/openai-python/blob/main/README.md) · [2](https://docs.litellm.ai/docs/proxy/user_keys) · [3](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html) · [4](https://python.langchain.com/docs/integrations/chat/openai/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La ruta OpenAI usa API y facturación de plataforma; la suscripción de Codex o ChatGPT no debe suponerse crédito para este SDK |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Es un cliente oficial de API, no un plugin de Codex; base_url configurable no confirma todas las funciones de servidores locales |
| Coste | Consumo de APIs o servicios. La ruta OpenAI usa API y facturación de plataforma; la suscripción de Codex o ChatGPT no debe suponerse crédito para este SDK |
| Equipo | Preparación según la ruta elegida. Python 3.10+; entorno virtual; clave de proyecto API |

Es un cliente oficial de API, no un plugin de Codex; base_url configurable no confirma todas las funciones de servidores locales

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10+
- entorno virtual
- clave de proyecto API

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
# install from PyPI
pip install openai
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/openai/openai-python/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar openai-python para mi objetivo y necesito pasos guiados. Lee https://github.com/openai/openai-python/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Envía una petición breve de ejemplo y revisa respuesta y uso informado.

**Qué comprobar:** Obtienes la salida del endpoint y puedes localizar el consumo del proyecto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Integrar respuestas de IA en una app Python
- Procesar audio o imágenes desde código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Integrar respuestas de IA en una app Python; Procesar audio o imágenes desde código | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un cliente oficial de API, no un plugin de Codex; base_url configurable no confirma todas las funciones de servidores locales

## Stack y modelos

- **Stack:** Python 3.10+; entorno virtual; clave de proyecto API
- **Etiquetas:** `code` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [openai/openai-python](https://github.com/openai/openai-python)
- 🌐 Web: <https://pypi.org/project/openai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openai/openai-python/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
