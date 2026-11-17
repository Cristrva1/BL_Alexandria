[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Respuesta a incidentes y forense

# 🖥️ Velociraptor

> EDR/IR open source para recolección forense a escala: consultas VQL sobre endpoints Windows, Linux y macOS.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.5k | AGPL-3.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** hard

**Nivel:** 4 Experto — preparación difícil; dominio especializado

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** AGPL-3.0. Fuente: [LICENSE](https://github.com/Velocidex/velociraptor/blob/master/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

Plataforma AGPL de Velocidex para respuesta a incidentes y caza en endpoints.

## ¿Qué hace?

Ejecuta artefactos VQL en clientes y centraliza resultados para IR y forense.

## ¿Cómo lo hace?

Binarios de release; se configura servidor/frontend y se despliegan clientes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Wazuh](wazuh.md) | Velociraptor profundiza en endpoints que Wazuh marca. | Alerta en Wazuh → recolección VQL. |
| [osquery](osquery.md) | Osquery aporta SQL continuo; Velociraptor hunts puntuales. | Usa osquery para baseline; Velociraptor para IR. |
| [Volatility 3](volatility3.md) | Volatilidad analiza memoria; Velociraptor la adquiere. | Adquiere con Velociraptor; analiza con Volatility3. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Hayabusa](hayabusa.md) · [The Sleuth Kit](sleuthkit.md)

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.77.3 (2026-10-05) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Velocidex/velociraptor#readme) · [2](https://docs.velociraptor.app/)</sub>

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
git clone https://github.com/Velocidex/velociraptor.git
```

Comando copiado literalmente de el README (sección «Building from source»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/Velocidex/velociraptor/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://docs.velociraptor.app/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Velociraptor para mi objetivo y necesito pasos guiados. Lee https://github.com/Velocidex/velociraptor/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Descarga el release desde GitHub y sigue docs.velociraptor.app para levantar servidor y cliente de lab..

**Qué comprobar:** La UI muestra el cliente online listo para una recolección..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- recolectar evidencias de un endpoint comprometido en lab
- lanzar un hunt de IOCs en una flota de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: recolectar evidencias de un endpoint comprometido en lab; lanzar un hunt de IOCs en una flota de prueba | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Gobierna con cuidado el acceso al servidor: puede leer y ejecutar en todos los endpoints enrolados.

## Stack y modelos

- **Stack:** Go, Makefile, go.mod
- **Etiquetas:** `security` `ir` `edr`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Velocidex/velociraptor](https://github.com/Velocidex/velociraptor)
- 🌐 Web: <https://docs.velociraptor.app/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Velocidex/velociraptor/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
