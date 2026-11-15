[🏠 Inicio](../README.md) › [🧬 Memoria, conocimiento y operación de IA](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🏛️ mempalace

> Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 60.6k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. El proveedor y la función elegidos determinan si hacen falta credenciales de IA. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Modelos locales | Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo. |
| Coste | Consumo del agente que ya utilizas. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente. |
| Equipo | Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Resuelve la memoria privada: cero llamadas a API, tus textos no salen de tu máquina.

## Por qué destaca

Prioriza la privacidad total (cero llamadas a API) reportando recall competitivo en benchmarks de memoria de largo plazo. Su diseño verbatim evita la pérdida de detalle que sufren los enfoques que resumen con un LLM remoto.

## Cómo funciona

Guarda los textos verbatim y los recupera mediante un backend de búsqueda conectable, sin depender de un LLM remoto para almacenar ni para indexar; el backend se puede cambiar según tus necesidades.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/MemPalace/mempalace/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mempalace para mi objetivo y necesito pasos guiados. Lee https://github.com/MemPalace/mempalace/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Memoria privada para agentes
- Recuerdo de largo plazo sin enviar datos a la nube
- Casos con requisitos de confidencialidad (sanidad, legal)

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| la privacidad es prioridad y no quieres llamadas a API | quieres un SaaS gestionado con escalado automático o integraciones de framework ya hechas (mem0) |

## Stack y modelos

- **Stack:** Python (PyPI)
- **Etiquetas:** `memory` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [open-notebook](open-notebook.md) | 42k | Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. |
| [odysseus](odysseus.md) | 95.6k | Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado. |

## Enlaces

- 🐙 GitHub: [MemPalace/mempalace](https://github.com/MemPalace/mempalace)
- 🌐 Web: <http://mempalaceofficial.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/MemPalace/mempalace/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
