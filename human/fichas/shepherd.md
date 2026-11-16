[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Infraestructura: sandboxes, herramientas y protocolos

# 📚 shepherd

> Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus recorridos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.6k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 49/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Shepherd, sustrato de ejecución para meta-agentes programables con trazas de ejecución reversibles, de shepherd-agents. Licencia MIT. Está en alfa temprana con APIs cambiantes, tiene ~2.6k estrellas y artículo citado.

## ¿Qué hace?

Registra las ejecuciones de agentes como trazas duraderas e inspeccionables. Los resultados se quedan en el workspace para revisarlos antes de aplicarlos o descartarlos, con permisos que se aplican a nivel de sistema operativo.

## ¿Cómo lo hace?

Requiere Python 3.11+ y se instala con `pip install shepherd-ai`. Aplica los permisos con Seatbelt en macOS y Landlock en Linux (en contenedor privilegiado); Windows no está soportado (usar WSL). El ejemplo principal ejecuta Claude Code dentro del sandbox.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Cuerpo de tarea documentado (requiere la CLI `claude`). | Instala e inicia sesión en Claude Code. |
| [Codex CLI](codex.md) | Otro agente como cuerpo de tarea. (combinación por arquitectura) | Envuelve Codex en una tarea. |
| [OpenCode](opencode.md) | Otro agente como cuerpo de tarea. (combinación por arquitectura) | Envuelve OpenCode en una tarea. |

**Notas:** Sin alternativas declaradas. Es alfa.

Estado en GitHub: activo · último push 2026-09-09 · última versión publicada v0.3.1 (2026-09-09) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/shepherd-agents/shepherd/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El ejemplo offline no necesita API; el ejemplo Claude usa suscripción o clave API y el entorno consume recursos |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La reversibilidad afecta al estado capturado por el runtime y no promete deshacer cualquier efecto externo; la demo offline no es un LLM local |
| Coste | El coste depende del proveedor o la ruta. El ejemplo offline no necesita API; el ejemplo Claude usa suscripción o clave API y el entorno consume recursos |
| Equipo | Preparación según la ruta elegida. Python 3.11+; entorno compatible; Claude CLI solo para ejemplo con modelo |

La reversibilidad afecta al estado capturado por el runtime y no promete deshacer cualquier efecto externo; la demo offline no es un LLM local

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.11+
- entorno compatible
- Claude CLI solo para ejemplo con modelo

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install shepherd-ai
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/shepherd-agents/shepherd/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar shepherd para mi objetivo y necesito pasos guiados. Lee https://github.com/shepherd-agents/shepherd/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Empieza por Offline Quickstart para observar una traza reversible sin llamar un modelo.

**Qué comprobar:** Puedes inspeccionar estados y bifurcaciones de la demostración.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar reproducción de ejecuciones
- Comparar una traza con un resultado final

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar reproducción de ejecuciones; Comparar una traza con un resultado final | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La reversibilidad afecta al estado capturado por el runtime y no promete deshacer cualquier efecto externo; la demo offline no es un LLM local

## Stack y modelos

- **Stack:** Python 3.11+; entorno compatible; Claude CLI solo para ejemplo con modelo
- **Etiquetas:** `infra` `framework` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [shepherd-agents/shepherd](https://github.com/shepherd-agents/shepherd)
- 🌐 Web: <https://shepherd-agents.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/shepherd-agents/shepherd/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
