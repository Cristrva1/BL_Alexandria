# Actualización de stars — 14 de noviembre de 2026

Se revisaron las **284 stars públicas de Cristrva1** y se conciliaron con las identidades actuales de GitHub. Todas están representadas en el catálogo: **87 repos agregados**, 197 ya cubiertos y ningún star pendiente en la comprobación de cierre. Se conserva también el resto de la biblioteca: **498 repositorios**, más dos utilidades internas y un alias, para **501 entradas**.

La lista exacta, los ids estables y las correspondencias del catálogo están en [el snapshot de la revisión](github-stars-2026-11-14.json). La fuente es la [API pública de stars de GitHub](https://api.github.com/users/Cristrva1/starred?per_page=100), consultada con paginación completa. Los contadores, nombres canónicos y estados de archivo se verificaron para los 498 repos.

## Conciliaciones

Se conservaron los ids internos y se actualizaron las rutas de tres repos que cambiaron de nombre o propietario:

| Id del catálogo | Ruta actual |
|---|---|
| `arcads-claude-code` | `mrpaidsocial/arcads-claude-code-mrpaidsocial` |
| `openmontage` | `OpenMontageInc/OpenMontage` |
| `wan2gp` | `deepbeepmeep/WanGP` |

Dos pares con nombres parecidos se mantuvieron separados porque corresponden a proyectos distintos: `3b1b/manim` y `ManimCommunity/manim`; `anomalyco/opencode` y el archivado `opencode-ai/opencode`.

## Fichas y fuentes

Los 87 nuevos tienen resumen en español, descripción, funcionamiento, instalación de referencia, criterios de elección, límites y enlaces originales. Sus entradas de `INDICE_IA.detalle.json` conservan el SHA del README y del árbol raíz revisado. La incorporación se basa en lectura de esas fuentes; no acredita pruebas de ejecución de los proyectos.

Se regeneraron las guías humanas, categorías, comparativas, recetas, menú portable, explorador de `docs/` y catálogo educativo de `web/`. Las 14 recetas del catálogo educativo leen los pasos del índice curado, evitando la divergencia con el rediseño.

Se registraron cautelas concretas de las fuentes: las licencias por capa de GlobalBuildingAtlas, el uso personal indicado por Cal.diy, el cambio a binarios propietarios de Palmier Pro y el estado archivado de varios proyectos. `muse-spark-app/muse-spark` queda como referencia de procedencia y funcionalidad no verificadas; su declaración de afiliación oficial no se adopta como hecho.

## Biblioteca local

El usuario confirmó que eliminó `../Repositorios_Prueba`. Se retiraron las 209 marcas históricas de clones locales y las rutas obsoletas del registro local. El historial de esa condición queda en los metadatos; la configuración mantiene la ruta prevista para una futura biblioteca. No se recreó la carpeta ni se descargaron de nuevo los clones.

## Git y validación

Se integró el [PR #1](https://github.com/Cristrva1/BL_Alexandria/pull/1), que estaba pendiente y amplía y rediseña la biblioteca. El trabajo local sin publicar del catálogo educativo y del menú portable se conservó en el commit `f14d7ef` y se combinó con ese rediseño.

- 49 pruebas pasan, incluidas cobertura de stars por identidad, ausencia de duplicados, procedencia de nuevas fichas, enlaces de guías y correspondencia de recetas.
- `guide build`, `menu export` y `web build` generan las salidas completas.
- `node --check web/app.js` pasa.
- La comprobación final de GitHub devolvió las mismas 284 stars, sin altas ni bajas respecto al snapshot.
