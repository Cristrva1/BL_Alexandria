[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Creación, renderizado y animación 3D

# 🖥️ OpenSCAD

> CAD 3D por código: describes la pieza en un lenguaje de script y OpenSCAD la compila a un sólido exportable (STL, 3MF), ideal para piezas paramétricas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.7k | GPL-2.0 (con excepción CGAL) | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 59/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Programa libre (GPL-2.0 con excepción para CGAL) para crear modelos CAD sólidos, disponible para Linux, Windows y macOS. Muy usado en impresión 3D (p. ej. el personalizador de Thingiverse). El código es activo, pero la última versión estable publicada es 2021.01; las novedades llegan en instantáneas de desarrollo.

## ¿Qué hace?

Convierte un script que describe un objeto en un modelo 3D: geometría sólida constructiva (uniones, diferencias, intersecciones) y extrusión de contornos 2D (incluidos DXF). Permite diseños parametrizables y exporta STL, 3MF, OFF, AMF, DXF y SVG.

## ¿Cómo lo hace?

No es un modelador interactivo, sino un "compilador 3D": interpreta el lenguaje OpenSCAD y renderiza con CGAL o, en las instantáneas de desarrollo, con el backend Manifold (más rápido). Se instala con paquetes oficiales; también funciona por línea de comandos para generar modelos en lote.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [FreeCAD](freecad.md) | FreeCAD importa archivos .scad mediante su banco de trabajo OpenSCAD, que llama al ejecutable de OpenSCAD. | Instala OpenSCAD; después configura su ruta en FreeCAD e importa el script. |
| [awesome-cad](awesome-cad.md) | El directorio awesome-cad incluye OpenSCAD entre sus herramientas CAD. | Consulta awesome-cad para bibliotecas y complementos; después úsalos con OpenSCAD. |
| [Claude Code](claude-code.md) | Los modelos de OpenSCAD son texto, así que un agente de código puede escribir y modificar scripts .scad y renderizarlos por CLI (combinación por arquitectura). | Instala OpenSCAD; después pide el script al agente y genera el STL con `openscad -o pieza.stl pieza.scad`. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada openscad-2021.01 (2021-02-07) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/openscad/openscad/blob/master/README.md) · [2](https://github.com/openscad/openscad/blob/master/COPYING) · [3](https://github.com/mlightcad/awesome-cad/blob/main/README.md)</sub>

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/openscad/openscad/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://www.openscad.org)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenSCAD para mi objetivo y necesito pasos guiados. Lee https://github.com/openscad/openscad/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala OpenSCAD, escribe `cube(10); translate([5,5,5]) sphere(6);`, renderiza con F6 y exporta a STL..

**Qué comprobar:** Obtienes un archivo STL listo para el laminador de la impresora..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- diseñar piezas paramétricas para impresión 3D cambiando variables
- generar variantes de una pieza (tamaños, agujeros) desde el mismo script

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: diseñar piezas paramétricas para impresión 3D cambiando variables; generar variantes de una pieza (tamaños, agujeros) desde el mismo script | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Licencia GPL-2.0 con una excepción para enlazar con la biblioteca CGAL. La última versión estable publicada es 2021.01; las mejoras recientes (como el backend Manifold) solo están en las instantáneas de desarrollo.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt
- **Etiquetas:** `cad` `3d` `code` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [openscad/openscad](https://github.com/openscad/openscad)
- 🌐 Web: <https://www.openscad.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openscad/openscad/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
