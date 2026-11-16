[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Observabilidad, evaluación y guardrails

# 🖥️ Claude-Code-Usage-Monitor

> Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a partir de la información disponible.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.8k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Claude Code Usage Monitor (`claude-monitor` en PyPI), monitor de terminal del uso de Claude Code, de @Maciek-roboblog. Licencia MIT. Es popular (~9k estrellas, v4.0.0) y su último cambio es de julio de 2026.

## ¿Qué hace?

Muestra en vivo el consumo de tokens, coste y mensajes por sesión, con previsiones de cuándo se alcanzará el límite y avisos. Captura los `rate_limits` oficiales mediante la statusline de Claude Code y, si no están disponibles, usa estimaciones locales etiquetadas. Ofrece planes predefinidos y un plan personalizado calculado con los últimos 8 días.

## ¿Cómo lo hace?

Se instala con `uv tool install claude-monitor` o `pip install claude-monitor` y se ejecuta con `claude-monitor`. Lee los registros locales de Claude Code con una interfaz Rich; no envía datos fuera.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Lee los datos locales y la statusline de Claude Code. | Instala el monitor y ejecútalo junto a tus sesiones. |
| [rtk](rtk.md) | Medir el efecto de reducir salidas de terminal. (combinación por arquitectura) | Compara el consumo antes y después de activar rtk. |
| [headroom](headroom.md) | Medir el ahorro de compresión de contexto. (combinación por arquitectura) | Compara el consumo con y sin `headroom wrap claude`. |
| [claude-token-efficient](claude-token-efficient.md) | Comprobar el efecto de un `CLAUDE.md` que pide respuestas concisas, cuyo README advierte que también añade tokens de entrada (combinación por arquitectura). | Mide antes y después de añadir el archivo al proyecto. |

**Notas:** Sin alternativas declaradas. Los límites por plan son estimaciones si no hay datos oficiales.

Estado en GitHub: activo · último push 2026-07-05 · última versión publicada v4.0.0 (2026-06-27) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor/blob/main/README.md) · [2](https://pypi.org/project/claude-monitor/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El monitor no necesita API de IA para leer datos; no amplía límites ni incluye el plan de Claude |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Las previsiones son estimaciones y las fuentes tienen distinta cobertura; es una integración de lectura de Claude Code y no un modelo alternativo |
| Coste | Sin pago a un modelo en la ruta básica. El monitor no necesita API de IA para leer datos; no amplía límites ni incluye el plan de Claude |
| Equipo | Preparación según la ruta elegida. uv o Python compatible; datos de uso de Claude Code |

Las previsiones son estimaciones y las fuentes tienen distinta cobertura; es una integración de lectura de Claude Code y no un modelo alternativo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- uv o Python compatible
- datos de uso de Claude Code

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
# Install directly from PyPI with uv (easiest)
uv tool install claude-monitor

# Run from anywhere
claude-monitor  # or cmonitor, ccmonitor for short
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Claude-Code-Usage-Monitor para mi objetivo y necesito pasos guiados. Lee https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre el monitor y compara una cifra con su etiqueta de procedencia y fecha.

**Qué comprobar:** Puedes distinguir consumo observado, estado oficial y previsión.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar el uso de una sesión
- Estudiar alertas y proyecciones de cuota

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar el uso de una sesión; Estudiar alertas y proyecciones de cuota | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las previsiones son estimaciones y las fuentes tienen distinta cobertura; es una integración de lectura de Claude Code y no un modelo alternativo

## Stack y modelos

- **Stack:** uv o Python compatible; datos de uso de Claude Code
- **Etiquetas:** `observabilidad` `app` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Maciek-roboblog/Claude-Code-Usage-Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
