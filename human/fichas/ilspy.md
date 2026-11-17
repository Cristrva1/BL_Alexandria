[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Ingeniería inversa y formatos binarios

# 🖥️ ILSpy

> Descompilador de .NET para explorar ensamblados y estudiar el código y metadatos de aplicaciones compatibles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.1k | MIT | C# | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — app de escritorio; hay que saber leer código .NET · corregido a mano

**Puntuación de calidad** 68/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Navegador y decompilador de ensamblados .NET open source y multiplataforma, del equipo icsharpcode. Licencia MIT. Es muy maduro (~27k estrellas, v11.2) y su motor se publica como paquete NuGet (ICSharpCode.Decompiler).

## ¿Qué hace?

Decompila ensamblados .NET a C# legible, permite navegar tipos y miembros, buscar, analizar usos y exportar proyectos. Su motor de decompilación lo reutilizan otras herramientas, como dnSpyEx. El README declara que no usa servicios de telemetría.

## ¿Cómo lo hace?

La interfaz de escritorio usa Avalonia y funciona en Windows, Linux y macOS; se descarga desde las releases. También existen `ilspycmd` (herramienta de línea de comandos para dotnet), el paquete NuGet del decompilador y extensiones para Visual Studio y VS Code; Visual Studio 2022/2026 ya trae sus motores para F12. Compilarlo requiere el SDK de .NET.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [dnSpy](dnspy.md) | dnSpyEx usa el motor de ILSpy y añade depuración y edición de ensamblados. | Decompila con ILSpy y pasa a dnSpyEx cuando necesites depurar o parchear. |
| [Claude Code](claude-code.md) | Que un agente lea la salida de `ilspycmd` para entender una librería sin código fuente. (combinación por arquitectura) | Instala `ilspycmd` como herramienta dotnet y exporta el proyecto para el agente. |
| [ImHex](imhex.md) | Inspeccionar recursos o formatos binarios incrustados. (combinación por arquitectura) | Extrae el recurso y ábrelo en ImHex. |

**Notas:** Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v11.2 (2026-10-27) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/icsharpcode/ILSpy/blob/master/README.md) · [2](https://github.com/icsharpcode/ILSpy/tree/master/ICSharpCode.ILSpyCmd)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere modelo ni API; la distribución usa licencia MIT |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es un descompilador; el resultado reconstruido puede diferir de la fuente original |
| Coste | Sin pago a un modelo en la ruta básica. No requiere modelo ni API; la distribución usa licencia MIT |
| Equipo | Preparación según la ruta elegida. App o ilspycmd del sistema; ensamblado .NET de práctica |

Es un descompilador; el resultado reconstruido puede diferir de la fuente original

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- App o ilspycmd del sistema
- ensamblado .NET de práctica

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/icsharpcode/ILSpy/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ILSpy para mi objetivo y necesito pasos guiados. Lee https://github.com/icsharpcode/ILSpy/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una biblioteca propia y navega por un método y sus referencias.

**Qué comprobar:** Puedes distinguir metadatos y C# descompilado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comprender una dependencia .NET
- Estudiar cómo se representa código compilado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comprender una dependencia .NET; Estudiar cómo se representa código compilado | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un descompilador; el resultado reconstruido puede diferir de la fuente original

## Stack y modelos

- **Stack:** App o ilspycmd del sistema; ensamblado .NET de práctica
- **Etiquetas:** `reversing` `app` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [icsharpcode/ILSpy](https://github.com/icsharpcode/ILSpy)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/icsharpcode/ILSpy/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
