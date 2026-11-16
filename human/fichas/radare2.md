[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Ingeniería inversa y formatos binarios

# 🖥️ radare2

> Conjunto de herramientas de consola para inspeccionar, desensamblar y depurar programas y archivos binarios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.4k | NOASSERTION | C | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Framework libre de ingeniería inversa para línea de comandos (r2), reescritura completa de radare. Licencia LGPL-3.0, aunque cada plugin puede tener la suya (GitHub muestra NOASSERTION; `r2 -Lj` lista las licencias). Es muy maduro y activo (~25k estrellas, 6.2.6).

## ¿Qué hace?

Ofrece librerías, herramientas y plugins para desensamblar, analizar, depurar, parchear y editar binarios en hexadecimal, con soporte para muchísimas arquitecturas y formatos. Se automatiza con su intérprete JavaScript embebido o con r2pipe desde cualquier lenguaje. Tiene un ecosistema de plugins como r2frida (instrumentación con Frida) y r2ghidra.

## ¿Cómo lo hace?

Está escrito en C; se recomienda instalarlo desde git con `sys/install.sh` (o paquetes) y añadir plugins con su gestor `r2pm`. Funciona en Linux, macOS, Windows, BSD, Android e iOS. La curva de aprendizaje de su interfaz de comandos es alta.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [frida](frida.md) | Instrumentar procesos en vivo desde r2 con el plugin oficial r2frida (`r2 frida://0`). | Instala Frida y luego `r2pm -ci r2frida`. |
| [Claude Code](claude-code.md) | Dar a un agente acceso a r2 con el servidor MCP oficial r2mcp (radareorg/radare2-mcp, no catalogado). | Instala r2mcp con r2pm y regístralo en el cliente MCP. |
| [ImHex](imhex.md) | Analizar formatos de datos con patrones visuales mientras r2 trabaja el código. (combinación por arquitectura) | Usa ambos sobre el mismo binario. |
| [YARA](yara.md) | Combinación recíproca: YARA lo enlaza como «Tras un match YARA, inspecciona el binario con radare2». | Orden indicado desde YARA: Match YARA → abrir en radare2. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[syzkaller](syzkaller.md)

**Notas:** Alternativas (elige una): rizin, ghidra. Úsalo solo con software y sistemas que tengas derecho a analizar.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 6.2.6 (2026-11-05) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/radareorg/radare2/blob/master/README.md) · [2](https://github.com/nowsecure/r2frida) · [3](https://github.com/radareorg/radare2-mcp)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita modelo; plugins pueden tener licencias y dependencias distintas |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El ecosistema permite depuración y escritura; para empezar limita la prueba a lectura estática |
| Coste | Sin pago a un modelo en la ruta básica. No necesita modelo; plugins pueden tener licencias y dependencias distintas |
| Equipo | Preparación según la ruta elegida. Release o compilación compatible; binario propio de práctica |

El ecosistema permite depuración y escritura; para empezar limita la prueba a lectura estática

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Release o compilación compatible
- binario propio de práctica

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/radareorg/radare2/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar radare2 para mi objetivo y necesito pasos guiados. Lee https://github.com/radareorg/radare2/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre el binario en modo de lectura y lista información de formato y funciones.

**Qué comprobar:** Puedes reconocer arquitectura, secciones y símbolos del ejemplo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Inspeccionar un archivo ELF propio
- Estudiar instrucciones de un programa de laboratorio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Inspeccionar un archivo ELF propio; Estudiar instrucciones de un programa de laboratorio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El ecosistema permite depuración y escritura; para empezar limita la prueba a lectura estática

## Stack y modelos

- **Stack:** Release o compilación compatible; binario propio de práctica
- **Etiquetas:** `reversing` `app` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [rizin](rizin.md) | 4.2k | Herramientas para analizar binarios y estudiar programas mediante desensamblado, depuración y otras funciones de consola. |
| [ghidra](ghidra.md) | 100k | Conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria. |

## Enlaces

- 🐙 GitHub: [radareorg/radare2](https://github.com/radareorg/radare2)
- 🌐 Web: <https://www.radare.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/radareorg/radare2/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
