[🏠 Inicio](../README.md) › [🧠 Aprender IA y escribir mejores prompts](../categorias/19-aprender-ia-prompts.md) › Prompts y prompt engineering

# 💡 Fabric

> CLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 44.6k | MIT | Go | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Framework open source (MIT) de Daniel Miessler para aumentar capacidades humanas con IA, organizado en torno a 'patterns' (prompts reutilizables por tarea). Es muy activo (v1.4.576, publicaciones casi diarias) y maduro.

## ¿Qué hace?

Ofrece cientos de patterns para tareas reales, como resumir, extraer ideas, analizar afirmaciones o escribir, que se aplican a texto desde la terminal con tuberías (`pbpaste | fabric -p summarize`). Puede extraer transcripciones de YouTube (vía yt-dlp) y procesar páginas web. Admite 'strategies' de prompting y sesiones. Incluye un servidor REST con documentación Swagger, un modo de compatibilidad con la API de Ollama y una interfaz web.

## ¿Cómo lo hace?

CLI en Go que se instala con binarios, Homebrew (como `fabric-ai`), paquetes de Arch, `go install` o Docker. `fabric --setup` configura proveedores y descarga los patterns. Admite OpenAI (incluido OAuth de suscripción ChatGPT/Codex vía un backend privado, según el README), Anthropic, Ollama, Azure OpenAI y otros. Los patterns son Markdown editables, y se pueden crear patterns propios.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Ejecutar los patterns con modelos locales (proveedor soportado en el README). | Instala Ollama y descarga un modelo; después elígelo en `fabric --setup`. |
| [yt-dlp](yt-dlp.md) | Extraer transcripciones de vídeos para resumirlas con `fabric -y`; Fabric delega en yt-dlp (opción `--yt-dlp-args`). | Instala yt-dlp en el PATH antes de usar las funciones de YouTube. |
| [Open WebUI](open-webui.md) | Usar el servidor REST de Fabric en modo de compatibilidad con Ollama como backend de una interfaz de chat. (combinación por arquitectura) (no hay guía conjunta) | Arranca `fabric --serve` con el modo Ollama y apunta el cliente a esa URL. |
| [n8n](n8n.md) | Llamar a patterns desde automatizaciones a través de la API REST. (combinación por arquitectura) | Arranca el servidor REST y usa nodos HTTP de n8n. |

**Notas:** Alternativas (elige una): prompts-chat. Ojo: el uso de OAuth de suscripción vía backend privado puede contravenir los términos del proveedor [DATO NO VERIFICADO].

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.4.576 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/danielmiessler/Fabric/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Ollama y LM Studio permiten modelos locales; API por consumo o backends de Claude Code y Codex con sus cuentas y límites |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Las rutas de suscripción son adaptadores del proyecto; Codex usa un backend privado y no garantiza continuidad ni cobertura de todo plan |
| Coste | El coste depende del proveedor o la ruta. Ollama y LM Studio permiten modelos locales; API por consumo o backends de Claude Code y Codex con sus cuentas y límites |
| Equipo | Preparación según la ruta elegida. Go o instalador para tu sistema; proveedor o CLI autenticado; texto breve propio |

Las rutas de suscripción son adaptadores del proyecto; Codex usa un backend privado y no garantiza continuidad ni cobertura de todo plan

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Go o instalador para tu sistema
- proveedor o CLI autenticado
- texto breve propio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (shell):**

```
go install github.com/danielmiessler/fabric/cmd/fabric@latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/danielmiessler/Fabric/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Fabric para mi objetivo y necesito pasos guiados. Lee https://github.com/danielmiessler/Fabric/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un proveedor y aplica un patrón de resumen a una nota breve que ya conozcas.

**Qué comprobar:** Obtienes un resumen que puedes contrastar con la nota original.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Extraer acciones de una reunión
- Convertir notas en un esquema de artículo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Extraer acciones de una reunión; Convertir notas en un esquema de artículo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las rutas de suscripción son adaptadores del proyecto; Codex usa un backend privado y no garantiza continuidad ni cobertura de todo plan

## Stack y modelos

- **Stack:** Go o instalador para tu sistema; proveedor o CLI autenticado; texto breve propio
- **Etiquetas:** `prompts` `automation` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [prompts.chat](prompts-chat.md) | 177k | La colección comunitaria de prompts más grande (antes Awesome ChatGPT Prompts), auto-hospedable. |

## Enlaces

- 🐙 GitHub: [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric)
- 🌐 Web: <https://danielmiessler.com/p/fabric-origin-story>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/danielmiessler/Fabric/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
