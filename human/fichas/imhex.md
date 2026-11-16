[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Ingeniería inversa y formatos binarios

# 🖥️ ImHex

> Editor hexadecimal para inspeccionar archivos binarios, identificar estructuras y describir formatos mediante patrones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 55.9k | GPL-2.0 | C++ | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — editor hexadecimal con instalador · corregido a mano

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Editor hexadecimal para ingenieros inversos y programadores, creado por @WerWolv. La mayor parte es GPL-2.0-only, con partes en LGPL-2.1 (librerías y plugins). Es muy popular y activo (~56k estrellas, v1.38.1).

## ¿Qué hace?

Además de la vista hexadecimal, ofrece un lenguaje de patrones tipo C++ para describir y resaltar formatos, inspector de datos, preprocesador por nodos, búsquedas, hashes, diffs, desensamblador integrado, reglas YARA, marcadores y visualizadores. Carga datos de archivos, procesos, discos y otras fuentes. Tiene un actualizador de contenido con patrones y bibliotecas de la comunidad.

## ¿Cómo lo hace?

Es una aplicación de escritorio en C++ (Dear ImGui) para Windows, macOS y Linux; se instala desde las releases o gestores de paquetes. Requiere una GPU con OpenGL 3.0. Se extiende con plugins y con su lenguaje de patrones.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ghidra](ghidra.md) | Analizar el formato de un archivo en ImHex y el código que lo procesa en Ghidra. (combinación por arquitectura) | Usa ambos sobre el mismo caso. |
| [radare2](radare2.md) | Combinar el editor visual con el análisis por línea de comandos. (combinación por arquitectura) | Usa ImHex para datos y r2 para código. |
| [x64dbg](x64dbg.md) | Estudiar volcados de memoria tomados durante la depuración. (combinación por arquitectura) | Vuelca la región en x64dbg y ábrela en ImHex. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (4). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[dnSpy](dnspy.md) · [ILSpy](ilspy.md) · [raddebugger](raddebugger.md) · [rizin](rizin.md)

**Notas:** Sin alternativas declaradas.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.38.1 (2025-12-21) · licencia declarada GPL-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/WerWolv/ImHex/blob/master/README.md) · [2](https://github.com/WerWolv/ImHex/blob/master/PLUGINS.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere modelo; GPU y almacenamiento son recursos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Un patrón ayuda a interpretar bytes y no demuestra por sí solo que toda estructura inferida sea correcta |
| Coste | Sin pago a un modelo en la ruta básica. No requiere modelo; GPU y almacenamiento son recursos propios |
| Equipo | Preparación según la ruta elegida. Release compatible; GPU OpenGL 3.0; archivo binario de prueba |

Un patrón ayuda a interpretar bytes y no demuestra por sí solo que toda estructura inferida sea correcta

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Release compatible
- GPU OpenGL 3.0
- archivo binario de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (powershell):**

```
choco install imhex
```

Comando copiado literalmente de la documentación del repositorio (sección «Windows»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/WerWolv/ImHex/blob/master/INSTALL.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ImHex para mi objetivo y necesito pasos guiados. Lee https://github.com/WerWolv/ImHex/blob/master/INSTALL.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre un archivo propio pequeño y aplica un patrón conocido para interpretar su cabecera.

**Qué comprobar:** Los campos interpretados coinciden con los bytes del archivo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar un formato de archivo
- Comparar dos versiones de una estructura binaria

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar un formato de archivo; Comparar dos versiones de una estructura binaria | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Un patrón ayuda a interpretar bytes y no demuestra por sí solo que toda estructura inferida sea correcta

## Stack y modelos

- **Stack:** Release compatible; GPU OpenGL 3.0; archivo binario de prueba
- **Etiquetas:** `reversing` `app` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [WerWolv/ImHex](https://github.com/WerWolv/ImHex)
- 🌐 Web: <https://imhex.werwolv.net/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/WerWolv/ImHex/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
