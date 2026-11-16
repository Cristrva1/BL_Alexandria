[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Inteligencia de fuentes abiertas y mapas

# 🖥️ Maigret

> Recopila un dossier sobre una persona a partir de un nombre de usuario comprobando miles de sitios y extrayendo datos públicos de los perfiles.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.8k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 63/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta OSINT de código abierto (MIT) creada por soxoj, derivada de Sherlock y ampliada. Activa; el autor advierte de que las comprobaciones de sitios se rompen con el tiempo y requieren mantenimiento.

## ¿Qué hace?

Busca cuentas en miles de sitios solo con el nombre de usuario, sin claves de API, extrae información disponible en las páginas (nombres, enlaces, otros alias) y busca recursivamente los nuevos identificadores. Genera informes HTML, PDF, XMind y JSON; ofrece interfaz web en Docker.

## ¿Cómo lo hace?

Requiere Python 3.10+; se instala con `pip install maigret` (el extra `maigret[pdf]` añade PDF) o con Docker, incluida una imagen web. Puede usar FlareSolverr para sitios protegidos y ejecutarse en cuadernos o shells en la nube.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [theHarvester](theharvester.md) | theHarvester aporta correos y nombres de un dominio autorizado que después se investigan como alias con Maigret (combinación por arquitectura). | Ejecuta theHarvester; después pasa los identificadores a Maigret. |
| [Claude Code](claude-code.md) | Un agente puede leer el informe JSON de Maigret y resumir hallazgos y coincidencias dudosas (combinación por arquitectura). | Genera el informe JSON; después pide al agente el resumen con verificación manual. |
| [DuckDB](duckdb.md) | Los informes JSON o CSV de varias búsquedas se pueden consolidar y consultar con DuckDB (combinación por arquitectura). | Exporta los informes; después consúltalos con DuckDB. |

**Notas:** Alternativas (elige una): sherlock. El README incluye patrocinios de proxies y servicios de pago no necesarios para la herramienta.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.6.6 (2026-09-18) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/soxoj/maigret/blob/main/README.md) · [2](https://maigret.readthedocs.io/)</sub>

## Ver similares

Grupo **Búsqueda de usuarios en redes sociales**: Maigret ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Sherlock](sherlock.md) ⭐ recomendado | 67 | Si buscas esto: cLI OSINT que busca un nombre de usuario en más de 400 redes sociales y sitios para localizar cuentas asociadas. |
| 2 | **Maigret** (esta ficha) | 63 | Si buscas esto: recopila un dossier sobre una persona a partir de un nombre de usuario comprobando miles de sitios y extrayendo datos públicos de los perfiles. |

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
pip install maigret
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/soxoj/maigret/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Maigret para mi objetivo y necesito pasos guiados. Lee https://github.com/soxoj/maigret/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install maigret` (Python 3.10+) y busca un alias propio con salida HTML..

**Qué comprobar:** Se genera un informe HTML con los perfiles encontrados y los datos extraídos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- auditar la huella pública de un alias propio
- investigaciones OSINT autorizadas que requieren un informe consolidado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: auditar la huella pública de un alias propio; investigaciones OSINT autorizadas que requieren un informe consolidado | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Uso OSINT sobre personas: respeta las leyes de protección de datos aplicables (p. ej. RGPD o LFPDPPP) y los términos de cada sitio.

## Stack y modelos

- **Stack:** Python, Dockerfile, pyproject.toml
- **Etiquetas:** `osint` `python` `cli` `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Sherlock](sherlock.md) | 113k | CLI OSINT que busca un nombre de usuario en más de 400 redes sociales y sitios para localizar cuentas asociadas. |

## Enlaces

- 🐙 GitHub: [soxoj/maigret](https://github.com/soxoj/maigret)
- 🌐 Web: <https://maigret.app/gh>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/soxoj/maigret/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
