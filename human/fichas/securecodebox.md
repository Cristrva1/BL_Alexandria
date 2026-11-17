[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ OWASP secureCodeBox

> Orquesta escáneres de seguridad (Nmap, ZAP, Nuclei, Trivy y otros) en Kubernetes para automatizar análisis continuos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 994 | Apache-2.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** hard

**Nivel:** 4 Experto — preparación difícil; despliegue con Kubernetes/Helm

**Puntuación de calidad** 58/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** Apache-2.0. Fuente: [LICENSE](https://github.com/secureCodeBox/secureCodeBox/blob/main/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Proyecto OWASP para automatizar y orquestar escáneres de seguridad en Kubernetes.

## ¿Qué hace?

Ejecuta escaneos únicos o programados con herramientas de código abierto, normaliza los hallazgos y los envía a sistemas de gestión.

## ¿Cómo lo hace?

Operador Go con CRD (Scan, ScheduledScan) y charts Helm por escáner y hook; licencia Apache-2.0 en LICENSE pese a NOASSERTION en la API de GitHub.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [DefectDojo](defectdojo.md) | Un hook de secureCodeBox envía los hallazgos a DefectDojo. | DefectDojo primero; después el hook en el clúster. |
| [Nuclei](nuclei.md) | Nuclei está disponible como escáner integrado. | Instala el chart del escáner tras el operador. |

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v5.9.0 (2026-09-15) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/secureCodeBox/secureCodeBox#readme) · [2](https://www.securecodebox.io/docs/getting-started/installation)</sub>

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

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno.

**Entrada documentada (bash):**

```
helm --namespace securecodebox-system upgrade --install --create-namespace securecodebox-operator oci://ghcr.io/securecodebox/helm/operator
```

Comando copiado literalmente de la documentación oficial enlazada desde el README; revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://www.securecodebox.io/docs/getting-started/installation)

[Abrir la web o descarga indicada por el autor](https://www.securecodebox.io/docs/getting-started/installation)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP secureCodeBox para mi objetivo y necesito pasos guiados. Lee https://www.securecodebox.io/docs/getting-started/installation. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala el operador con Helm según la guía de instalación oficial en un clúster de pruebas..

**Qué comprobar:** El operador queda listo para lanzar un escaneo de ejemplo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- programar escaneos periódicos de un entorno de staging autorizado
- enviar resultados de varios escáneres a DefectDojo

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: programar escaneos periódicos de un entorno de staging autorizado; enviar resultados de varios escáneres a DefectDojo | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** Go
- **Etiquetas:** `security` `kubernetes` `scanner` `devsecops` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [secureCodeBox/secureCodeBox](https://github.com/secureCodeBox/secureCodeBox)
- 🌐 Web: <https://www.secureCodeBox.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/secureCodeBox/secureCodeBox/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
