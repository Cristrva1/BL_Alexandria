[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ mitmproxy

> Proxy interactivo para inspeccionar tráfico HTTP y HTTPS al depurar aplicaciones o realizar pruebas autorizadas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 47k | MIT | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Proxy interceptor interactivo con soporte SSL/TLS para HTTP/1, HTTP/2 y WebSockets. Licencia MIT. Es muy maduro y activo (~47k estrellas, v12.3.1).

## ¿Qué hace?

Intercepta, inspecciona, modifica y reproduce tráfico. Tiene tres interfaces: `mitmproxy` (consola interactiva), `mitmdump` (línea de comandos, «tcpdump para HTTP») y `mitmweb` (web). Se automatiza con addons en Python y funciona en modos proxy normal, transparente, inverso, SOCKS y otros.

## ¿Cómo lo hace?

Está escrito en Python; se instala con los binarios oficiales, `pipx install mitmproxy` o gestores de paquetes según la guía. Para ver HTTPS, el cliente debe confiar en la CA que genera mitmproxy. Las apps con certificate pinning necesitan pasos adicionales.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [frida](frida.md) | Saltar el certificate pinning de apps móviles para inspeccionar su tráfico. (combinación por arquitectura) | Instala la CA de mitmproxy y carga un script de Frida contra el pinning. |
| [playwright](playwright.md) | Pasar un navegador automatizado por el proxy con la opción `proxy` documentada por Playwright. | Arranca mitmproxy y lanza Playwright con `proxy: { server: 'http://localhost:8080' }`. |
| [k6](k6.md) | Convertir tráfico capturado en un HAR y de ahí en un script de carga con el conversor HAR de k6. (combinación por arquitectura) (la exportación HAR de mitmproxy depende de la versión) | Captura con mitmproxy, exporta a HAR y conviértelo con `har-to-k6`. |
| [Apktool](apktool.md) | Combinación recíproca: Apktool lo enlaza como «Modificar `network_security_config` para que la app confíe en el certificado de mitmproxy. (combinación por arquitectura)». | Orden indicado desde Apktool: Edita la configuración con Apktool, reconstruye, firma e intercepta. |
| [Selenium](selenium.md) | Combinación recíproca: Selenium lo enlaza como «Inspección de tráfico en pruebas. (combinación por arquitectura)». | Orden indicado desde Selenium: Configura el proxy en el navegador. |
| [shannon](shannon.md) | Combinación recíproca: shannon lo enlaza como «Observar el tráfico de la prueba contra el entorno de staging. (combinación por arquitectura)». | Orden indicado desde shannon: Enruta el tráfico del objetivo por mitmproxy en el entorno de pruebas. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (4). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[ffuf](ffuf.md) · [Katana](katana.md) · [sqlmap](sqlmap.md) · [Wireshark](wireshark.md)

**Notas:** Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v12.3.1 (2026-10-25) · licencia declarada MIT (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mitmproxy/mitmproxy/blob/main/README.md) · [2](https://docs.mitmproxy.org/stable/overview-installation/) · [3](https://playwright.dev/docs/network#http-proxy) · [4](https://grafana.com/docs/k6/latest/using-k6/test-authoring/create-tests-from-recordings/using-the-har-converter/)</sub>

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
