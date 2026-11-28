[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# 📚 CodeQL

> Busca vulnerabilidades en el código de un repositorio público siguiendo cómo viajan los datos y muestra cada alerta en la pestaña de seguridad de GitHub.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.4k | MIT (consultas y bibliotecas); CodeQL CLI con términos propios de GitHub | CodeQL | 2026-11-27 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟢 fácil

**Nivel:** 2 Intermedio — preparación sencilla; requiere programar con él

**Puntuación de calidad** 67/100 · métricas del 2026-11-28 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia y costes:** Las consultas y bibliotecas de este repositorio son MIT. El motor que las ejecuta (CodeQL CLI y el paquete que usa GitHub Actions) se rige por los GitHub CodeQL Terms and Conditions, que no son una licencia de código abierto. Permiten usarlo gratis para investigación académica, demostraciones, pruebas de consultas publicadas con licencia OSI y análisis de código publicado con una licencia aprobada por la OSI; para generar bases de datos en análisis automático, CI o CD, ese código abierto debe estar alojado en GitHub.com. Analizar código privado o cerrado (por ejemplo, un repositorio privado) exige una licencia de pago de GitHub Advanced Security, hoy GitHub Code Security. Los términos prohíben también ofrecer CodeQL como servicio para terceros.

## ¿Qué es?

Colección abierta de consultas y bibliotecas con la que GitHub busca vulnerabilidades en el código.

## ¿Qué hace?

Señala en tu repositorio los puntos donde datos de fuera llegan a operaciones peligrosas, como comandos del sistema o consultas a bases de datos.

## ¿Cómo lo hace?

Extrae el código a una base de datos consultable, ejecuta consultas QL que rastrean el flujo de datos y publica los resultados como alertas de code scanning en formato SARIF.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [GitHub MCP Server](github-mcp-server.md) | Permite que un agente lea y resuma las alertas de code scanning del repositorio mediante sus herramientas code_security. | — |
| [OSV-Scanner](osv-scanner.md) | Revisa las dependencias contra vulnerabilidades publicadas; CodeQL revisa el código que escribes tú. | — |
| [DefectDojo](defectdojo.md) | Importa el informe SARIF para seguir los hallazgos junto con los de otros escáneres. | — |

Estado en GitHub: activo · último push 2026-11-27 · licencia declarada MIT (consultado el 2026-11-27).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-27); no se instaló ni ejecutó. Fuentes: [1](https://github.com/github/codeql/blob/ddc0325ff08acb437bfaf503904ab96360fb169a/README.md) · [2](https://github.com/github/codeql/blob/ddc0325ff08acb437bfaf503904ab96360fb169a/LICENSE) · [3](https://github.com/github/codeql-cli-binaries/blob/9d0dcfbe60daef8e62688852c0977065865c80a0/LICENSE.md) · [4](https://github.com/github/codeql-cli-binaries/blob/9d0dcfbe60daef8e62688852c0977065865c80a0/README.md) · [5](https://github.com/github/codeql-cli-binaries/releases/tag/v2.27.6) · [6](https://github.com/github/codeql-action/releases/tag/codeql-bundle-v2.27.6) · [7](https://github.com/github/codeql-action/releases/tag/v4.39.5) · [8](https://github.com/github/codeql-action/blob/38112626f97ac1fd7acf3df7ebca51f4677c1b38/README.md) · [9](https://github.com/github/codeql-action/blob/915412ff23e8b7659517e607487dbeae018f2934/src/defaults.json) · [10](https://github.com/github/codeql-action/blob/915412ff23e8b7659517e607487dbeae018f2934/.github/workflows/__multi-language-autodetect.yml) · [11](https://github.com/github/codeql-action/actions/runs/45419775563) · [12](https://github.com/github/codeql/blob/ddc0325ff08acb437bfaf503904ab96360fb169a/python/ql/src/Security/CWE-078/CommandInjection.ql) · [13](https://github.com/github/codeql/blob/ddc0325ff08acb437bfaf503904ab96360fb169a/python/ql/test/query-tests/Security/CWE-078-CommandInjection/command_injection.py) · [14](https://github.com/github/docs/blob/6dd875c27b0a1262bb71679e979059c80ff8de72/content/code-security/how-tos/find-and-fix-code-vulnerabilities/configure-code-scanning/configure-code-scanning.md) · [15](https://github.com/github/docs/blob/6dd875c27b0a1262bb71679e979059c80ff8de72/data/reusables/gated-features/code-scanning.md) · [16](https://github.com/github/docs/blob/6dd875c27b0a1262bb71679e979059c80ff8de72/content/billing/concepts/product-billing/github-actions.md) · [17](https://github.com/github/codeql-cli-binaries/security/advisories) · [18](https://github.com/github/codeql-action/security/advisories) · [19](https://github.com/github/codeql/security/advisories) · [20](https://github.com/github/github-mcp-server/blob/1a3b6a7a9151343200f3566ac24ea5db29f7319e/README.md) · [21](https://github.com/DefectDojo/django-DefectDojo/tree/cd0a4483a224707f72a0fc3112359089c1446b55/dojo/tools/sarif)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita clave de API de IA, solo una cuenta gratuita de GitHub. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El análisis no usa modelos de IA: aplica consultas al código. |
| Coste | Sin pago a un modelo en la ruta básica. Code scanning y los ejecutores estándar de GitHub Actions son gratuitos en repositorios públicos. En repositorios privados de organizaciones hace falta GitHub Code Security, de pago. El CLI no puede usarse gratis con código cerrado. |
| Equipo | Equipo normal; revisar dependencias. Con la configuración predeterminada basta un navegador: el análisis corre en servidores de GitHub. El paquete local pesa entre 400 y 700 MB comprimido según el sistema, y necesita las herramientas de compilación de los lenguajes que lo requieran. |

Un agente de código puede ayudarte a preparar el repositorio o a leer las alertas, por ejemplo con el servidor MCP de GitHub. CodeQL se ejecuta en GitHub Actions o en tu equipo sin suscripción de IA. Las sugerencias de corrección con IA de GitHub (Copilot Autofix) son un servicio aparte y opcional.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Crea una cuenta gratuita de GitHub y un repositorio público nuevo de prueba con licencia MIT u otra aprobada por la OSI. Los términos de CodeQL solo permiten el uso gratuito sobre código abierto publicado así o para investigación académica.
2. No instales nada: en Settings > Advanced Security, junto a «CodeQL analysis», elige Set up > Default y pulsa Enable CodeQL. GitHub ejecuta en sus servidores el paquete vigente (codeql-action v4.39.5 usa CodeQL 2.27.6 por defecto), sin coste en repositorios públicos.
3. Sube el app.py de la primera prueba, espera a que el flujo CodeQL termine en Actions y abre Code scanning en la pestaña de seguridad. Para usarlo en tu equipo, descarga el CLI 2.27.6 desde github/codeql-cli-binaries; se aplican las mismas condiciones de licencia.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/github/codeql/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar CodeQL para mi objetivo y necesito pasos guiados. Lee https://github.com/github/codeql/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En un repositorio público propio con licencia MIT, sube app.py con una ruta Flask que lee carpeta = request.args.get('carpeta') y ejecuta subprocess.Popen('ls ' + carpeta, shell=True). Activa CodeQL en Settings > Advanced Security > CodeQL analysis > Set up > Default.

**Qué comprobar:** Cuando termina el flujo CodeQL en la pestaña Actions, el apartado Code scanning de la pestaña de seguridad muestra la alerta «Uncontrolled command line» con la regla py/command-line-injection en la línea de Popen.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Activar el análisis automático en un repositorio público propio y revisar las alertas antes de publicar una versión
- Comprobar si un cambio en una pequeña aplicación Flask abre una inyección de comandos antes de fusionarlo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Activar el análisis automático en un repositorio público propio y revisar las alertas antes de publicar una versión; Comprobar si un cambio en una pequeña aplicación Flask abre una inyección de comandos antes de fusionarlo | Necesitas analizar código privado o de clientes sin licencia de pago de GitHub, o prefieres reglas sencillas que puedas escribir sin aprender el lenguaje QL. |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Úsalo gratis solo con repositorios públicos con licencia de código abierto o con fines académicos: el código privado o de clientes requiere licencia de pago de GitHub. No subas secretos ni código ajeno al repositorio de prueba. Si instalas el CLI, usa 2.20.3 o posterior por los avisos publicados (mejor 2.27.6) y no publiques artefactos de depuración en repositorios públicos.

## Stack y modelos

- **Stack:** CodeQL, Cargo.toml
- **Etiquetas:** `análisis estático` `flujo de datos` `github` `sarif` `seguridad`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Semgrep](semgrep.md) | 17.7k | Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. |

## Enlaces

- 🐙 GitHub: [github/codeql](https://github.com/github/codeql)
- 🌐 Web: <https://codeql.github.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-27. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/github/codeql-cli-binaries/blob/9d0dcfbe60daef8e62688852c0977065865c80a0/LICENSE.md)
- [Fuente 2](https://github.com/github/codeql-action/blob/38112626f97ac1fd7acf3df7ebca51f4677c1b38/README.md)
- [Fuente 3](https://github.com/github/docs/blob/6dd875c27b0a1262bb71679e979059c80ff8de72/data/reusables/gated-features/code-scanning.md)
- [Fuente 4](https://github.com/github/docs/blob/6dd875c27b0a1262bb71679e979059c80ff8de72/content/billing/concepts/product-billing/github-actions.md)
- [Fuente 5](https://github.com/github/docs/blob/6dd875c27b0a1262bb71679e979059c80ff8de72/data/reusables/rai/code-scanning/gated-feature-autofix.md)
- [Fuente 6](https://github.com/github/codeql-cli-binaries/releases/tag/v2.27.6)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
