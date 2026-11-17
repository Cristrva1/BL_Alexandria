[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ OWASP Juice Shop

> Aplicación web vulnerable oficial de OWASP para entrenar AppSec: cientos de retos y puntuación.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.5k | MIT | TypeScript | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 75/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Lab web vulnerable OWASP (MIT).

## ¿Qué hace?

Sirve una tienda con fallos intencionados y un scoreboard.

## ¿Cómo lo hace?

npm o Docker.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ZAP (Zed Attack Proxy)](zaproxy.md) | ZAP contra Juice Shop. | Levanta Juice Shop; escanea con ZAP. |
| [Nuclei](nuclei.md) | Plantillas Nuclei sobre el lab. | Juice Shop → Nuclei. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (4). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[ModSecurity](modsecurity.md) · [OWASP CheatSheet Series](cheatsheetseries.md) · [OWASP Top 10](owasp-top10.md) · [OWASP Web Security Testing Guide](wstg.md)

Estado en GitHub: activo · último push 2026-11-11 · última versión publicada v20.4.0 (2026-11-08) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/juice-shop/juice-shop#readme) · [2](https://owasp-juice.shop)</sub>

## Ver similares

Grupo **Aplicaciones web vulnerables para practicar**: OWASP Juice Shop ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **OWASP Juice Shop** (esta ficha) ⭐ recomendado | 75 | Si quieres retos tipo CTF sobre una tienda moderna en JavaScript. |
| 2 | [WebGoat](webgoat.md) | 62 | Si prefieres lecciones guiadas paso a paso sobre una aplicación Java. |

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
npm install
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/juice-shop/juice-shop/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://owasp-juice.shop)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP Juice Shop para mi objetivo y necesito pasos guiados. Lee https://github.com/juice-shop/juice-shop/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona el repo, `npm install` y `npm start`, o usa la imagen Docker oficial..

**Qué comprobar:** Abres la tienda vulnerable en localhost..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- practicar OWASP Top 10 en local
- validar un scanner contra retos conocidos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: practicar OWASP Top 10 en local; validar un scanner contra retos conocidos | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Solo laboratorio; no desplegar expuesto a Internet.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, package.json
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [WebGoat](webgoat.md) | 9.5k | Aplicación web deliberadamente insegura de OWASP con lecciones guiadas para aprender y practicar vulnerabilidades del Top 10. |

## Enlaces

- 🐙 GitHub: [juice-shop/juice-shop](https://github.com/juice-shop/juice-shop)
- 🌐 Web: <https://owasp-juice.shop>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/juice-shop/juice-shop/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
