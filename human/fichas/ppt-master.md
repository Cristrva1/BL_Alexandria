[🏠 Inicio](../README.md) › [📄 Presentaciones, diagramas y explicación visual](../categorias/31-presentaciones-diagramas.md) › Presentaciones

# 📊 ppt-master

> Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 76.8k | MIT | Python | 2026-06-23 |

**Ejecución** 🔀 híbrido · **Rol** 🎨 skill/prompt · **Setup** 🟢 fácil

**Puntuación de calidad** 69/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

PPT Master, workflow (skill) que genera presentaciones PowerPoint nativas y editables a partir de cualquier documento, de @hugohe3. Licencia MIT. Creado en diciembre de 2025, tiene ~77k estrellas (v6.9.0); el README incluye patrocinios de servicios de reventa de APIs.

## ¿Qué hace?

Dentro de un agente («haz una presentación de este PDF») analiza, diseña y exporta localmente un PPTX con patrones, formas nativas y gráficos y tablas con datos. También extrae plantillas de marca o rellena una existente.

## ¿Cómo lo hace?

Requiere Python 3.10–3.14 y `pip install -r requirements.txt` (Pandoc opcional). Funciona con cualquier agente y modelo (Kimi, Gemini, GPT, Claude).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Agente que ejecuta el workflow. (combinación por arquitectura) | Clona el repo e invoca la skill. |
| [markitdown](markitdown.md) | Convertir documentos fuente. (combinación por arquitectura) | Preprocesa a Markdown. |
| [Pandoc](pandoc.md) | Conversión de documentos. | Instala Pandoc si se necesita. |

**Notas:** Alternativas (elige una): presenton.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v6.9.0 (2026-11-08) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/hugohe3/ppt-master/blob/main/README.md)</sub>

## Ver similares

Grupo **Generación de presentaciones con IA**: ppt-master ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **ppt-master** (esta ficha) ⭐ recomendado | 69 | Si buscas esto: herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos. |
| 2 | [Presenton](presenton.md) | 60 | Si buscas esto: generador de presentaciones con IA, open source y con API, alternativa a Gamma o Beautiful.ai. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. Usa el agente y posibles proveedores de imagen o voz; no incluye créditos ni acceso a patrocinadores |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Dentro del agente: skills o instrucciones |
| Antigravity | Depende del recurso o la configuración |
| Modelos locales | Modelo local no documentado. Claude Code es la ruta más probada por el autor y Codex figura como CLI compatible; logos de patrocinadores no prueban integración ni precio de sus servicios |
| Coste | El coste depende del proveedor o la ruta. Usa el agente y posibles proveedores de imagen o voz; no incluye créditos ni acceso a patrocinadores |
| Equipo | Preparación según la ruta elegida. Python 3.10–3.14; agente con archivos; dependencias; documento y plantilla autorizados |

Claude Code es la ruta más probada por el autor y Codex figura como CLI compatible; logos de patrocinadores no prueban integración ni precio de sus servicios

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10–3.14
- agente con archivos
- dependencias
- documento y plantilla autorizados

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ppt-master para mi objetivo y necesito pasos guiados. Lee https://github.com/hugohe3/ppt-master/blob/main/docs/getting-started.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Genera tres diapositivas de un texto breve y revisa cifras, editabilidad y fuentes en PowerPoint.

**Qué comprobar:** Puedes editar formas y comprobar que el contenido coincide con el documento.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar una presentación de un informe
- Adaptar una plantilla corporativa

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar una presentación de un informe; Adaptar una plantilla corporativa | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Claude Code es la ruta más probada por el autor y Codex figura como CLI compatible; logos de patrocinadores no prueban integración ni precio de sus servicios

## Stack y modelos

- **Stack:** Python 3.10–3.14; agente con archivos; dependencias; documento y plantilla autorizados
- **Etiquetas:** `slides` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Presenton](presenton.md) | 11.9k | Generador de presentaciones con IA, open source y con API, alternativa a Gamma o Beautiful.ai. |

## Enlaces

- 🐙 GitHub: [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)
- 🌐 Web: <https://hugohe3.github.io/ppt-master-examples/>
- 🧪 Receta: [Documentos → presentaciones](../playbooks/documentos-presentaciones.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/hugohe3/ppt-master/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
