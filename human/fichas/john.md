[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ John the Ripper (jumbo)

> Crackeador de contraseñas offline de Openwall en su versión comunitaria jumbo: cientos de tipos de hash y cifrado, CPU, GPU y FPGA.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.9k | GPL-2.0 (con partes bajo otras licencias) | C | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 55/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Crackeador de contraseñas de Openwall (Solar Designer); esta es la versión jumbo con aportes de la comunidad. Licencia GPL-2.0 con archivos bajo licencias más permisivas (ver doc/LICENSE). El README avisa de que parte del código jumbo no es maduro.

## ¿Qué hace?

Detecta contraseñas débiles a partir de cientos de tipos de hash y cifrado, con modos single, diccionario con reglas e incremental, soporte de GPU y FPGA en algunos formatos, y utilidades *2john para extraer hashes de ZIP, PDF, capturas WPA y otros formatos.

## ¿Cómo lo hace?

Escrito en C; se compila desde el código (doc/INSTALL) o se instala con paquetes oficiales (john-packages, Snap, etc.). El soporte de GPU requiere OpenCL.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Metasploit Framework](metasploit.md) | Los módulos crack_* de Metasploit pueden usar John the Ripper como motor. | Instala John; después ejecuta el módulo con la acción john. |
| [Wireshark](wireshark.md) | John incluye utilidades como wpapcap2john para extraer hashes de capturas de red como las de Wireshark. | Captura con Wireshark en tu red; después extrae el hash con wpapcap2john. |
| [BloodHound Community Edition](bloodhound.md) | Los hashes de cuentas que BloodHound señala como expuestas se auditan después con John (combinación por arquitectura). | Analiza con BloodHound; después audita los hashes autorizados con John. |

**Notas:** Alternativas (elige una): hashcat.

Estado en GitHub: activo · último push 2026-11-16 · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/openwall/john/blob/bleeding-jumbo/README.md) · [2](https://www.openwall.com/john/)</sub>

## Ver similares

Grupo **Cracking de contraseñas**: John the Ripper (jumbo) ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [hashcat](hashcat.md) ⭐ recomendado | 62 | Si buscas esto: utilidad de recuperación de contraseñas más rápida, acelerada por GPU, con más de 630 modos de hash y 10 modos de ataque. |
| 2 | **John the Ripper (jumbo)** (esta ficha) | 55 | Si buscas esto: crackeador de contraseñas offline de Openwall en su versión comunitaria jumbo: cientos de tipos de hash y cifrado, CPU, GPU y FPGA. |

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

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/openwall/john/blob/bleeding-jumbo/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar John the Ripper (jumbo) para mi objetivo y necesito pasos guiados. Lee https://github.com/openwall/john/blob/bleeding-jumbo/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Compila John desde `src/` según doc/INSTALL o usa los paquetes de john-packages y ejecuta `john --test`..

**Qué comprobar:** John muestra la velocidad de los formatos soportados en tu equipo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- auditar contraseñas débiles a partir de hashes autorizados
- extraer el hash de un archivo cifrado propio para recuperarlo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: auditar contraseñas débiles a partir de hashes autorizados; extraer el hash de un archivo cifrado propio para recuperarlo | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Romper contraseñas ajenas sin permiso es delito; úsalo solo con datos propios o autorizados.

## Stack y modelos

- **Stack:** C
- **Etiquetas:** `pruebas` `c` `security` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [hashcat](hashcat.md) | 27.4k | Utilidad de recuperación de contraseñas más rápida, acelerada por GPU, con más de 630 modos de hash y 10 modos de ataque. |

## Enlaces

- 🐙 GitHub: [openwall/john](https://github.com/openwall/john)
- 🌐 Web: <https://www.openwall.com/john/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/openwall/john/blob/bleeding-jumbo/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
