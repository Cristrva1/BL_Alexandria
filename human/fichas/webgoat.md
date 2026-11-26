[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ WebGoat

> Aplicación web deliberadamente insegura de OWASP con lecciones guiadas para aprender y practicar vulnerabilidades del Top 10.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.5k | GPL-2.0-or-later | JavaScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 58/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** GPL-2.0-or-later. SPDX-License-Identifier en LICENSE.txt. Fuente: [LICENSE](https://github.com/WebGoat/WebGoat/blob/main/LICENSE.txt). GitHub la marca como NOASSERTION.

## ¿Qué es?

Proyecto OWASP de formación: una aplicación web con vulnerabilidades intencionadas y lecciones para explotarlas y corregirlas.

## ¿Qué hace?

Guía al usuario por lecciones de inyección, autenticación rota, XSS, XXE, deserialización insegura y otros fallos, con pistas y validación.

## ¿Cómo lo hace?

Aplicación Spring Boot más WebWolf (servidor de apoyo para ataques); se distribuye como imagen Docker, imagen con escritorio Linux o JAR.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ZAP (Zed Attack Proxy)](zaproxy.md) | ZAP intercepta y modifica el tráfico necesario en muchas lecciones. | WebGoat en local; ZAP como proxy del navegador. |
| [Caido](caido.md) | Caido sirve como proxy alternativo para resolver las lecciones. | WebGoat en local; Caido como proxy. |
| [OWASP Web Security Testing Guide](wstg.md) | La WSTG explica la metodología de prueba detrás de cada lección. | Lee la sección de la WSTG antes de cada lección. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2026.5 (2026-10-12) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/WebGoat/WebGoat#readme) · [2](https://owasp.org/www-project-webgoat/)</sub>

## Ver similares

Grupo **Aplicaciones web vulnerables para practicar**: WebGoat ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [OWASP Juice Shop](juice-shop.md) ⭐ recomendado | 75 | Si quieres retos tipo CTF sobre una tienda moderna en JavaScript. |
| 2 | **WebGoat** (esta ficha) | 58 | Si prefieres lecciones guiadas paso a paso sobre una aplicación Java. |

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

**Entrada documentada (bash):**

```
docker run -it -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 webgoat/webgoat
```

Comando copiado literalmente de el README (sección «1. Run using Docker»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/WebGoat/WebGoat/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://owasp.org/www-project-webgoat/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar WebGoat para mi objetivo y necesito pasos guiados. Lee https://github.com/WebGoat/WebGoat/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta la imagen Docker oficial ligada a 127.0.0.1 como indica el README y abre WebGoat en el navegador..

**Qué comprobar:** Accedes a las lecciones y completas la primera..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- practicar inyección SQL y XSS siguiendo lecciones paso a paso
- formar a desarrolladores en errores comunes de seguridad web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: practicar inyección SQL y XSS siguiendo lecciones paso a paso; formar a desarrolladores en errores comunes de seguridad web | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Aplicación deliberadamente vulnerable: ejecútala solo en local o en una red aislada, nunca expuesta a Internet ni en equipos con datos reales. Licencia GPL-2.0-or-later en LICENSE.txt pese a NOASSERTION en la API de GitHub.

## Stack y modelos

- **Stack:** JavaScript, Dockerfile, pom.xml
- **Etiquetas:** `security` `training` `vulnerable-app` `java`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OWASP Juice Shop](juice-shop.md) | 14.5k | Aplicación web vulnerable oficial de OWASP para entrenar AppSec: cientos de retos y puntuación. |

## Enlaces

- 🐙 GitHub: [WebGoat/WebGoat](https://github.com/WebGoat/WebGoat)
- 🌐 Web: <https://owasp.org/www-project-webgoat/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/WebGoat/WebGoat/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
