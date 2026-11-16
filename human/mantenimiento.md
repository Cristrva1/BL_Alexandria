[Inicio](README.md)

# Mantener Alexandria

## Incorporar un repo

La vía recomendada es `uv run repo-intelligence add`. Lee con `gh api` estrellas, licencia, último push, archivado, temas, web, rama por defecto, id numérico, README y árbol raíz; rechaza repos archivados, privados o ya catalogados (por id numérico, `owner/repo`, URL o id) y los retirados salvo `--force`. Escribe `INDICE_IA.json`, `INDICE_IA.detalle.json`, el lote de 4 secciones (`curation/descripciones-4s/48-altas-<lote>.json`), la especificación (`curation/altas/<lote>.json`) y el informe (`reports/altas/<lote>.json`). No instala ni ejecuta el proyecto.

```powershell
uv run repo-intelligence add owner/repo --categoria 16 --sub defensa [--ligero] [--simular]
uv run repo-intelligence add --desde curation/altas/mi-lote.json [--ligero] [--construir]
uv run repo-intelligence add <id> --sugerir-combos [--aplicar-combos]
```

- Un alta individual sin lote deja los textos como `PENDIENTE`: complétalos antes de publicar (las pruebas rechazan borradores).
- El lote (JSON o YAML) lleva por repo `gh`, `id`, `cat`, `sub`, `kind`, `one`, `how`, 2 `examples`, `try` = [acción, resultado], `que_es`, `que_hace`, `como_lo_hace`, `combina_con` y `fuentes`; opcionalmente `cmd`, `ai`, `models`, `caveat`, `alt` y `ligero`. A nivel de lote admite `alt_groups` y `subcategorias_nuevas`.
- Completo (por defecto): 3 a 6 combinaciones; la recíproca se añade sola en el destino si tiene hueco (máximo 6) y no es un hub. Ligero (`--ligero` o `"ligero": true`): 0 a 6 combinaciones, exento de la simetría; los ids que declare deben existir y sigue apareciendo en «Usado por».
- `--sugerir-combos` propone combinaciones a partir de lo que combinan sus alternativas, su área práctica, los hubs de su categoría y su categoría; `--aplicar-combos` las escribe con reciprocidad. Revisa los motivos: son sugerencias.
- `--construir` regenera guías, menú portable, `web/` y `docs/`. Después ejecuta `uv run pytest -q`.

Pasos editoriales que el comando no sustituye:

1. Revisa el README original y la documentación de instalación, autenticación y precios que enlaza.
2. Añade o corrige la entrada en los dos índices canónicos. Conserva un id estable aunque cambie el propietario en GitHub.
3. Escribe qué resultado produce, cuándo usarlo y cuál es su alternativa. Ubícalo en una categoría y subcategoría existentes antes de crear otra.
4. Registra acceso, coste, modelos locales y clientes por separado. Usa por confirmar cuando no exista evidencia suficiente.
5. Guarda la fuente, fecha y procedencia del comando. Un nombre de repo no basta para deducir un paquete.
6. Regenera las guías y comprueba las referencias antes de publicar.

## Consultar fuentes

```powershell
uv run python scripts/audit_sources.py --id <id>
uv run repo-intelligence guide build
uv run repo-intelligence menu export
uv run repo-intelligence web build
uv run pytest
```

El script de auditoría guarda material para revisar; no convierte coincidencias de palabras en compatibilidad o precios verificados. Los scripts de curaduría e importación fechados son migraciones históricas: no repetirlos sin adaptar sus categorías y decisiones. El enriquecedor propone borradores heurísticos; revisar categoría y subcategoría contra el mapa actual antes de incorporarlos.

## Fechas diferentes

- Añadido a Alexandria: primera aparición del id en su historial de Git.
- Revisión de acceso: consulta de fuentes sobre modelos, cuentas e instalación.
- Actividad del proyecto: fecha comunicada por su fuente, cuando se haya verificado.

No confundir una fecha de revisión editorial con actividad reciente del autor. No marcar todos los repos no descargados como novedades.

## Mantener las guías de configuración y servicios

El contenido de Configurar IA, Servicios y despliegue, Prompts y comandos vive en `data/handbook.json`. Complementa el inventario de repos: no se añade un servicio o concepto al recuento de proyectos por aparecer en este manual.

Revisa la fuente del proyecto, la fecha, la ruta de acceso y el contexto de cada comando. Conserva los límites cuando falte evidencia y distingue la prueba propuesta de una instalación ejecutada. Las plantillas originales indican los datos que necesita aportar la persona.

`guide build` genera también `human/MANUAL_IA.md` y el sitio de Pages. `web build` actualiza la copia web. El cargador comprueba fuentes, comandos y referencias antes de publicar.

## Mantener técnicas e ideas

Las técnicas, reglas y sitios útiles viven en `data/techniques.json`. Escribe resúmenes y pasos propios, enlaza fuentes públicas (repositorio o documentación oficial antes que una publicación social) y copia los comandos tal como aparecen en la fuente, con lugar de ejecución y efecto. Marca como no verificadas las cifras de terceros.

`guide build` genera `human/TECNICAS.md`. El cargador rechaza enlaces privados o de Google Docs, áreas inexistentes, identificadores repetidos y comandos sin fuente.

## Retirar repos obsoletos

Retira un repo solo con evidencia: archivado en GitHub, aviso de abandono de sus autores, sustituto oficial o años sin cambios en la rama principal. Comprueba la fecha del último commit, no la del último push. Presenta la lista a la persona responsable antes de borrar.

Al retirar, quita la ficha de `INDICE_IA.json` e `INDICE_IA.detalle.json`, limpia sus apariciones en `alt`, `combines_with`, áreas, objetivos y recetas, y regístrala en `data/retired.json` con motivo, evidencia, último commit y sustitutos del catálogo. El detector de stars no vuelve a proponer los repos de esa lista. El registro histórico de la revisión de 679 fichas no se modifica.
