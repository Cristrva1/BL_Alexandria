[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de dominio: marketing, SEO y negocio

# 🎨 claude-seo

> Skills de Claude Code para revisar SEO técnico, contenido, presencia en buscadores de IA y otros aspectos de una web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 29.4k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 70/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plugin SEO gratuito y de código abierto (MIT) para Claude Code, de AgriciDaniel. Activo (v2.6.2), con 29 subskills y 20 agentes especialistas.

## ¿Qué hace?

Ejecuta una auditoría SEO completa en 10–15 minutos y entrega un plan priorizado: SEO técnico (rastreo, indexación, sitemaps, redirecciones, Core Web Vitals), calidad de contenido (E-E-A-T, páginas pobres), datos estructurados Schema.org, visibilidad en buscadores con IA (GEO), SEO local y de comercio electrónico. Hasta 17 agentes trabajan en paralelo y cada recomendación explica por qué importa.

## ¿Cómo lo hace?

Plugin de Claude Code (marketplace e instalación del plugin) con unos 30 comandos `/seo` en seis grupos, más extensiones opcionales como datos en vivo, generación de imágenes y análisis con PostHog.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Es un plugin de Claude Code. | Añade el marketplace e instala el plugin. |
| [posthog](posthog.md) | Extensión `seo-posthog` para cruzar datos de analítica. | Configura credenciales de PostHog de solo lectura. |
| [open-seo](open-seo.md) | Datos de palabras clave y posiciones vía MCP (combinación por arquitectura). | Conecta el MCP de OpenSEO al mismo agente. |

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v2.6.2 (2026-11-15) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/AgriciDaniel/claude-seo/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Plugin público MIT con consumo de Claude; extensiones de datos y versión privada tienen condiciones distintas |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. No promete mejorar ranking ni sustituir una auditoría humana; las funciones de datos en vivo requieren configuración adicional |
| Coste | El coste depende del proveedor o la ruta. Plugin público MIT con consumo de Claude; extensiones de datos y versión privada tienen condiciones distintas |
| Equipo | Preparación según la ruta elegida. Claude Code; Python 3.11–3.14; web propia; dependencias de navegador |

No promete mejorar ranking ni sustituir una auditoría humana; las funciones de datos en vivo requieren configuración adicional

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
- Python 3.11–3.14
- web propia
- dependencias de navegador

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo
/seo setup
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/AgriciDaniel/claude-seo/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar claude-seo para mi objetivo y necesito pasos guiados. Lee https://github.com/AgriciDaniel/claude-seo/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Usa setup y revisa una página de prueba para comprobar los hallazgos técnicos.

**Qué comprobar:** Puedes contrastar títulos, enlaces o schema con la página.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una auditoría SEO inicial
- Revisar indexabilidad de una landing

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una auditoría SEO inicial; Revisar indexabilidad de una landing | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No promete mejorar ranking ni sustituir una auditoría humana; las funciones de datos en vivo requieren configuración adicional

## Stack y modelos

- **Stack:** Claude Code; Python 3.11–3.14; web propia; dependencias de navegador
- **Etiquetas:** `dominio` `skill` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)
- 🌐 Web: <skool.com/ai-marketing-hub-pro>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/AgriciDaniel/claude-seo/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
