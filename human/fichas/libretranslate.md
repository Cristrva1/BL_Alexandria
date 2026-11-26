[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Alojamiento y backend

# ⚙️ LibreTranslate

> Traduce texto con una interfaz web y una API que puedes alojar en tu equipo usando modelos de traducción de Argos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.8k | AGPL-3.0 | Python | 2026-11-22 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio · **MCP** 🔌 sí

**Nivel:** 3 Avanzado — preparación media; necesita GPU

**Puntuación de calidad** 57/100 · métricas del 2026-11-26 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Un servicio de traducción que ofrece una interfaz web y una API HTTP para aplicaciones.

## ¿Qué hace?

Traduce texto con una interfaz web y una API que puedes alojar en tu equipo usando modelos de traducción de Argos.

## ¿Cómo lo hace?

Recibe texto, elige el par de idiomas y lo traduce con Argos Translate en la instancia que configuraste.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v1.9.6 (2026-05-26) · licencia declarada AGPL-3.0 (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/LibreTranslate/LibreTranslate/blob/84cd56c061a7ba3955b49efdaee2ac54dcbca07f/README.md) · [2](https://docs.libretranslate.com/guides/installation/) · [3](https://docs.libretranslate.com/guides/mcp_server/) · [4](https://docs.libretranslate.com/) · [5](https://pypi.org/project/libretranslate/1.9.6/) · [6](https://github.com/LibreTranslate/LibreTranslate/blob/main/LICENSE)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La instancia propia no necesita clave de un proveedor de IA. El servicio alojado sí exige su propia clave para integrar la API. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. Argos ejecuta los modelos de traducción en la instancia; estos no son un chat ni un LLM de propósito general. |
| Coste | El coste depende del proveedor o la ruta. Código AGPL-3.0 y consumo de tu equipo al autoalojar; alojamiento y API gestionada tienen condiciones propias. |
| Equipo | Preparación según la ruta elegida. CPU y disco para modelos de idiomas. La aceleración CUDA es una opción distinta. |
| Otras rutas | MCP oficial documentado para Claude y OpenCode. Revisa el endpoint: el ejemplo apunta al servicio alojado. |

El proyecto documenta un conector MCP para Claude y OpenCode. No se verificó configuración específica de Claude Code, Codex o Antigravity; un plan no incluye acceso a la instancia alojada.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Entorno Python compatible con la versión elegida o Docker.
- Conexión para descargar paquetes y modelos de idiomas; espacio para los idiomas seleccionados.

1. Elige una versión y prepara un entorno Python aislado o Docker; abre la guía de instalación.
2. Para una prueba en Python instala libretranslate y carga solo los idiomas necesarios. Limita el servicio al equipo de prueba.
3. Abre la interfaz local y traduce una frase pública. Si después usas la instancia alojada o MCP, revisa la URL y la clave de esa instancia.

**Entrada documentada (consulta la sintaxis original):**

```
pip install libretranslate
```

La primera prueba se propone; no se ejecutó el proyecto.

[Instrucciones originales de instalación](https://docs.libretranslate.com/guides/installation/)

[Abrir la web o descarga indicada por el autor](https://docs.libretranslate.com/guides/installation/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar LibreTranslate para mi objetivo y necesito pasos guiados. Lee https://docs.libretranslate.com/guides/installation/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre la interfaz de una instancia local, elige inglés a español y escribe «Good morning»..

**Qué comprobar:** La interfaz muestra la traducción al español; el navegador sigue conectado a tu propia instancia..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Traducir un borrador de una ficha entre español e inglés sin enviarla a un proveedor de LLM.
- Conectar una aplicación interna a una instancia de traducción administrada por tu equipo.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Traducir un borrador de una ficha entre español e inglés sin enviarla a un proveedor de LLM.; Conectar una aplicación interna a una instancia de traducción administrada por tu equipo. | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** En un despliegue de red, configurar autenticación y límites; el endpoint MCP de ejemplo envía texto a la instancia alojada. Revisión documental; no acredita binarios ni una instalación probada.

## Stack y modelos

- **Stack:** Python, docker-compose.yml, pyproject.toml
- **Etiquetas:** `traducción` `argos` `autoalojado`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [LibreTranslate/LibreTranslate](https://github.com/LibreTranslate/LibreTranslate)
- 🌐 Web: <https://libretranslate.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/LibreTranslate/LibreTranslate/blob/84cd56c061a7ba3955b49efdaee2ac54dcbca07f/README.md)
- [Fuente 2](https://docs.libretranslate.com/guides/installation/)
- [Fuente 3](https://docs.libretranslate.com/guides/mcp_server/)
- [Fuente 4](https://docs.libretranslate.com/)
- [Fuente 5](https://pypi.org/project/libretranslate/1.9.6/)
- [Fuente 6](https://github.com/LibreTranslate/LibreTranslate/blob/main/LICENSE)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
