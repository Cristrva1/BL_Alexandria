[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Ingeniería inversa y formatos binarios

# 🖥️ capa

> Detecta capacidades en binarios/malware (anti-debug, C2, persistencia…) mediante reglas y análisis estático.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.3k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 3 Avanzado — preparación sencilla; dominio especializado

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Capability scanner de Mandiant (Apache-2.0).

## ¿Qué hace?

Infiere comportamientos de un binario sin ejecutarlo.

## ¿Cómo lo hace?

Releases / pip.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ghidra](ghidra.md) | capa prioriza; Ghidra profundiza. | capa → Ghidra. |
| [YARA](yara.md) | YARA firma; capa describe capacidades. | Ambos sobre la muestra. |

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada v10.0.0 (2026-10-16) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mandiant/capa#readme) · [2](https://mandiant.github.io/capa/)</sub>

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

[Instrucciones originales de instalación](https://github.com/mandiant/capa/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://mandiant.github.io/capa/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar capa para mi objetivo y necesito pasos guiados. Lee https://github.com/mandiant/capa/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga el release standalone y ejecuta `capa muestra.exe` en un sandbox..

**Qué comprobar:** Listas capacidades detectadas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- clasificar una muestra de lab
- priorizar qué abrir en Ghidra

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: clasificar una muestra de lab; priorizar qué abrir en Ghidra | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Python, pyproject.toml, requirements.txt
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [mandiant/capa](https://github.com/mandiant/capa)
- 🌐 Web: <https://mandiant.github.io/capa/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/mandiant/capa/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
