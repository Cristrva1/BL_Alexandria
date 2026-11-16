[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 📚 Metasploit Framework

> Framework de referencia para pruebas de penetración: módulos de exploits, cargas útiles, escáneres y post-explotación con consola interactiva.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39.6k | BSD-3-Clause | Ruby | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Framework de explotación de código abierto (licencia de estilo BSD; ver COPYING) de Rapid7 y la comunidad. Estándar del sector desde hace más de 15 años; Rapid7 vende Metasploit Pro aparte.

## ¿Qué hace?

Reúne exploits, payloads (incluido Meterpreter), módulos auxiliares de escaneo y fuerza bruta, post-explotación y evasión, con base de datos de hosts y credenciales, importación de escaneos de Nmap y módulos que analizan hashes con John the Ripper o Hashcat.

## ¿Cómo lo hace?

Escrito en Ruby; se recomienda instalar con los instaladores nightly oficiales en Linux o macOS (también viene en Kali). Usa PostgreSQL para la base de datos y se maneja con msfconsole o su API RPC.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Nmap](nmap.md) | Metasploit importa resultados de Nmap y ejecuta escaneos con `db_nmap` desde msfconsole. | Inicializa la base de datos de Metasploit; después lanza db_nmap o importa el XML de Nmap. |
| [hashcat](hashcat.md) | Los módulos `auxiliary/analyze/crack_*` usan Hashcat o John the Ripper para probar los hashes recogidos. | Instala Hashcat en el sistema; después ejecuta el módulo de crackeo con la acción hashcat. |
| [John the Ripper (jumbo)](john.md) | Los mismos módulos `crack_*` pueden usar John the Ripper como motor. | Instala John; después ejecuta el módulo con la acción john. |
| [BloodHound Community Edition](bloodhound.md) | BloodHound mapea rutas de ataque en Active Directory que después se validan con módulos de Metasploit en un ejercicio autorizado (combinación por arquitectura). | Recoge y analiza datos con BloodHound; después prueba las rutas en el laboratorio. |

**Notas:** Mantén Metasploit en una VM o laboratorio aislado; los antivirus suelen detectar sus cargas útiles.

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/rapid7/metasploit-framework/blob/master/README.md) · [2](https://docs.metasploit.com/) · [3](https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/analyze/crack_windows.rb)</sub>

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/rapid7/metasploit-framework/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Metasploit Framework para mi objetivo y necesito pasos guiados. Lee https://github.com/rapid7/metasploit-framework/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Metasploit con los instaladores oficiales en una VM de laboratorio y arranca `msfconsole` para buscar un módulo auxiliar de escaneo..

**Qué comprobar:** La consola muestra los módulos disponibles y sus opciones..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- validar en un laboratorio si una vulnerabilidad conocida es explotable
- practicar post-explotación y escalada en máquinas vulnerables de entrenamiento

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: validar en un laboratorio si una vulnerabilidad conocida es explotable; practicar post-explotación y escalada en máquinas vulnerables de entrenamiento | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Úsalo solo contra sistemas propios o con autorización escrita: usarlo contra terceros sin permiso es delito en la mayoría de países.

## Stack y modelos

- **Stack:** Ruby, Dockerfile, Gemfile, docker-compose.yml
- **Etiquetas:** `pruebas` `ruby` `security` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [rapid7/metasploit-framework](https://github.com/rapid7/metasploit-framework)
- 🌐 Web: <https://www.metasploit.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/rapid7/metasploit-framework/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
