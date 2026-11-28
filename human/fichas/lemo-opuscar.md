[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎨 lemo-opuscar

> Biblioteca de estilos para video por código orientada a Claude,con licencias diferentes para código,guías y medios.

## Cuándo elegir esta ficha

Útil como biblioteca de estilos para Claude con derechos separados; no ofrezca demos o guías para redistribuir por la licencia del código. Las alternativas son plantillas o pautas para producir, parciales respecto de su catálogo estético.

Referencia de consulta del catálogo.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/lemomo-ai/lemo-opuscar/blob/439b98af08b04400f8fd8a8dd19cd773c0c96532/README.md) · [Fuente 2](https://github.com/lemomo-ai/lemo-opuscar/commit/439b98af08b04400f8fd8a8dd19cd773c0c96532) · [Fuente 3](https://github.com/lemomo-ai/lemo-opuscar/blob/main/README.md)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.3k | MIT (código) + CC-BY-NC-4.0 (docs) + CC-BY-4.0 (demos) | JavaScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 65/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** MIT (código) + CC-BY-NC-4.0 (docs) + CC-BY-4.0 (demos). La documentación es solo para uso no comercial. Fuente: [LICENSE](https://github.com/lemomo-ai/lemo-opuscar/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Lemo-Opuscar, colección de 99 estilos cinematográficos para que un agente de código haga películas cortas íntegramente con código, de Lemomo (@lemomo_ai). Licencia mixta (por eso GitHub muestra NOASSERTION): código MIT, documentación (incluidos los STYLE.md de cada estilo) CC BY-NC 4.0 y películas demo CC BY 4.0. Tiene ~17k estrellas (v2.0.0).

## ¿Qué hace?

Eliges un estilo, aportas tu historia y el agente produce la película con una demo de referencia para cada estilo.

## ¿Cómo lo hace?

Se instala como plugin de Claude Code (`claude plugin marketplace add lemomo-ai/lemo-opuscar`). Requiere Node 20+, FFmpeg 7+ y Python 3.11+ (o uv). Está pensado para modelos Claude con esfuerzo alto.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin oficial. | Añade el marketplace e instala el plugin. |
| [FFmpeg](ffmpeg.md) | Render (versión 7+). | Instala FFmpeg 7 o superior. |
| [three.js](three-js.md) | Escenas 3D en código. (combinación por arquitectura) | Según el estilo elegido. |

**Notas:** Sin alternativas declaradas. La documentación de los estilos es no comercial (CC BY-NC).

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v2.0.0 (2026-11-12) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/lemomo-ai/lemo-opuscar/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Código MIT; prompts y guías actuales CC BY-NC con permiso adicional acotado para crear films; otros usos comerciales pueden requerir licencia |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Compatibilidad por confirmar |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | Modelos locales documentados. El autor lo orienta a Claude y advierte diferencias con otros modelos; demos, guías, voz y assets no comparten una licencia única; Kokoro local no sustituye el agente |
| Coste | El coste depende del proveedor o la ruta. Código MIT; prompts y guías actuales CC BY-NC con permiso adicional acotado para crear films; otros usos comerciales pueden requerir licencia |
| Equipo | Preparación según la ruta elegida. Claude Code; dependencias del estilo; material propio; Kokoro según voz |

El autor lo orienta a Claude y advierte diferencias con otros modelos; demos, guías, voz y assets no comparten una licencia única; Kokoro local no sustituye el agente

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
- dependencias del estilo
- material propio
- Kokoro según voz

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (sh):**

```
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/lemomo-ai/lemo-opuscar/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar lemo-opuscar para mi objetivo y necesito pasos guiados. Lee https://github.com/lemomo-ai/lemo-opuscar/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Elige un estilo y crea una escena de prueba revisando créditos antes de adaptar el resto.

**Qué comprobar:** Puedes identificar código, estilo y assets de la salida.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar una dirección visual para un video
- Preparar una pieza por código

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar una dirección visual para un video; Preparar una pieza por código | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El autor lo orienta a Claude y advierte diferencias con otros modelos; demos, guías, voz y assets no comparten una licencia única; Kokoro local no sustituye el agente

## Stack y modelos

- **Stack:** Claude Code; dependencias del estilo; material propio; Kokoro según voz
- **Etiquetas:** `programatico` `skill` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)
- 🌐 Web: <https://lemomo-ai.github.io/lemo-opuscar/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/lemomo-ai/lemo-opuscar/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
