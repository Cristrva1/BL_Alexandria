[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de dominio: marketing, SEO y negocio

# 📈 Arcads AI Video Skill Pack

> Pack de skills para Claude Code y Cursor que crea anuncios en video e imagen con la API de Arcads (Seedance, Sora, Veo, Kling).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.7k | MIT | Python | 2026-08-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Puntuación de calidad** 39/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Paquete de skills (MIT) de «Mr. Paid Social» para crear videos e imágenes publicitarios con la cuenta de Arcads desde Claude Code o Cursor. El README usa enlaces de afiliado y promociona una comunidad de pago.

## ¿Qué hace?

Automatiza flujos creativos de Arcads: generación de imágenes y videos, anuncios estilo Pixar o plastilina con storyboard, guías de anuncios con canción y subtítulos incrustados en cualquier video. Pensado para equipos de compra de medios que producen muchas variantes.

## ¿Cómo lo hace?

Scripts Python 3.10+ (los generadores de imagen solo usan la biblioteca estándar) que llaman a la API de Arcads con tu clave. Los flujos avanzados requieren ffmpeg (unión y chroma key), jq, Node.js con `npx hyperframes` (subtítulos) y el paquete `openai-whisper` para transcripción.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FFmpeg](ffmpeg.md) | Necesario para unir clips y superponer elementos. | Instálalo antes de los flujos de video. |
| [HyperFrames](hyperframes.md) | Usado para incrustar subtítulos. | Requiere Node.js; se ejecuta con npx bajo demanda. |
| [whisper](whisper.md) | Transcribe el audio para los subtítulos. | `pip install openai-whisper`; el modelo medium necesita bastante memoria. |
| [Claude Code](claude-code.md) | Agente que ejecuta las skills. | Configura la clave de API de Arcads como variable de entorno, no en el chat. |

**Notas:** Requiere cuenta de pago de Arcads; cada generación consume créditos.

Estado en GitHub: activo · último push 2026-10-19 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. La generación usa la API de Arcads y el agente por separado; publicar en Meta añade credenciales y condiciones |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. El repositorio es gratuito pero no incluye generaciones ni acceso gratuito a todos los modelos; empieza por crear sin publicar |
| Coste | Consumo de APIs o servicios. La generación usa la API de Arcads y el agente por separado; publicar en Meta añade credenciales y condiciones |
| Equipo | Preparación según la ruta elegida. Claude Code o Cursor; cuenta y acceso API Arcads; presupuesto de generación |

El repositorio es gratuito pero no incluye generaciones ni acceso gratuito a todos los modelos; empieza por crear sin publicar

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code o Cursor
- cuenta y acceso API Arcads
- presupuesto de generación

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/krusemediallc/arcads-claude-code.git
cd arcads-claude-code
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Arcads AI Video Skill Pack para mi objetivo y necesito pasos guiados. Lee https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prepara un brief y revisa el coste y modelo antes de generar una única pieza de prueba.

**Qué comprobar:** Puedes identificar proveedor, entrada y resultado generado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Prototipar un anuncio vertical
- Preparar variantes de una imagen de producto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Prototipar un anuncio vertical; Preparar variantes de una imagen de producto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El repositorio es gratuito pero no incluye generaciones ni acceso gratuito a todos los modelos; empieza por crear sin publicar

## Stack y modelos

- **Stack:** Claude Code o Cursor; cuenta y acceso API Arcads; presupuesto de generación
- **Etiquetas:** `video` `image` `skills` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [mrpaidsocial/arcads-claude-code-mrpaidsocial](https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mrpaidsocial/arcads-claude-code-mrpaidsocial/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
