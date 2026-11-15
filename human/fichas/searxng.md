[🏠 Inicio](../README.md) › [🕷️ Buscar y extraer información web](../categorias/04-scraping-b-squeda-research-web.md) › Búsqueda, monitoreo y research web

# 🔍 SearXNG

> Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39.6k | AGPL-3.0 | Python | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Combina resultados de más de 70 servicios sin rastrearte. Muchos agentes de investigación lo usan como API de búsqueda gratuita y propia.

## Por qué destaca

Buscador auto-hospedado sin coste por consulta, con salida JSON para agentes.

## Cómo funciona

Envía tu consulta a varios motores, combina y ordena los resultados y los devuelve en HTML o JSON.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/searxng/searxng/blob/master/README.rst)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SearXNG para mi objetivo y necesito pasos guiados. Lee https://github.com/searxng/searxng/blob/master/README.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Búsqueda para agentes sin pagar API
- Buscador privado del equipo
- Research con fuentes variadas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| tus agentes necesitan buscar en la web sin coste por consulta | necesitas resultados con SLA comercial |

**Limitaciones:** Licencia AGPL-3.0; algunos motores pueden bloquear consultas masivas.

## Stack y modelos

- **Stack:** Python, Docker
- **Etiquetas:** `search` `research` `python` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [gpt-researcher](gpt-researcher.md) | 30.7k | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. |
| [Open WebUI](open-webui.md) | 159k | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. |
| [Vane](vane.md) | 38.2k | Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica). |

## Enlaces

- 🐙 GitHub: [searxng/searxng](https://github.com/searxng/searxng)
- 🌐 Web: <https://docs.searxng.org>
- 🧪 Receta: [Agente de research profundo](../playbooks/agente-de-research-profundo.md)
- 🧪 Receta: [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md)
- 🧪 Receta: [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/searxng/searxng/blob/master/README.rst)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
