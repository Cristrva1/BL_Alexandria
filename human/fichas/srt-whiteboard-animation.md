[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎨 srt-whiteboard-animation

> Skill para crear animaciones de pizarra con trazos y contenido organizados a partir de archivos de subtítulos SRT.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.6k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

SRT 白板动画, skill que convierte subtítulos SRT en vídeos de pizarra dibujados a mano siguiendo la narración, de @geeklee. Licencia MIT. Tiene ~5.6k estrellas (v1.0.0) y el README está en chino.

## ¿Qué hace?

Combina máscaras por zonas con trazos de pluma continuos: cada elemento aparece al ritmo de los subtítulos sobre papel color crema. Sirve para explicaciones, narraciones y cursos.

## ¿Cómo lo hace?

Trae scripts Python con entorno virtual propio (`python scripts/prepare_env.py`) y un parser de SRT con duración objetivo (`parse_srt.py`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [whisperX](whisperx.md) | Generar el SRT desde audio. (combinación por arquitectura) | Transcribe y exporta SRT. |
| [Kokoro](kokoro.md) | Locución del guion. (combinación por arquitectura) | Genera el audio. |
| [manim](manim-community.md) | Otro estilo explicativo. (combinación por arquitectura) | Elige según el formato. |

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-07-27 · última versión publicada v1.0.0 (2026-07-27) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/geeklee/srt-whiteboard-animation/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El render básico usa recursos propios y el agente; modelos o medios añadidos tienen condiciones independientes |
| Claude Code | Depende del recurso o la configuración |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | La función básica no necesita un modelo. Incluye metadatos Codex; no se confirma una instalación específica equivalente de otros hosts y el SRT no aporta automáticamente una narración |
| Coste | Consumo del agente que ya utilizas. El render básico usa recursos propios y el agente; modelos o medios añadidos tienen condiciones independientes |
| Equipo | Preparación según la ruta elegida. Agente con skill; Python y renderizadores del proyecto; SRT y recursos autorizados |

Incluye metadatos Codex; no se confirma una instalación específica equivalente de otros hosts y el SRT no aporta automáticamente una narración

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente con skill
- Python y renderizadores del proyecto
- SRT y recursos autorizados

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/geeklee/srt-whiteboard-animation/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar srt-whiteboard-animation para mi objetivo y necesito pasos guiados. Lee https://github.com/geeklee/srt-whiteboard-animation/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Usa tres líneas de subtítulos y revisa el orden de trazos y la sincronización con cada frase.

**Qué comprobar:** Puedes comparar tiempos del SRT y salida MP4.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Crear una explicación de pizarra
- Prototipar una secuencia narrada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Crear una explicación de pizarra; Prototipar una secuencia narrada | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Incluye metadatos Codex; no se confirma una instalación específica equivalente de otros hosts y el SRT no aporta automáticamente una narración

## Stack y modelos

- **Stack:** Agente con skill; Python y renderizadores del proyecto; SRT y recursos autorizados
- **Etiquetas:** `programatico` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [geeklee/srt-whiteboard-animation](https://github.com/geeklee/srt-whiteboard-animation)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/geeklee/srt-whiteboard-animation/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
