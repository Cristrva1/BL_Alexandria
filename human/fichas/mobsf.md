[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# ⚙️ MobSF (Mobile Security Framework)

> Analiza apps Android, iOS y Windows propias desde el navegador y genera un informe de permisos, configuración, código y librerías con riesgo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 22.4k | GPL-3.0 | Python | 2026-11-27 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 72/100 · métricas del 2026-11-28 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de código abierto para evaluar la seguridad de aplicaciones móviles Android, iOS y Windows.

## ¿Qué hace?

Genera informes de análisis estático de archivos APK, IPA, APPX o del código fuente y, con un emulador o dispositivo preparado, observa la app mientras se ejecuta.

## ¿Cómo lo hace?

Descompila la app con herramientas como jadx y apktool, revisa manifiesto, binarios y código con reglas propias y presenta los hallazgos en una interfaz web y una API REST.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OWASP MASTG](mastg.md) | La guía de pruebas móviles de OWASP explica cómo interpretar y ampliar cada hallazgo del informe. | — |
| [jadx](jadx.md) | Abre el código descompilado de la misma APK para revisar a mano las líneas que señala el informe. | — |
| [DefectDojo](defectdojo.md) | Importa los informes de MobSF para seguir los hallazgos junto con los de otros escáneres. | — |

Estado en GitHub: activo · último push 2026-11-25 · última versión publicada v4.6.9 (2026-11-18) · licencia declarada GPL-3.0 (consultado el 2026-11-27).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-27); no se instaló ni ejecutó. Fuentes: [1](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/README.md) · [2](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/LICENSE) · [3](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/.github/SECURITY.md) · [4](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/Dockerfile) · [5](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/scripts/entrypoint.sh) · [6](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/mobsf/MobSF/settings.py) · [7](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/mobsf/MalwareAnalyzer/views/MalwareDomainCheck.py) · [8](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/.github/workflows/mobsf-test.yml) · [9](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/.github/workflows/docker-release.yml) · [10](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/mobsf/StaticAnalyzer/tests.py) · [11](https://github.com/MobSF/Mobile-Security-Framework-MobSF/actions/runs/44250422514) · [12](https://github.com/MobSF/Mobile-Security-Framework-MobSF/actions/runs/44358831543) · [13](https://github.com/MobSF/Mobile-Security-Framework-MobSF/releases/tag/v4.6.9) · [14](https://github.com/MobSF/Mobile-Security-Framework-MobSF/security/advisories) · [15](https://hub.docker.com/r/opensecurity/mobile-security-framework-mobsf/tags) · [16](https://pypi.org/project/mobsf/4.6.9/) · [17](https://github.com/MobSF/docs/blob/545d88f9c19a97933ba36e60fdb9c6946d7aa9e2/docker_options.md) · [18](https://github.com/MobSF/docs/blob/545d88f9c19a97933ba36e60fdb9c6946d7aa9e2/running_mobsf_docker.md) · [19](https://github.com/MobSF/docs/blob/545d88f9c19a97933ba36e60fdb9c6946d7aa9e2/configurations.md) · [20](https://github.com/OWASP/mastg/blob/c80a12abf2ece138fbd906e90c325ccca2754a4f/Crackmes/README.md) · [21](https://github.com/OWASP/mastg/blob/c80a12abf2ece138fbd906e90c325ccca2754a4f/Crackmes/Android/Level_01/UnCrackable-Level1.apk) · [22](https://github.com/OWASP/mastg/blob/c80a12abf2ece138fbd906e90c325ccca2754a4f/License.md) · [23](https://github.com/OWASP/mastg/blob/c80a12abf2ece138fbd906e90c325ccca2754a4f/techniques/android/MASTG-TECH-0043.md) · [24](https://github.com/DefectDojo/django-DefectDojo/tree/cd0a4483a224707f72a0fc3112359089c1446b55/dojo/tools/mobsf)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa API de IA. VirusTotal es opcional, está desactivado por defecto y necesita clave propia; con MOBSF_VT_UPLOAD=1 subiría los archivos a ese servicio. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El análisis estático corre en tu equipo sin modelos de IA. Algunas comprobaciones usan la red: resuelven por DNS los dominios hallados en la app y descargan listas de amenazas. MOBSF_DOMAIN_MALWARE_SCAN=0 desactiva esa comprobación. |
| Coste | Sin pago a un modelo en la ruta básica. Licencia GPL-3.0, sin pago para la ruta descrita. El soporte empresarial y los cursos del autor son opcionales y de pago. |
| Equipo | Preparación según la ruta elegida. Docker en un equipo de 64 bits (imágenes amd64 y arm64). El análisis dinámico requiere además un emulador, simulador o dispositivo preparado. |

Un agente de código puede ayudarte a lanzar el contenedor o a usar la API REST, pero MobSF no necesita ninguna suscripción de IA.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Instala Docker (Docker Desktop en Windows o macOS, o Docker Engine en Linux). La descarga comprimida de la imagen v4.6.9 ronda los 750 MB. Docker Desktop tiene condiciones de licencia propias para empresas grandes.
2. Arranca la versión fijada solo para tu equipo: docker run -it --rm -p 127.0.0.1:8000:8000 -e DJANGO_SUPERUSER_PASSWORD=una-clave-tuya opensecurity/mobile-security-framework-mobsf:v4.6.9. Abre http://127.0.0.1:8000 e inicia sesión con el usuario mobsf y esa clave.
3. Descarga UnCrackable-Level1.apk de OWASP/mastg, súbela en la página principal y espera el informe. Para terminar, pulsa Ctrl+C en la terminal: con --rm se borran el contenedor y sus resultados.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/MobSF/Mobile-Security-Framework-MobSF/releases/tag/v4.6.9)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar MobSF (Mobile Security Framework) para mi objetivo y necesito pasos guiados. Lee https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Con MobSF 4.6.9 publicado solo en 127.0.0.1, sube UnCrackable-Level1.apk, la app de práctica con licencia CC BY-SA 4.0 del repositorio OWASP/mastg (Crackmes/Android/Level_01).

**Qué comprobar:** Al terminar el análisis estático se abre el informe del paquete owasp.mstg.uncrackable1 con su puntuación de seguridad y las secciones de permisos, manifiesto y código con sus hallazgos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar la APK de tu propia app antes de publicarla para detectar permisos excesivos, copias de seguridad habilitadas o claves escritas en el código
- Practicar con una app de entrenamiento de OWASP y comparar el informe con las pruebas de la guía MASTG

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar la APK de tu propia app antes de publicarla para detectar permisos excesivos, copias de seguridad habilitadas o claves escritas en el código; Practicar con una app de entrenamiento de OWASP y comparar el informe con las pruebas de la guía MASTG | Quieres analizar apps de terceros sin permiso o compartir el servidor en una red sin reforzar su configuración. |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Usa 4.6.6 o posterior (recomendada 4.6.9): las versiones anteriores tienen avisos publicados, entre ellos XSS almacenado que puede provocar la propia app analizada. Publica el puerto solo en 127.0.0.1 (el ejemplo del README, -p 8000:8000, lo abre a tu red) y no uses la clave predeterminada mobsf/mobsf. Analiza solo apps propias o con permiso, y no subas apps privadas a mobsf.live, que es un servicio en línea.

## Stack y modelos

- **Stack:** Python, Dockerfile, pyproject.toml
- **Etiquetas:** `móvil` `android` `ios` `análisis estático` `seguridad`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF)
- 🌐 Web: <https://opensecurity.in>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-27. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/README.md)
- [Fuente 2](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/Dockerfile)
- [Fuente 3](https://github.com/MobSF/Mobile-Security-Framework-MobSF/blob/fa87c37892b264cf76bed8c358cc2d5d5323c8c2/mobsf/MobSF/settings.py)
- [Fuente 4](https://github.com/MobSF/docs/blob/545d88f9c19a97933ba36e60fdb9c6946d7aa9e2/configurations.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
