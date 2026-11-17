[🏠 Inicio](../README.md) › [📄 Presentaciones, diagramas y explicación visual](../categorias/31-presentaciones-diagramas.md) › Diagramas y documentación

# 🖥️ draw.io

> Editor de diagramas en el navegador o escritorio, sin servidor: diagramas de flujo, redes, UML y arquitectura cloud, con importación de Mermaid y PlantUML.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.4k | Apache-2.0 | JavaScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 69/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Editor de diagramas de código abierto (Apache-2.0) de JGraph, muy usado y activo. Los iconos, plantillas y librerías de formas tienen condiciones adicionales. El proyecto no acepta contribuciones externas.

## ¿Qué hace?

Permite crear diagramas de flujo, UML, ER, redes, arquitectura cloud, BPMN y organigramas con más de 10.000 formas, importar Mermaid, PlantUML y CSV, colaborar mediante almacenamiento en la nube y exportar a PNG, SVG, PDF y XML.

## ¿Cómo lo hace?

Funciona por completo en el cliente (navegador o draw.io Desktop con Electron); los diagramas se guardan como XML en archivos .drawio. El servidor oficial `jgraph/drawio-mcp` permite a asistentes de IA crear y abrir diagramas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | El repositorio oficial jgraph/drawio-mcp ofrece un servidor MCP y un plugin para Claude Code que generan diagramas .drawio editables. | Instala draw.io Desktop (para exportar); después añade el plugin o el MCP de draw.io al agente. |
| [Mermaid](mermaid.md) | draw.io importa diagramas Mermaid y los convierte en diagramas editables. | Escribe el diagrama en Mermaid; después usa Organizar > Insertar > Avanzado > Mermaid en draw.io. |
| [PlantUML](plantuml.md) | draw.io puede insertar diagramas PlantUML desde el menú avanzado. | Escribe el diagrama PlantUML; después insértalo con Organizar > Insertar > Avanzado > PlantUML. |
| [Kroki](kroki.md) | Kroki renderiza diagramas de Diagrams.net (draw.io) de forma experimental desde su API. | Despliega Kroki con su contenedor complementario; después envía el XML a `/diagramsnet`. |

Estado en GitHub: activo · último push 2026-11-04 · última versión publicada v32.6.10 (2026-11-04) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/jgraph/drawio/blob/dev/README.md) · [2](https://github.com/jgraph/drawio-mcp/blob/main/README.md) · [3](https://github.com/yuzutech/kroki/blob/main/README.adoc)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un sistema compatible y una copia de datos o archivos para la primera prueba.

1. Abre las descargas o la web de la aplicación enlazadas por el autor; elige la versión para tu sistema.
2. Sigue su guía de inicio y configura únicamente la función que necesitas probar.
3. Abre un archivo o caso pequeño, guarda un resultado y comprueba que puedes recuperarlo antes de importar material real.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/jgraph/drawio/blob/dev/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar draw.io para mi objetivo y necesito pasos guiados. Lee https://github.com/jgraph/drawio/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre app.diagrams.net en el navegador o instala draw.io Desktop, y crea un diagrama desde una plantilla..

**Qué comprobar:** Guardas un archivo .drawio editable o lo exportas a PNG, SVG o PDF..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- dibujar diagramas de arquitectura o redes con iconos de AWS, Azure o GCP
- convertir un diagrama Mermaid en uno editable a mano

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: dibujar diagramas de arquitectura o redes con iconos de AWS, Azure o GCP; convertir un diagrama Mermaid en uno editable a mano | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Código Apache-2.0, pero los iconos y plantillas no pueden usarse en productos de Atlassian sin permiso. El proyecto no acepta pull requests.

## Stack y modelos

- **Stack:** JavaScript
- **Etiquetas:** `diagrams` `editor` `javascript` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [jgraph/drawio](https://github.com/jgraph/drawio)
- 🌐 Web: <https://www.drawio.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/jgraph/drawio/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
