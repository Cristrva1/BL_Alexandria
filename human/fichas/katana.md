[🏠 Inicio](../README.md) › [🕷️ Buscar, extraer y monitorear información web](../categorias/04-scraping-b-squeda-research-web.md) › Crawlers y extracción para IA

# 🖥️ Katana

> Crawler web de ProjectDiscovery en Go, en modo estándar o headless, con análisis de JavaScript, control de alcance y salida JSON.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.9k | MIT | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Crawler de código abierto (MIT) de ProjectDiscovery, el equipo de nuclei y subfinder. Muy activo y orientado a reconocimiento de seguridad.

## ¿Qué hace?

Rastrea sitios de forma rápida y configurable: modo estándar y headless, análisis y rastreo de JavaScript, relleno automático de formularios, control de alcance por campos o expresiones regulares, clasificación de páginas y formularios con un modelo descargado automáticamente, y salidas filtrables en texto o JSON.

## ¿Cómo lo hace?

Escrito en Go; requiere una versión reciente de Go para `go install` (con CGO) o se usa con la imagen Docker. El modo headless usa Chrome del sistema y puede conectarse a una sesión de navegador ya autenticada con depuración remota; admite proxy.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [mitmproxy](mitmproxy.md) | Katana admite proxy en modo headless: enviar su tráfico a mitmproxy permite inspeccionar y registrar las peticiones del rastreo (combinación por arquitectura). | Arranca mitmproxy en un puerto local; después pasa la opción de proxy a Katana. |
| [DuckDB](duckdb.md) | La salida JSON de Katana se puede consultar con DuckDB para filtrar y agrupar endpoints (combinación por arquitectura). | Ejecuta Katana con salida JSON; después consulta el archivo con DuckDB. |
| [Claude Code](claude-code.md) | Un agente puede lanzar Katana sobre un objetivo autorizado y resumir los endpoints descubiertos (combinación por arquitectura). | Instala Katana y define el alcance permitido; después pide al agente el análisis. |
| [theHarvester](theharvester.md) | Combinación recíproca: theHarvester lo enlaza como «Los hosts y subdominios descubiertos se rastrean con Katana para listar sus endpoints (combinación por arquitectura)». | Orden indicado desde theHarvester: Exporta los hosts de theHarvester; después pásalos a Katana dentro del alcance autorizado. |
| [Nuclei](nuclei.md) | Combinación recíproca: Nuclei lo enlaza como «katana rastrea URLs y endpoints que Nuclei escanea a continuación». | Orden indicado desde Nuclei: Rastrea con katana; después pasa las URLs a nuclei. |
| [subfinder](subfinder.md) | Combinación recíproca: subfinder lo enlaza como «katana rastrea los subdominios descubiertos para mapear endpoints». | Orden indicado desde subfinder: Enumera con subfinder; después pasa los hosts a katana. |

**Notas:** Herramienta de reconocimiento: define siempre el alcance permitido antes de ejecutarla.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.8.0 (2026-10-05) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/projectdiscovery/katana/blob/dev/README.md)</sub>

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
go install github.com/projectdiscovery/katana/cmd/katana@latest
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/projectdiscovery/katana/blob/dev/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Katana para mi objetivo y necesito pasos guiados. Lee https://github.com/projectdiscovery/katana/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta la imagen Docker oficial contra el sitio de ejemplo books.toscrape.com que usa el README..

**Qué comprobar:** Katana lista las URLs descubiertas sin errores..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- descubrir los endpoints de una aplicación propia antes de una auditoría autorizada
- mapear rutas generadas por JavaScript en un sitio de pruebas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: descubrir los endpoints de una aplicación propia antes de una auditoría autorizada; mapear rutas generadas por JavaScript en un sitio de pruebas | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Úsalo solo en sitios propios o con autorización: el rastreo agresivo puede violar términos de uso o leyes.

## Stack y modelos

- **Stack:** Go, Dockerfile, go.mod
- **Etiquetas:** `scraping` `go` `security` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [projectdiscovery/katana](https://github.com/projectdiscovery/katana)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/projectdiscovery/katana/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
