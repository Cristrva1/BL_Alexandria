[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Detección, SIEM e IDS

# 📚 OWASP Coraza

> WAF en Go compatible con ModSecurity SecLang y el OWASP Core Rule Set, embebible en servidores y proxies como Caddy, Envoy o Traefik.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4k | Apache-2.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

**Puntuación de calidad** 59/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto OWASP de nivel producción: un framework WAF en Go compatible con ModSecurity y el OWASP CRS.

## ¿Qué hace?

Inspecciona peticiones y respuestas HTTP con reglas SecLang y permite interrumpirlas, registrar eventos y aplicar el CRS.

## ¿Cómo lo hace?

Biblioteca Go importable que procesa transacciones por fases; se integra en servidores mediante módulos (Caddy, proxy-wasm para Envoy, Traefik y otros).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OWASP CRS](coreruleset.md) | Coraza ejecuta el OWASP CRS como conjunto de reglas base. | Integra Coraza; después carga el CRS en modo detección. |
| [Caddy](caddy.md) | El módulo coraza-caddy añade el WAF a Caddy. | Compila Caddy con el módulo de Coraza y configura las reglas. |
| [Traefik Proxy](traefik.md) | Coraza figura entre las integraciones para Traefik en su README. | Traefik desplegado; añade la integración de Coraza según su documentación. |

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v3.8.1 (2026-10-02) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/corazawaf/coraza#readme) · [2](https://coraza.io/docs/)</sub>

## Ver similares

Grupo **WAF compatibles con SecLang y el OWASP CRS**: OWASP Coraza ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ModSecurity](modsecurity.md) ⭐ recomendado | 70 | Si usas Nginx o Apache y quieres el motor WAF de referencia con sus conectores. |
| 2 | **OWASP Coraza** (esta ficha) | 59 | Si tu servicio o proxy está en Go (Caddy, Traefik, Envoy vía proxy-wasm) y quieres el WAF embebido. |

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

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/corazawaf/coraza/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://coraza.io/docs/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP Coraza para mi objetivo y necesito pasos guiados. Lee https://github.com/corazawaf/coraza/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue el ejemplo de uso de Coraza del README en un programa Go de prueba con una regla sencilla..

**Qué comprobar:** La transacción con la carga de prueba queda interrumpida por la regla..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- añadir un WAF con el CRS a un servicio escrito en Go
- proteger un Caddy de laboratorio con el módulo de Coraza

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: añadir un WAF con el CRS a un servicio escrito en Go; proteger un Caddy de laboratorio con el módulo de Coraza | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Es una biblioteca: el despliegue depende de la integración elegida; prueba el CRS en modo detección antes de bloquear.

## Stack y modelos

- **Stack:** Go, go.mod
- **Etiquetas:** `security` `waf` `go` `seclang`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ModSecurity](modsecurity.md) | 9.9k | Motor WAF de código abierto (libmodsecurity v3) que inspecciona peticiones HTTP con reglas SecLang como el OWASP Core Rule Set. |

## Enlaces

- 🐙 GitHub: [corazawaf/coraza](https://github.com/corazawaf/coraza)
- 🌐 Web: <https://www.coraza.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/corazawaf/coraza/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
