[🏠 Inicio](../README.md) › [🤖 Automatizar procesos y crear herramientas internas](../categorias/01-automatizaci-n-mensajer-a-crm.md) › Motores de workflow y automatización

# 🔁 Windmill

> Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.6k | NOASSERTION | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La Community Edition tiene condiciones y cuotas; servidor, planes comerciales y APIs de IA son partidas distintas |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelo local no documentado. Ofrece MCP remoto autenticado para operar un workspace; conectar Claude Code, Codex o Antigravity no incluye el modelo ni autoriza todas las acciones del workspace |
| Coste | El coste depende del proveedor o la ruta. La Community Edition tiene condiciones y cuotas; servidor, planes comerciales y APIs de IA son partidas distintas |
| Equipo | Preparación según la ruta elegida. Docker Compose;  espacio para la base y los trabajadores |

Ofrece MCP remoto autenticado para operar un workspace; conectar Claude Code, Codex o Antigravity no incluye el modelo ni autoriza todas las acciones del workspace

## Qué puedes hacer con él

Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida.

## Por qué destaca

Usos propuestos: Convertir un script de conciliación en una herramienta interna con formulario; Programar una consulta de datos como tarea recurrente.

## Cómo funciona

Ofrece MCP remoto autenticado para operar un workspace; conectar Claude Code, Codex o Antigravity no incluye el modelo ni autoriza todas las acciones del workspace

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker Compose
-  espacio para la base y los trabajadores

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/docker-compose.yml -o docker-compose.yml
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/Caddyfile -o Caddyfile
curl https://raw.githubusercontent.com/windmill-labs/windmill/main/.env -o .env

docker compose up -d
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/windmill-labs/windmill/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Windmill para mi objetivo y necesito pasos guiados. Lee https://github.com/windmill-labs/windmill/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea un script que reciba un nombre y devuelva un saludo.

**Qué comprobar:** La ejecución guarda el resultado del script y sus logs.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Convertir un script de conciliación en una herramienta interna con formulario
- Programar una consulta de datos como tarea recurrente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Convertir un script de conciliación en una herramienta interna con formulario; Programar una consulta de datos como tarea recurrente | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ofrece MCP remoto autenticado para operar un workspace; conectar Claude Code, Codex o Antigravity no incluye el modelo ni autoriza todas las acciones del workspace

## Stack y modelos

- **Stack:** Docker Compose;  espacio para la base y los trabajadores
- **Etiquetas:** `automation` `agents` `rust` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [langfuse](langfuse.md) | 37.4k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [Kestra](kestra.md) | 30.2k | Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. |
| [Trigger.dev](trigger-dev.md) | 16.8k | Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. |

## Enlaces

- 🐙 GitHub: [windmill-labs/windmill](https://github.com/windmill-labs/windmill)
- 🌐 Web: <https://windmill.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/windmill-labs/windmill/blob/main/README.md)
- [Fuente 2](https://www.windmill.dev/docs/core_concepts/mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
