[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Explotación, C2 y post-explotación

# 🖥️ Sliver

> Framework C2 open source de Bishop Fox para emulación de adversario autorizada: implants multiplataforma y canales mTLS/WireGuard/HTTP/DNS.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.3k | GPL-3.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** hard

**Nivel:** 4 Experto — preparación difícil; dominio especializado

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

C2 open source de Bishop Fox orientado a red team y emulación autorizada (alternativa a Cobalt Strike de pago).

## ¿Qué hace?

Genera implants únicos, gestiona sesiones C2 y ofrece capacidades de post-explotación en macOS, Windows y Linux.

## ¿Cómo lo hace?

Se instala desde releases o `curl https://sliver.sh/install|sudo bash`; el operador trabaja en la consola Sliver.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Metasploit Framework](metasploit.md) | Sliver gestiona implants mientras Metasploit aporta exploits y post-módulos. | Levanta Sliver; usa Metasploit solo si el escenario lo requiere. |
| [Nmap](nmap.md) | Nmap delimita el alcance antes de desplegar implants. | Nmap primero; implants solo en hosts autorizados. |
| [Wireshark](wireshark.md) | Wireshark valida el tráfico C2 generado en lab. | Captura con Wireshark mientras el implant habla con el server. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Ligolo-ng](ligolo-ng.md)

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v1.7.9 (2026-10-25) · licencia declarada GPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/BishopFox/sliver#readme) · [2](https://sliver.sh/docs)</sub>

## Ver similares

Grupo **Frameworks de C2 y post-explotación**: Sliver ocupa la posición 1 de 3 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Sliver** (esta ficha) ⭐ recomendado | 72 | Si buscas esto: framework C2 open source de Bishop Fox para emulación de adversario autorizada: implants multiplataforma y canales mTLS/WireGuard/HTTP/DNS. |
| 2 | [Empire](empire.md) | 60 | Si buscas esto: framework post-explotación/C2 centrado en PowerShell y agentes multiplataforma para labs autorizados. |
| 3 | [Mythic](mythic.md) | 51 | Si buscas esto: framework C2 colaborativo con UI: agentes y perfiles C2 se instalan aparte vía mythic-cli. |

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
curl https://sliver.sh/install|sudo bash
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/BishopFox/sliver/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://sliver.sh/docs)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Sliver para mi objetivo y necesito pasos guiados. Lee https://github.com/BishopFox/sliver/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `curl https://sliver.sh/install|sudo bash` (o el release) en una VM aislada y arranca `sliver`..

**Qué comprobar:** Obtienes la consola del servidor lista para generar implants de lab..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- montar un C2 de laboratorio con implant Linux/Windows
- probar detección de canales C2 en un entorno controlado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: montar un C2 de laboratorio con implant Linux/Windows; probar detección de canales C2 en un entorno controlado | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** Go, Dockerfile, Makefile, go.mod
- **Etiquetas:** `security` `c2` `redteam`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Mythic](mythic.md) | 4.9k | Framework C2 colaborativo con UI: agentes y perfiles C2 se instalan aparte vía mythic-cli. |
| [Empire](empire.md) | 5.4k | Framework post-explotación/C2 centrado en PowerShell y agentes multiplataforma para labs autorizados. |

## Enlaces

- 🐙 GitHub: [BishopFox/sliver](https://github.com/BishopFox/sliver)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/BishopFox/sliver/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
