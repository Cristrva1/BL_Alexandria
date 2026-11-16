[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Inteligencia de amenazas

# ⚙️ MISP

> Plataforma de intercambio de threat intelligence: eventos, IOCs, taxonomías y sincronización entre organizaciones.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.7k | AGPL-3.0 | PHP | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** hard

**Nivel:** 3 Avanzado — plataforma de inteligencia con Docker; requiere curar feeds · corregido a mano

**Puntuación de calidad** 50/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto AGPL de compartir información de amenazas usado por CERTs y SOCs.

## ¿Qué hace?

Almacena eventos STIX-like, atributos y galaxias, y sincroniza con otras instancias MISP.

## ¿Cómo lo hace?

Instalación documentada (bash guides/Docker); se opera vía UI y REST API.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Wazuh](wazuh.md) | MISP enriquece alertas de Wazuh con IOCs. | Conecta el módulo MISP de Wazuh a tu instancia. |
| [OpenCTI](opencti.md) | OpenCTI y MISP se sincronizan vía conectores. | Elige un sentido de sync y configura el conector. |
| [YARA](yara.md) | Reglas YARA se publican/consumen como objetos MISP. | Sube la regla a MISP; despliega en sensores. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[LOKI](loki.md) · [Shuffle](shuffle.md)

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v2.5.51 (2026-11-11) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/MISP/MISP#readme) · [2](https://www.misp-project.org/)</sub>

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

[Instrucciones originales de instalación](https://github.com/MISP/MISP/blob/2.5/README.md)

[Abrir la web o descarga indicada por el autor](https://www.misp-project.org/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MISP para mi objetivo y necesito pasos guiados. Lee https://github.com/MISP/MISP/blob/2.5/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue la guía de instalación en misp-project.org y levanta una instancia de laboratorio..

**Qué comprobar:** Creas un evento de prueba y exportas IOCs..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- compartir IOCs de un incidente interno con un partner
- ingerir un feed OSINT y enriquecer alertas del SIEM

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: compartir IOCs de un incidente interno con un partner; ingerir un feed OSINT y enriquecer alertas del SIEM | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** PHP, requirements.txt
- **Etiquetas:** `security` `ti` `soc`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [MISP/MISP](https://github.com/MISP/MISP)
- 🌐 Web: <https://www.misp-project.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/MISP/MISP/blob/2.5/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
