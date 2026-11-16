[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Explotación, C2 y post-explotación

# 🖥️ PEASS-ng

> LinPEAS/WinPEAS: scripts y binarios que enumeran rutas de escalada de privilegios en hosts Linux/Windows/macOS comprometidos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 20.8k | NOASSERTION | C# | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Suite PEASS-ng (GPL) con LinPEAS y WinPEAS para privilege escalation enumeration.

## ¿Qué hace?

Automatiza chequeos locales que un pentester haría a mano tras obtener una shell.

## ¿Cómo lo hace?

Se bajan binarios/scripts de Releases y se ejecutan en el host objetivo autorizado.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Metasploit Framework](metasploit.md) | Tras Meterpreter, PEASS enumera privesc. | Sesión Metasploit → upload/ejecuta PEASS. |
| [BloodHound Community Edition](bloodhound.md) | En AD, BloodHound da rutas de dominio; PEASS el host. | Usa ambos niveles. |
| [Lynis](lynis.md) | Lynis endurece; PEASS encuentra lo explotable. | Audita con Lynis; valida con PEASS en lab. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 20261116-7dd73e1d (2026-11-16) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/peass-ng/PEASS-ng#readme) · [2](https://book.hacktricks.xyz)</sub>

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

[Instrucciones originales de instalación](https://github.com/peass-ng/PEASS-ng/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PEASS-ng para mi objetivo y necesito pasos guiados. Lee https://github.com/peass-ng/PEASS-ng/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga el release desde GitHub y ejecuta LinPEAS/WinPEAS en el host de laboratorio..

**Qué comprobar:** La salida destaca vectores de escalada..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- enumerar privesc en una VM Linux de HTB/GOAD
- revisar un bastión Windows tras un acceso autorizado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: enumerar privesc en una VM Linux de HTB/GOAD; revisar un bastión Windows tras un acceso autorizado | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** C#
- **Etiquetas:** `security` `privesc`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [peass-ng/PEASS-ng](https://github.com/peass-ng/PEASS-ng)
- 🌐 Web: <https://book.hacktricks.xyz>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/peass-ng/PEASS-ng/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
