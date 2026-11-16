[🏠 Inicio](../README.md) › [🧑‍💻 Procesar datos y trabajar con notebooks](../categorias/25-datos-notebooks.md) › Datos y notebooks

# 🧑‍💻 GlobalBuildingAtlas

> Dataset global y código de procesamiento de edificios con polígonos, alturas y modelos tridimensionales LoD1.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.3k | MIT + Commons Clause | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🔴 pesado

**Nivel:** 1 Básico — material de consulta: se lee, no se instala

**Puntuación de calidad** 35/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** MIT + Commons Clause. No permite vender el software. Fuente: [LICENSE](https://github.com/zhu-xlab/GlobalBuildingAtlas/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

GlobalBuildingAtlas, dataset global de edificios en nivel de detalle LoD1 (polígonos, alturas y modelos 3D) del grupo zhu-xlab (TUM). Tiene licencias mixtas: polígonos ODbL más polígonos, LoD1 y mapas de altura CC BY-NC 4.0 (GitHub muestra NOASSERTION). Tiene ~2.3k estrellas (v1.0.0) y no cambia desde julio de 2026.

## ¿Qué hace?

Ofrece polígonos y alturas de edificios a escala mundial, con un visor web. El README advierte que combinar las partes del dataset puede tener implicaciones de licencia.

## ¿Cómo lo hace?

Los datos se descargan por partes (`GBA.ODbLPolygon`, `GBA.Polygon`, `GBA.LoD1`, `GBA.Height`) y el código de procesamiento está en el repo. El visor web puede reiniciarse por tráfico alto.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [three.js](three-js.md) | Visualizar los modelos LoD1 en 3D web. (combinación por arquitectura) | Convierte los modelos a glTF y cárgalos. |
| [DuckDB](duckdb.md) | Consultar los polígonos con la extensión espacial. (combinación por arquitectura) | Carga los archivos con `spatial`. |
| [3dviz-pro-max](3dviz-pro-max.md) | Escenas 3D asistidas por agente. (combinación por arquitectura) | Usa los datos como entrada. |

**Notas:** Sin alternativas declaradas. Ojo con la parte CC BY-NC para usos comerciales.

Estado en GitHub: activo · último push 2026-07-06 · última versión publicada v1.0.0 (2025-11-06) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/zhu-xlab/GlobalBuildingAtlas/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa API de IA para consultar datos; descarga, almacenamiento y procesamiento tienen costes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. GBA.ODbLPolygon usa ODbL, mientras otras capas de polígonos, LoD1 y alturas usan CC BY-NC 4.0; no toda la colección permite el mismo uso comercial |
| Coste | Sin pago a un modelo en la ruta básica. No usa API de IA para consultar datos; descarga, almacenamiento y procesamiento tienen costes |
| Equipo | Preparación según la ruta elegida. Navegador o GIS; espacio de descarga; zona pequeña; licencia de la capa |

GBA.ODbLPolygon usa ODbL, mientras otras capas de polígonos, LoD1 y alturas usan CC BY-NC 4.0; no toda la colección permite el mismo uso comercial

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Navegador o GIS
- espacio de descarga
- zona pequeña
- licencia de la capa

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/zhu-xlab/GlobalBuildingAtlas/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GlobalBuildingAtlas para mi objetivo y necesito pasos guiados. Lee https://github.com/zhu-xlab/GlobalBuildingAtlas/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Selecciona una zona y distingue polígonos, alturas y LoD1 antes de descargar una capa.

**Qué comprobar:** Puedes identificar formato, licencia y escala del dato.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Explorar edificios en un GIS
- Preparar una escena urbana de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Explorar edificios en un GIS; Preparar una escena urbana de prueba | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** GBA.ODbLPolygon usa ODbL, mientras otras capas de polígonos, LoD1 y alturas usan CC BY-NC 4.0; no toda la colección permite el mismo uso comercial

## Stack y modelos

- **Stack:** Navegador o GIS; espacio de descarga; zona pequeña; licencia de la capa
- **Etiquetas:** `datos` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [zhu-xlab/GlobalBuildingAtlas](https://github.com/zhu-xlab/GlobalBuildingAtlas)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/zhu-xlab/GlobalBuildingAtlas/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
