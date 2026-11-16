[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Detección, SIEM e IDS

# ⚙️ Wazuh

> Plataforma de seguridad abierta con SIEM y XDR: agentes en los equipos, detección de intrusiones, integridad de archivos, vulnerabilidades y cumplimiento.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 17.8k | GPL-2.0 + AGPL-3.0 (partes) | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

## ¿Qué es?

Plataforma de seguridad de código abierto de Wazuh Inc. (GPL-2.0 en su mayor parte, con componentes bajo otras licencias, como AGPL). Muy madura; la empresa vende cloud y soporte.

## ¿Qué hace?

Detecta intrusiones y malware con agentes, analiza registros con reglas, vigila la integridad de archivos, detecta vulnerabilidades, evalúa configuración y cumplimiento, responde a incidentes y protege cargas en contenedores y nube.

## ¿Cómo lo hace?

Componentes: agente (C/C++) en cada equipo, servidor de gestión, indexador y panel. Se instala con el asistente, paquetes, Docker, Kubernetes u OVA; necesita recursos de servidor según el número de agentes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [CrowdSec](crowdsec.md) | CrowdSec bloquea IP maliciosas en el perímetro y Wazuh centraliza la detección y el cumplimiento en los equipos (combinación por arquitectura). | Despliega CrowdSec en los servidores expuestos; después envía sus registros a Wazuh. |
| [Lynis](lynis.md) | Lynis hace auditorías puntuales de endurecimiento y Wazuh vigila de forma continua (combinación por arquitectura). | Audita con Lynis; después monitoriza con agentes de Wazuh. |
| [Trivy](trivy.md) | Trivy escanea imágenes antes del despliegue y Wazuh vigila vulnerabilidades en ejecución (combinación por arquitectura). | Integra Trivy en CI; después despliega agentes de Wazuh en los hosts. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (14). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Atomic Red Team](atomic-red-team.md) · [CALDERA](caldera.md) · [Empire](empire.md) · [Evilginx2](evilginx2.md) · [Falco](falco.md) · [MISP](misp.md) · [Mythic](mythic.md) · [OpenCTI](opencti.md) · [osquery](osquery.md) · [Security Onion](securityonion.md) · [Sigma](sigma.md) · [Suricata](suricata.md) · [Velociraptor](velociraptor.md) · [Zeek](zeek.md)

**Notas:** La curva de aprendizaje de reglas y decodificadores es alta; empieza con pocas fuentes.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v4.14.10 (2026-11-09) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/wazuh/wazuh/blob/main/README.md) · [2](https://documentation.wazuh.com)</sub>

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

[Instrucciones originales de instalación](https://github.com/wazuh/wazuh/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Wazuh para mi objetivo y necesito pasos guiados. Lee https://github.com/wazuh/wazuh/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega Wazuh en una VM con el asistente o Docker siguiendo su guía rápida e instala un agente en otro equipo..

**Qué comprobar:** El panel muestra el agente conectado y sus primeras alertas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- vigilar los servidores de tu laboratorio o pyme con alertas centralizadas
- auditar cumplimiento (PCI DSS, CIS) y detectar cambios en archivos críticos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: vigilar los servidores de tu laboratorio o pyme con alertas centralizadas; auditar cumplimiento (PCI DSS, CIS) y detectar cambios en archivos críticos | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** C++
- **Etiquetas:** `security` `server` `self-hosted` `cpp`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [wazuh/wazuh](https://github.com/wazuh/wazuh)
- 🌐 Web: <https://wazuh.com/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/wazuh/wazuh/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
