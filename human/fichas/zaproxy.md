[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ ZAP (Zed Attack Proxy)

> Escáner de seguridad de aplicaciones web más usado (antes OWASP ZAP, ahora ZAP by Checkmarx): proxy interceptor, araña y escaneo activo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.2k | Apache-2.0 | Java | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Escáner de aplicaciones web de código abierto (Apache-2.0), nacido en OWASP y patrocinado ahora por Checkmarx. Muy maduro y comunitario.

## ¿Qué hace?

Encuentra vulnerabilidades en aplicaciones web durante el desarrollo y en pruebas manuales: intercepta y modifica tráfico, rastrea la aplicación, detecta problemas de forma pasiva y activa, y se automatiza con API, marco de automatización, Docker y acciones de CI.

## ¿Cómo lo hace?

Escrito en Java; se instala con los instaladores multiplataforma, paquetes o imágenes Docker. Requiere Java para la versión de escritorio; el marketplace añade complementos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [sqlmap](sqlmap.md) | Cuando ZAP señala una posible inyección SQL, sqlmap la confirma con más profundidad (combinación por arquitectura). | Escanea con ZAP; después guarda la petición y pásala a sqlmap con `-r`. |
| [playwright](playwright.md) | Las pruebas E2E de Playwright pueden pasar por el proxy de ZAP para que analice el tráfico real de la aplicación (combinación por arquitectura). | Arranca ZAP como proxy; después configura el proxy en Playwright y ejecuta las pruebas. |
| [Nuclei](nuclei.md) | Nuclei comprueba CVE concretos mientras ZAP analiza la lógica y las respuestas de la aplicación (combinación por arquitectura). | Ejecuta ambos escaneos sobre el mismo entorno de pruebas. |
| [PayloadsAllTheThings](payloadsallthethings.md) | Combinación recíproca: PayloadsAllTheThings lo enlaza como «Usa payloads del repo dentro de ZAP». | Orden indicado desde PayloadsAllTheThings: Define el alcance en ZAP; consulta PayloadsAllTheThings. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[OWASP Juice Shop](juice-shop.md)

**Notas:** No hay alternativa equivalente abierta en el catálogo (Burp Suite es propietario); mitmproxy es un proxy de depuración, no un escáner.

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v2.17.0 (2025-12-15) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/zaproxy/zaproxy/blob/main/README.md) · [2](https://www.zaproxy.org/docs/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo. |
| Coste | Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |

Poder usar un agente para instalar código no acredita que su suscripción ejecute esta aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/zaproxy/zaproxy/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ZAP (Zed Attack Proxy) para mi objetivo y necesito pasos guiados. Lee https://github.com/zaproxy/zaproxy/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga ZAP desde zaproxy.org y ejecuta el escaneo automatizado contra una aplicación de laboratorio propia..

**Qué comprobar:** ZAP muestra alertas clasificadas por riesgo con evidencias y soluciones..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- buscar vulnerabilidades comunes en tu aplicación web durante el desarrollo
- integrar un escaneo DAST en el pipeline de CI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: buscar vulnerabilidades comunes en tu aplicación web durante el desarrollo; integrar un escaneo DAST en el pipeline de CI | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Úsalo solo contra sistemas propios o con autorización escrita: usarlo contra terceros sin permiso es delito en la mayoría de países.

## Stack y modelos

- **Stack:** Java
- **Etiquetas:** `pruebas` `java` `security` `app`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Caido](caido.md) | 2.7k | Proxy de pentest web moderno (alternativa a Burp): core HTTP gratis (Basic); Individual/Team/Enterprise de pago. No es open source. |

## Enlaces

- 🐙 GitHub: [zaproxy/zaproxy](https://github.com/zaproxy/zaproxy)
- 🌐 Web: <https://www.zaproxy.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/zaproxy/zaproxy/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
