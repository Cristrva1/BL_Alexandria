[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ WPScan

> Escáner de WordPress: usuarios, temas, plugins y vulns vía API (25 req/día gratis; DB Enterprise de pago).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.9k | WPScan Public Source License (no OSI) | Ruby | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia y costes:** WPScan usa la «WPScan Public Source License»: gratis para pentesting propio o como parte de una auditoría, pero el uso comercial (SaaS, producto o servicio de valor añadido) exige licencia de pago. Los datos de vulnerabilidades vienen de la API de wpscan.com: 25 peticiones/día gratis con token; sin token o agotada la cuota escanea sin datos de vulnerabilidades. La base local Enterprise es de pago.

> **Licencia revisada el 2026-11-16:** WPScan Public Source License (no OSI). La comercialización requiere licencia comercial. Fuente: [LICENSE](https://github.com/wpscanteam/wpscan/blob/master/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Escáner de WordPress (WPScan Public Source License, source-available con cláusula comercial). La base de vulnerabilidades depende de la API de wpscan.com: 25 peticiones/día gratis; Enterprise de pago.

## ¿Qué hace?

Enumera y detecta vulnerabilidades en sitios WordPress.

## ¿Cómo lo hace?

gem, brew tap o Docker wpscanteam/wpscan.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Nuclei](nuclei.md) | Nuclei amplía checks web genéricos. | WPScan para WP; Nuclei para el resto. |
| [ffuf](ffuf.md) | Fuzzing de rutas junto al escaneo WP. | WPScan → ffuf. |

Estado en GitHub: activo · último push 2026-11-07 · última versión publicada v4.2.0 (2026-10-27) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/wpscanteam/wpscan#readme) · [2](https://wpscan.com/wordpress-cli-scanner)</sub>

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

**Entrada documentada (consulta la sintaxis original):**

```
gem install wpscan
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/wpscanteam/wpscan/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar WPScan para mi objetivo y necesito pasos guiados. Lee https://github.com/wpscanteam/wpscan/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `gem install wpscan` o Docker y escanea un WP de lab con `--api-token` si tienes..

**Qué comprobar:** Informe de usuarios/plugins/vulns según cuota API..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- auditar un WordPress de staging propio
- enumerar plugins desactualizados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: auditar un WordPress de staging propio; enumerar plugins desactualizados | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo. API vulns: 25 peticiones/día gratis; Enterprise Local DB de pago. Licencia source-available con cláusula comercial.

## Stack y modelos

- **Stack:** Ruby, Dockerfile, Gemfile
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [wpscanteam/wpscan](https://github.com/wpscanteam/wpscan)
- 🌐 Web: <https://wpscan.com/wordpress-cli-scanner>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/wpscanteam/wpscan/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
