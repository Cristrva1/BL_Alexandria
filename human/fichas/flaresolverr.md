[🏠 Inicio](../README.md) › [🕷️ Navegadores y automatización web](../categorias/32-navegadores-automatizacion-web.md) › Automatización y pruebas por código

# ⚙️ FlareSolverr

> Servidor proxy que abre páginas protegidas por Cloudflare o DDoS-GUARD en un Chrome automatizado y devuelve el HTML y las cookies para otros clientes HTTP.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.2k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 55/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Servidor de código abierto (MIT) mantenido por la comunidad (ngosang y colaboradores), muy usado junto a indexadores multimedia. Activo, aunque depende de que Cloudflare no cambie sus desafíos.

## ¿Qué hace?

Recibe peticiones por una API HTTP, abre la URL en un Chrome automatizado, espera a que se resuelva el desafío de Cloudflare o DDoS-GUARD (o a que expire) y devuelve el HTML y las cookies. Admite sesiones persistentes, proxies y peticiones POST.

## ¿Cómo lo hace?

Está escrito en Python y usa Selenium con undetected-chromedriver para controlar Chrome. Se ejecuta normalmente con Docker; también hay binarios y ejecución desde el código con Python 3.11 o superior.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Selenium](selenium.md) | FlareSolverr usa Selenium con undetected-chromedriver para controlar Chrome internamente. | Ejecuta FlareSolverr con Docker (incluye Selenium y Chrome); después llama a su API. |
| [scrapy](scrapy.md) | Un spider de Scrapy puede pedir a FlareSolverr la página o las cookies de un sitio autorizado y continuar con peticiones normales (combinación por arquitectura). | Despliega FlareSolverr; después llama a su API desde el spider o un middleware. |
| [crawlee-python](crawlee-python.md) | Un crawler HTTP de Crawlee puede obtener de FlareSolverr las cookies de un sitio autorizado antes de continuar (combinación por arquitectura). | Despliega FlareSolverr; después usa sus cookies en las peticiones de Crawlee. |

Estado en GitHub: activo · último push 2026-10-24 · última versión publicada v3.5.2 (2026-09-12) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/FlareSolverr/FlareSolverr/blob/master/README.md)</sub>

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

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (consulta la sintaxis original):**

```
docker run -d --name=flaresolverr -p 127.0.0.1:8191:8191 -e LOG_LEVEL=info --restart unless-stopped ghcr.io/flaresolverr/flaresolverr:latest
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/FlareSolverr/FlareSolverr/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar FlareSolverr para mi objetivo y necesito pasos guiados. Lee https://github.com/FlareSolverr/FlareSolverr/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta el contenedor con Docker y envía un POST a `http://localhost:8191/v1` con `cmd: request.get` y una URL autorizada..

**Qué comprobar:** Obtienes el HTML de la página y las cookies de la sesión..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- dar acceso a indexadores (como Prowlarr o Jackett) a sitios propios o autorizados detrás de Cloudflare
- obtener cookies válidas para que un scraper autorizado continúe con un cliente HTTP ligero

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: dar acceso a indexadores (como Prowlarr o Jackett) a sitios propios o autorizados detrás de Cloudflare; obtener cookies válidas para que un scraper autorizado continúe con un cliente HTTP ligero | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Evadir protecciones anti-bot puede violar los términos de servicio de los sitios; úsalo solo con autorización. Cada petición lanza un navegador: alto consumo de memoria. Los solucionadores de captcha no funcionan actualmente.

## Stack y modelos

- **Stack:** Python, Dockerfile, docker-compose.yml, package.json, requirements.txt
- **Etiquetas:** `scraping` `proxy` `cloudflare` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [FlareSolverr/FlareSolverr](https://github.com/FlareSolverr/FlareSolverr)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/FlareSolverr/FlareSolverr/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
