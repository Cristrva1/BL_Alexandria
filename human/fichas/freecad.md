[🏠 Inicio](../README.md) › [🎨 Animación, gráficos y creación 3D](../categorias/26-animacion-graficos-3d.md) › Creación, renderizado y animación 3D

# 🖥️ FreeCAD

> Modelador CAD 3D paramétrico libre para diseño de producto, ingeniería mecánica y arquitectura (BIM), con planos técnicos, FEM, CAM y Python.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 35.5k | LGPL-2.1 | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 71/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Modelador 3D paramétrico de código abierto (LGPL-2.1) desarrollado por la comunidad, con financiación de la FreeCAD Project Association. Activo; versión 1.x estable.

## ¿Qué hace?

Permite diseñar objetos reales de cualquier tamaño modificando parámetros del historial del modelo: bocetos 2D con restricciones, sólidos, ensamblajes, planos técnicos, BIM para arquitectura, análisis por elementos finitos (FEM), trayectorias de mecanizado (CAM) e importación/exportación de STEP, IGES, STL, DXF y otros.

## ¿Cómo lo hace?

Aplicación de escritorio en C++ y Qt sobre el núcleo geométrico OpenCASCADE, organizada en bancos de trabajo. Todo es scriptable en Python (consola, macros y complementos con el Addon Manager). El banco OpenSCAD importa archivos .scad usando el programa OpenSCAD.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OpenSCAD](openscad.md) | FreeCAD incluye el banco de trabajo OpenSCAD, que importa y procesa archivos .scad llamando al ejecutable de OpenSCAD. | Instala OpenSCAD e indica su ruta en las preferencias del banco OpenSCAD de FreeCAD; después importa el .scad. |
| [blender](blender.md) | FreeCAD exporta mallas (OBJ, STL, glTF) que Blender usa para renderizar o animar el diseño (combinación por arquitectura). | Exporta la pieza desde FreeCAD; después impórtala en Blender para materiales y render. |
| [awesome-cad](awesome-cad.md) | El directorio awesome-cad incluye FreeCAD entre sus programas CAD de referencia. | Consulta awesome-cad para elegir herramientas complementarias; después instálalas junto a FreeCAD. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 1.1.4 (2026-09-28) · licencia declarada LGPL-2.1 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/FreeCAD/FreeCAD/blob/main/README.md) · [2](https://github.com/FreeCAD/FreeCAD/tree/main/src/Mod/OpenSCAD) · [3](https://wiki.freecad.org/OpenSCAD_Workbench)</sub>

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

[Instrucciones originales de instalación](https://github.com/FreeCAD/FreeCAD/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/FreeCAD/FreeCAD/releases)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FreeCAD para mi objetivo y necesito pasos guiados. Lee https://github.com/FreeCAD/FreeCAD/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala FreeCAD desde su web, crea un boceto en Part Design y extrúyelo..

**Qué comprobar:** Obtienes un sólido paramétrico que cambia al editar las cotas del boceto..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- diseñar una pieza mecánica paramétrica y exportarla a STL para impresión 3D
- generar planos técnicos acotados a partir de un modelo 3D

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: diseñar una pieza mecánica paramétrica y exportarla a STL para impresión 3D; generar planos técnicos acotados a partir de un modelo 3D | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt
- **Etiquetas:** `cad` `3d` `cpp` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD)
- 🌐 Web: <https://www.freecad.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/FreeCAD/FreeCAD/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
