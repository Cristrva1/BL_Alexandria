[🏠 Inicio](../README.md) › [🕸️ Programar con agentes de código](../categorias/20-agentes-de-codigo.md) › Agentes de terminal

# 🕸️ openclaude

> Agente de código abierto para terminal que conecta proveedores remotos y modelos locales con herramientas y MCP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 34.4k | NOASSERTION | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

OpenClaude, CLI de agente de programación multi-proveedor publicada por Twigpine. Según su propio NOTICE, deriva del código propietario de Claude Code de Anthropic y solo las modificaciones se ofrecen con MIT «donde sea legalmente posible» (GitHub muestra NOASSERTION). Tiene ~34k estrellas (v0.36.0) y fue creado en abril de 2026.

## ¿Qué hace?

Mantiene un flujo de trabajo de terminal (herramientas, agentes, MCP, comandos slash) con proveedores compatibles con OpenAI, Gemini, GitHub Models, Codex OAuth, Ollama y otros. Usa Exa como búsqueda web por defecto en modelos que no son de Anthropic.

## ¿Cómo lo hace?

Se instala con `npm install -g @twigpine/openclaude@latest` (Node.js ≥24.22.1). El paquete anterior ya no se actualiza. Declara no estar afiliado a Anthropic.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Proveedor local soportado. | Configura Ollama como backend. |
| [litellm](litellm.md) | Usar el proxy LiteLLM como backend compatible con OpenAI. (combinación por arquitectura) | Apunta el proveedor OpenAI al proxy. |
| [Context7](context7.md) | Documentación de librerías vía MCP. (combinación por arquitectura) | Añade el MCP de Context7. |

**Notas:** Sin alternativas declaradas. Riesgo legal y de propiedad intelectual: deriva de código propietario de Anthropic. Pregunta de pertenencia al catálogo (solo anotada).

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.36.0 (2026-11-13) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Twigpine/openclaude/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Admite modelos locales y proveedores remotos con API u OAuth; las cuotas dependen de la ruta elegida |
| Claude Code | Integración no documentada |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El paquete actual es @twigpine/openclaude; no es Claude Code y el autor indica no copiar indiscriminadamente sus credenciales ni .claude |
| Coste | El coste depende del proveedor o la ruta. Admite modelos locales y proveedores remotos con API u OAuth; las cuotas dependen de la ruta elegida |
| Equipo | Preparación según la ruta elegida. Node >=24.22.1; proveedor o Ollama; carpeta de prueba |

El paquete actual es @twigpine/openclaude; no es Claude Code y el autor indica no copiar indiscriminadamente sus credenciales ni .claude

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node >=24.22.1
- proveedor o Ollama
- carpeta de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npm install -g @twigpine/openclaude@latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Twigpine/openclaude/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar openclaude para mi objetivo y necesito pasos guiados. Lee https://github.com/Twigpine/openclaude/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala el paquete actual y configura un modelo antes de solicitar una explicación sin edición.

**Qué comprobar:** Puedes revisar proveedor, contexto y permisos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Usar un agente con Ollama
- Comparar un backend API con Codex OAuth

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Usar un agente con Ollama; Comparar un backend API con Codex OAuth | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El paquete actual es @twigpine/openclaude; no es Claude Code y el autor indica no copiar indiscriminadamente sus credenciales ni .claude

## Stack y modelos

- **Stack:** Node >=24.22.1; proveedor o Ollama; carpeta de prueba
- **Etiquetas:** `coding` `ai` `ai-agent` `ai-tools` `cli` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Twigpine/openclaude](https://github.com/Twigpine/openclaude)
- 🌐 Web: <https://openclaude.twigpine.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Twigpine/openclaude/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
