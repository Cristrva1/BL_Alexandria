[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# 🖥️ Bandit

> Revisa código Python en busca de fallos de seguridad habituales, como comandos con shell=True o yaml.load inseguro, e indica la línea de cada hallazgo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.4k | Apache-2.0 | Python | 2026-11-27 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 62/100 · métricas del 2026-11-28 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Analizador de seguridad para código Python mantenido por la comunidad PyCQA.

## ¿Qué hace?

Detecta patrones de riesgo como comandos con shell, deserialización insegura, contraseñas escritas en el código o criptografía débil.

## ¿Cómo lo hace?

Recorre el árbol de sintaxis de cada archivo con complementos identificados por códigos (B101, B602, B506…) y clasifica cada hallazgo por gravedad y confianza.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [pre-commit](pre-commit.md) | Ejecuta Bandit antes de cada commit con el gancho que publica el propio repositorio. | — |
| [Gitleaks](gitleaks.md) | Busca claves y contraseñas filtradas en todo el historial de git, que Bandit no revisa. | — |
| [DefectDojo](defectdojo.md) | Importa los informes de Bandit para seguir y deduplicar hallazgos junto con los de otros escáneres. | — |

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada 1.9.4 (2026-02-25) · licencia declarada Apache-2.0 (consultado el 2026-11-27).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-27); no se instaló ni ejecutó. Fuentes: [1](https://github.com/PyCQA/bandit/blob/92ae8b82fb422a639f0ed8d99e96cea769594e08/README.rst) · [2](https://github.com/PyCQA/bandit/blob/92ae8b82fb422a639f0ed8d99e96cea769594e08/LICENSE) · [3](https://github.com/PyCQA/bandit/blob/92ae8b82fb422a639f0ed8d99e96cea769594e08/doc/source/start.rst) · [4](https://github.com/PyCQA/bandit/blob/92ae8b82fb422a639f0ed8d99e96cea769594e08/bandit/plugins/injection_shell.py) · [5](https://github.com/PyCQA/bandit/blob/92ae8b82fb422a639f0ed8d99e96cea769594e08/bandit/plugins/yaml_load.py) · [6](https://github.com/PyCQA/bandit/blob/92ae8b82fb422a639f0ed8d99e96cea769594e08/.github/workflows/pythonpackage.yml) · [7](https://github.com/PyCQA/bandit/blob/92ae8b82fb422a639f0ed8d99e96cea769594e08/tox.ini) · [8](https://github.com/PyCQA/bandit/blob/92ae8b82fb422a639f0ed8d99e96cea769594e08/tests/functional/test_functional.py) · [9](https://github.com/PyCQA/bandit/blob/92ae8b82fb422a639f0ed8d99e96cea769594e08/.pre-commit-hooks.yaml) · [10](https://github.com/PyCQA/bandit/actions/runs/22385359689) · [11](https://github.com/PyCQA/bandit/actions/runs/22385508641) · [12](https://github.com/PyCQA/bandit/releases/tag/1.9.4) · [13](https://pypi.org/project/bandit/1.9.4/) · [14](https://github.com/PyCQA/bandit/security/advisories) · [15](https://github.com/DefectDojo/django-DefectDojo/tree/cd0a4483a224707f72a0fc3112359089c1446b55/dojo/tools/bandit)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita clave de API ni conexión durante el análisis. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Aplica reglas fijas sobre el código. No usa modelos de IA. |
| Coste | Sin pago a un modelo en la ruta básica. Licencia Apache-2.0, sin pago para instalarlo ni ejecutarlo. |
| Equipo | Equipo normal; revisar dependencias. Cualquier equipo con Python 3.10 o posterior. |

Un agente de código puede ayudarte a instalar Bandit y a interpretar el informe, pero Bandit se ejecuta en tu equipo sin cuenta ni suscripción de IA.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Instala Python 3.10 o posterior, que Bandit 1.9.4 exige. En una carpeta de prueba crea un entorno virtual con python -m venv bandit-env y actívalo.
2. Instala la versión revisada desde PyPI con pip install bandit==1.9.4 y comprueba que bandit --version muestra 1.9.4. También existe una imagen oficial firmada en ghcr.io/pycqa/bandit/bandit.
3. Crea prueba.py con la llamada de la primera prueba, ejecuta bandit prueba.py y localiza B602. Cambia la llamada a subprocess.call(['ls', carpeta]) sin shell=True y repite: B602 desaparece y solo quedan avisos informativos de gravedad Low, como B404 o B603.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/PyCQA/bandit/blob/main/README.rst)

[Abrir la web o descarga indicada por el autor](https://bandit.readthedocs.io/en/latest/start.html)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Bandit para mi objetivo y necesito pasos guiados. Lee https://github.com/PyCQA/bandit/blob/main/README.rst. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea prueba.py con import subprocess y subprocess.call(input('Carpeta: '), shell=True) y ejecuta bandit prueba.py.

**Qué comprobar:** El informe muestra el hallazgo B602 (subprocess_popen_with_shell_equals_true) con gravedad High y confianza High en la línea de la llamada.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar un script propio de automatización antes de compartirlo para encontrar llamadas peligrosas al sistema
- Añadir una comprobación de seguridad antes de cada commit en un proyecto Python mediante pre-commit

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar un script propio de automatización antes de compartirlo para encontrar llamadas peligrosas al sistema; Añadir una comprobación de seguridad antes de cada commit en un proyecto Python mediante pre-commit | Tu proyecto no está escrito en Python o necesitas seguir el recorrido de los datos entre varios archivos. |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Cada hallazgo señala un patrón de riesgo, no una vulnerabilidad confirmada: revisa la línea antes de cambiarla. Bandit analiza archivo por archivo y no revisa dependencias ni secretos del historial de git. Úsalo solo con código propio o con permiso.

## Stack y modelos

- **Stack:** Python, requirements.txt, setup.py
- **Etiquetas:** `python` `análisis estático` `seguridad` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [PyCQA/bandit](https://github.com/PyCQA/bandit)
- 🌐 Web: <https://bandit.readthedocs.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-27. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/PyCQA/bandit/blob/92ae8b82fb422a639f0ed8d99e96cea769594e08/README.rst)
- [Fuente 2](https://github.com/PyCQA/bandit/blob/92ae8b82fb422a639f0ed8d99e96cea769594e08/doc/source/start.rst)
- [Fuente 3](https://pypi.org/project/bandit/1.9.4/)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
