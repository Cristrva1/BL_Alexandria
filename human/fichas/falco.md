[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Nube, contenedores e IaC

# 🖥️ Falco

> Runtime security para contenedores y Linux: reglas que alertan sobre syscalls anómalas en nodos y clústeres Kubernetes.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.6k | Apache-2.0 | C++ | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** hard

**Nivel:** 4 Experto — preparación difícil

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto CNCF de seguridad en tiempo de ejecución para hosts Linux y Kubernetes.

## ¿Qué hace?

Observa syscalls y eventos del kernel y dispara reglas cuando el comportamiento se sale del perfil esperado.

## ¿Cómo lo hace?

Se instala como paquete, DaemonSet o binario según la guía oficial; las reglas se ajustan en YAML.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Trivy](trivy.md) | Trivy endurece la imagen; Falco vigila el runtime. | Escanea con Trivy antes del deploy; Falco en el nodo. |
| [Wazuh](wazuh.md) | Falco puede reenviar alertas hacia un SIEM como Wazuh. | Despliega ambos; configura el forwarder documentado. |
| [CrowdSec](crowdsec.md) | CrowdSec bloquea IPs; Falco detecta abuso dentro del host. | Complementa red (CrowdSec) con runtime (Falco). |
| [Grype](grype.md) | Combinación recíproca: Grype lo enlaza como «Grype endurece la imagen; Falco vigila el runtime». | Orden indicado desde Grype: Grype en CI; Falco en el nodo. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[kube-bench](kube-bench.md)

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada 0.45.2 (2026-10-29) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/falcosecurity/falco#readme) · [2](https://falco.org)</sub>

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

[Instrucciones originales de instalación](https://github.com/falcosecurity/falco/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://falco.org)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Falco para mi objetivo y necesito pasos guiados. Lee https://github.com/falcosecurity/falco/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue https://falco.org/docs/getting-started e instala Falco en un nodo o clúster de laboratorio..

**Qué comprobar:** Al provocar un evento de prueba ves la alerta correspondiente..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- detectar un shell interactivo en un pod de producción propia
- alertar sobre escritura inesperada en /etc dentro de un contenedor

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: detectar un shell interactivo en un pod de producción propia; alertar sobre escritura inesperada en /etc dentro de un contenedor | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** C++, CMakeLists.txt, Makefile
- **Etiquetas:** `security` `k8s` `runtime`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [falcosecurity/falco](https://github.com/falcosecurity/falco)
- 🌐 Web: <https://falco.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/falcosecurity/falco/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
