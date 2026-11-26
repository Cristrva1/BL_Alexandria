[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ Gobuster

> Fuzzing y descubrimiento de directorios, DNS y buckets en Go; clásico de pentest web autorizado.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.3k | Apache-2.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 56/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Dirbuster/fuzzer en Go muy usado en pentest.

## ¿Qué hace?

Fuerza rutas, DNS y vhosts con diccionarios.

## ¿Cómo lo hace?

`go install` o Docker ghcr.io/oj/gobuster.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [SecLists](seclists.md) | SecLists alimenta Gobuster. | Clona SecLists; `-w` a Gobuster. |
| [Nuclei](nuclei.md) | Nuclei tras descubrir rutas. | Gobuster → Nuclei. |

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada v3.8.2 (2025-09-04) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OJ/gobuster#readme)</sub>

## Ver similares

Grupo **Fuzzing de rutas y contenido web**: Gobuster ocupa la posición 4 de 4 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [ffuf](ffuf.md) ⭐ recomendado | 66 | Si quieres el fuzzer web más versátil (rutas, parámetros, vhosts) y rápido en Go. |
| 2 | [dirsearch](dirsearch.md) | 58 | Si prefieres una herramienta en Python con listas y reportes listos. |
| 3 | [feroxbuster](feroxbuster.md) | 58 | Si quieres descubrimiento recursivo de contenido automático en Rust. |
| 4 | **Gobuster** (esta ficha) | 56 | Si quieres un enumerador simple de directorios, DNS y vhosts. |

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
go install github.com/OJ/gobuster/v3@latest
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/OJ/gobuster/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Gobuster para mi objetivo y necesito pasos guiados. Lee https://github.com/OJ/gobuster/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `go install github.com/OJ/gobuster/v3@latest` y lanza modo dir contra un lab..

**Qué comprobar:** Listas rutas encontradas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- descubrir rutas ocultas en una app de lab
- enumerar vhosts de un dominio propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: descubrir rutas ocultas en una app de lab; enumerar vhosts de un dominio propio | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** Go, Dockerfile, go.mod
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [feroxbuster](feroxbuster.md) | 8.2k | Dirbuster rápido en Rust con recursión, filtros y salidas flexibles para descubrimiento de contenidos web. |
| [dirsearch](dirsearch.md) | 15.1k | Dirbuster en Python ampliamente usado para descubrir rutas y ficheros en aplicaciones web de laboratorio. |
| [ffuf](ffuf.md) | 17.1k | Fuzzer web rápido en Go para descubrir contenido, hosts virtuales y parámetros, con filtros, modo interactivo y proxy. |

## Enlaces

- 🐙 GitHub: [OJ/gobuster](https://github.com/OJ/gobuster)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OJ/gobuster/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
