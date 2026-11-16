[🏠 Inicio](../README.md) › [🧑‍💻 Entender código y comprobar su calidad](../categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md) › Entender y empaquetar código para agentes

# 🧬 Repomix

> Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 29.3k | MIT | TypeScript | 2026-06-24 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil · **MCP** 🔌 sí

## ¿Qué es?

Repomix, herramienta para empaquetar un repositorio en un único archivo apto para LLM, de @yamadashy. Licencia MIT. Es madura y muy usada (~29k estrellas, v1.19.0) y tiene patrocinadores destacados en el README.

## ¿Qué hace?

Genera un archivo XML, Markdown o texto plano con la estructura y el contenido del repo, con recuento de tokens por archivo. Respeta `.gitignore`, detecta credenciales con Secretlint y puede comprimir el código con Tree-sitter para quedarse con firmas y estructura. Trabaja con repos remotos, puede actuar como servidor MCP y genera Agent Skills.

## ¿Cómo lo hace?

Se ejecuta con `npx repomix@latest`, `npm install -g repomix` o `brew install repomix`, o se usa en la web repomix.com. Está escrito en TypeScript y requiere Node.js. La carga de configuración de repos remotos está desactivada por defecto por seguridad.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Generar skills para Claude Code (`--skill-generate`) o usar Repomix como MCP. | Ejecuta `repomix --mcp` o genera la skill en `.claude/skills/`. |
| [tree-sitter](tree-sitter.md) | La opción `--compress` usa Tree-sitter. | Usa `repomix --compress` para reducir tokens. |
| [markitdown](markitdown.md) | Convertir documentos del repo a Markdown antes de empaquetar. (combinación por arquitectura) | Convierte PDF/DOCX con MarkItDown y empaqueta después. |
| [tools](tools.md) | Combinación recíproca: tools lo enlaza como «Envoltorio `repomix_runner.py`». | Orden indicado desde tools: Instala repomix (npm). |
| [codebase-memory-mcp](codebase-memory-mcp.md) | Combinación recíproca: codebase-memory-mcp lo enlaza como «Empaquetar módulos concretos tras localizarlos en el grafo. (combinación por arquitectura)». | Orden indicado desde codebase-memory-mcp: Localiza con el grafo y empaqueta con Repomix. |

**Notas:** Alternativas (elige una): gitnexus.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v1.19.0 (2026-11-08) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/yamadashy/repomix/blob/main/README.md) · [2](https://repomix.com)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Empaquetar no usa modelo; enviarlo a un agente consume su contexto y presupuesto |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Ofrece MCP stdio y plugins o skills; revisa secretos y archivos excluidos aunque el paquete incluya un detector |
| Coste | Sin pago a un modelo en la ruta básica. Empaquetar no usa modelo; enviarlo a un agente consume su contexto y presupuesto |
| Equipo | Preparación según la ruta elegida. Node.js; repositorio de prueba; filtros de inclusión |

Ofrece MCP stdio y plugins o skills; revisa secretos y archivos excluidos aunque el paquete incluya un detector

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js
- repositorio de prueba
- filtros de inclusión

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
npx repomix@latest
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/yamadashy/repomix/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Repomix para mi objetivo y necesito pasos guiados. Lee https://github.com/yamadashy/repomix/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Empaqueta una carpeta pequeña y abre el resultado antes de entregarlo a una IA.

**Qué comprobar:** Puedes comprobar archivos incluidos, tamaño y exclusiones.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar contexto de código para una consulta
- Compartir una muestra reproducible de un proyecto

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar contexto de código para una consulta; Compartir una muestra reproducible de un proyecto | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Ofrece MCP stdio y plugins o skills; revisa secretos y archivos excluidos aunque el paquete incluya un detector

## Stack y modelos

- **Stack:** Node.js; repositorio de prueba; filtros de inclusión
- **Etiquetas:** `code` `coding-agent` `typescript`
- **Modo de instalación sugerido:** 🌍 **Global** — instálalo una vez en tu máquina

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [GitNexus](gitnexus.md) | 48.5k | Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva. |

## Enlaces

- 🐙 GitHub: [yamadashy/repomix](https://github.com/yamadashy/repomix)
- 🌐 Web: <https://repomix.com>
- 🧪 Receta: [Análisis de repos grandes](../playbooks/analisis-de-repos-grandes.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/yamadashy/repomix/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
