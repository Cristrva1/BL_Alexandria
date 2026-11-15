[Inicio](README.md)

# Mantener Alexandria

## Incorporar un repo

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
