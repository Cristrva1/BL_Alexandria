[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Active Directory y red interna

# 📂 GOAD

> Lab Active Directory vulnerable (Orange Cyberdefense) para practicar ataques AD en VMs locales aisladas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 8.6k | GPL-3.0 | PowerShell | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** hard

**Puntuación de calidad** 55/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Lab AD vulnerable documentado (GPL-3).

## ¿Qué hace?

Despliega dominios AD rotos a propósito.

## ¿Cómo lo hace?

Automatización documentada por Orange.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [BloodHound Community Edition](bloodhound.md) | Analiza el lab con BloodHound. | GOAD → BloodHound. |
| [Certipy](certipy.md) | Practica AD CS en GOAD. | GOAD → Certipy. |
| [NetExec](netexec.md) | Enumera el lab con NetExec. | GOAD → NetExec. |

Estado en GitHub: activo · último push 2026-10-23 · licencia declarada GPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Orange-Cyberdefense/GOAD#readme) · [2](https://orange-cyberdefense.github.io/GOAD/)</sub>

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

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Abre el material original y localiza la sección relacionada con tu tarea.
2. Elige una referencia o ejemplo; revisa sus requisitos y su procedencia antes de instalar nada.
3. Conserva solo las piezas que necesitas y consulta la ficha de cada proyecto enlazado.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Orange-Cyberdefense/GOAD/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://orange-cyberdefense.github.io/GOAD/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar GOAD para mi objetivo y necesito pasos guiados. Lee https://github.com/Orange-Cyberdefense/GOAD/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue https://orange-cyberdefense.github.io/GOAD/ en hardware con suficiente RAM..

**Qué comprobar:** VMs AD listas para atacar en aislamiento..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- montar un lab AD completo
- practicar BloodHound/Certipy/NetExec con seguridad

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: montar un lab AD completo; practicar BloodHound/Certipy/NetExec con seguridad | necesitas una aplicación lista para ejecutar en lugar de material de consulta |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Solo lab local/aislado. Nunca exponer a Internet.

## Stack y modelos

- **Stack:** PowerShell, Dockerfile, pyproject.toml
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [Orange-Cyberdefense/GOAD](https://github.com/Orange-Cyberdefense/GOAD)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Orange-Cyberdefense/GOAD/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
