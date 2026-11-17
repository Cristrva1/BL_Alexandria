[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ OWASP WrongSecrets

> Aplicación vulnerable de OWASP con retos sobre cómo no gestionar secretos en código, contenedores, Kubernetes, nube y binarios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.5k | AGPL-3.0 | HTML | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 62/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto OWASP de formación centrado en errores de gestión de secretos.

## ¿Qué hace?

Plantea retos en los que hay que encontrar secretos mal guardados en código, configuración, contenedores, Kubernetes, gestores de secretos y servicios en la nube.

## ¿Cómo lo hace?

Aplicación Java con niveles de despliegue progresivos (Docker, Kubernetes, Vault, nube); licencia AGPL-3.0.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Gitleaks](gitleaks.md) | Gitleaks detecta secretos en repositorios, una habilidad que los retos ejercitan. | Resuelve el reto; después prueba Gitleaks en un repo propio. |
| [TruffleHog](trufflehog.md) | TruffleHog busca y verifica secretos como los de los retos. | Úsalo tras los retos en repositorios propios. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.14.2 (2026-10-20) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/OWASP/wrongsecrets#readme) · [2](https://owasp.org/www-project-wrongsecrets/)</sub>

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
docker run -p 8080:8080 -p 8090:8090 jeroenwillemsen/wrongsecrets:latest-no-vault
```

Comando copiado literalmente de el README (sección «Basic docker exercises»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/OWASP/wrongsecrets/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://owasp.org/www-project-wrongsecrets/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP WrongSecrets para mi objetivo y necesito pasos guiados. Lee https://github.com/OWASP/wrongsecrets/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Ejecuta la imagen Docker sin Vault como indica el README y abre la aplicación en localhost:8080..

**Qué comprobar:** Accedes a los retos básicos de secretos..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- enseñar a detectar secretos filtrados en imágenes de contenedor
- practicar la gestión de secretos en Kubernetes

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: enseñar a detectar secretos filtrados en imágenes de contenedor; practicar la gestión de secretos en Kubernetes | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Aplicación deliberadamente vulnerable: ejecútala solo en local o en una red aislada, nunca expuesta a Internet ni en equipos con datos reales. Licencia AGPL-3.0.

## Stack y modelos

- **Stack:** HTML, Dockerfile, package.json, pom.xml
- **Etiquetas:** `security` `secrets` `training` `kubernetes`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [OWASP/wrongsecrets](https://github.com/OWASP/wrongsecrets)
- 🌐 Web: <https://owasp.org/www-project-wrongsecrets/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/OWASP/wrongsecrets/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
