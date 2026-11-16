[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Depuración e inspección de procesos

# 🖥️ pwndbg

> Mejoras para GDB/LLDB orientadas a exploit-dev: heap, ROPgadget, contexto de registros y más.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 11.2k | MIT | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; dominio especializado

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plugin GDB/LLDB para pwn.

## ¿Qué hace?

Añade comandos y vistas útiles en depuración ofensiva.

## ¿Cómo lo hace?

Installer documentado.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [pwntools](pwntools.md) | Desarrollo del exploit + debug. | Ambos en el workflow. |
| [ghidra](ghidra.md) | RE estático + debug dinámico. | Ghidra ↔ pwndbg. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 2026.10.28 (2026-10-28) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/pwndbg/pwndbg#readme) · [2](https://pwndbg.re/stable/setup)</sub>

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
brew install pwndbg/tap/pwndbg-gdb
```

Comando copiado literalmente de la documentación del repositorio (sección «Homebrew»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/pwndbg/pwndbg/blob/dev/docs/setup.md)

[Abrir la web o descarga indicada por el autor](https://pwndbg.re/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar pwndbg para mi objetivo y necesito pasos guiados. Lee https://github.com/pwndbg/pwndbg/blob/dev/docs/setup.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue https://pwndbg.re/stable/setup e inicia GDB con pwndbg sobre un binario de lab..

**Qué comprobar:** Ves el layout enriquecido..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- depurar un binario vulnerable de lab
- inspeccionar heap tras un overflow

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: depurar un binario vulnerable de lab; inspeccionar heap tras un overflow | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** Python, Dockerfile, docker-compose.yml, pyproject.toml
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [pwndbg/pwndbg](https://github.com/pwndbg/pwndbg)
- 🌐 Web: <https://pwndbg.re/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/pwndbg/pwndbg/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
