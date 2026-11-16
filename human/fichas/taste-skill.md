[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🍷 taste-skill

> Skill design-taste-frontend para dirección visual y revisión de sitios; otros skills del pack antiguo se movieron a repos propios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 116k | MIT | JavaScript | 2026-06-23 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## ¿Qué es?

Skill de agente (MIT) de Leonxlnx para que los agentes construyan webs de empresa de calidad profesional en lugar de landings genéricas. Muy popular y activa (v2.5.1), con patrocinadores.

## ¿Qué hace?

Parte de un único sistema (plantilla HTML y CSS con una sección por pantalla y bordes de contenido iguales), incluye fragmentos de interfaz reales y fotografías de archivos abiertos con crédito, y ejecuta un verificador antes de entregar. Incluye variantes como minimalista, brutalista industrial o una para Stitch.

## ¿Cómo lo hace?

Se instala con `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` o como plugin de Claude Code. Sus scripts requieren Node 22+ y Chrome, Edge o Chromium instalado; ffmpeg es opcional para generar WebP.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Plugin y skill nativos. | Node 22+ y Chrome antes de usarla. |
| [FFmpeg](ffmpeg.md) | Dependencia opcional para exportar WebP. | Añádelo al PATH si necesitas WebP. |
| [Stitch Skills](stitch-skills.md) | Trae una variante `stitch-design-taste` para trabajar con Stitch. | Configura antes el MCP de Stitch. |

**Notas:** Alternativas (elige una): ui-ux-pro-max-skill, impeccable, hallmark.

Estado en GitHub: activo · último push 2026-11-08 · última versión publicada v2.5.1 (2026-11-07) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Leonxlnx/taste-skill/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Los scripts no piden API; el agente usa su plan y los recursos conservan sus licencias |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Actualmente contiene design-taste-frontend y otros skills se movieron a repos propios; no se debe presentar el pack antiguo completo como contenido actual |
| Coste | Consumo del agente que ya utilizas. Los scripts no piden API; el agente usa su plan y los recursos conservan sus licencias |
| Equipo | Preparación según la ruta elegida. Node 22+; Chrome, Edge o Chromium; agente; brief de sitio |

Actualmente contiene design-taste-frontend y otros skills se movieron a repos propios; no se debe presentar el pack antiguo completo como contenido actual

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node 22+
- Chrome, Edge o Chromium
- agente
- brief de sitio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Leonxlnx/taste-skill/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar taste-skill para mi objetivo y necesito pasos guiados. Lee https://github.com/Leonxlnx/taste-skill/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Diseña una página de prueba con referencias acreditadas y ejecuta su comprobación visual.

**Qué comprobar:** Puedes revisar composición, texto y créditos de recursos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una web de empresa
- Revisar dirección visual de una landing

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una web de empresa; Revisar dirección visual de una landing | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Actualmente contiene design-taste-frontend y otros skills se movieron a repos propios; no se debe presentar el pack antiguo completo como contenido actual

## Stack y modelos

- **Stack:** Node 22+; Chrome, Edge o Chromium; agente; brief de sitio
- **Etiquetas:** `skills` `design` `javascript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ui-ux-pro-max-skill](ui-ux-pro-max-skill.md) | 150k | Conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para que las interfaces que genera dejen de verse a "plantilla". |
| [impeccable](impeccable.md) | 110k | Vocabulario y playbooks de diseño para agentes, con detector determinista y hooks según herramienta. |
| [hallmark](hallmark.md) | 55.1k | Skill de diseño para agentes que ayuda a construir interfaces con decisiones visuales más específicas y coherentes. |

## Enlaces

- 🐙 GitHub: [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
- 🌐 Web: <https://tasteskill.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Leonxlnx/taste-skill/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
