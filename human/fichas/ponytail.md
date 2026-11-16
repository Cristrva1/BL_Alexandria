[🏠 Inicio](../README.md) › [🧠 Skills, plugins y métodos para agentes](../categorias/02-skills-prompts-gu-as-de-agente.md) › Metodologías y harness para agentes de código

# 🧭 Ponytail

> Skill que hace que tu agente de código piense como un senior minimalista: el mejor código es el que no escribes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 191k | MIT | JavaScript | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill de DietrichGebert (MIT) que hace que el agente escriba solo el código necesario. Activa (v5.3.3); sus benchmarks son del propio proyecto.

## ¿Qué hace?

Antes de escribir código, sube una «escalera» de preguntas (¿hace falta?, ¿ya existe en el código?, ¿lo resuelve la plataforma?) y nunca recorta validación, gestión de errores, seguridad ni accesibilidad. El README dice que, frente a no usarla, reduce un 53 % el código, un 41 % el tiempo, un 26 % el coste y un 45 % los tokens [DATO NO VERIFICADO: benchmark propio en Claude Code, 39 tareas].

## ¿Cómo lo hace?

Se instala como plugin de Claude Code (`/plugin marketplace add DietrichGebert/ponytail`). En otros agentes se copia su `AGENTS.md` o se instala `skills/ponytail/SKILL.md`.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin oficial y entorno de sus benchmarks. | Instala el plugin. |
| [Codex CLI](codex.md) | Funciona copiando el AGENTS.md. | Copia el AGENTS.md al proyecto. |
| [andrej-karpathy-skills](andrej-karpathy-skills.md) | Principios compatibles de simplicidad y cambios mínimos (combinación por arquitectura). | Evita instrucciones contradictorias si usas ambos. |

**Notas:** Se quitó superpowers porque no hay integración.

Estado en GitHub: activo · último push 2026-10-29 · última versión publicada v5.3.3 (2026-10-29) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/DietrichGebert/ponytail/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Se consume el acceso del agente; las cifras de ahorro del autor no predicen el coste de tu sesión |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Codex tiene hooks propios; los adaptadores de solo instrucciones no ofrecen todos los comandos ni la banda de estado |
| Coste | Consumo del agente que ya utilizas. Se consume el acceso del agente; las cifras de ahorro del autor no predicen el coste de tu sesión |
| Equipo | Preparación según la ruta elegida. Agente compatible;  proyecto donde comparar un cambio pequeño |

Codex tiene hooks propios; los adaptadores de solo instrucciones no ofrecen todos los comandos ni la banda de estado

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
-  proyecto donde comparar un cambio pequeño

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (consulta la sintaxis original):**

```
/plugin marketplace add DietrichGebert/ponytail

/plugin install ponytail@ponytail
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/DietrichGebert/ponytail/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Ponytail para mi objetivo y necesito pasos guiados. Lee https://github.com/DietrichGebert/ponytail/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Solicita resolver un problema reutilizando el código existente antes de añadir funciones.

**Qué comprobar:** La propuesta explica qué reutiliza y presenta un diff limitado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar deuda técnica y detectar código que se puede eliminar
- Evaluar alternativas sencillas antes de crear una abstracción nueva

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar deuda técnica y detectar código que se puede eliminar; Evaluar alternativas sencillas antes de crear una abstracción nueva | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Codex tiene hooks propios; los adaptadores de solo instrucciones no ofrecen todos los comandos ni la banda de estado

## Stack y modelos

- **Stack:** Agente compatible;  proyecto donde comparar un cambio pequeño
- **Etiquetas:** `skills` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
- 🌐 Web: <https://ponytail.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/DietrichGebert/ponytail/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
