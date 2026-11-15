[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ mitmproxy

> Proxy interactivo para inspeccionar tráfico HTTP y HTTPS al depurar aplicaciones o realizar pruebas autorizadas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 47k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa modelo; recursos de ejecución y servicios inspeccionados son independientes |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Para HTTPS se configura confianza de certificados; no es una observación transparente sin cambios en el cliente |
| Coste | Sin pago a un modelo en la ruta básica. No usa modelo; recursos de ejecución y servicios inspeccionados son independientes |
| Equipo | Preparación según la ruta elegida. Distribución compatible; cliente y servicio propios de prueba; certificado solo en el entorno de ensayo |

Para HTTPS se configura confianza de certificados; no es una observación transparente sin cambios en el cliente

## Qué puedes hacer con él

Proxy interactivo para inspeccionar tráfico HTTP y HTTPS al depurar aplicaciones o realizar pruebas autorizadas.

## Por qué destaca

Usos propuestos: Depurar llamadas HTTP de una app propia; Comprender un error de integración de desarrollo.

## Cómo funciona

Para HTTPS se configura confianza de certificados; no es una observación transparente sin cambios en el cliente

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Distribución compatible
- cliente y servicio propios de prueba
- certificado solo en el entorno de ensayo

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://docs.mitmproxy.org/stable/overview-installation/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar mitmproxy para mi objetivo y necesito pasos guiados. Lee https://docs.mitmproxy.org/stable/overview-installation/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Inspecciona una petición de tu app de laboratorio y revisa cabeceras y respuesta.

**Qué comprobar:** Puedes reconocer origen, destino y contenido capturado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Depurar llamadas HTTP de una app propia
- Comprender un error de integración de desarrollo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Depurar llamadas HTTP de una app propia; Comprender un error de integración de desarrollo | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Para HTTPS se configura confianza de certificados; no es una observación transparente sin cambios en el cliente

## Stack y modelos

- **Stack:** Distribución compatible; cliente y servicio propios de prueba; certificado solo en el entorno de ensayo
- **Etiquetas:** `pruebas` `app` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy)
- 🌐 Web: <https://mitmproxy.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mitmproxy/mitmproxy/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
