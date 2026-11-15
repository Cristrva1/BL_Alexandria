[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Memoria persistente para agentes

# 📚 dsh-noema

> Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 144 | MIT | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión. |
| Coste | Consumo del agente que ya utilizas. Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función. |
| Equipo | Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida. |
| Otras rutas | Plugin para DeepSeek Harness (DSH). La cuenta, API o modelo se configura en ese anfitrión; no se declara instalación nativa en Claude Code o Codex. |

Consume el acceso y los límites del agente donde lo configures. No incluye servicios externos de generación, datos o alojamiento.

## Qué puedes hacer con él

Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración.

## Cómo funciona

Se instala dentro de DeepSeek Harness para añadir herramientas y una interfaz a ese entorno.

## Cómo empezar

Se configura en tu agente. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- El agente compatible indicado por el proyecto y acceso activo al modelo de ese agente.
- DeepSeek Harness y los controladores específicos que indica el plugin.

1. Abre la instalación del README y elige la ruta para el agente que utilizas.
2. Añade la skill o el plugin concreto; prepara los programas y servicios que indique su documentación.
3. Pide una primera tarea pequeña sobre archivos de prueba y comprueba qué herramientas y cuentas activa.

[Instrucciones originales de instalación](https://github.com/ZSeven-W/dsh-noema/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar dsh-noema para mi objetivo y necesito pasos guiados. Lee https://github.com/ZSeven-W/dsh-noema/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| buscas esta función: Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración. | necesitas un producto autónomo y esta pieza requiere un anfitrión compatible |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `memoria` `plugin` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [ZSeven-W/dsh-noema](https://github.com/ZSeven-W/dsh-noema)
- 🌐 Web: <op.zseven.tech>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/ZSeven-W/dsh-noema/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
