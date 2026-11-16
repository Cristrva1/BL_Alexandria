[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Inteligencia de amenazas

# ⚙️ OpenCTI

> Plataforma de threat intel orientada a grafos (Filigran): Community Edition Apache-2.0; Enterprise añade playbooks, SSO, IA y más bajo licencia EE.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.4k | NOASSERTION | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** hard

> ⚠️ **Licencia y costes:** Open-core: la Community Edition es Apache-2.0 y gratuita. La Enterprise Edition (mismo repositorio, ficheros con cabecera EE) requiere licencia Filigran: registro de actividad, playbooks, segregación por organización, indexado de texto completo, AI Insights/NLP, PIR, SSO configurado desde la UI, campos personalizados, entre otros. Filigran ofrece licencias de prueba y gratuitas para I+D y ONG.

## ¿Qué es?

Plataforma de threat intel de Filigran. Open-core: Community Edition Apache-2.0; Enterprise Edition (playbooks, SSO por UI, IA/NLP, PIR, auditoría) con licencia de pago.

## ¿Qué hace?

Ingiere, relaciona y visualiza conocimiento de amenazas en un grafo STIX.

## ¿Cómo lo hace?

Docker Compose/Helm según la documentación; la EE se activa con licencia Filigran en settings.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [MISP](misp.md) | Conector MISP↔OpenCTI para intercambiar IOCs. | Levanta ambos; configura el conector oficial. |
| [Wazuh](wazuh.md) | OpenCTI aporta contexto a alertas de Wazuh. | Exporta IOCs hacia el SIEM. |
| [Sigma](sigma.md) | Reglas Sigma se gestionan junto al intel en el SOC. | Vincula detecciones Sigma a CTI en OpenCTI. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 7.261116.0 (2026-11-16) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OpenCTI-Platform/opencti#readme) · [2](https://docs.opencti.io/) · [3](https://docs.opencti.io/latest/administration/enterprise/)</sub>

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

[Instrucciones originales de instalación](https://github.com/OpenCTI-Platform/opencti/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://opencti.io)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OpenCTI para mi objetivo y necesito pasos guiados. Lee https://github.com/OpenCTI-Platform/opencti/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega con Docker según https://docs.opencti.io/latest/deployment/installation/#using-docker..

**Qué comprobar:** Accedes a la UI Community sin licencia EE..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- modelar una campaña APT con relaciones STIX
- centralizar feeds y casos de amenaza del SOC

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: modelar una campaña APT con relaciones STIX; centralizar feeds y casos de amenaza del SOC | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. CE Apache-2.0 gratuita. EE (playbooks, SSO por UI, AI Insights, NLP, PIR, full-text, etc.) requiere licencia Filigran (trial disponible).

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `security` `ti` `stix`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OpenCTI-Platform/opencti](https://github.com/OpenCTI-Platform/opencti)
- 🌐 Web: <https://opencti.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OpenCTI-Platform/opencti/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
