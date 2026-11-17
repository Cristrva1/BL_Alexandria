[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Ingeniería inversa y formatos binarios

# 🖥️ Apktool

> Herramienta para decodificar recursos y reconstruir paquetes APK de Android durante el análisis de una aplicación.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.2k | Apache-2.0 | Java | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; dominio especializado

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta para hacer ingeniería inversa de apps Android binarias y cerradas, de @iBotPeaches. Licencia Apache-2.0. Es muy madura (~27k estrellas, v3.0.3).

## ¿Qué hace?

Decodifica los recursos de una APK casi a su forma original (XML, manifest, smali) y vuelve a construir la app tras modificarla. Facilita depurar smali paso a paso y trabajar con la estructura de proyecto de la app. Sirve para localización, auditoría o parches.

## ¿Cómo lo hace?

Es una herramienta Java: se descarga el JAR y el script envoltorio según la guía de apktool.org (requiere Java). Se usa con `apktool d app.apk` y `apktool b carpeta`; la APK reconstruida debe alinearse y firmarse antes de instalarla. No convierte smali a Java legible: para eso se usa un decompilador.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [jadx](jadx.md) | Leer el código en Java con JADX mientras editas smali y recursos con Apktool. (combinación por arquitectura) | Decompila en JADX para entender y modifica con Apktool. |
| [frida](frida.md) | Incrustar Frida Gadget en la APK reconstruida cuando no hay root. (combinación por arquitectura) | Añade la librería del gadget con Apktool, reconstruye y firma. |
| [mitmproxy](mitmproxy.md) | Modificar `network_security_config` para que la app confíe en el certificado de mitmproxy. (combinación por arquitectura) | Edita la configuración con Apktool, reconstruye, firma e intercepta. |

**Notas:** Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v3.0.3 (2026-07-20) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/iBotPeaches/Apktool/blob/main/README.md) · [2](https://apktool.org/docs/install)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita IA; equipo y herramientas son propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. No reconstruye el código Java original ni certifica el comportamiento de toda la aplicación |
| Coste | Sin pago a un modelo en la ruta básica. No necesita IA; equipo y herramientas son propios |
| Equipo | Preparación según la ruta elegida. Java y distribución de Apktool; APK propio de prueba |

No reconstruye el código Java original ni certifica el comportamiento de toda la aplicación

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Java y distribución de Apktool
- APK propio de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación, plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://apktool.org/wiki/the-basics/intro)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Apktool para mi objetivo y necesito pasos guiados. Lee https://apktool.org/wiki/the-basics/intro. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Decodifica recursos de un APK de laboratorio y localiza su manifiesto.

**Qué comprobar:** Puedes contrastar nombres de recursos y permisos declarados.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar recursos de una app Android
- Revisar una configuración de manifiesto propia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar recursos de una app Android; Revisar una configuración de manifiesto propia | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** No reconstruye el código Java original ni certifica el comportamiento de toda la aplicación

## Stack y modelos

- **Stack:** Java y distribución de Apktool; APK propio de prueba
- **Etiquetas:** `reversing` `app` `java`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [iBotPeaches/Apktool](https://github.com/iBotPeaches/Apktool)
- 🌐 Web: <https://apktool.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/iBotPeaches/Apktool/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
