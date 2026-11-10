# Trabajo recuperado (sesión del 2026-11-05)

La sesión que rediseñaba BL_Alexandria se cortó por límite de uso antes de hacer commit.
Estos archivos se reconstruyeron desde su transcripción para no perderlos:

- `BRIEF.md`: guía de estilo y esquema de las fichas en español.
- `categories.json`: nuevo orden de 13 secciones con subcategorías.
- `recipes.json`: recetas de integración (flujos entre repos).
- `merge.py`: une las fichas en `INDICE_IA.json` + `INDICE_IA.detalle.json` (esquema 1.2).
- `cmd_*.sh`: comandos que crearon `new_repos.tsv` (202 repos nuevos), `renamed.json`,
  `existing_target.tsv` (categoría destino de los 212 actuales) y los paquetes de trabajo.
- `codigo/`: nuevas versiones de `core/catalog.py`, `guides/render.py` y `guides/explorer.py` (sin probar).
- `fichas/`: 35 fichas ya redactadas (paquetes p02 y p09).

Esta carpeta es temporal: se borra cuando el trabajo quede integrado.

## pipeline/ (reconstruido el 2026-11-10)

Scripts de la sesión original reejecutados con rutas nuevas (`/home/claude/work`):
metadatos de GitHub frescos para los 414 repos (`research/`), lista de repos nuevos, destino de
categorías y los 9 paquetes de trabajo `plan/p01..p09.json` listos para redactar fichas.
`merge.py` ya corre sobre ellos: hoy hay 35 fichas y faltan 379.

Probado en una copia: con `codigo/` en `src/` y `merge.py --write`, `guide build` genera
414 fichas, 13 categorías, 22 comparativas y 14 playbooks; 28 tests pasan y
`tests/test_render_guide.py` queda obsoleto (Guia.md pasa a ser generado).
