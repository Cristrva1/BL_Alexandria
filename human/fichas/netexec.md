[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Active Directory y red interna

# 🖥️ NetExec

> Suite de post-explotación y enumeración de redes Windows/AD (sucesora de CrackMapExec) para validar credenciales y movimientos laterales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6k | BSD-2-Clause | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; dominio especializado

**Puntuación de calidad** 75/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta comunitaria sucesora de CrackMapExec para enumerar y post-explotar redes Windows/AD.

## ¿Qué hace?

Prueba protocolos Windows, ejecuta módulos de recolección/ejecución y resume accesos válidos.

## ¿Cómo lo hace?

Se instala con pipx desde GitHub; el binario `nxc` opera por protocolo (smb, ldap, winrm…).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Impacket](impacket.md) | NetExec apoya muchos flujos en Impacket (SMB/Kerberos). | Instala Impacket; después NetExec. |
| [BloodHound Community Edition](bloodhound.md) | Los hallazgos de NetExec orientan la recolección para BloodHound. | Enumera con NetExec; importa el grafo en BloodHound. |
| [Nmap](nmap.md) | Nmap delimita hosts Windows antes de NetExec. | Nmap primero; NetExec sobre el alcance. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[GOAD](goad.md) · [Responder](responder.md)

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.5.1 (2026-02-23) · licencia declarada BSD-2-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Pennyw0rth/NetExec#readme) · [2](https://netexec.wiki/)</sub>

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
pipx install git+https://github.com/Pennyw0rth/NetExec
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Pennyw0rth/NetExec/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://netexec.wiki/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar NetExec para mi objetivo y necesito pasos guiados. Lee https://github.com/Pennyw0rth/NetExec/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pipx install git+https://github.com/Pennyw0rth/NetExec` y prueba `nxc smb` contra un host de laboratorio..

**Qué comprobar:** Obtienes qué hosts aceptan las credenciales y módulos aplicables..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- validar un set de credenciales contra un segmento Windows de lab
- enumerar shares y sesiones tras un compromiso autorizado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: validar un set de credenciales contra un segmento Windows de lab; enumerar shares y sesiones tras un compromiso autorizado | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** Python, Dockerfile, Makefile, pyproject.toml
- **Etiquetas:** `security` `ad` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Pennyw0rth/NetExec](https://github.com/Pennyw0rth/NetExec)
- 🌐 Web: <https://netexec.wiki/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Pennyw0rth/NetExec/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
