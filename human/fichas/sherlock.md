[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Inteligencia de fuentes abiertas y mapas

# 🖥️ Sherlock

> CLI OSINT que busca un nombre de usuario en más de 400 redes sociales y sitios para localizar cuentas asociadas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 113k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta OSINT de código abierto (MIT) mantenida por el Sherlock Project y su comunidad. Muy popular; el README advierte de que los paquetes de terceros para ParrotOS y Ubuntu 24.04 parecen estar rotos.

## ¿Qué hace?

Busca cuentas por nombre de usuario en más de 400 redes sociales y sitios, informa de las URL encontradas y exporta resultados en texto, CSV o XLSX, con opciones de proxy, Tor y tiempo de espera.

## ¿Cómo lo hace?

Escrito en Python; se instala con pipx, pip, uv o Docker (`docker run -it --rm sherlock/sherlock`). La lista de sitios y sus reglas de detección vive en un archivo JSON mantenido por la comunidad, por lo que los falsos positivos y negativos cambian con el tiempo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [theHarvester](theharvester.md) | theHarvester recoge correos, nombres y dominios de una organización y Sherlock busca los alias encontrados en redes sociales (combinación por arquitectura). | Ejecuta theHarvester sobre el dominio autorizado; después pasa los alias a Sherlock. |
| [Claude Code](claude-code.md) | Un agente puede ejecutar Sherlock y resumir o verificar los perfiles encontrados (combinación por arquitectura). | Instala Sherlock; después pide al agente la búsqueda y la revisión manual de resultados. |
| [DuckDB](duckdb.md) | Los resultados en CSV de varias búsquedas se pueden cruzar con DuckDB (combinación por arquitectura). | Exporta a CSV con Sherlock; después consulta los archivos con DuckDB. |

**Notas:** Alternativas (elige una): maigret.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v0.16.2 (2026-09-08) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/sherlock-project/sherlock/blob/master/docs/README.md)</sub>

## Ver similares

Grupo **Búsqueda de usuarios en redes sociales**: Sherlock ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Sherlock** (esta ficha) ⭐ recomendado | 67 | Si buscas esto: cLI OSINT que busca un nombre de usuario en más de 400 redes sociales y sitios para localizar cuentas asociadas. |
| 2 | [Maigret](maigret.md) | 63 | Si buscas esto: recopila un dossier sobre una persona a partir de un nombre de usuario comprobando miles de sitios y extrayendo datos públicos de los perfiles. |

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
pipx install sherlock-project
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/sherlock-project/sherlock/blob/master/docs/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Sherlock para mi objetivo y necesito pasos guiados. Lee https://github.com/sherlock-project/sherlock/blob/master/docs/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pipx install sherlock-project` y busca un nombre de usuario propio..

**Qué comprobar:** La salida lista las URL de los perfiles encontrados y guarda un archivo de resultados..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- comprobar dónde está registrado un nombre de usuario propio o de tu marca
- iniciar una investigación OSINT autorizada a partir de un alias

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: comprobar dónde está registrado un nombre de usuario propio o de tu marca; iniciar una investigación OSINT autorizada a partir de un alias | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Uso OSINT sobre personas: respeta las leyes de protección de datos aplicables (p. ej. RGPD o LFPDPPP) y los términos de cada sitio.

## Stack y modelos

- **Stack:** Python, Dockerfile, pyproject.toml
- **Etiquetas:** `osint` `python` `cli` `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Maigret](maigret.md) | 40.8k | Recopila un dossier sobre una persona a partir de un nombre de usuario comprobando miles de sitios y extrayendo datos públicos de los perfiles. |

## Enlaces

- 🐙 GitHub: [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock)
- 🌐 Web: <https://sherlockproject.xyz>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/sherlock-project/sherlock/blob/master/docs/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
