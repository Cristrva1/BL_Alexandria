[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ ffuf

> Fuzzer web rápido en Go para descubrir contenido, hosts virtuales y parámetros, con filtros, modo interactivo y proxy.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.1k | MIT | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Fuzzer web de código abierto (MIT) creado por Joona Hoikkala (joohoi). Maduro; ritmo de cambios moderado (último push en septiembre de 2026).

## ¿Qué hace?

Descubre directorios y archivos, hosts virtuales sin DNS, parámetros GET y datos POST mediante fuzzing, con mutadores externos, archivos de configuración, varios formatos de salida y modo interactivo para ajustar filtros.

## ¿Cómo lo hace?

Escrito en Go; se instala con binarios, Homebrew, Scoop, Winget o `go install`. Admite proxy (`-x`) y reenvío de coincidencias a otro proxy (`-replay-proxy`).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [subfinder](subfinder.md) | subfinder encuentra subdominios que después se fuzzean con ffuf (combinación por arquitectura). | Enumera con subfinder; después lanza ffuf sobre cada host. |
| [mitmproxy](mitmproxy.md) | ffuf puede enviar o reenviar sus peticiones a un proxy como mitmproxy para inspeccionarlas. | Arranca mitmproxy; después usa `-x` o `-replay-proxy` en ffuf. |
| [Nuclei](nuclei.md) | Las rutas que descubre ffuf se revisan después con plantillas de Nuclei (combinación por arquitectura). | Guarda la salida de ffuf; después pasa las URLs a nuclei. |
| [sqlmap](sqlmap.md) | Combinación recíproca: sqlmap lo enlaza como «ffuf descubre rutas y parámetros ocultos que después se prueban con sqlmap (combinación por arquitectura)». | Orden indicado desde sqlmap: Fuzzea con ffuf; después prueba los parámetros encontrados con sqlmap. |
| [SecLists](seclists.md) | Combinación recíproca: SecLists lo enlaza como «SecLists alimenta ffuf». | Orden indicado desde SecLists: Clona SecLists; pasa la wordlist a ffuf. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (3). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Caido](caido.md) · [dirsearch](dirsearch.md) · [WPScan](wpscan.md)

**Notas:** Ajusta la tasa de peticiones para no saturar el servidor objetivo.

Estado en GitHub: activo · último push 2026-09-26 · última versión publicada v2.3.0 (2026-09-09) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/ffuf/ffuf/blob/master/README.md)</sub>

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
brew install ffuf
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/ffuf/ffuf/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar ffuf para mi objetivo y necesito pasos guiados. Lee https://github.com/ffuf/ffuf/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `brew install ffuf` o `go install` y lanza un descubrimiento de directorios contra un servidor de laboratorio..

**Qué comprobar:** ffuf lista las rutas que responden con códigos de interés..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- descubrir rutas o archivos olvidados en tu aplicación web
- probar parámetros GET y POST en una auditoría autorizada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: descubrir rutas o archivos olvidados en tu aplicación web; probar parámetros GET y POST en una auditoría autorizada | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Úsalo solo contra sistemas propios o con autorización escrita: usarlo contra terceros sin permiso es delito en la mayoría de países.

## Stack y modelos

- **Stack:** Go, go.mod
- **Etiquetas:** `pruebas` `go` `security` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Gobuster](gobuster.md) | 14.3k | Fuzzing y descubrimiento de directorios, DNS y buckets en Go; clásico de pentest web autorizado. |
| [feroxbuster](feroxbuster.md) | 8.2k | Dirbuster rápido en Rust con recursión, filtros y salidas flexibles para descubrimiento de contenidos web. |

## Enlaces

- 🐙 GitHub: [ffuf/ffuf](https://github.com/ffuf/ffuf)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/ffuf/ffuf/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
