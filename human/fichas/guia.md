[🏠 Inicio](../README.md)

# 🧰 Guía (histórica)

> Guía editorial original de la biblioteca, hoy integrada en las fichas de cada repo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| — | — | — | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

> 🧰 Carpeta interna del hub; no es un producto para instalar.

## ¿Qué es?

Guía (histórica), entrada interna del hub BL_Alexandria, no un proyecto externo. Corresponde a la guía editorial original de la biblioteca; su texto escrito a mano se incorporó a las fichas, y hoy `Guia.md` se genera automáticamente desde el índice. No tiene repositorio en GitHub ni licencia propia.

## ¿Qué hace?

`Guia.md` reúne todas las fichas en un solo documento agrupado por categoría y subcategoría, con leyenda de etiquetas y mapa de categorías, para leer de corrido o buscar con Ctrl+F. Sirve como historial editorial y referencia de redacción, no como herramienta para otros proyectos.

## ¿Cómo lo hace?

Lo regenera `uv run repo-intelligence guide build` a partir de `INDICE_IA.json` e `INDICE_IA.detalle.json`. No se edita a mano. AGENTS.md pide a los agentes no leer `Guia.md` entero (es para humanos) y consultar el índice. No se instala: forma parte de este repositorio.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [tools](tools.md) | Utilidades internas del hub que alimentan y verifican el índice del que se genera la guía. | Ambas vienen con el repositorio; no requieren instalación. |

**Notas:** Entrada local (categoría 0), excluida del recuento de cobertura. Las combinaciones anteriores (skills de agentes) no tenían relación con la guía y se sustituyen.

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Cristrva1/BL_Alexandria/blob/main/Guia.md) · [2](https://github.com/Cristrva1/BL_Alexandria/blob/main/AGENTS.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API: por confirmar. No se ha verificado si la ruta elegida necesita una API de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Ejecución con modelos locales por confirmar. Ejecutar el programa en tu equipo no demuestra que el modelo también sea local. |
| Coste | Coste por confirmar. Código disponible no significa servicios, modelos, infraestructura o licencias sin coste. |
| Equipo | Requisitos por confirmar. Consultar los requisitos originales de la variante que vayas a usar. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

No se instala: es parte de este repositorio.

## Casos de uso

- Consultar el historial editorial
- Referencia de redacción
- Uso interno

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres ver el origen del texto de las fichas | buscas una herramienta para tu proyecto |

## Stack y modelos

- **Stack:** Markdown
- **Etiquetas:** `learning`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
