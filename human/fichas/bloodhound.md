[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Active Directory y red interna

# ⚙️ BloodHound Community Edition

> Aplicación de análisis de rutas de ataque basada en grafos para Active Directory, Entra ID y otros sistemas de identidad (edición comunitaria).

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.6k | Apache-2.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

## ¿Qué es?

Herramienta de código abierto (Apache-2.0) de SpecterOps, que vende BloodHound Enterprise. Muy usada por equipos rojos y azules; la edición comunitaria es la versión actual del proyecto original.

## ¿Qué hace?

Revela relaciones ocultas y no intencionadas en sistemas de identidad y acceso mediante teoría de grafos, mostrando rutas de ataque en Active Directory y Entra ID, y extensible con OpenGraph a otras plataformas.

## ¿Cómo lo hace?

Backend en Go con frontend React; se despliega con Docker Compose (PostgreSQL y base de grafos) según la guía rápida. Los colectores se ejecutan en el entorno a analizar.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [hashcat](hashcat.md) | Las cuentas que BloodHound señala como expuestas se auditan después con Hashcat (combinación por arquitectura). | Identifica las cuentas con BloodHound; después audita sus hashes con Hashcat. |
| [John the Ripper (jumbo)](john.md) | John the Ripper sirve para la misma auditoría de contraseñas de las cuentas señaladas (combinación por arquitectura). | Identifica las cuentas; después audita con John. |
| [Metasploit Framework](metasploit.md) | Las rutas de ataque encontradas se validan con módulos de Metasploit en un ejercicio autorizado (combinación por arquitectura). | Analiza con BloodHound; después valida en laboratorio con Metasploit. |
| [Impacket](impacket.md) | Combinación recíproca: Impacket lo enlaza como «Impacket recolecta datos que BloodHound analiza como rutas de ataque». | Orden indicado desde Impacket: Recolecta con Impacket/SharpHound; después importa en BloodHound. |
| [NetExec](netexec.md) | Combinación recíproca: NetExec lo enlaza como «Los hallazgos de NetExec orientan la recolección para BloodHound». | Orden indicado desde NetExec: Enumera con NetExec; importa el grafo en BloodHound. |
| [PEASS-ng](peass-ng.md) | Combinación recíproca: PEASS-ng lo enlaza como «En AD, BloodHound da rutas de dominio; PEASS el host». | Orden indicado desde PEASS-ng: Usa ambos niveles. |

**Notas:** Ejecutar colectores en un dominio genera actividad detectable; coordínalo con el equipo de seguridad.

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v9.9.2 (2026-11-06) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/SpecterOps/BloodHound/blob/main/README.md) · [2](https://bloodhound.specterops.io/)</sub>

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

[Instrucciones originales de instalación](https://github.com/SpecterOps/BloodHound/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar BloodHound Community Edition para mi objetivo y necesito pasos guiados. Lee https://github.com/SpecterOps/BloodHound/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue la guía rápida de BloodHound CE con Docker Compose en un laboratorio y carga los datos de ejemplo o de un dominio de pruebas..

**Qué comprobar:** El grafo muestra rutas de ataque entre usuarios, grupos y equipos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- identificar rutas de escalada hacia administrador de dominio en tu propio AD
- priorizar qué permisos excesivos corregir primero

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: identificar rutas de escalada hacia administrador de dominio en tu propio AD; priorizar qué permisos excesivos corregir primero | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Úsalo solo contra sistemas propios o con autorización escrita: usarlo contra terceros sin permiso es delito en la mayoría de países.

## Stack y modelos

- **Stack:** Go, go.mod, package.json, pyproject.toml
- **Etiquetas:** `pruebas` `go` `security` `graph`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [SpecterOps/BloodHound](https://github.com/SpecterOps/BloodHound)
- 🌐 Web: <https://specterops.io/bloodhound-enterprise/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/SpecterOps/BloodHound/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
