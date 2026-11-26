[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ OWASP Nettacker

> Marco OWASP de pruebas de penetración automatizadas: escaneo de puertos, subdominios, servicios y vulnerabilidades con módulos YAML.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.7k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 61/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto OWASP de pruebas de penetración automatizadas y recopilación de información.

## ¿Qué hace?

Escanea puertos, subdominios, servicios HTTP, credenciales débiles y vulnerabilidades conocidas, y compara resultados entre escaneos.

## ¿Cómo lo hace?

Motor Python con módulos declarativos en YAML, base de datos de resultados, informes HTML/JSON y una API con interfaz web.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Nmap](nmap.md) | Nmap profundiza en el fingerprint de los servicios que Nettacker detecta. | Nettacker para el barrido; Nmap sobre los hosts de interés. |
| [Nuclei](nuclei.md) | Nuclei aplica plantillas de vulnerabilidades a los servicios web encontrados. | Tras Nettacker, pasa las URLs vivas a Nuclei. |
| [DefectDojo](defectdojo.md) | DefectDojo centraliza los hallazgos para su seguimiento. | Exporta resultados e impórtalos en DefectDojo. |

Estado en GitHub: activo · último push 2026-11-17 · última versión publicada 0.4.1 (2026-08-24) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OWASP/Nettacker#readme) · [2](https://nettacker.readthedocs.io/)</sub>

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

**Entrada documentada (bash):**

```
docker run owasp/nettacker --help
```

Comando copiado literalmente de el README (sección «CLI (Docker)»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/OWASP/Nettacker/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://nettacker.readthedocs.io/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP Nettacker para mi objetivo y necesito pasos guiados. Lee https://github.com/OWASP/Nettacker/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta la ayuda de la imagen Docker oficial como indica el README y lanza un port_scan contra un host propio..

**Qué comprobar:** Obtienes un informe con puertos abiertos y servicios detectados..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- inventariar puertos y servicios de una red de laboratorio
- detectar cambios en la superficie expuesta entre dos escaneos autorizados

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: inventariar puertos y servicios de una red de laboratorio; detectar cambios en la superficie expuesta entre dos escaneos autorizados | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** Python, Dockerfile, Makefile, docker-compose.yml, pyproject.toml
- **Etiquetas:** `security` `pentest` `scanner` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OWASP/Nettacker](https://github.com/OWASP/Nettacker)
- 🌐 Web: <https://owasp.org/nettacker>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OWASP/Nettacker/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
