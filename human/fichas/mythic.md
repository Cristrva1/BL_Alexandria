[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Explotación, C2 y post-explotación

# 🖥️ Mythic

> Framework C2 colaborativo con UI: agentes y perfiles C2 se instalan aparte vía mythic-cli.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 4.9k | BSD-3-Clause | JavaScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** hard

**Nivel:** 4 Experto — preparación difícil; dominio especializado

**Puntuación de calidad** 48/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** BSD-3-Clause. Fuente: [LICENSE](https://github.com/its-a-feature/Mythic/blob/master/LICENSE). GitHub la marca como NOASSERTION.

## ¿Qué es?

C2 colaborativo (BSD-3 según LICENSE; API NOASSERTION).

## ¿Qué hace?

Orquesta agents/profiles vía UI y API.

## ¿Cómo lo hace?

mythic-cli + contenedores.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [CALDERA](caldera.md) | CALDERA emulación ATT&CK; Mythic C2 operator-centric. | Complementarios. |
| [Wazuh](wazuh.md) | Valida detección del C2 en lab. | Mythic → Wazuh. |

Estado en GitHub: activo · último push 2026-11-14 · última versión publicada v3.4.0.5 (2025-10-10) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/its-a-feature/Mythic#readme)</sub>

## Ver similares

Grupo **Frameworks de C2 y post-explotación**: Mythic ocupa la posición 3 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Sliver](sliver.md) ⭐ recomendado | 69 | Si buscas esto: framework C2 open source de Bishop Fox para emulación de adversario autorizada: implants multiplataforma y canales mTLS/WireGuard/HTTP/DNS. |
| 2 | [Empire](empire.md) | 60 | Si buscas esto: framework post-explotación/C2 centrado en PowerShell y agentes multiplataforma para labs autorizados. |
| 3 | **Mythic** (esta ficha) | 48 | Si buscas esto: framework C2 colaborativo con UI: agentes y perfiles C2 se instalan aparte vía mythic-cli. |

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

[Instrucciones originales de instalación](https://github.com/its-a-feature/Mythic/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Mythic para mi objetivo y necesito pasos guiados. Lee https://github.com/its-a-feature/Mythic/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona Mythic, `sudo make` y `sudo ./mythic-cli start` en una VM aislada..

**Qué comprobar:** UI del servidor lista; instala un agente..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- montar un C2 de lab con un agente oficial
- ejercicio purple team multi-operador

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: montar un C2 de lab con un agente oficial; ejercicio purple team multi-operador | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** JavaScript, Makefile
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Empire](empire.md) | 5.4k | Framework post-explotación/C2 centrado en PowerShell y agentes multiplataforma para labs autorizados. |
| [Sliver](sliver.md) | 12.3k | Framework C2 open source de Bishop Fox para emulación de adversario autorizada: implants multiplataforma y canales mTLS/WireGuard/HTTP/DNS. |

## Enlaces

- 🐙 GitHub: [its-a-feature/Mythic](https://github.com/its-a-feature/Mythic)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/its-a-feature/Mythic/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
