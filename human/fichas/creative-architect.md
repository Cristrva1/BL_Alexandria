[🏠 Inicio](../README.md) › [🎨 Skills de diseño, contenido y especialidades](../categorias/27-skills-especializadas.md) › Skills de diseño para agentes

# 🎨 Creative Architect

> Plugin de dirección de arte para Claude Code: prepara fotos de producto, UGC y anuncios con proveedores de imagen o video.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 24 | MIT | Markdown | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## ¿Qué es?

Plugin para Claude Code (MIT) de Hainrixz, documentado en español, que actúa como director de arte y productor de imagen y video con IA. Muy nuevo y con poca adopción (v1.0.1, 24 estrellas).

## ¿Qué hace?

Produce fotos de producto, avatares de marca, UGC, animación y anuncios con estructura probada mediante un flujo en pasos que incluye revisar antipatrones y la fidelidad al producto real. Informa del coste estimado en créditos cuando el proveedor lo permite.

## ¿Cómo lo hace?

Se instala como plugin (`/plugin marketplace add Hainrixz/creative-architect`) y genera con el proveedor conectado: Higgsfield (conector MCP o CLI), Magnific (MCP HTTP), OpenAI u otros.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Es un plugin de Claude Code. | Instala el plugin y conecta al menos un proveedor de generación. |
| [HyperFrames](hyperframes.md) | Montar los clips generados en piezas de video (combinación por arquitectura). | Genera primero; compón después. |
| [remotion](remotion.md) | Alternativa programática para componer anuncios (combinación por arquitectura). | Igual que arriba. |

**Notas:** El README dice que el repositorio es privado, pero es público en GitHub: documentación desactualizada. Los proveedores son de pago.

Estado en GitHub: activo · último push 2026-10-25 · última versión publicada v1.0.1 (2026-10-17) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Hainrixz/creative-architect/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El trabajo de brief usa Claude; generar usa Higgsfield, Magnific, OpenAI u otro proveedor con sus propios planes o APIs |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. No incluye créditos audiovisuales ni acceso idéntico por MCP, CLI y REST; generar una pieza y publicarla son acciones diferentes |
| Coste | El coste depende del proveedor o la ruta. El trabajo de brief usa Claude; generar usa Higgsfield, Magnific, OpenAI u otro proveedor con sus propios planes o APIs |
| Equipo | Preparación según la ruta elegida. Claude Code; brief; proveedor de imagen o video solo al generar; presupuesto |

No incluye créditos audiovisuales ni acceso idéntico por MCP, CLI y REST; generar una pieza y publicarla son acciones diferentes

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
- brief
- proveedor de imagen o video solo al generar
- presupuesto

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (text):**

```
/plugin marketplace add Hainrixz/creative-architect
/plugin install creative-architect@creative-architect
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Hainrixz/creative-architect/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Creative Architect para mi objetivo y necesito pasos guiados. Lee https://github.com/Hainrixz/creative-architect/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Prepara la dirección de arte y revisa modelo, coste y referencia antes de generar una pieza.

**Qué comprobar:** Puedes identificar proveedor y resultado y decidir una iteración concreta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una foto de producto
- Planificar un anuncio UGC

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una foto de producto; Planificar un anuncio UGC | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No incluye créditos audiovisuales ni acceso idéntico por MCP, CLI y REST; generar una pieza y publicarla son acciones diferentes

## Stack y modelos

- **Stack:** Claude Code; brief; proveedor de imagen o video solo al generar; presupuesto
- **Etiquetas:** `direccion-de-arte` `fotos-producto` `ugc` `claude-code` `creative-architect`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Hainrixz/creative-architect](https://github.com/Hainrixz/creative-architect)
- 🌐 Web: <https://www.tododeia.com/community/creative-architect>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Hainrixz/creative-architect/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
