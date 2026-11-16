[🏠 Inicio](../README.md) › [🕸️ Asistentes e investigación con agentes](../categorias/21-asistentes-investigacion.md) › Asistentes autónomos y equipos de agentes

# 🖥️ fugu

> Ejemplos y acceso a un sistema multiagente de Sakana que se consume como un servicio de modelos mediante API.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1k | — | Shell | 2026-11-14 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Sakana Fugu, sistema multiagente comercial de Sakana AI que se consume como un único modelo. El repo solo contiene ejemplos e instaladores, sin licencia; el servicio es de pago o con registro en console.sakana.ai. Tiene ~1k estrellas.

## ¿Qué hace?

Orquesta dinámicamente un conjunto de modelos frontera para resolver tareas complejas de varios pasos, expuesto como un único endpoint de modelo. Las cifras de rendimiento provienen del informe técnico de Sakana.

## ¿Cómo lo hace?

Se integra con Codex o Claude Code mediante `curl -fsSL https://sakana.ai/fugu/install | bash`, que crea los comandos `codex-fugu` y `claude-fugu` (Ubuntu y macOS; en Windows hay configuración manual). Con Claude Code hay diferencias de compatibilidad, mayormente cosméticas.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Codex CLI](codex.md) | Integración nativa (`codex-fugu`). | Instala Codex y luego el script de Fugu. |
| [Claude Code](claude-code.md) | Integración nativa (`claude-fugu`). | Instala Claude Code y luego el script de Fugu. |
| [T3 Code](t3code.md) | Controlar desde web o móvil el Codex que usa Fugu. (combinación por arquitectura) | Usa T3 Code sobre Codex. |

**Notas:** Sin alternativas declaradas. Pregunta de pertenencia al catálogo: el repo es un cliente de un servicio propietario (solo anotado).

Estado en GitHub: activo · último push 2026-10-28 · última versión publicada user-demo-v1 (2026-06-26) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/SakanaAI/fugu/blob/main/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA necesaria. Se consume mediante Sakana API y sus condiciones; usar los launchers no incluye créditos del plan Claude Code o Codex |
| Claude Code | Integración documentada por el proyecto |
| Codex | Integración documentada por el proyecto |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Los launchers son adaptaciones de proveedor; el autor documenta diferencias con Claude Code y un procedimiento manual específico para Windows |
| Coste | Consumo de APIs o servicios. Se consume mediante Sakana API y sus condiciones; usar los launchers no incluye créditos del plan Claude Code o Codex |
| Equipo | Preparación según la ruta elegida. Acceso Sakana API; Claude Code o Codex si eliges sus launchers; carpeta de prueba |

Los launchers son adaptaciones de proveedor; el autor documenta diferencias con Claude Code y un procedimiento manual específico para Windows

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Acceso Sakana API
- Claude Code o Codex si eliges sus launchers
- carpeta de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.
3. Configura la cuenta,el proveedor o los modelos de la ruta elegida según Acceso y costes. Comprueba qué servicio recibirá tus datos y qué consumo puede generar.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/SakanaAI/fugu/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar fugu para mi objetivo y necesito pasos guiados. Lee https://github.com/SakanaAI/fugu/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue la configuración manual para tu sistema y consulta un archivo breve antes de permitir cambios.

**Qué comprobar:** Puedes identificar Fugu como proveedor y revisar la respuesta.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Probar un sistema multiagente como proveedor
- Comparar un flujo de código con Fugu

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Probar un sistema multiagente como proveedor; Comparar un flujo de código con Fugu | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Los launchers son adaptaciones de proveedor; el autor documenta diferencias con Claude Code y un procedimiento manual específico para Windows

## Stack y modelos

- **Stack:** Acceso Sakana API; Claude Code o Codex si eliges sus launchers; carpeta de prueba
- **Etiquetas:** `asistentes` `agent` `shell`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [SakanaAI/fugu](https://github.com/SakanaAI/fugu)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/SakanaAI/fugu/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
