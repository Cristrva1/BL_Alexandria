[🏠 Inicio](../README.md) › [🎨 Diseñar y construir interfaces web](../categorias/09-dise-o-ui-frontend.md) › UI generada con IA y frontends para agentes

# 📚 json-render

> Framework para generar interfaces desde una representación JSON y un catálogo de componentes definido por el desarrollador.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.6k | Apache-2.0 | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de UI generativa (Apache-2.0) de Vercel Labs: la IA genera interfaces desde prompts, restringidas a un catálogo de componentes definido por ti. Es muy activo (v0.23.1, aún 0.x).

## ¿Qué hace?

Defines un catálogo de componentes y acciones con esquemas; el modelo genera un JSON (o YAML) que cumple ese esquema y se renderiza de forma progresiva mientras llega. Sus puntos fuertes son las barreras de seguridad (solo componentes del catálogo) y la previsibilidad. Desde el mismo catálogo renderiza en React, Vue, Svelte, Solid y React Native, y también vídeos con Remotion, PDFs y emails. Incluye 36 componentes shadcn/ui listos, devtools e integración con MCP Apps para Claude, ChatGPT, Cursor y VS Code.

## ¿Cómo lo hace?

Paquetes npm por destino (`@json-render/core` más `@json-render/react`, `/shadcn`, `/react-native`, `/remotion`, `/react-pdf`, `/react-email`, `/mcp`, `/yaml`…). Funciona con cualquier modelo que produzca salida estructurada; el formato YAML incluye una transformación para el AI SDK.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ui](ui.md) | 36 componentes shadcn/ui preconstruidos (`@json-render/shadcn`). | Instala `@json-render/shadcn` junto al núcleo. |
| [remotion](remotion.md) | Renderizar vídeos desde la misma especificación (`@json-render/remotion`). | Instala Remotion y el paquete de json-render correspondiente. |
| [AI SDK (Vercel)](vercel-ai.md) | Generar y transmitir la especificación con el AI SDK (transformación documentada en el paquete YAML). | Usa el AI SDK para la llamada al modelo y json-render para renderizar. |

**Notas:** Sin alternativas declaradas; enfoques comparables: openui, copilotkit (A2UI).

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.23.1 (2026-11-16) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/vercel-labs/json-render/blob/main/README.md) · [2](https://json-render.dev)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Renderizar JSON no exige modelo; generar el JSON con IA sí usa el proveedor elegido; otros renderers añaden dependencias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. La integración MCP Apps necesita soporte de UI en el cliente; no equivale a soporte universal de todos los agentes MCP |
| Coste | El coste depende del proveedor o la ruta. Renderizar JSON no exige modelo; generar el JSON con IA sí usa el proveedor elegido; otros renderers añaden dependencias |
| Equipo | Preparación según la ruta elegida. Node; renderer del framework; catálogo y esquema; modelo solo para generación |

La integración MCP Apps necesita soporte de UI en el cliente; no equivale a soporte universal de todos los agentes MCP

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- renderer del framework
- catálogo y esquema
- modelo solo para generación

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
# for React
npm install @json-render/core @json-render/react
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/vercel-labs/json-render/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar json-render para mi objetivo y necesito pasos guiados. Lee https://github.com/vercel-labs/json-render/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Renderiza primero un JSON escrito a mano con una tarjeta y un botón permitido.

**Qué comprobar:** La interfaz refleja el JSON y rechaza componentes fuera de catálogo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear interfaces dinámicas desde datos
- Acotar la UI que puede proponer un modelo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear interfaces dinámicas desde datos; Acotar la UI que puede proponer un modelo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La integración MCP Apps necesita soporte de UI en el cliente; no equivale a soporte universal de todos los agentes MCP

## Stack y modelos

- **Stack:** Node; renderer del framework; catálogo y esquema; modelo solo para generación
- **Etiquetas:** `ia-ui` `library` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [vercel-labs/json-render](https://github.com/vercel-labs/json-render)
- 🌐 Web: <https://json-render.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/vercel-labs/json-render/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
