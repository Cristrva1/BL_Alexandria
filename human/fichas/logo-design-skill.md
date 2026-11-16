[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 logo-design-skill

> Skill para diseñar logotipos con un agente, desde la idea y las referencias hasta SVG y comprobaciones de diseño.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.9k | MIT | HTML | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Skill de diseño de logotipos (MIT) de Kaan Kızıltuğ para Claude y otros agentes compatibles con Agent Skills (Gemini CLI, Codex CLI, Cursor, GitHub Copilot). Activa (v1.4.5).

## ¿Qué hace?

Convierte al agente en diseñador de identidad, desde el brief hasta SVG de producción y guía de marca: proceso, construcción geométrica, correcciones ópticas, color, tipografía y presentación. Incluye una biblioteca de referencia con más de 1.400 logotipos SVG reales clasificados, para estudiar convenciones y evitar parecidos, no para copiar.

## ¿Cómo lo hace?

Herramientas Python 3.8+ sin dependencias que auditan un SVG contra principios de logotipos, generan hojas de concepto y de prueba (16 px, una tinta, invertido, espejo, estantería de competidores), tableros de presentación con mockups y el set de favicon/app-icon/manifest. La exportación a PNG/ICO usa el renderizador disponible (cairosvg u otros). Se instala como plugin de Claude Code.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin oficial. | `/plugin marketplace add kaankiziltug/logo-design-skill`. |
| [Gemini CLI](gemini-cli.md) | Agente compatible citado. | Copia la skill al directorio de skills. |
| [Codex CLI](codex.md) | Agente compatible citado. | Igual que arriba. |

**Notas:** Revisa los derechos de los logotipos de referencia: solo deben usarse para estudio.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v1.4.5 (2026-10-20) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el plan del agente; exportación y referencias tienen requisitos y licencias separados |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. El formato es portable entre hosts Agent Skills; un diseño generado necesita revisión de identidad, originalidad y posibles coincidencias de marca |
| Coste | Consumo del agente que ya utilizas. Usa el plan del agente; exportación y referencias tienen requisitos y licencias separados |
| Equipo | Preparación según la ruta elegida. Agente compatible; brief de marca; Python para utilidades; renderer opcional |

El formato es portable entre hosts Agent Skills; un diseño generado necesita revisión de identidad, originalidad y posibles coincidencias de marca

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
- brief de marca
- Python para utilidades
- renderer opcional

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.
4. Configura la cuenta, el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (text):**

```
/plugin marketplace add kaankiziltug/logo-design-skill
```

Comando copiado literalmente de el README (sección «Claude Code — plugin marketplace»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar logo-design-skill para mi objetivo y necesito pasos guiados. Lee https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea tres bocetos SVG simples y prueba legibilidad a tamaño pequeño.

**Qué comprobar:** Puedes comparar silueta, espaciado y contraste.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar un logotipo
- Preparar variantes monocromas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar un logotipo; Preparar variantes monocromas | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El formato es portable entre hosts Agent Skills; un diseño generado necesita revisión de identidad, originalidad y posibles coincidencias de marca

## Stack y modelos

- **Stack:** Agente compatible; brief de marca; Python para utilidades; renderer opcional
- **Etiquetas:** `skills` `skill` `html`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/kaankiziltug/logo-design-skill/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
