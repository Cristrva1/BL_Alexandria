[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🏛️ mempalace

> Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 60.6k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La ruta básica usa embeddings locales sin API; proveedores opcionales de embeddings pueden costar; no necesita LLM generativo para buscar |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. El primer uso descarga el modelo; montar archivos en Docker es necesario para que pueda leerlos; los porcentajes de benchmark son del autor |
| Coste | El coste depende del proveedor o la ruta. La ruta básica usa embeddings locales sin API; proveedores opcionales de embeddings pueden costar; no necesita LLM generativo para buscar |
| Equipo | Preparación según la ruta elegida. Python o Docker; modelo de embeddings descargado; directorio de prueba |

El primer uso descarga el modelo; montar archivos en Docker es necesario para que pueda leerlos; los porcentajes de benchmark son del autor

## Qué puedes hacer con él

Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos.

## Por qué destaca

Usos propuestos: Recuperar decisiones antiguas; Consultar archivos de contexto sin resúmenes destructivos.

## Cómo funciona

El primer uso descarga el modelo; montar archivos en Docker es necesario para que pueda leerlos; los porcentajes de benchmark son del autor

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python o Docker
- modelo de embeddings descargado
- directorio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
python -m venv .venv && source .venv/bin/activate
pip install mempalace
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/MemPalace/mempalace/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mempalace para mi objetivo y necesito pasos guiados. Lee https://github.com/MemPalace/mempalace/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Indexa dos notas propias y busca una decisión con palabras distintas a las originales.

**Qué comprobar:** Puedes abrir el fragmento literal y comprobar su origen.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Recuperar decisiones antiguas
- Consultar archivos de contexto sin resúmenes destructivos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Recuperar decisiones antiguas; Consultar archivos de contexto sin resúmenes destructivos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El primer uso descarga el modelo; montar archivos en Docker es necesario para que pueda leerlos; los porcentajes de benchmark son del autor

## Stack y modelos

- **Stack:** Python o Docker; modelo de embeddings descargado; directorio de prueba
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

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/MemPalace/mempalace/blob/develop/README.md)
- [Fuente 2](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
