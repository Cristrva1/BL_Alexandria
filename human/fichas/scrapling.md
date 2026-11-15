[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🩹 Scrapling

> Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 103k | BSD-3-Clause | Python | 2026-06-23 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio · **MCP** 🔌 sí

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El motor no necesita LLM; proxies y servicios de terceros son opcionales y pueden costar |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. La instalación base solo trae parser; MCP requiere scrapling[ai]; los tres clientes admiten sus transportes estándar sin prueba de instalación aquí |
| Coste | Sin pago a un modelo en la ruta básica. El motor no necesita LLM; proxies y servicios de terceros son opcionales y pueden costar |
| Equipo | Preparación según la ruta elegida. Python 3.10+; navegadores del paquete; extra ai para MCP |

La instalación base solo trae parser; MCP requiere scrapling[ai]; los tres clientes admiten sus transportes estándar sin prueba de instalación aquí

## Qué puedes hacer con él

Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia.

## Por qué destaca

Usos propuestos: Recopilar un catálogo público permitido; Extraer texto para un índice de búsqueda.

## Cómo funciona

La instalación base solo trae parser; MCP requiere scrapling[ai]; los tres clientes admiten sus transportes estándar sin prueba de instalación aquí

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python 3.10+
- navegadores del paquete
- extra ai para MCP

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
pip install "scrapling[fetchers]"
<br>
    scrapling install           # normal install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/D4Vinci/Scrapling/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Scrapling para mi objetivo y necesito pasos guiados. Lee https://github.com/D4Vinci/Scrapling/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Extrae nombre y precio de tres productos de una página de prueba mediante selectores.

**Qué comprobar:** Obtienes tres registros que coinciden con el HTML.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Recopilar un catálogo público permitido
- Extraer texto para un índice de búsqueda

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Recopilar un catálogo público permitido; Extraer texto para un índice de búsqueda | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La instalación base solo trae parser; MCP requiere scrapling[ai]; los tres clientes admiten sus transportes estándar sin prueba de instalación aquí

## Stack y modelos

- **Stack:** Python 3.10+; navegadores del paquete; extra ai para MCP
- **Etiquetas:** `automation` `scraping` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [scrapy](scrapy.md) | 65.4k | Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala. |

## Enlaces

- 🐙 GitHub: [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
- 🌐 Web: <https://scrapling.readthedocs.io/en/latest/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/D4Vinci/Scrapling/blob/main/README.md)
- [Fuente 2](https://scrapling.readthedocs.io/en/latest/ai/mcp-server.html)
- [Fuente 3](https://antigravity.google/docs/ide-mcp)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
