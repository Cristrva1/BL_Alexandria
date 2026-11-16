[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# 🛡️ Semgrep

> Análisis estático ligero para muchos lenguajes con reglas que se parecen al código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.7k | LGPL-2.1 | C | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Herramienta de análisis estático rápida y open source para buscar código, encontrar bugs y aplicar normas de seguridad. La edición comunitaria es LGPL-2.1; la empresa Semgrep vende la AppSec Platform con reglas y análisis propietarios. Es muy madura y activa (~18k estrellas, v1.185.0).

## ¿Qué hace?

Busca patrones con reglas que se parecen al propio código, en más de 30 lenguajes, y se usa en local, en el editor o en CI. Tiene un registro público de reglas. El README admite que, en seguridad, la edición comunitaria pierde muchos verdaderos positivos porque solo analiza dentro de una función o archivo; el análisis entre archivos, SCA y secretos con más de 20.000 reglas propietarias es de pago.

## ¿Cómo lo hace?

Está escrito en OCaml con envoltorio Python; se instala con `brew install semgrep`, `pip install semgrep` o Docker, y se ejecuta con `semgrep scan` o `semgrep ci`. El servidor MCP para escanear desde agentes vive ahora dentro del propio binario `semgrep` (el repo independiente semgrep/mcp está archivado). Las reglas propias se escriben en YAML.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Ejecutar escaneos desde el agente con el servidor MCP incluido en el binario de Semgrep. | Instala Semgrep y registra su servidor MCP en el agente. |
| [security-audit-skill](security-audit-skill.md) | Usar hallazgos deterministas de Semgrep como candidatos que el agente valida. (combinación por arquitectura) | Ejecuta Semgrep primero y pasa los resultados a la auditoría. |
| [strix](strix.md) | Combinar análisis estático en CI con pruebas dinámicas por agentes. (combinación por arquitectura) | Pon Semgrep en cada PR y Strix en entornos de prueba. |
| [Defending Code Reference Harness](defending-code-reference-harness.md) | Combinación recíproca: Defending Code Reference Harness lo enlaza como «Añadir candidatos deterministas al reconocimiento. (combinación por arquitectura)». | Orden indicado desde Defending Code Reference Harness: Ejecuta Semgrep y aporta sus hallazgos a la fase de búsqueda. |
| [raddebugger](raddebugger.md) | Combinación recíproca: raddebugger lo enlaza como «Encontrar con análisis estático los fallos que luego reproduces en el depurador. (combinación por arquitectura)». | Orden indicado desde raddebugger: Ejecuta Semgrep en CI y depura los hallazgos con RAD Debugger. |
| [shannon](shannon.md) | Combinación recíproca: shannon lo enlaza como «Análisis estático previo para priorizar rutas. (combinación por arquitectura)». | Orden indicado desde shannon: Ejecuta Semgrep en el repo antes de la prueba. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (9). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[AFL++](aflplusplus.md) · [Checkov](checkov.md) · [Gitleaks](gitleaks.md) · [Grype](grype.md) · [OWASP CheatSheet Series](cheatsheetseries.md) · [pre-commit](pre-commit.md) · [Prowler](prowler.md) · [Trivy](trivy.md) · [TruffleHog](trufflehog.md)

**Notas:** Alternativas (elige una): ast-grep. La combinación con defending-code-reference-harness pasa a marcarse por arquitectura.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.185.0 (2026-11-10) · licencia declarada LGPL-2.1 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/semgrep/semgrep/blob/develop/README.md) · [2](https://github.com/semgrep/semgrep/tree/develop/cli/src/semgrep/mcp) · [3](https://semgrep.dev/docs/getting-started/quickstart)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El motor abierto no necesita LLM; AppSec, análisis comerciales y funciones AI tienen condiciones propias |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El README documenta plugin de Claude Code; un hallazgo estático necesita revisión y no demuestra por sí solo una vulnerabilidad explotable |
| Coste | El coste depende del proveedor o la ruta. El motor abierto no necesita LLM; AppSec, análisis comerciales y funciones AI tienen condiciones propias |
| Equipo | Preparación según la ruta elegida. Python mediante uv o pipx; carpeta de prueba; WSL si tu ruta Windows lo necesita |

El README documenta plugin de Claude Code; un hallazgo estático necesita revisión y no demuestra por sí solo una vulnerabilidad explotable

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python mediante uv o pipx
- carpeta de prueba
- WSL si tu ruta Windows lo necesita

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (shell):**

```
uv tool install semgrep
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/semgrep/semgrep/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Semgrep para mi objetivo y necesito pasos guiados. Lee https://github.com/semgrep/semgrep/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta una regla sencilla sobre un archivo ficticio con un patrón conocido.

**Qué comprobar:** El hallazgo señala la línea y puedes comprobarlo manualmente.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Detectar patrones inseguros repetidos
- Aplicar reglas de calidad en CI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Detectar patrones inseguros repetidos; Aplicar reglas de calidad en CI | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El README documenta plugin de Claude Code; un hallazgo estático necesita revisión y no demuestra por sí solo una vulnerabilidad explotable

## Stack y modelos

- **Stack:** Python mediante uv o pipx; carpeta de prueba; WSL si tu ruta Windows lo necesita
- **Etiquetas:** `security` `code`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ast-grep](ast-grep.md) | 16.6k | CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. |
| [SonarQube Community Build](sonarqube.md) | 11.2k | Plataforma de inspección continua de calidad y seguridad del código: análisis estático de bugs, vulnerabilidades y mantenibilidad en muchos lenguajes. |

## Enlaces

- 🐙 GitHub: [semgrep/semgrep](https://github.com/semgrep/semgrep)
- 🌐 Web: <https://semgrep.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría corregida en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/semgrep/semgrep/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
