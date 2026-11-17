[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Skills de análisis y seguridad

# 🛡️ Defending Code Reference Harness

> Arnés de referencia de Anthropic con skills para modelar amenazas, escanear, priorizar y parchear vulnerabilidades.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.8k | Apache-2.0 | Python | 2026-06-24 |

**Ejecución** ☁️ cloud/API · **Rol** 🎨 skill/prompt · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; se instala dentro de un agente (skill, plugin o MCP)

**Puntuación de calidad** 49/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** Apache-2.0. Fuente: [LICENSE](https://github.com/anthropics/defending-code-reference-harness/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Implementación de referencia de Anthropic para descubrir y corregir vulnerabilidades de forma autónoma con Claude, basada en su trabajo con equipos de seguridad tras lanzar Claude Mythos Preview. El archivo LICENSE es Apache-2.0, aunque GitHub muestra NOASSERTION. Es una referencia para adaptar, no un producto (~8k estrellas, sin releases).

## ¿Qué hace?

Sigue el ciclo reconocimiento → búsqueda → triaje → informe → parche, con verificación en varias etapas para reducir falsos positivos y gestión de hallazgos (triaje, validación de la corrección, generación rápida de parches). Incluye skills de Claude Code (`/quickstart`, `/threat-model`, `/vuln-scan`, entre otras) y un arnés con agentes en contenedores. Comprueba que la prueba de concepto deja de fallar y que los tests del objetivo siguen pasando.

## ¿Cómo lo hace?

Es Python (`pip install -e .`) con Docker y gVisor para aislar los agentes (`scripts/setup_sandbox.sh`). Funciona con cualquier acceso a la API de Claude (API key, token OAuth de Claude Code, Bedrock, Vertex o Azure). Las skills se pueden usar sin sandbox solo si revisas y apruebas cada uso de herramientas en Claude Code.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Claude Code](claude-code.md) | Las skills del repo se ejecutan en Claude Code. | Clona el repo y usa `/quickstart` desde Claude Code. |
| [Semgrep](semgrep.md) | Añadir candidatos deterministas al reconocimiento. (combinación por arquitectura) | Ejecuta Semgrep y aporta sus hallazgos a la fase de búsqueda. |
| [strix](strix.md) | Validar dinámicamente en un entorno de prueba los hallazgos del arnés. (combinación por arquitectura) | Despliega el objetivo en un entorno aislado y lanza Strix contra él. |

**Notas:** Sin alternativas declaradas. Úsalo solo contra sistemas propios o con autorización escrita.

Estado en GitHub: activo · último push 2026-08-06 · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/anthropics/defending-code-reference-harness/blob/main/README.md) · [2](https://claude.com/blog/using-llms-to-secure-source-code) · [3](https://www.anthropic.com/glasswing)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Depende de la ruta elegida. Skills interactivas usan el agente; el harness autónomo tiene autenticación API, OAuth o Bedrock según su guía y consume por ejecución |
| Claude Code | Dentro del agente: skills o instrucciones |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El CLI autónomo y las skills son rutas distintas; el sandbox usa dependencias adicionales y no se configura solo por clonar |
| Coste | El coste depende del proveedor o la ruta. Skills interactivas usan el agente; el harness autónomo tiene autenticación API, OAuth o Bedrock según su guía y consume por ejecución |
| Equipo | Preparación según la ruta elegida. Claude Code; Python y Docker para harness aislado; objetivo canary de práctica |

El CLI autónomo y las skills son rutas distintas; el sandbox usa dependencias adicionales y no se configura solo por clonar

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Claude Code
- Python y Docker para harness aislado
- objetivo canary de práctica

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.
4. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

**Entrada documentada (bash):**

```
git clone https://github.com/anthropics/defending-code-reference-harness
cd defending-code-reference-harness
claude
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/anthropics/defending-code-reference-harness/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Defending Code Reference Harness para mi objetivo y necesito pasos guiados. Lee https://github.com/anthropics/defending-code-reference-harness/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Abre el repositorio en Claude Code y usa quickstart sobre el canary incluido.

**Qué comprobar:** Puedes revisar un hallazgo contra el objetivo y su evidencia de práctica.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Aprender un flujo de modelado de amenazas
- Priorizar y revisar parches en software autorizado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Aprender un flujo de modelado de amenazas; Priorizar y revisar parches en software autorizado | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El CLI autónomo y las skills son rutas distintas; el sandbox usa dependencias adicionales y no se configura solo por clonar

## Stack y modelos

- **Stack:** Claude Code; Python y Docker para harness aislado; objetivo canary de práctica
- **Etiquetas:** `security` `skills` `coding-agent`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [anthropics/defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness)
- 🌐 Web: <https://claude.com/blog/using-llms-to-secure-source-code>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría corregida en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/anthropics/defending-code-reference-harness/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
