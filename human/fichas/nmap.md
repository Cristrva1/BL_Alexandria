[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Reconocimiento y superficie de ataque

# 🖥️ Nmap

> El escáner de red de referencia: descubre hosts, puertos, servicios y sistemas operativos, con scripts NSE para detección avanzada.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14k | NPSL (no OSI) | C | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Escáner de red creado por Gordon Lyon (Fyodor) en 1997; el repositorio de GitHub es un espejo del SVN oficial. Licencia propia (Nmap Public Source License) que permite el uso libre a usuarios finales y ofrece licencia comercial para redistribuirlo.

## ¿Qué hace?

Descubre hosts, puertos abiertos, servicios y versiones, sistema operativo y vulnerabilidades mediante cientos de scripts NSE; produce salidas en texto, XML y grepeable. Incluye Ncat, Nping y la interfaz Zenmap.

## ¿Cómo lo hace?

Escrito en C/C++ con Lua para NSE; hay instaladores para Windows, macOS y Linux en nmap.org, o se compila con `./configure && make && make install`. Algunas técnicas requieren privilegios de administrador.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Metasploit Framework](metasploit.md) | Metasploit integra Nmap con `db_nmap` e importa su XML en la base de datos del proyecto. | Instala Nmap; después úsalo desde msfconsole con db_nmap. |
| [Nuclei](nuclei.md) | Los servicios que encuentra Nmap se revisan con plantillas de Nuclei (combinación por arquitectura). | Escanea con Nmap; después pasa los objetivos a nuclei. |
| [Wireshark](wireshark.md) | Wireshark permite ver a nivel de paquete qué envía un escaneo de Nmap, útil para aprender o depurar reglas de red (combinación por arquitectura). | Inicia la captura en Wireshark; después lanza el escaneo. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (7). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Amass](amass.md) · [Impacket](impacket.md) · [masscan](masscan.md) · [Naabu](naabu.md) · [NetExec](netexec.md) · [RustScan](rustscan.md) · [Sliver](sliver.md)

**Notas:** Escanear redes ajenas sin permiso puede ser delito o violar contratos de proveedores de internet o cloud.

Estado en GitHub: activo · último push 2026-11-12 · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/nmap/nmap/blob/master/README.md) · [2](https://nmap.org/book/man-legal.html) · [3](https://docs.metasploit.com/docs/using-metasploit/intermediate/metasploit-database-support.html)</sub>

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

[Instrucciones originales de instalación](https://github.com/nmap/nmap/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Nmap para mi objetivo y necesito pasos guiados. Lee https://github.com/nmap/nmap/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Nmap desde nmap.org o tu gestor de paquetes y escanea tu propio equipo con `nmap localhost`..

**Qué comprobar:** Obtienes la lista de puertos abiertos y los servicios detectados..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- inventariar los equipos y puertos abiertos de tu red doméstica
- comprobar qué servicios expone un servidor propio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: inventariar los equipos y puertos abiertos de tu red doméstica; comprobar qué servicios expone un servidor propio | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Licencia propia NPSL (no aprobada por la OSI, basada en GPLv2 pero no compatible). Úsalo solo contra sistemas propios o con autorización escrita: usarlo contra terceros sin permiso es delito en la mayoría de países.

## Stack y modelos

- **Stack:** C
- **Etiquetas:** `pruebas` `c` `security` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [nmap/nmap](https://github.com/nmap/nmap)
- 🌐 Web: <https://svn.nmap.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/nmap/nmap/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
