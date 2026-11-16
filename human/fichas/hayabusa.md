[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Respuesta a incidentes y forense

# 🖥️ Hayabusa

> Triaje forense de event logs Windows con reglas Sigma: rápido, firmado y orientado a DFIR.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 3.5k | AGPL-3.0 | Rust | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

DFIR timeline/rules (AGPL) de Yamato Security.

## ¿Qué hace?

Aplica Sigma a event logs Windows.

## ¿Cómo lo hace?

Releases firmados.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Sigma](sigma.md) | Usa reglas SigmaHQ. | Paquete Sigma → Hayabusa. |
| [Velociraptor](velociraptor.md) | Velociraptor recolecta; Hayabusa tria. | Recolección → Hayabusa. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Autopsy](autopsy.md)

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada v4.4.0 (2026-11-10) · licencia declarada AGPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Yamato-Security/hayabusa#readme) · [2](https://yamato-security.github.io/hayabusa/getting-started/)</sub>

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Yamato-Security/hayabusa/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Hayabusa para mi objetivo y necesito pasos guiados. Lee https://github.com/Yamato-Security/hayabusa/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga el release firmado y ejecuta Hayabusa sobre un evtx de lab..

**Qué comprobar:** Tabla de hits Sigma..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- triar logs de un endpoint Windows de lab
- buscar técnicas ATT&CK en evtx

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: triar logs de un endpoint Windows de lab; buscar técnicas ATT&CK en evtx | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Rust, Cargo.toml
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Yamato-Security/hayabusa](https://github.com/Yamato-Security/hayabusa)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Yamato-Security/hayabusa/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
