[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# 🔍 Vane

> Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.2k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. El contenedor incluye SearxNG; el modelo puede ser local o API de pago; alojamiento y hardware siguen siendo costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Antes llamado Perplexica; búsqueda web privada no significa que los sitios externos no reciban consultas |
| Coste | El coste depende del proveedor o la ruta. El contenedor incluye SearxNG; el modelo puede ser local o API de pago; alojamiento y hardware siguen siendo costes |
| Equipo | Preparación según la ruta elegida. Docker; modelo local accesible o clave de proveedor |

Antes llamado Perplexica; búsqueda web privada no significa que los sitios externos no reciban consultas

## Qué puedes hacer con él

Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica).

## Por qué destaca

Usos propuestos: Investigar un tema con citas; Consultar la web usando Ollama.

## Cómo funciona

Antes llamado Perplexica; búsqueda web privada no significa que los sitios externos no reciban consultas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- modelo local accesible o clave de proveedor

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker run -d -p 3000:3000 -v vane-data:/home/vane/data --name vane itzcrazykns1337/vane:latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/ItzCrazyKns/Vane/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Vane para mi objetivo y necesito pasos guiados. Lee https://github.com/ItzCrazyKns/Vane/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Busca una pregunta de actualidad sencilla y abre las referencias antes de aceptar el resumen.

**Qué comprobar:** La respuesta muestra enlaces que apoyan sus afirmaciones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Investigar un tema con citas
- Consultar la web usando Ollama

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Investigar un tema con citas; Consultar la web usando Ollama | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Antes llamado Perplexica; búsqueda web privada no significa que los sitios externos no reciban consultas

## Stack y modelos

- **Stack:** Docker; modelo local accesible o clave de proveedor
- **Etiquetas:** `search` `research` `local` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [SearXNG](searxng.md) | 39.6k | Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. |
| [Ollama](ollama.md) | 187k | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [gpt-researcher](gpt-researcher.md) | 30.7k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |

## Enlaces

- 🐙 GitHub: [ItzCrazyKns/Vane](https://github.com/ItzCrazyKns/Vane)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ItzCrazyKns/Vane/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
