[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Respuesta a incidentes y forense

# 🖥️ Volatility 3

> Framework forense de memoria RAM (v3): analiza dumps Windows/Linux/macOS para procesos, redes y malware.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.6k | Volatility Software License 1.0 (no OSI) | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 3 Avanzado — preparación media; dominio especializado

**Puntuación de calidad** 53/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia revisada el 2026-11-16:** Volatility Software License 1.0 (no OSI). Copyleft: exige compartir el código de cambios y del software construido con ella. Fuente: [LICENSE](https://github.com/volatilityfoundation/volatility3/blob/develop/LICENSE.txt). GitHub la marca como NOASSERTION.

## ¿Qué es?

Volatility 3 de Volatility Foundation; licencia propia (Volatility Software License) aunque la API marca NOASSERTION.

## ¿Qué hace?

Interpreta dumps de memoria y reconstruye artefactos del sistema operativo.

## ¿Cómo lo hace?

pip (`volatility3`) o editable desde el repo; requiere un memory dump previo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Velociraptor](velociraptor.md) | Velociraptor adquiere; Volatility analiza. | Adquisición → dump → Volatility3. |
| [YARA](yara.md) | Escaneo YARA sobre regiones de memoria con plugins. | Carga reglas YARA en el plugin adecuado. |
| [Wireshark](wireshark.md) | Reconstruye PCAP desde memoria y ábrelo en Wireshark. | Plugin de red → Wireshark. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[The Sleuth Kit](sleuthkit.md)

Estado en GitHub: activo · último push 2026-10-12 · última versión publicada v2.28.2 (2026-09-17) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/volatilityfoundation/volatility3#readme) · [2](https://volatilityfoundation.org/)</sub>

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

**Entrada documentada (consulta la sintaxis original):**

```
pip install volatility3
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/volatilityfoundation/volatility3/blob/develop/README.md)

[Abrir la web o descarga indicada por el autor](https://volatilityfoundation.org/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Volatility 3 para mi objetivo y necesito pasos guiados. Lee https://github.com/volatilityfoundation/volatility3/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install volatility3` y ejecuta un plugin sobre un dump de laboratorio..

**Qué comprobar:** Obtienes la tabla del plugin (pslist, netscan, etc.)..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- listar procesos ocultos en un dump de lab
- extraer conexiones de red desde memoria

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: listar procesos ocultos en un dump de lab; extraer conexiones de red desde memoria | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Python, pyproject.toml
- **Etiquetas:** `security` `forensics` `memory`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [volatilityfoundation/volatility3](https://github.com/volatilityfoundation/volatility3)
- 🌐 Web: <https://volatilityfoundation.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/volatilityfoundation/volatility3/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
