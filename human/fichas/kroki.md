[🏠 Inicio](../README.md) › [📄 Presentaciones, diagramas y explicación visual](../categorias/31-presentaciones-diagramas.md) › Diagramas y documentación

# ⚙️ Kroki

> Servidor que unifica más de 25 lenguajes de diagramas (PlantUML, Mermaid, D2, Graphviz, Excalidraw…) detrás de una sola API HTTP que devuelve SVG o PNG.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.4k | MIT | JavaScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Servidor de código abierto (MIT) de Yuzutech, con instancia pública gratuita en kroki.io y despliegue propio con Docker. Activo.

## ¿Qué hace?

Ofrece una API unificada para renderizar BlockDiag, BPMN, Bytefield, C4 (con PlantUML), D2, DBML, Diagrams.net (experimental), Ditaa, Erd, Excalidraw, GraphViz, Mermaid, Nomnoml, Pikchr, PlantUML, SvgBob, Vega, WaveDrom y otros a SVG, PNG o PDF según el tipo.

## ¿Cómo lo hace?

El gateway en Java incluye la mayoría de herramientas; Mermaid, BPMN, Excalidraw y Diagrams.net se ejecutan en contenedores complementarios (Node.js) que se conectan por variables de entorno en Docker Compose. Los diagramas se envían por POST o codificados en la URL de un GET.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [PlantUML](plantuml.md) | Kroki incluye PlantUML (y C4-PlantUML) en su servidor principal. | Ejecuta Kroki; después usa el endpoint `/plantuml/svg`. |
| [D2](d2.md) | Kroki incluye D2 entre sus lenguajes soportados. | Ejecuta Kroki; después usa el endpoint `/d2/svg`. |
| [Mermaid](mermaid.md) | Kroki renderiza Mermaid con el contenedor complementario `yuzutech/kroki-mermaid`. | Despliega Kroki y `kroki-mermaid` con Docker Compose; después usa `/mermaid/svg`. |
| [Excalidraw](excalidraw.md) | Kroki renderiza Excalidraw con el contenedor complementario `yuzutech/kroki-excalidraw`. | Despliega Kroki y `kroki-excalidraw`; después envía el JSON a `/excalidraw/svg`. |
| [draw.io](drawio.md) | Kroki renderiza diagramas de Diagrams.net (draw.io) de forma experimental con un contenedor complementario. | Despliega Kroki con el complemento de Diagrams.net; después usa `/diagramsnet/svg`. |

**Notas:** Útil como backend para Asciidoctor, MkDocs y otros generadores; autoalojarlo evita enviar diagramas a kroki.io.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.36.0 (2026-11-09) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/yuzutech/kroki/blob/main/README.adoc) · [2](https://docs.kroki.io/kroki/setup/install/)</sub>

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

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (consulta la sintaxis original):**

```
docker run -d -p 8000:8000 yuzutech/kroki
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/yuzutech/kroki/blob/main/README.adoc)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Kroki para mi objetivo y necesito pasos guiados. Lee https://github.com/yuzutech/kroki/blob/main/README.adoc. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta `docker run -d -p 8000:8000 yuzutech/kroki` y abre `http://localhost:8000/plantuml/svg/` con un diagrama codificado..

**Qué comprobar:** Obtienes el SVG del diagrama desde tu propio servidor..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- renderizar diagramas de varios lenguajes en una wiki o generador de documentación
- autoalojar el renderizado para no enviar diagramas a servicios públicos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: renderizar diagramas de varios lenguajes en una wiki o generador de documentación; autoalojar el renderizado para no enviar diagramas a servicios públicos | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** JavaScript, package.json, pom.xml
- **Etiquetas:** `diagrams` `api` `self-hosted` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [yuzutech/kroki](https://github.com/yuzutech/kroki)
- 🌐 Web: <https://kroki.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/yuzutech/kroki/blob/main/README.adoc)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
