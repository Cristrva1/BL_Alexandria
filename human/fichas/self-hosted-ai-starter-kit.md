[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Ecosistema n8n

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
| API de IA | Sin clave propia de API de IA en la ruta básica. La ruta con pesos locales evita una API de modelo; siguen existiendo costes de equipo y energía |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El README distingue perfiles CPU, NVIDIA y alternativas de Mac; elige el de tu equipo antes de descargar pesos |
| Coste | Sin pago a un modelo en la ruta básica. La ruta con pesos locales evita una API de modelo; siguen existiendo costes de equipo y energía |
| Equipo | Preparación según la ruta elegida. Docker Compose;  memoria y almacenamiento para el modelo;  archivo .env preparado |

El README distingue perfiles CPU, NVIDIA y alternativas de Mac; elige el de tu equipo antes de descargar pesos

## Qué puedes hacer con él

Plantilla Docker Compose de n8n con Ollama, Qdrant y PostgreSQL para IA local en minutos.

## Por qué destaca

Usos propuestos: Probar un asistente local que responde preguntas sobre material de ejemplo; Explorar cómo se conectan n8n, Ollama y una base vectorial.

## Cómo funciona

El README distingue perfiles CPU, NVIDIA y alternativas de Mac; elige el de tu equipo antes de descargar pesos

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker Compose
-  memoria y almacenamiento para el modelo
-  archivo .env preparado

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git
cd self-hosted-ai-starter-kit
cp .env.example .env # you should update secrets and passwords inside
docker compose --profile cpu up
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Self-hosted AI Starter Kit para mi objetivo y necesito pasos guiados. Lee https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre n8n y ejecuta el flujo local incluido con una pregunta sencilla.

**Qué comprobar:** El flujo devuelve una respuesta usando el servicio Ollama del stack.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un asistente local que responde preguntas sobre material de ejemplo
- Explorar cómo se conectan n8n, Ollama y una base vectorial

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un asistente local que responde preguntas sobre material de ejemplo; Explorar cómo se conectan n8n, Ollama y una base vectorial | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README distingue perfiles CPU, NVIDIA y alternativas de Mac; elige el de tu equipo antes de descargar pesos

## Stack y modelos

- **Stack:** Docker Compose;  memoria y almacenamiento para el modelo;  archivo .env preparado
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

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/n8n-io/self-hosted-ai-starter-kit/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
