[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ sqlmap

> Herramienta de pruebas de penetración que detecta y explota automáticamente inyecciones SQL y permite tomar el control de servidores de bases de datos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 39k | GPL-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de código abierto (GPL-2.0 con aclaraciones propias; ver LICENSE) de Bernardo Damele y Miroslav Stampar. Muy madura y activa desde 2006.

## ¿Qué hace?

Detecta y explota inyecciones SQL con varias técnicas (booleana, basada en tiempo, errores, UNION, consultas apiladas), identifica el motor, enumera bases de datos, tablas y usuarios, extrae datos y puede acceder al sistema de archivos o ejecutar comandos según el motor.

## ¿Cómo lo hace?

Escrito en Python; funciona con Python 2.7 y 3.x sin dependencias tras clonar el repositorio. Admite proxies, peticiones guardadas y registros de proxies, y tamper scripts.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [mitmproxy](mitmproxy.md) | sqlmap puede enviar su tráfico por un proxy como mitmproxy para inspeccionarlo o reutilizar peticiones capturadas (combinación por arquitectura). | Arranca mitmproxy; después ejecuta sqlmap con `--proxy`. |
| [ZAP (Zed Attack Proxy)](zaproxy.md) | ZAP descubre parámetros sospechosos y sqlmap confirma y explota la inyección (combinación por arquitectura). | Escanea con ZAP; después pasa la petición guardada a sqlmap con `-r`. |
| [ffuf](ffuf.md) | ffuf descubre rutas y parámetros ocultos que después se prueban con sqlmap (combinación por arquitectura). | Fuzzea con ffuf; después prueba los parámetros encontrados con sqlmap. |
| [PayloadsAllTheThings](payloadsallthethings.md) | Combinación recíproca: PayloadsAllTheThings lo enlaza como «Complementa SQLi manual del cheatsheet con sqlmap». | Orden indicado desde PayloadsAllTheThings: Prueba manual; automatiza con sqlmap si procede. |

**Notas:** Las técnicas de extracción pueden alterar datos o cargar el servidor; nunca lo uses en producción sin acuerdo previo.

Estado en GitHub: activo · último push 2026-11-12 · última versión publicada 1.10 (2026-01-01) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/sqlmapproject/sqlmap/blob/master/README.md) · [2](https://github.com/sqlmapproject/sqlmap/wiki/Usage)</sub>

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

[Instrucciones originales de instalación](https://github.com/sqlmapproject/sqlmap/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar sqlmap para mi objetivo y necesito pasos guiados. Lee https://github.com/sqlmapproject/sqlmap/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona el repositorio y ejecuta `python sqlmap.py -h` para ver las opciones; después pruébalo contra una aplicación vulnerable de laboratorio..

**Qué comprobar:** sqlmap identifica el parámetro inyectable y el motor de base de datos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- comprobar si un formulario de tu aplicación es vulnerable a inyección SQL
- reproducir un hallazgo de inyección en una auditoría autorizada

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: comprobar si un formulario de tu aplicación es vulnerable a inyección SQL; reproducir un hallazgo de inyección en una auditoría autorizada | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Úsalo solo contra sistemas propios o con autorización escrita: usarlo contra terceros sin permiso es delito en la mayoría de países.

## Stack y modelos

- **Stack:** Python
- **Etiquetas:** `pruebas` `python` `security` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [sqlmapproject/sqlmap](https://github.com/sqlmapproject/sqlmap)
- 🌐 Web: <http://sqlmap.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/sqlmapproject/sqlmap/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
