[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎬 rea-video

> Herramienta y skills para descomponer un video plano por plano y documentar cómo recrearlo en un archivo VIDEO.md.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.6k | Apache-2.0 | Python | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

rea-video, herramienta y skill para hacer ingeniería inversa de vídeos plano a plano, de @JuneYaooo. Licencia Apache-2.0. Es muy reciente (octubre de 2026, ~9.3k estrellas, v0.1.0).

## ¿Qué hace?

Descompone un vídeo plano a plano, determina si cada plano fue filmado, generado por IA o hecho con código, y explica cómo rehacerlo. Lo documenta en VIDEO.md, un formato abierto que los agentes leen por capas.

## ¿Cómo lo hace?

Funciona dentro de Claude Code, Codex o cualquier agente con shell, que instala la CLI. Requiere FFmpeg y Python 3.10+; opcionalmente se conecta un modelo con vídeo (Gemini o Doubao).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [remotion](remotion.md) | Rehacer planos hechos con código. (combinación por arquitectura) | Usa el desglose como guion. |
| [FFmpeg](ffmpeg.md) | Extracción de planos. | Instala FFmpeg. |
| [Claude Code](claude-code.md) | Agente anfitrión documentado. | Pide al agente que instale la CLI. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.1.0 (2026-11-11) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/JuneYaooo/rea-video/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Tools-only funciona offline; análisis con modelo o generación adicional cobra según proveedor y el agente usa su plan |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelo local no documentado. Las clasificaciones de material AI o filmado son estimaciones, no pruebas forenses; recrea técnicas con recursos de los que tengas derechos |
| Coste | El coste depende del proveedor o la ruta. Tools-only funciona offline; análisis con modelo o generación adicional cobra según proveedor y el agente usa su plan |
| Equipo | Preparación según la ruta elegida. Python >=3.10; FFmpeg; video autorizado; modelo con visión solo si eliges revisión AI |

Las clasificaciones de material AI o filmado son estimaciones, no pruebas forenses; recrea técnicas con recursos de los que tengas derechos

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python >=3.10
- FFmpeg
- video autorizado
- modelo con visión solo si eliges revisión AI

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
pip install "rea-video[ocr] @ git+https://github.com/JuneYaooo/rea-video"
```

Comando copiado literalmente de la documentación del repositorio (sección «安装（一次性）»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/JuneYaooo/rea-video/blob/main/skills/rea-video/references/setup.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar rea-video para mi objetivo y necesito pasos guiados. Lee https://github.com/JuneYaooo/rea-video/blob/main/skills/rea-video/references/setup.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Analiza un clip corto y contrasta los planos del VIDEO.md con el original.

**Qué comprobar:** Puedes revisar tiempos, estructura e hipótesis de técnica.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar ritmo de una pieza
- Preparar un plan de recreación con material propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar ritmo de una pieza; Preparar un plan de recreación con material propio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las clasificaciones de material AI o filmado son estimaciones, no pruebas forenses; recrea técnicas con recursos de los que tengas derechos

## Stack y modelos

- **Stack:** Python >=3.10; FFmpeg; video autorizado; modelo con visión solo si eliges revisión AI
- **Etiquetas:** `programatico` `agent-skills` `ai-video` `aigc-detection` `claude-code` `codex` `ffmpeg` `prompt-engineering`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video)
- 🌐 Web: <https://www.reavideo.ai/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/JuneYaooo/rea-video/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
