[🏠 Inicio](../README.md) › [🔌 Conectar herramientas con MCP](../categorias/05-mcp-conectividad.md) › Servidores MCP destacados

# 🔌 Context7

> Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 64.8k | MIT | TypeScript | 2026-08-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Context7, servicio de Upstash que da a los agentes documentación actualizada y ejemplos de código de librerías. Licencia MIT para el repo; el servicio es alojado y requiere clave. Es muy popular (~65k estrellas).

## ¿Qué hace?

Evita APIs inventadas o ejemplos viejos: el agente consulta la documentación vigente y por versión de la librería que usa. Funciona en dos modos: CLI + skill (`ctx7`, sin MCP) o servidor MCP con herramientas de documentación. Tiene paquetes como un toolkit para el AI SDK.

## ¿Cómo lo hace?

Se configura con `npx ctx7 setup` (Node.js 22.13+), que autentica por OAuth, genera una clave e instala la skill o el MCP (`--cursor`, `--claude`, `--opencode`…). También se puede usar el servidor remoto `https://mcp.context7.com/mcp` con cabecera de autorización. La documentación lista la instalación manual para más de 30 clientes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Configuración automática con `npx ctx7 setup --claude`. | Ejecuta el setup y elige modo CLI + skill o MCP. |
| [OpenCode](opencode.md) | Configuración automática con `--opencode`. | Ejecuta `npx ctx7 setup --opencode`. |
| [Cline](cline.md) | Instalación manual como servidor MCP, según la lista de clientes de Context7. | Añade el servidor remoto con tu clave en la configuración MCP de Cline. |

**Notas:** Sin alternativas declaradas. Las consultas salen hacia el servicio de Upstash.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada @upstash/context7-tools-ai-sdk@1.0.4 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/upstash/context7/blob/master/README.md) · [2](https://context7.com/docs/resources/all-clients)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La documentación tiene cupos y modalidades de acceso; el modelo del agente se paga o limita aparte |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Conectar documentación actual no acredita que todo ejemplo sea válido para la versión instalada en tu proyecto |
| Coste | El coste depende del proveedor o la ruta. La documentación tiene cupos y modalidades de acceso; el modelo del agente se paga o limita aparte |
| Equipo | Preparación según la ruta elegida. Node.js >=22.13; cliente MCP; clave Context7 recomendada |

Conectar documentación actual no acredita que todo ejemplo sea válido para la versión instalada en tu proyecto

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js >=22.13
- cliente MCP
- clave Context7 recomendada

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npx ctx7 setup
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/upstash/context7/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Context7 para mi objetivo y necesito pasos guiados. Lee https://github.com/upstash/context7/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Pide documentación de una versión concreta y contrasta el ejemplo devuelto con la fuente.

**Qué comprobar:** El agente identifica la biblioteca y la versión consultada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Consultar APIs recientes durante programación
- Evitar mezclar instrucciones de versiones distintas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Consultar APIs recientes durante programación; Evitar mezclar instrucciones de versiones distintas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Conectar documentación actual no acredita que todo ejemplo sea válido para la versión instalada en tu proyecto

## Stack y modelos

- **Stack:** Node.js >=22.13; cliente MCP; clave Context7 recomendada
- **Etiquetas:** `mcp` `docs` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [upstash/context7](https://github.com/upstash/context7)
- 🌐 Web: <https://context7.com>
- 🧪 Receta: [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/upstash/context7/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
