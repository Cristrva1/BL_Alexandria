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

El script de auditoría guarda material para revisar; no convierte coincidencias de palabras en compatibilidad o precios verificados. `curate_access.py` y `curate_discovery.py` son migraciones editoriales fechadas: revisar sus decisiones antes de reutilizarlas para nuevas incorporaciones.

## Fechas diferentes

- Añadido a Alexandria: primera aparición del id en su historial de Git.
- Revisión de acceso: consulta de fuentes sobre modelos, cuentas e instalación.
- Actividad del proyecto: fecha comunicada por su fuente, cuando se haya verificado.

No confundir una fecha de revisión editorial con actividad reciente del autor. No marcar todos los repos no descargados como novedades.
