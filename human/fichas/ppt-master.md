[🏠 Inicio](../README.md) › [📄 Trabajar con documentos y presentaciones](../categorias/13-documentos-presentaciones.md) › Presentaciones

# 📊 ppt-master

> Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 76.8k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones usan el modelo del agente anfitrión; los scripts o servicios opcionales pueden tener requisitos adicionales. |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Modelos locales | La función básica no necesita un modelo. Una skill no trae un modelo. El modelo lo decide y ejecuta el agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. No incluye una cuenta de IA. Utiliza tu acceso al agente, con sus límites y su autenticación. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

Usar la skill consume los límites del agente anfitrión. Servicios de terceros y generaciones externas se pagan por separado cuando apliquen.

## Qué puedes hacer con él

Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos. Necesita un agente con acceso a un modelo; los servicios opcionales de imágenes o contenido se revisan por separado.

## Por qué destaca

Entrega un PPTX realmente editable (formas y textos nativos) en lugar de un PDF plano, ahorrando el tedio de maquetar slides desde cero; útil para borradores rápidos a partir de un informe.

## Cómo funciona

El agente prepara y genera las diapositivas con las herramientas del proyecto.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un agente compatible y el entorno Python de la ruta documentada.

1. Añade la skill o abre las instrucciones del proyecto en tu agente.
2. Entrega un documento fuente y especifica audiencia, contenido y formato de la presentación.
3. Genera un PPTX editable y ábrelo para revisar contenido y diseño. Las generaciones externas de imágenes se configuran por separado.

**Comando de entrada documentado:**

```shell
npx skills add hugohe3/ppt-master
```

Comando presente en el README revisado; no es una prueba de instalación.

[Instrucciones originales de instalación](https://github.com/hugohe3/ppt-master/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ppt-master para mi objetivo y necesito pasos guiados. Lee https://github.com/hugohe3/ppt-master/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Pasar un informe Markdown a un borrador de slides corporativos en segundos
- Generar una primera versión editable de una presentación a partir de notas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres PPTX editable de Office rápido | prefieres slides web por código (reveal.js) o control de diseño pixel-perfect |

## Stack y modelos

- **Stack:** Python, python-pptx
- **Etiquetas:** `slides` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [markitdown](markitdown.md) | 195k | Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Presenton](presenton.md) | 11.9k | Generador de presentaciones con IA, open source y con API, alternativa a Gamma o Beautiful.ai. |

## Enlaces

- 🐙 GitHub: [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)
- 🌐 Web: <https://hugohe3.github.io/ppt-master-examples/>
- 🧪 Receta: [Documentos → presentaciones](../playbooks/documentos-presentaciones.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/hugohe3/ppt-master/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
