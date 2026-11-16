[🏠 Inicio](../README.md) › [🎬 Video con código y agentes creativos](../categorias/30-video-codigo-agentes.md) › Skills y métodos de producción audiovisual

# 🎞️ Remotion Superpowers

> Orquestación de video con Remotion y servicios audiovisuales externos; requiere claves y revisar costes por etapa.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 168 | MIT | Shell | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; se instala dentro de un agente (skill, plugin o MCP); requiere clave de API

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Remotion Superpowers, plugin que conecta voz en off, música, efectos, material de archivo, imágenes y clips de IA, subtítulos y un ciclo de revisión con Remotion a través del agente, de DojoCodingLabs. Licencia MIT. Es de nicho (~170 estrellas, v2.3.0).

## ¿Qué hace?

Convierte un prompt en un MP4 terminado orquestando servicios audiovisuales externos y las skills oficiales de Remotion y ElevenLabs.

## ¿Cómo lo hace?

Requiere Node.js 22.18+ y las skills oficiales, que instala `/setup`. El servidor opcional de ElevenLabs usa uv y está deprecado en origen; varias funciones requieren claves de servicios externos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [remotion](remotion.md) | Motor de render. | Crea el proyecto Remotion. |
| [Remotion Agent Skills](skills-remotion.md) | Skills oficiales sobre las que se construye. | Las instala `/setup`. |
| [Claude Code](claude-code.md) | Agente anfitrión del plugin. (combinación por arquitectura) | Instala el plugin. |
| [ElevenLabs (SDK de Python)](elevenlabs-python.md) | Combinación recíproca: ElevenLabs (SDK de Python) lo enlaza como «El plugin usa las skills oficiales de ElevenLabs para locución, efectos y música. (combinación por arquitectura)». | Orden indicado desde ElevenLabs (SDK de Python): Configura la clave de ElevenLabs al instalar el plugin. |

**Notas:** Alternativas (elige una): openmontage, video-use. Depende de servicios de pago.

Estado en GitHub: activo · último push 2026-10-29 · última versión publicada v2.3.0 (2026-10-27) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/DojoCodingLabs/remotion-superpowers/blob/main/README.md)</sub>

## Ver similares

Grupo **Skills y flujos de producción de video**: Remotion Superpowers ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OpenMontage](openmontage.md) ⭐ recomendado | 72 | Si buscas esto: pipelines y herramientas para producir video con un agente,recursos propios,modelos locales o servicios opcionales. |
| 2 | [video-use](video-use.md) | 60 | Si buscas esto: edición con agentes y FFmpeg,con transcripción documentada mediante ElevenLabs Scribe. |
| 3 | **Remotion Superpowers** (esta ficha) | 48 | Si buscas esto: orquestación de video con Remotion y servicios audiovisuales externos; requiere claves y revisar costes por etapa. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. ElevenLabs, KIE y TwelveLabs aparecen como claves necesarias del flujo; modelos, Remotion y agente tienen condiciones distintas |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | Modelos locales documentados. Las captions pueden usar Whisper local pero el conjunto no es enteramente local; hooks y subagentes son extras de Claude Code y no se heredan en todos los hosts |
| Coste | Consumo de APIs o servicios. ElevenLabs, KIE y TwelveLabs aparecen como claves necesarias del flujo; modelos, Remotion y agente tienen condiciones distintas |
| Equipo | Preparación según la ruta elegida. Node 22.18+; Remotion; skills oficiales; claves de medios; uv para MCP opcional |

Las captions pueden usar Whisper local pero el conjunto no es enteramente local; hooks y subagentes son extras de Claude Code y no se heredan en todos los hosts

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node 22.18+
- Remotion
- skills oficiales
- claves de medios
- uv para MCP opcional

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
codex plugin marketplace add DojoCodingLabs/remotion-superpowers
codex plugin add remotion-superpowers@remotion-superpowers
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/DojoCodingLabs/remotion-superpowers/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Remotion Superpowers para mi objetivo y necesito pasos guiados. Lee https://github.com/DojoCodingLabs/remotion-superpowers/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta setup y prepara un guion corto con estimación de servicios antes de generar.

**Qué comprobar:** Puedes identificar claves, proveedores y resultado de cada etapa.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un video narrado
- Combinar clips y subtítulos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un video narrado; Combinar clips y subtítulos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Las captions pueden usar Whisper local pero el conjunto no es enteramente local; hooks y subagentes son extras de Claude Code y no se heredan en todos los hosts

## Stack y modelos

- **Stack:** Node 22.18+; Remotion; skills oficiales; claves de medios; uv para MCP opcional
- **Etiquetas:** `video` `skills` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OpenMontage](openmontage.md) | 80.5k | Pipelines y herramientas para producir video con un agente,recursos propios,modelos locales o servicios opcionales. |
| [video-use](video-use.md) | 31.1k | Edición con agentes y FFmpeg,con transcripción documentada mediante ElevenLabs Scribe. |

## Enlaces

- 🐙 GitHub: [DojoCodingLabs/remotion-superpowers](https://github.com/DojoCodingLabs/remotion-superpowers)
- 🌐 Web: <https://github.com/DojoCodingLabs/remotion-superpowers>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/DojoCodingLabs/remotion-superpowers/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
