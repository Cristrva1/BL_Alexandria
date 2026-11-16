[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 🏛️ mempalace

> Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 60.6k | MIT | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Sistema de memoria de IA «local primero» de código abierto (MIT) del proyecto MemPalace, distribuido en PyPI. Muy activo (v3.12.0); avisa de sitios web impostores: solo el repositorio, el paquete de PyPI y su web oficial son legítimos.

## ¿Qué hace?

Guarda el historial de conversaciones de forma literal (sin resumir ni parafrasear) y lo recupera con búsqueda semántica, organizado en «alas» (personas y proyectos), «salas» (temas) y «cajones» (contenido original) para acotar las búsquedas. Según su README alcanza 96,6 % R@5 en LongMemEval sin llamadas a API [DATO NO VERIFICADO: benchmark propio]. Puede funcionar como memoria privada local, como «cerebro compartido» o como cliente de un hub existente.

## ¿Cómo lo hace?

Paquete Python (`pip install mempalace`) con CLI y servidor MCP, y una imagen de contenedor. El backend de recuperación es intercambiable y por defecto usa ChromaDB. Publica tres skills (`npx skills add MemPalace/mempalace`) para instalación guiada, recuerdo antes de responder y delegación; la skill de instalación configura el MCP pero no lo instala por sí sola. Nada sale de tu máquina salvo que lo actives.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Integración con hooks de autoguardado y MCP; el README advierte que sin hooks las sesiones de Claude Code caducan a los 30 días. | Instala las skills, deja que el agente configure el MCP y conecta los hooks de autoguardado. |
| [Chroma](chroma.md) | Backend de recuperación por defecto. | Se usa embebido; solo instala un servidor Chroma aparte si quieres compartirlo. |
| [Codex CLI](codex.md) | Las skills y el servidor MCP sirven para otros agentes compatibles (combinación por arquitectura). | Registra el servidor MCP en la configuración de Codex. |

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v3.12.0 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/MemPalace/mempalace/blob/develop/README.md)</sub>

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
