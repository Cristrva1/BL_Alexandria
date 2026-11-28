[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Depuración e inspección de procesos

# 🖥️ dnSpyEx

> Depurador y editor de ensamblados .NET para inspeccionar y analizar aplicaciones de esa plataforma.

## Cuándo elegir esta ficha

El upstream de la ficha es dnSpyEx y se declara continuación no oficial. El identificador confirma qué proyecto está catalogado.

Revisión documental del 2026-11-27. [Fuente 1](https://github.com/dnSpyEx/dnSpy/blob/bb09d2c54718e0f73d01d2e1085ddb8772aee555/README.md) · [Fuente 2](https://github.com/dnSpyEx/dnSpy/commit/bb09d2c54718e0f73d01d2e1085ddb8772aee555)

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.5k | GPL-3.0 | C# | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 3 Avanzado — preparación sencilla; app o instalador listo para usar; dominio especializado

**Puntuación de calidad** 51/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

dnSpyEx, continuación no oficial del proyecto dnSpy (archivado): depurador y editor de ensamblados .NET. Licencia GPL-3.0. Es activo (~11k estrellas, v6.6.0).

## ¿Qué hace?

Permite depurar y editar ensamblados .NET y Unity aunque no tengas el código fuente. Pone breakpoints y tracepoints, depura varios procesos a la vez, evalúa expresiones C# o Visual Basic y depura ensamblados que se descifran en memoria; decompila con el motor de ILSpy y permite editar el código. Para depurar juegos Unity necesita el repositorio adicional dnSpy-Unity-mono.

## ¿Cómo lo hace?

Es una aplicación de escritorio para Windows que se descarga desde las releases; también hay builds de CI. Para compilarlo se necesita el SDK de .NET, según el README.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ILSpy](ilspy.md) | Su decompilador se basa en el motor de ILSpy, según los créditos del README. | Usa ILSpy para revisar y dnSpyEx para depurar o editar. |
| [x64dbg](x64dbg.md) | Depurar las partes nativas de un proceso que mezcla .NET y código nativo. (combinación por arquitectura) | Adjunta x64dbg al proceso cuando llegues a código nativo. |
| [ImHex](imhex.md) | Comparar o inspeccionar binarios parcheados. (combinación por arquitectura) | Usa el diff de ImHex entre el ensamblado original y el modificado. |

**Notas:** Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v6.6.0 (2026-06-20) · licencia declarada GPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/dnSpyEx/dnSpy/blob/master/README.md) · [2](https://github.com/dnSpyEx/dnSpy/releases)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita modelo ni API; herramientas y entorno son locales |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. dnSpyEx es continuación no oficial de dnSpy; no confundas las releases de ambos proyectos |
| Coste | Sin pago a un modelo en la ruta básica. No necesita modelo ni API; herramientas y entorno son locales |
| Equipo | Preparación según la ruta elegida. Distribución dnSpyEx compatible; ensamblado .NET propio de prueba |

dnSpyEx es continuación no oficial de dnSpy; no confundas las releases de ambos proyectos

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Distribución dnSpyEx compatible
- ensamblado .NET propio de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
git clone --recursive https://github.com/dnSpyEx/dnSpy.git
```

Comando copiado literalmente de el README (sección «Building»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/dnSpyEx/dnSpy/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dnSpyEx para mi objetivo y necesito pasos guiados. Lee https://github.com/dnSpyEx/dnSpy/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre un ensamblado de ejemplo e inspecciona una clase y sus metadatos.

**Qué comprobar:** Puedes localizar el método y distinguir código reconstruido de fuente original.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar estructura de una app .NET
- Depurar un programa propio sin proyecto fuente completo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar estructura de una app .NET; Depurar un programa propio sin proyecto fuente completo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** dnSpyEx es continuación no oficial de dnSpy; no confundas las releases de ambos proyectos

## Stack y modelos

- **Stack:** Distribución dnSpyEx compatible; ensamblado .NET propio de prueba
- **Etiquetas:** `depuracion` `app` `c`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [dnSpyEx/dnSpy](https://github.com/dnSpyEx/dnSpy)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/dnSpyEx/dnSpy/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
