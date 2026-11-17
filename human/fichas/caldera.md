[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Explotación, C2 y post-explotación

# 🖥️ CALDERA

> Framework Apache de emulación de adversario automatizado: agentes, adversarios ATT&CK y operaciones controladas desde web.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.5k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** hard

**Nivel:** 4 Experto — preparación difícil; dominio especializado

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto Apache de emulación de adversario con UI, agentes y biblioteca de habilidades ATT&CK.

## ¿Qué hace?

Orquesta agentes que ejecutan habilidades mapeadas a ATT&CK y registra resultados de la operación.

## ¿Cómo lo hace?

Docker (`ghcr.io/apache/caldera`) o `git clone --recursive` + pip; se opera desde la interfaz web.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Atomic Red Team](atomic-red-team.md) | CALDERA orquesta; Atomic aporta pruebas ATT&CK unitarias. | Usa Atomic para validar una técnica; CALDERA para campañas. |
| [Wazuh](wazuh.md) | Las operaciones deben producir alertas en Wazuh. | Wazuh monitoriza; CALDERA ataca el lab. |
| [Metasploit Framework](metasploit.md) | Algunas habilidades se apoyan en el mismo tipo de post-explotación que Metasploit. | Elige CALDERA para orquestación ATT&CK; Metasploit para exploits puntuales. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Mythic](mythic.md)

Estado en GitHub: activo · último push 2026-10-12 · última versión publicada 5.3.0 (2025-04-24) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/apache/caldera#readme) · [2](https://caldera.apache.org/)</sub>

## Ver similares

Grupo **Emulación de adversarios**: CALDERA ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Atomic Red Team](atomic-red-team.md) ⭐ recomendado | 65 | Si buscas esto: biblioteca de pruebas ATT&CK pequeñas y documentadas para validar detecciones y controles en un laboratorio propio. |
| 2 | **CALDERA** (esta ficha) | 64 | Si buscas esto: framework Apache de emulación de adversario automatizado: agentes, adversarios ATT&CK y operaciones controladas desde web. |

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
docker run -p 8888:8888 ghcr.io/apache/caldera:latest
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/apache/caldera/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://caldera.apache.org/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar CALDERA para mi objetivo y necesito pasos guiados. Lee https://github.com/apache/caldera/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca con `docker run -p 8888:8888 ghcr.io/apache/caldera:latest` y abre la UI en el puerto 8888..

**Qué comprobar:** Accedes a la consola para crear una operación de lab..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- lanzar una operación ATT&CK contra VMs de laboratorio
- comparar cobertura de detección entre dos campañas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: lanzar una operación ATT&CK contra VMs de laboratorio; comparar cobertura de detección entre dos campañas | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** Python, Dockerfile, docker-compose.yml, package.json, requirements.txt
- **Etiquetas:** `security` `attack` `purple`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [apache/caldera](https://github.com/apache/caldera)
- 🌐 Web: <https://caldera.apache.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/apache/caldera/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
