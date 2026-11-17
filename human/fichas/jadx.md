[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Ingeniería inversa y formatos binarios

# 🖥️ jadx

> Descompilador de archivos DEX y APK para explorar código Java reconstruido y recursos de aplicaciones Android.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 51.8k | Apache-2.0 | Java | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — app con interfaz gráfica; hay que saber leer código Java · corregido a mano

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Decompilador de Dex a Java con herramientas de línea de comandos y GUI, de @skylot. Licencia Apache-2.0. Es muy maduro y popular (~52k estrellas, v1.5.6).

## ¿Qué hace?

Produce código Java a partir de APK, DEX, AAB, APKS, APKM, XAPK y ZIP, y también decompila bytecode Java (jar, class) y smali. Decodifica `AndroidManifest.xml` y recursos, e incluye desofuscador. La GUI permite resaltar sintaxis, saltar a declaraciones, buscar usos y texto completo, y tiene un depurador smali. El README avisa que casi nunca decompila el 100 % del código.

## ¿Cómo lo hace?

Es Java (requiere Java 11+); se instala desde las releases, con `brew install jadx` u otros gestores. Se usa con `jadx -d salida app.apk` o con `jadx-gui`. Admite plugins y opciones para modos de decompilación alternativos cuando falla el principal.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [frida](frida.md) | Localizar clases y métodos para escribir hooks de Frida. (combinación por arquitectura) | Analiza en JADX y escribe el script de Frida con las firmas encontradas. |
| [Apktool](apktool.md) | Modificar y reconstruir la app tras entenderla en JADX. (combinación por arquitectura) | Usa JADX para leer y Apktool para editar smali y recursos. |
| [ghidra](ghidra.md) | Analizar las librerías nativas `.so` que JADX no cubre. (combinación por arquitectura) | Extrae `lib/` de la APK y ábrelas en Ghidra. |
| [rea](rea.md) | Combinación recíproca: rea lo enlaza como «Análisis de APK mediante JADX headless». | Orden indicado desde rea: Instala JADX y un JDK completo. |
| [awesome-ai-reverse-engineering](awesome-ai-reverse-engineering.md) | Combinación recíproca: awesome-ai-reverse-engineering lo enlaza como «Herramienta móvil de la lista. (combinación por arquitectura)». | Orden indicado desde awesome-ai-reverse-engineering: Úsalo con un servidor MCP de Android si lo necesitas. |
| [OWASP MASTG](mastg.md) | Combinación recíproca: OWASP MASTG lo enlaza como «jadx decompila a Java para revisar la lógica de la app». | Orden indicado desde OWASP MASTG: Abre la APK en jadx durante las pruebas estáticas. |

**Notas:** Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v1.5.6 (2026-07-10) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/skylot/jadx/blob/master/README.md) · [2](https://github.com/skylot/jadx/wiki)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa modelo ni API; equipo y herramientas son propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El Java reconstruido no es necesariamente el código original ni compila de nuevo sin cambios |
| Coste | Sin pago a un modelo en la ruta básica. No usa modelo ni API; equipo y herramientas son propios |
| Equipo | Preparación según la ruta elegida. Java y release apropiada; APK o DEX propio |

El Java reconstruido no es necesariamente el código original ni compila de nuevo sin cambios

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Java y release apropiada
- APK o DEX propio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
brew install jadx
```

Comando copiado literalmente de el README (sección «Install»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/skylot/jadx/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar jadx para mi objetivo y necesito pasos guiados. Lee https://github.com/skylot/jadx/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre una app Android de prueba y navega por una clase y sus recursos.

**Qué comprobar:** Puedes identificar métodos y líneas que no se reconstruyen correctamente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar una app Android propia
- Documentar recursos y referencias de un APK

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar una app Android propia; Documentar recursos y referencias de un APK | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El Java reconstruido no es necesariamente el código original ni compila de nuevo sin cambios

## Stack y modelos

- **Stack:** Java y release apropiada; APK o DEX propio
- **Etiquetas:** `reversing` `app` `java`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [skylot/jadx](https://github.com/skylot/jadx)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/skylot/jadx/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
