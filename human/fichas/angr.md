[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Ingeniería inversa y formatos binarios

# 📚 angr

> Plataforma en Python para analizar programas binarios mediante técnicas como ejecución simbólica y análisis de flujo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 9.4k | BSD-2-Clause | Python | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; requiere programar con él; dominio especializado

**Puntuación de calidad** 72/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Framework de análisis binario en Python, independiente de la plataforma, del Computer Security Lab de UC Santa Barbara, SEFCOM de Arizona State University y el equipo CTF Shellphish. Licencia BSD-2-Clause. Es maduro y muy usado en investigación y CTF (~9k estrellas).

## ¿Qué hace?

Carga un binario y permite desensamblarlo y elevarlo a una representación intermedia, instrumentarlo, ejecutarlo simbólicamente, analizar el flujo de control y las dependencias de datos, hacer análisis de conjuntos de valores (VSA) y decompilar. Sirve para encontrar entradas que alcanzan cierto código, resolver retos o automatizar análisis de vulnerabilidades.

## ¿Cómo lo hace?

Es un conjunto de librerías Python 3: se instala con `pip install angr`, en un entorno virtual propio, como recomienda el README. Se usa desde scripts o un REPL como IPython. La ejecución simbólica puede consumir mucha memoria y tiempo con binarios grandes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ghidra](ghidra.md) | Explorar el binario en Ghidra y automatizar la búsqueda de rutas en angr. (combinación por arquitectura) | Identifica direcciones en Ghidra y úsalas en el script de angr. |
| [frida](frida.md) | Combinar análisis dinámico en ejecución con análisis simbólico. (combinación por arquitectura) | Captura valores reales con Frida y úsalos como restricciones en angr. |
| [Claude Code](claude-code.md) | Escribir y depurar scripts de angr con un agente. (combinación por arquitectura) | Instala angr en un entorno virtual y abre el proyecto con el agente. |
| [GhidraMCP](ghidramcp.md) | Combinación recíproca: GhidraMCP lo enlaza como «Automatizar con ejecución simbólica las rutas que el agente identifique. (combinación por arquitectura)». | Orden indicado desde GhidraMCP: Usa angr en scripts aparte sobre el mismo binario. |
| [rizin](rizin.md) | Combinación recíproca: rizin lo enlaza como «Ejecución simbólica sobre las rutas que identifiques en Rizin. (combinación por arquitectura)». | Orden indicado desde rizin: Localiza la función en Rizin y modela la búsqueda en angr. |

**Notas:** Sin alternativas declaradas. Úsalo solo con software y sistemas que tengas derecho a analizar.

Estado en GitHub: activo · último push 2026-11-14 · licencia declarada BSD-2-Clause (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/angr/angr/blob/master/README.md) · [2](https://docs.angr.io/en/latest/getting-started/installing.html)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere LLM; resolver estados consume recursos y puede crecer mucho con el programa |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es una plataforma de análisis que requiere programación; el ejemplo de hooks no es su instalación |
| Coste | Sin pago a un modelo en la ruta básica. No requiere LLM; resolver estados consume recursos y puede crecer mucho con el programa |
| Equipo | Preparación según la ruta elegida. Python y entorno compatible; binario de laboratorio |

Es una plataforma de análisis que requiere programación; el ejemplo de hooks no es su instalación

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python y entorno compatible
- binario de laboratorio

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
pip install angr
```

Comando copiado literalmente de la documentación oficial enlazada desde el README (sección «Installing from PyPI¶»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://docs.angr.io/introductory-errata/install)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar angr para mi objetivo y necesito pasos guiados. Lee https://docs.angr.io/introductory-errata/install. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Carga un programa propio sencillo y explora sus funciones y estados simbólicos.

**Qué comprobar:** Puedes relacionar una ruta analizada con la lógica del ejemplo.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar ejecución simbólica
- Analizar rutas de un binario de práctica

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar ejecución simbólica; Analizar rutas de un binario de práctica | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es una plataforma de análisis que requiere programación; el ejemplo de hooks no es su instalación

## Stack y modelos

- **Stack:** Python y entorno compatible; binario de laboratorio
- **Etiquetas:** `reversing` `library` `python`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [angr/angr](https://github.com/angr/angr)
- 🌐 Web: <http://angr.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/angr/angr/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
