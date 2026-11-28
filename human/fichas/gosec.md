[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# 🖥️ gosec

> Revisa código Go en busca de problemas de seguridad, como criptografía débil, comandos armados con datos externos o credenciales en el código.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9k | Apache-2.0 | Go | 2026-11-27 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 71/100 · métricas del 2026-11-28 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Analizador de seguridad de código fuente para Go, del proyecto securego.

## ¿Qué hace?

Encuentra patrones de riesgo en programas Go, los relaciona con categorías CWE y los entrega en texto, JSON, SARIF y otros formatos.

## ¿Cómo lo hace?

Combina reglas sobre el árbol de sintaxis, analizadores sobre la forma SSA del programa y un análisis de contaminación que sigue datos de entrada hasta llamadas peligrosas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OSV-Scanner](osv-scanner.md) | Revisa las dependencias de go.mod contra vulnerabilidades publicadas; gosec revisa tu propio código. | — |
| [DefectDojo](defectdojo.md) | Importa los informes de gosec para seguir y deduplicar hallazgos junto con los de otros escáneres. | — |

Estado en GitHub: activo · último push 2026-11-28 · última versión publicada v2.30.0 (2026-10-23) · licencia declarada Apache-2.0 (consultado el 2026-11-27).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-27); no se instaló ni ejecutó. Fuentes: [1](https://github.com/securego/gosec/blob/5eb1d104ef85ff2c905c877eb600e8c1dee33a22/README.md) · [2](https://github.com/securego/gosec/blob/5eb1d104ef85ff2c905c877eb600e8c1dee33a22/LICENSE.txt) · [3](https://github.com/securego/gosec/blob/5eb1d104ef85ff2c905c877eb600e8c1dee33a22/RULES.md) · [4](https://github.com/securego/gosec/blob/5eb1d104ef85ff2c905c877eb600e8c1dee33a22/go.mod) · [5](https://github.com/securego/gosec/blob/5eb1d104ef85ff2c905c877eb600e8c1dee33a22/rules/weakcrypto.go) · [6](https://github.com/securego/gosec/blob/5eb1d104ef85ff2c905c877eb600e8c1dee33a22/autofix/ai.go) · [7](https://github.com/securego/gosec/blob/5eb1d104ef85ff2c905c877eb600e8c1dee33a22/.github/workflows/ci.yml) · [8](https://github.com/securego/gosec/blob/5eb1d104ef85ff2c905c877eb600e8c1dee33a22/Makefile) · [9](https://github.com/securego/gosec/blob/5eb1d104ef85ff2c905c877eb600e8c1dee33a22/.goreleaser.yml) · [10](https://github.com/securego/gosec/actions/runs/39929569892) · [11](https://github.com/securego/gosec/actions/runs/39930030604) · [12](https://github.com/securego/gosec/releases/tag/v2.30.0) · [13](https://pkg.go.dev/github.com/securego/gosec/v2) · [14](https://formulae.brew.sh/formula/gosec) · [15](https://github.com/securego/gosec/security/advisories) · [16](https://github.com/DefectDojo/django-DefectDojo/tree/cd0a4483a224707f72a0fc3112359089c1446b55/dojo/tools/gosec)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. El análisis no necesita API. Las sugerencias de corrección admiten Atlas Cloud, Gemini, Claude, OpenAI o un servicio compatible con OpenAI, cada uno con su clave. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelos locales documentados. El análisis es local y no usa modelos. Para las sugerencias opcionales, el README admite una URL compatible con OpenAI, como Ollama o LocalAI. |
| Coste | El coste depende del proveedor o la ruta. gosec es Apache-2.0 y gratuito. Solo las sugerencias opcionales consumen la API del proveedor elegido; el README incluye promoción comercial de un proveedor patrocinador. |
| Equipo | Equipo normal; revisar dependencias. Cualquier equipo con Go 1.26 o posterior. |

Una suscripción de Claude Code o Codex no activa las sugerencias de gosec: requieren una clave de API propia. Un agente puede ayudarte a instalar gosec y a leer el informe.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Instala Go 1.26 o posterior desde go.dev: el go.mod de v2.30.0 declara go 1.26.0, aunque el README todavía indica 1.25.
2. Instala la versión revisada con go install github.com/securego/gosec/v2/cmd/gosec@v2.30.0 y comprueba gosec -version. Otras vías: los binarios de la publicación v2.30.0, con sumas de verificación y firmas cosign, o la fórmula gosec de Homebrew, que mantiene Homebrew y el README no menciona.
3. Prepara el módulo de la primera prueba y ejecuta gosec ./... para ver G401 y G501. Cambia a crypto/sha256 con sha256.Sum256 y repite: los dos hallazgos desaparecen.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/securego/gosec/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/securego/gosec/releases/tag/v2.30.0)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar gosec para mi objetivo y necesito pasos guiados. Lee https://github.com/securego/gosec/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En una carpeta nueva ejecuta go mod init ejemplo y crea main.go que importe crypto/md5 y fmt e imprima md5.Sum([]byte("hola")); después ejecuta gosec ./....

**Qué comprobar:** El informe lista G401 (uso de MD5 o SHA1) y G501 (importación bloqueada de crypto/md5) con archivo y línea, y el comando termina con código de salida 1.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar un servicio web propio en Go antes de publicarlo para encontrar inyecciones de comandos o rutas de archivo sin validar
- Generar un informe SARIF en GitHub Actions y verlo junto con las demás alertas de code scanning

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar un servicio web propio en Go antes de publicarlo para encontrar inyecciones de comandos o rutas de archivo sin validar; Generar un informe SARIF en GitHub Actions y verlo junto con las demás alertas de code scanning | Tu código no está escrito en Go o buscas revisar dependencias en lugar de tu propio código. |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Revisa cada hallazgo a mano y analiza solo código propio o con permiso. Las sugerencias de corrección con IA solo se activan si configuras proveedor y clave: según autofix/ai.go en v2.30.0 envían al servicio la descripción de cada hallazgo y consumen tu API.

## Stack y modelos

- **Stack:** Go, Dockerfile, Makefile, go.mod
- **Etiquetas:** `go` `análisis estático` `seguridad` `sarif`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [securego/gosec](https://github.com/securego/gosec)
- 🌐 Web: <https://securego.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-27. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/securego/gosec/blob/5eb1d104ef85ff2c905c877eb600e8c1dee33a22/README.md)
- [Fuente 2](https://github.com/securego/gosec/blob/5eb1d104ef85ff2c905c877eb600e8c1dee33a22/autofix/ai.go)
- [Fuente 3](https://github.com/securego/gosec/blob/5eb1d104ef85ff2c905c877eb600e8c1dee33a22/go.mod)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
