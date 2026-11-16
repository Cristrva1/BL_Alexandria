[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Active Directory y red interna

# 📚 Impacket

> Biblioteca Python de protocolos Windows (SMB, MSRPC, Kerberos…) usada como base de casi todo el tooling de Active Directory.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.3k | NOASSERTION | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Colección de clases Python para protocolos de red Windows, mantenida por Fortra (Core Security).

## ¿Qué hace?

Permite construir, parsear y automatizar SMB, MSRPC, Kerberos y otros protocolos usados en AD.

## ¿Cómo lo hace?

Se instala con pipx/pip; expone scripts listos y una API para herramientas como NetExec.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [BloodHound Community Edition](bloodhound.md) | Impacket recolecta datos que BloodHound analiza como rutas de ataque. | Recolecta con Impacket/SharpHound; después importa en BloodHound. |
| [Nmap](nmap.md) | Nmap ubica hosts Windows antes de usar scripts de Impacket. | Nmap primero; Impacket sobre el alcance confirmado. |
| [Metasploit Framework](metasploit.md) | Módulos de Metasploit y scripts de Impacket se usan juntos en post-explotación AD. | Define el alcance; elige Impacket o Metasploit según el escenario. |
| [NetExec](netexec.md) | Combinación recíproca: NetExec lo enlaza como «NetExec apoya muchos flujos en Impacket (SMB/Kerberos)». | Orden indicado desde NetExec: Instala Impacket; después NetExec. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Certipy](certipy.md) · [Rubeus](rubeus.md)

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada impacket_0_13_1 (2026-05-19) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/fortra/impacket#readme) · [2](https://www.coresecurity.com)</sub>

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

**Entrada documentada (consulta la sintaxis original):**

```
python3 -m pipx install impacket
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/fortra/impacket/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Impacket para mi objetivo y necesito pasos guiados. Lee https://github.com/fortra/impacket/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `python3 -m pipx install impacket` y ejecuta un script de ejemplo contra un lab GOAD/HTB..

**Qué comprobar:** Obtienes salida del protocolo (hashes, shells o tickets) en el entorno autorizado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- extraer hashes con secretsdump en un DC de laboratorio
- simular autenticación SMB/Kerberos en un lab aislado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: extraer hashes con secretsdump en un DC de laboratorio; simular autenticación SMB/Kerberos en un lab aislado | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo. Licencia Apache modificada (LICENSE). Solo labs autorizados.

## Stack y modelos

- **Stack:** Python, Dockerfile, requirements.txt, setup.py
- **Etiquetas:** `security` `ad` `python` `library`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [fortra/impacket](https://github.com/fortra/impacket)
- 🌐 Web: <https://www.coresecurity.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/fortra/impacket/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
