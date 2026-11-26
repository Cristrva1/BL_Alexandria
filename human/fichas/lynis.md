[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# 🖥️ Lynis

> Herramienta de auditoría de seguridad y endurecimiento para Linux, macOS y otros Unix, sin agente, que sugiere mejoras concretas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 16.7k | GPL-3.0 | Shell | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 55/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Herramienta de auditoría de código abierto (GPL-3.0) de CISOfy, con versión Enterprise de pago. Muy madura; ritmo de cambios moderado (último push en septiembre de 2026).

## ¿Qué hace?

Audita la seguridad del sistema en el que se ejecuta: configuración, servicios, cuentas, kernel, red, permisos y software, con pruebas de cumplimiento, detección de vulnerabilidades y sugerencias de endurecimiento; también ayuda en gestión de parches y pentesting interno.

## ¿Cómo lo hace?

Script de shell sin dependencias ni instalación obligatoria; se ejecuta desde el repositorio o con paquetes de la distribución. Algunas pruebas requieren privilegios de root.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Wazuh](wazuh.md) | Wazuh mantiene vigilancia continua de los sistemas que Lynis audita puntualmente (combinación por arquitectura). | Corrige lo que señala Lynis; después vigila con Wazuh. |
| [Trivy](trivy.md) | Trivy revisa imágenes y dependencias mientras Lynis audita el sistema anfitrión (combinación por arquitectura). | Audita el host con Lynis; escanea las imágenes con Trivy. |
| [Claude Code](claude-code.md) | Un agente puede explicar y priorizar las sugerencias del informe de Lynis (combinación por arquitectura). | Ejecuta Lynis y guarda el informe; después pásalo al agente sin datos sensibles. |
| [Prowler](prowler.md) | Combinación recíproca: Prowler lo enlaza como «Lynis endurece el host; Prowler la nube». | Orden indicado desde Prowler: Audita VMs con Lynis y cuentas con Prowler. |
| [PEASS-ng](peass-ng.md) | Combinación recíproca: PEASS-ng lo enlaza como «Lynis endurece; PEASS encuentra lo explotable». | Orden indicado desde PEASS-ng: Audita con Lynis; valida con PEASS en lab. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[ScubaGear](scubagear.md)

**Notas:** Las sugerencias son genéricas; valida cada cambio antes de aplicarlo en producción.

Estado en GitHub: activo · último push 2026-09-16 · última versión publicada 3.1.7 (2026-06-25) · licencia declarada GPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/CISOfy/lynis/blob/master/README.md) · [2](https://cisofy.com/documentation/lynis/)</sub>

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

Sin comando de instalación literal en el README ni en la documentación revisada el 2026-11-16: ver README oficial. No se deduce ningún comando por el nombre del repo.

[Instrucciones originales de instalación](https://github.com/CISOfy/lynis/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Lynis para mi objetivo y necesito pasos guiados. Lee https://github.com/CISOfy/lynis/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona el repositorio y ejecuta `./lynis audit system` en una máquina propia..

**Qué comprobar:** Obtienes advertencias, sugerencias y un índice de endurecimiento..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- revisar el endurecimiento de un servidor Linux recién instalado
- preparar una auditoría de cumplimiento (ISO 27001, PCI DSS, HIPAA)

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: revisar el endurecimiento de un servidor Linux recién instalado; preparar una auditoría de cumplimiento (ISO 27001, PCI DSS, HIPAA) | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Shell
- **Etiquetas:** `security` `shell` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [CISOfy/lynis](https://github.com/CISOfy/lynis)
- 🌐 Web: <https://cisofy.com/lynis/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/CISOfy/lynis/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
