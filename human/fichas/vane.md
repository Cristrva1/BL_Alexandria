[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# 🔍 Vane

> Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 38.2k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 57/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Motor de respuestas con IA centrado en la privacidad que se ejecuta en tu propio equipo, de @ItzCrazyKns. Licencia MIT. Es popular (~38k estrellas, v1.12.2) y su último cambio es de septiembre de 2026.

## ¿Qué hace?

Responde preguntas buscando en internet con SearXNG y citando fuentes, al estilo de un buscador con IA. Tiene modos rápido, equilibrado y de calidad, admite subir documentos (PDF, texto, imágenes) y también puede usar Tavily o Exa. Funciona con modelos locales vía Ollama o con OpenAI, Claude, Gemini, Groq y otros.

## ¿Cómo lo hace?

Se despliega con Docker: la imagen completa incluye SearXNG (`docker run -p 3000:3000 … itzcrazykns1337/vane:latest`) y la versión `slim` usa una instancia propia mediante `SEARXNG_API_URL`. Los proveedores y modelos se configuran en la interfaz web.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [SearXNG](searxng.md) | Motor de búsqueda que usa por defecto. | Usa la imagen completa o apunta a tu SearXNG con JSON activado. |
| [Ollama](ollama.md) | Modelos locales soportados de forma nativa. | Levanta Ollama y configura su URL en Vane (cuidado con la red de Docker). |
| [markitdown](markitdown.md) | Convertir documentos de Office a texto antes de subirlos. (combinación por arquitectura) | Convierte con MarkItDown y sube el resultado. |

**Notas:** Alternativas (elige una): gpt-researcher.

Estado en GitHub: activo · último push 2026-09-01 · última versión publicada v1.12.2 (2026-04-10) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ItzCrazyKns/Vane/blob/master/README.md)</sub>

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
