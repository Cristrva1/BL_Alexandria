[🏠 Inicio](../README.md) › [🕸️ Construir agentes y coordinar equipos de IA](../categorias/03-frameworks-orquestaci-n-de-agentes.md) › Builders visuales y plataformas de agentes

# 🧩 AutoGPT

> Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 188k | NOASSERTION | Python | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. La plataforma alojada es de pago y ofrece acceso a modelos; self-hosting usa tus credenciales o modelo local y recursos propios |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. La plataforma actual expone MCP Streamable HTTP con clave y permisos; no confundirla con tutoriales del agente Classic ni con acceso incluido al modelo |
| Coste | El coste depende del proveedor o la ruta. La plataforma alojada es de pago y ofrece acceso a modelos; self-hosting usa tus credenciales o modelo local y recursos propios |
| Equipo | Preparación según la ruta elegida. Docker para self-hosting; credenciales o modelo local |

La plataforma actual expone MCP Streamable HTTP con clave y permisos; no confundirla con tutoriales del agente Classic ni con acceso incluido al modelo

## Qué puedes hacer con él

Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques.

## Por qué destaca

Usos propuestos: Procesar solicitudes recurrentes; Componer una investigación con revisión humana.

## Cómo funciona

La plataforma actual expone MCP Streamable HTTP con clave y permisos; no confundirla con tutoriales del agente Classic ni con acceso incluido al modelo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker para self-hosting
- credenciales o modelo local

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker run -d \
  --name autogpt \
  --restart unless-stopped \
  --shm-size 2g \
  --ulimit nofile=65536:65536 \
  --log-driver json-file \
  --log-opt max-size=50m \
  --log-opt max-file=5 \
  -p 127.0.0.1:3000:3000 \
  -e AUTOGPT_PUBLIC_URL=http://localhost:3000 \
  -v autogpt-data:/data \
  significantgravitas/autogpt:latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Significant-Gravitas/AutoGPT/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar AutoGPT para mi objetivo y necesito pasos guiados. Lee https://github.com/Significant-Gravitas/AutoGPT/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una automatización breve que transforma una entrada de texto y revisa cada bloque.

**Qué comprobar:** Ves la salida y el historial de una ejecución acotada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Procesar solicitudes recurrentes
- Componer una investigación con revisión humana

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Procesar solicitudes recurrentes; Componer una investigación con revisión humana | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La plataforma actual expone MCP Streamable HTTP con clave y permisos; no confundirla con tutoriales del agente Classic ni con acceso incluido al modelo

## Stack y modelos

- **Stack:** Docker para self-hosting; credenciales o modelo local
- **Etiquetas:** `agents` `automation` `python`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Sim](sim.md) | 30.1k | Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. |
| [langflow](langflow.md) | 157k | Constructor visual de flujos LLM/agentes construido sobre LangChain. |

## Enlaces

- 🐙 GitHub: [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)
- 🌐 Web: <https://agpt.co>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Significant-Gravitas/AutoGPT/blob/master/README.md)
- [Fuente 2](https://agpt.co/docs/platform/api-and-integrations/api-guide/mcp-server.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
