[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ hashcat

> Utilidad de recuperación de contraseñas más rápida, acelerada por GPU, con más de 630 modos de hash y 10 modos de ataque.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 27.4k | MIT | C | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de recuperación de contraseñas de código abierto (MIT) del proyecto hashcat, creada por Jens Steube. Muy madura y activa.

## ¿Qué hace?

Recupera contraseñas a partir de hashes con más de 630 modos (incluidas recetas de hash compuestas), 10 modos de ataque, motor de reglas en el kernel, cadenas de Markov, reanudación de sesiones, Brain para evitar repeticiones y redes de cracking distribuido.

## ¿Cómo lo hace?

Escrito en C; se usa con binarios de la release o paquetes de la plataforma. Requiere los drivers y runtimes de la GPU (CUDA, HIP, Metal u OpenCL) indicados en su documentación.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Metasploit Framework](metasploit.md) | Los módulos de análisis de Metasploit pueden usar Hashcat para probar los hashes recogidos en un ejercicio. | Instala Hashcat; después ejecuta el módulo crack_* con la acción hashcat. |
| [BloodHound Community Edition](bloodhound.md) | BloodHound identifica cuentas expuestas (por ejemplo, kerberoasteables) cuyos hashes se auditan con Hashcat (combinación por arquitectura). | Analiza el dominio con BloodHound; después audita los hashes autorizados con Hashcat. |
| [Claude Code](claude-code.md) | Un agente puede ayudar a construir reglas, máscaras y comandos de Hashcat para una auditoría (combinación por arquitectura). | Describe la política de contraseñas; después revisa el comando propuesto. |
| [SecLists](seclists.md) | Combinación recíproca: SecLists lo enlaza como «Diccionarios de SecLists alimentan ataques de contraseña en lab». | Orden indicado desde SecLists: SecLists primero; Hashcat con la lista autorizada. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Aircrack-ng](aircrack-ng.md) · [Responder](responder.md)

**Notas:** Alternativas (elige una): john.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v8.0.0 (2026-10-25) (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/hashcat/hashcat/blob/master/README.md) · [2](https://hashcat.net/hashcat/)</sub>

## Ver similares

Grupo **Cracking de contraseñas**: hashcat ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **hashcat** (esta ficha) ⭐ recomendado | 62 | Si buscas esto: utilidad de recuperación de contraseñas más rápida, acelerada por GPU, con más de 630 modos de hash y 10 modos de ataque. |
| 2 | [John the Ripper (jumbo)](john.md) | 54 | Si buscas esto: crackeador de contraseñas offline de Openwall en su versión comunitaria jumbo: cientos de tipos de hash y cifrado, CPU, GPU y FPGA. |

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

[Instrucciones originales de instalación](https://github.com/hashcat/hashcat/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar hashcat para mi objetivo y necesito pasos guiados. Lee https://github.com/hashcat/hashcat/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga la release oficial y ejecuta el benchmark (`hashcat -b`) en tu equipo..

**Qué comprobar:** Obtienes la velocidad de cálculo por tipo de hash en tu GPU o CPU..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- auditar la fortaleza de las contraseñas de tu organización a partir de hashes autorizados
- recuperar la contraseña de un archivo propio olvidado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: auditar la fortaleza de las contraseñas de tu organización a partir de hashes autorizados; recuperar la contraseña de un archivo propio olvidado | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Romper hashes o contraseñas ajenas sin permiso es delito; úsalo solo con datos propios o autorizados.

## Stack y modelos

- **Stack:** C
- **Etiquetas:** `pruebas` `c` `security` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [John the Ripper (jumbo)](john.md) | 13.9k | Crackeador de contraseñas offline de Openwall en su versión comunitaria jumbo: cientos de tipos de hash y cifrado, CPU, GPU y FPGA. |

## Enlaces

- 🐙 GitHub: [hashcat/hashcat](https://github.com/hashcat/hashcat)
- 🌐 Web: <https://hashcat.net/hashcat/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/hashcat/hashcat/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
