[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Escritura y calidad de texto

# 🎨 i-have-adhd

> Skill para que un agente presente primero la respuesta y organice su salida con menos distracciones y rodeos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 61.2k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 66/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill/plugin de código abierto (MIT) de ayghri que hace las respuestas de los asistentes de código más directas («apto para TDAH, sin diagnóstico necesario»). Popular y activo (v0.4.1).

## ¿Qué hace?

Evita que el asistente entierre la respuesta: primero la acción, pasos numerados, referencias a archivo y línea, y sin relleno como «¡Espero que ayude!». Cambia el formato de las respuestas, no las capacidades del agente.

## ¿Cómo lo hace?

Instrucciones en formato skill/plugin; se instala pidiéndole al agente que siga el `AGENTS.md` del repositorio o con la guía `INSTALL.md` (incluye plugin de Claude Code).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Instalable como plugin. | Si tenías una copia anterior, desinstálala antes (el README lo indica). |
| [Codex CLI](codex.md) | Instalación guiada por `AGENTS.md` en agentes que lo leen (combinación por arquitectura). | Pide al agente que siga el AGENTS.md. |
| [Gemini CLI](gemini-cli.md) | Igual que con Codex (combinación por arquitectura). | Igual que arriba. |

Estado en GitHub: activo · último push 2026-10-19 · última versión publicada v0.4.1 (2026-10-19) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ayghri/i-have-adhd/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el modelo o plan del anfitrión sin API adicional |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. INSTALL.md documenta Claude Code, Codex y Antigravity CLI; la activación y always-on difieren entre hosts; es formato de comunicación, no intervención médica |
| Coste | Consumo del agente que ya utilizas. Usa el modelo o plan del anfitrión sin API adicional |
| Equipo | Preparación según la ruta elegida. Agente soportado; preferencia personal de presentación |

INSTALL.md documenta Claude Code, Codex y Antigravity CLI; la activación y always-on difieren entre hosts; es formato de comunicación, no intervención médica

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente soportado
- preferencia personal de presentación

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (text):**

```
claude plugin install i-have-adhd@i-have-adhd
```

Comando copiado literalmente de el README (sección «Tune it»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/ayghri/i-have-adhd/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar i-have-adhd para mi objetivo y necesito pasos guiados. Lee https://github.com/ayghri/i-have-adhd/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Activa el skill y pide explicar cómo crear una carpeta vacía para comparar la estructura de respuesta.

**Qué comprobar:** Puedes reconocer una respuesta directa y pasos delimitados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Reducir distracciones en instrucciones
- Organizar una explicación de trabajo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Reducir distracciones en instrucciones; Organizar una explicación de trabajo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** INSTALL.md documenta Claude Code, Codex y Antigravity CLI; la activación y always-on difieren entre hosts; es formato de comunicación, no intervención médica

## Stack y modelos

- **Stack:** Agente soportado; preferencia personal de presentación
- **Etiquetas:** `escritura` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ayghri/i-have-adhd/blob/main/README.md)
- [Fuente 2](https://github.com/ayghri/i-have-adhd/blob/main/INSTALL.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
