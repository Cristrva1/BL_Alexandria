[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 📚 pwntools

> Framework Python para CTF y desarrollo de exploits: tubos, packing, ROP y utilidades de binarios.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 13.9k | NOASSERTION | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## ¿Qué es?

Framework CTF/exploit-dev (MIT mayoritario).

## ¿Qué hace?

Acelera escritura de exploits y wrappers.

## ¿Cómo lo hace?

pip.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [pwndbg](pwndbg.md) | Depura el binario mientras desarrollas el exploit. | pwndbg + pwntools. |
| [ghidra](ghidra.md) | RE del binario objetivo. | Ghidra → pwntools. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[AFL++](aflplusplus.md)

Estado en GitHub: activo · último push 2026-11-08 · última versión publicada 4.15.0 (2025-10-12) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Gallopsled/pwntools#readme) · [2](http://pwntools.com)</sub>

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

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de desarrollo compatible con el lenguaje y los requisitos del README.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.
2. Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.
3. Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación.

**Entrada documentada (consulta la sintaxis original):**

```
python3 -m pip install --upgrade pwntools
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Gallopsled/pwntools/blob/dev/README.md)

[Abrir la web o descarga indicada por el autor](http://pwntools.com)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar pwntools para mi objetivo y necesito pasos guiados. Lee https://github.com/Gallopsled/pwntools/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

`python3 -m pip install --upgrade pwntools` y lanza un script mínimo contra un binario local..

**Qué comprobar:** Interacción local/remota funcionando..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- escribir un exploit de un challenge CTF
- automatizar I/O con un servicio de lab

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: escribir un exploit de un challenge CTF; automatizar I/O con un servicio de lab | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** Python, pyproject.toml, setup.py
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Gallopsled/pwntools](https://github.com/Gallopsled/pwntools)
- 🌐 Web: <http://pwntools.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Gallopsled/pwntools/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
