[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Análisis y pruebas con agentes

# 🎨 rea

> Herramientas e instrucciones para estudiar el comportamiento y la estructura de software mediante agentes de código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 460k | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio · **MCP** 🔌 sí

## ¿Qué es?

REA, un servidor MCP para hacer ingeniería inversa con agentes, desde el comportamiento de una aplicación hasta binarios nativos, de @morluto. Licencia MIT. Su número de estrellas es anómalo (~462k en siete meses, desde abril de 2026), sin explicación pública [DATO NO VERIFICADO sobre su origen].

## ¿Qué hace?

Registra herramientas MCP e instrucciones de flujo de trabajo para analizar instalaciones de escritorio, binarios nativos (pseudocódigo, ensamblado, cadenas, símbolos), APK Android, WASM, apps Electron y JavaScript, ejecutables PyInstaller, firmware y fallos de Linux. Valida cada resultado del lado del servidor y ofrece esquemas compactos para gastar menos contexto. También permite crear entornos de aprendizaje por refuerzo a partir de los análisis.

## ¿Cómo lo hace?

Requiere Node.js y npm: `npx rea-agents setup` registra el servidor en el agente (Claude Code, Codex, Cursor y otros) con copias de seguridad de la configuración previa. El análisis nativo usa una instalación existente de Hopper, Ghidra, IDA o Kuna; los APK, JADX headless con un JDK completo; otros análisis, pwntools o WABT aportados por el usuario.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Registro automático como servidor MCP y plugin de Claude Code. | Ejecuta `npx rea-agents setup` y elige Claude Code. |
| [ghidra](ghidra.md) | Motor de análisis nativo compatible, según el README. | Instala Ghidra (JDK incluido) antes de configurar REA. |
| [jadx](jadx.md) | Análisis de APK mediante JADX headless. | Instala JADX y un JDK completo. |
| [Codex CLI](codex.md) | Plugin de Codex disponible. | Ejecuta el setup y elige Codex. |
| [awesome-ai-reverse-engineering](awesome-ai-reverse-engineering.md) | Combinación recíproca: awesome-ai-reverse-engineering lo enlaza como «Listado como herramienta destacada». | Orden indicado desde awesome-ai-reverse-engineering: Consulta su ficha antes de instalarlo. |
| [awesome-reverse-engineering](awesome-reverse-engineering.md) | Combinación recíproca: awesome-reverse-engineering lo enlaza como «Herramienta destacada por los mismos autores». | Orden indicado desde awesome-reverse-engineering: Lee la sección de REA y su documentación antes de instalarlo. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[bla](bla.md) · [craft-anything](craft-anything.md)

**Notas:** Sin alternativas declaradas. Revisa qué escribe el setup en la configuración de tu agente. Úsalo solo con software propio o con autorización escrita.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada rea-agents-6.9.0 (2026-11-12) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/morluto/rea/blob/main/README.md) · [2](https://rea.tools/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El análisis y MCP no exigen modelo propio; el agente y herramientas como Hopper pueden tener licencia o consumo adicional |
| Claude Code | Herramienta MCP para el agente |
| Codex | Herramienta MCP para el agente |
| Antigravity | Herramienta MCP para el agente |
| Modelos locales | La función básica no necesita un modelo. Los backends tienen requisitos distintos; el setup propone cambios de cliente y conserva copias; no todos los formatos funcionan solo con Node |
| Coste | El coste depende del proveedor o la ruta. El análisis y MCP no exigen modelo propio; el agente y herramientas como Hopper pueden tener licencia o consumo adicional |
| Equipo | Preparación según la ruta elegida. Node y npm; agente; herramientas nativas solo según formato; programa propio |

Los backends tienen requisitos distintos; el setup propone cambios de cliente y conserva copias; no todos los formatos funcionan solo con Node

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node y npm
- agente
- herramientas nativas solo según formato
- programa propio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
npx rea-agents setup
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/morluto/rea/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar rea para mi objetivo y necesito pasos guiados. Lee https://github.com/morluto/rea/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Analiza estáticamente un pequeño proyecto JavaScript propio y revisa el informe y sus rutas de archivos.

**Qué comprobar:** Puedes contrastar cada elemento con el código del proyecto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Entender estructura de una app propia
- Comparar dos versiones de un formato de laboratorio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Entender estructura de una app propia; Comparar dos versiones de un formato de laboratorio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los backends tienen requisitos distintos; el setup propone cambios de cliente y conserva copias; no todos los formatos funcionan solo con Node

## Stack y modelos

- **Stack:** Node y npm; agente; herramientas nativas solo según formato; programa propio
- **Etiquetas:** `agentes` `skill` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [morluto/rea](https://github.com/morluto/rea)
- 🌐 Web: <https://rea.tools>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/morluto/rea/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
