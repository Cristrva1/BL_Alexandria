[🏠 Inicio](../README.md) › [📄 Presentaciones, diagramas y explicación visual](../categorias/31-presentaciones-diagramas.md) › Diagramas y documentación

# 🎨 diagram-design

> Skill para que un agente cree diagramas explicativos con HTML y SVG, con criterios de composición y legibilidad.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 67.2k | MIT | HTML | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

## ¿Qué es?

diagram-design, skill que dibuja diagramas como un único archivo HTML + SVG autocontenido con tu marca, de @cathrynlavery. Licencia MIT. Creado en abril de 2026, tiene ~67k estrellas y sin releases.

## ¿Qué hace?

Ofrece 50 tipos de diagrama con estética cuidada (sin sombras, a diferencia del «Mermaid genérico») y exportación a PNG.

## ¿Cómo lo hace?

Se instala con `npx skills add cathrynlavery/diagram-design`. La exportación a PNG usa Playwright (`pip install playwright && playwright install chromium`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [playwright](playwright.md) | Rasterizado a PNG. | Instala Playwright y Chromium. |
| [Claude Code](claude-code.md) | Agente anfitrión. (combinación por arquitectura) | Instala la skill. |
| [Slidev](slidev.md) | Incrustar diagramas en presentaciones. (combinación por arquitectura) | Exporta SVG/PNG e insértalos. |

**Notas:** Sin alternativas declaradas. Tiene un grupo funcional con archify.

Estado en GitHub: activo · último push 2026-11-12 · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/cathrynlavery/diagram-design/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Usa el agente; el archivo puede evitar red usando fuentes del sistema en lugar de Google Fonts |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Portable en hosts Agent Skills; un solo HTML con SVG no implica que todas las fuentes o recursos externos se hayan incrustado |
| Coste | Consumo del agente que ya utilizas. Usa el agente; el archivo puede evitar red usando fuentes del sistema en lugar de Google Fonts |
| Equipo | Preparación según la ruta elegida. Agente compatible; proceso descrito; marca opcional; navegador |

Portable en hosts Agent Skills; un solo HTML con SVG no implica que todas las fuentes o recursos externos se hayan incrustado

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Agente compatible
- proceso descrito
- marca opcional
- navegador

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx skills add cathrynlavery/diagram-design
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/cathrynlavery/diagram-design/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar diagram-design para mi objetivo y necesito pasos guiados. Lee https://github.com/cathrynlavery/diagram-design/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera un diagrama de cinco pasos y revisa orden, etiquetas y legibilidad a tamaño móvil.

**Qué comprobar:** Puedes explicar cada relación y abrir el HTML.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Documentar un proceso comercial
- Explicar una arquitectura con SVG

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Documentar un proceso comercial; Explicar una arquitectura con SVG | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Portable en hosts Agent Skills; un solo HTML con SVG no implica que todas las fuentes o recursos externos se hayan incrustado

## Stack y modelos

- **Stack:** Agente compatible; proceso descrito; marca opcional; navegador
- **Etiquetas:** `diagramas` `skill` `html`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)
- 🌐 Web: <https://diagramdesign.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/cathrynlavery/diagram-design/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
