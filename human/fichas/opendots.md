[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🖥️ OpenDots

> Interfaz abierta de asistentes persistentes que requiere CopilotKit Intelligence, alojado, evaluado localmente o con licencia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.6k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere clave de API

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

OpenDots, plantilla open source de CopilotKit para agentes persistentes, cada uno con su propio ordenador, en web y móvil. Licencia MIT. Tiene ~6.6k estrellas; CopilotKit ofrece ahora la versión más robusta como skin de OpenBot.

## ¿Qué hace?

Los «Dots» conversan por texto, llamadas y Slack, navegan, redactan y guardan resultados en páginas editables tras una tarjeta de aprobación humana. Usan herramientas MCP y apps de Composio con aprobación para escrituras.

## ¿Cómo lo hace?

Se autoaloja, pero las conversaciones requieren CopilotKit Intelligence: servicio alojado, evaluación local con Docker o despliegue autoalojado con licencia. La telemetría del SDK está activa.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [CopilotKit](copilotkit.md) | Framework base y requisito (CopilotKit Intelligence). | Crea el proyecto con `npx copilotkit@latest login`. |
| [Composio](composio.md) | Apps conectadas integradas. | Añade la clave de Composio. |
| [servers](servers.md) | Servidores MCP de referencia como herramientas. (combinación por arquitectura) | Añade los MCP por Dot. |

**Notas:** Alternativa (elige una): openbot. No es autónomo del todo: depende de un servicio de CopilotKit.

Estado en GitHub: activo · último push 2026-11-14 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/CopilotKit/OpenDots/blob/main/README.md)</sub>

## Ver similares

Grupo **Espacios de asistentes de CopilotKit**: OpenDots ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OpenBot](openbot.md) ⭐ recomendado | 70 | Si buscas esto: espacio autoalojable de CopilotKit para compañeros de IA con navegador propio, permisos, aprobaciones y auditoría, conectables por AG-UI. |
| 2 | **OpenDots** (esta ficha) | 48 | Si buscas esto: interfaz abierta de asistentes persistentes que requiere CopilotKit Intelligence, alojado, evaluado localmente o con licencia. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La UI MIT requiere Intelligence hospedado, evaluación Docker local o despliegue autoalojado con licencia; modelos y voz pueden cobrar aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Autoalojar OpenDots no incluye automáticamente el servicio Intelligence ni una pila enteramente local |
| Coste | El coste depende del proveedor o la ruta. La UI MIT requiere Intelligence hospedado, evaluación Docker local o despliegue autoalojado con licencia; modelos y voz pueden cobrar aparte |
| Equipo | Preparación según la ruta elegida. Node; CopilotKit Intelligence; proveedores y conectores elegidos |

Autoalojar OpenDots no incluye automáticamente el servicio Intelligence ni una pila enteramente local

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node
- CopilotKit Intelligence
- proveedores y conectores elegidos

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
git clone https://github.com/CopilotKit/OpenDots.git
cd OpenDots
npm ci
cp .env.example .env
npm run dev
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/CopilotKit/OpenDots/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenDots para mi objetivo y necesito pasos guiados. Lee https://github.com/CopilotKit/OpenDots/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un Dot de prueba y haz una pregunta sin conceder herramientas de escritura.

**Qué comprobar:** Puedes comprobar la respuesta y el panel de conexiones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un asistente persistente
- Estudiar aprobación de acciones conectadas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un asistente persistente; Estudiar aprobación de acciones conectadas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Autoalojar OpenDots no incluye automáticamente el servicio Intelligence ni una pila enteramente local

## Stack y modelos

- **Stack:** Node; CopilotKit Intelligence; proveedores y conectores elegidos
- **Etiquetas:** `asistentes` `agent` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenBot](openbot.md) | 12.5k | Espacio autoalojable de CopilotKit para compañeros de IA con navegador propio, permisos, aprobaciones y auditoría, conectables por AG-UI. |

## Enlaces

- 🐙 GitHub: [CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots)
- 🌐 Web: <https://www.copilotkit.ai/opendots>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/CopilotKit/OpenDots/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
