[🏠 Inicio](../README.md) › [📄 Presentaciones, diagramas y explicación visual](../categorias/31-presentaciones-diagramas.md) › Presentaciones

# 🖥️ Presenton

> Generador de presentaciones con IA, open source y con API, alternativa a Gamma o Beautiful.ai.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.9k | Apache-2.0 | TypeScript | 2026-11-10 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Presenton, generador open source de presentaciones con IA y API, alternativa a Gamma o Beautiful AI. Licencia Apache-2.0. Tiene ~12k estrellas; app web autoalojada con Docker y app de escritorio en beta.

## ¿Qué hace?

Genera presentaciones desde un prompt, un documento o tu propio diseño de PowerPoint, con plantillas y exportación. Incluye una API de generación y un servidor MCP.

## ¿Cómo lo hace?

Se despliega con `docker run -p 5001:80 ghcr.io/presenton/presenton:latest`, o en desarrollo con Node.js, Python 3.11 y otras dependencias. Funciona con Ollama, OpenAI, Gemini, Anthropic, Bedrock y otros proveedores compatibles.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Ollama](ollama.md) | Modelos locales soportados. | Configura Ollama como proveedor. |
| [Claude Code](claude-code.md) | Cliente MCP para generar presentaciones. (combinación por arquitectura) | Conecta el MCP de Presenton. |
| [litellm](litellm.md) | Proveedor compatible con OpenAI. (combinación por arquitectura) | Apunta Presenton al proxy. |

**Notas:** Alternativas (elige una): ppt-master.

Estado en GitHub: activo · último push 2026-11-06 · última versión publicada electron-v0.9.12-beta (2026-10-26) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/presenton/presenton/blob/main/README.md) · [2](https://docs.presenton.ai/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Admite API, Ollama, LM Studio y ruta Codex con OAuth; imágenes y otros servicios pueden tener costes separados |
| Claude Code | Herramienta MCP para el agente |
| Codex | Integración documentada por el proyecto |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | Modelos locales documentados. El servidor ofrece MCP Streamable HTTP autenticado; MCP está desactivado en la app Electron y Codex como proveedor es distinto de Codex como cliente MCP |
| Coste | El coste depende del proveedor o la ruta. Admite API, Ollama, LM Studio y ruta Codex con OAuth; imágenes y otros servicios pueden tener costes separados |
| Equipo | Preparación según la ruta elegida. Docker o app compatible; proveedor de texto e imagen; contraseña propia; datos ficticios |

El servidor ofrece MCP Streamable HTTP autenticado; MCP está desactivado en la app Electron y Codex como proveedor es distinto de Codex como cliente MCP

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o app compatible
- proveedor de texto e imagen
- contraseña propia
- datos ficticios

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
docker run -it --name presenton \
  -p 5001:80 \
  -e AUTH_USERNAME=admin \
  -e AUTH_PASSWORD=change-this-password \
  -v "./app_data:/app_data" \
  ghcr.io/presenton/presenton:latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/presenton/presenton/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Presenton para mi objetivo y necesito pasos guiados. Lee https://github.com/presenton/presenton/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera tres slides y revisa afirmaciones, diseño y exportación antes de compartir.

**Qué comprobar:** Puedes identificar proveedores y editar el contenido generado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una presentación desde un documento
- Comparar una plantilla con generación libre

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una presentación desde un documento; Comparar una plantilla con generación libre | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El servidor ofrece MCP Streamable HTTP autenticado; MCP está desactivado en la app Electron y Codex como proveedor es distinto de Codex como cliente MCP

## Stack y modelos

- **Stack:** Docker o app compatible; proveedor de texto e imagen; contraseña propia; datos ficticios
- **Etiquetas:** `slides` `agents` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ppt-master](ppt-master.md) | 76.8k | Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos. |

## Enlaces

- 🐙 GitHub: [presenton/presenton](https://github.com/presenton/presenton)
- 🌐 Web: <https://presenton.ai>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/presenton/presenton/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
