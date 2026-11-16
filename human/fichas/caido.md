[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ Caido

> Proxy de pentest web moderno (alternativa a Burp): core HTTP gratis (Basic); Individual/Team/Enterprise de pago. No es open source.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 2.7k | — | Shell | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

> ⚠️ **Licencia y costes:** Caido no es open source: el repositorio de GitHub solo aloja roadmap, issues y plugins, no el código del producto. Plan Basic gratuito con límites (2 proyectos, 7 workflows, 3 plugins, sin asistente IA ni backups); planes Individual, Team y Enterprise de pago (caido.io/pricing, consultado 2026-11-16). Alternativa open source en el catálogo: ZAP.

## ¿Qué es?

Proxy de pentest web propietario (no open source) de Caido Labs. Plan Basic gratuito con límites; Individual, Team y Enterprise de pago.

## ¿Qué hace?

Intercepta, inspecciona y reenvía HTTP/S para AppSec.

## ¿Cómo lo hace?

Descarga desde el dashboard; este repo es branding/roadmap/plugins.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Nuclei](nuclei.md) | Tras mapear con Caido, Nuclei escanea. | Caido → Nuclei. |
| [ffuf](ffuf.md) | Fuzzing junto al proxy. | Caido + ffuf. |

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v0.59.1 (2026-11-13) (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/caido/caido#readme) · [2](https://caido.io/) · [3](https://caido.io/pricing)</sub>

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/caido/caido/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Caido para mi objetivo y necesito pasos guiados. Lee https://github.com/caido/caido/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea cuenta en dashboard.caido.io, descarga el cliente Basic y apunta el proxy al lab..

**Qué comprobar:** Tráfico HTTP visible en Caido..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- interceptar tráfico de una app de lab
- reproducir requests en un ejercicio web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: interceptar tráfico de una app de lab; reproducir requests en un ejercicio web | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo. No es open source. Basic gratis limitado; Individual/Team/Enterprise de pago. Repo GitHub ≠ código del producto.

## Stack y modelos

- **Stack:** Shell
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [ZAP (Zed Attack Proxy)](zaproxy.md) | 16.2k | Escáner de seguridad de aplicaciones web más usado (antes OWASP ZAP, ahora ZAP by Checkmarx): proxy interceptor, araña y escaneo activo. |

## Enlaces

- 🐙 GitHub: [caido/caido](https://github.com/caido/caido)
- 🌐 Web: <https://caido.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/caido/caido/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
