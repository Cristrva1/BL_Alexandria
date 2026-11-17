[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Reconocimiento y superficie de ataque

# 🖥️ OWASP Noir

> Descubre endpoints y parámetros en el código fuente (y API ocultas) para mapear la superficie de ataque y alimentar pruebas DAST.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.5k | MIT | Crystal | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 61/100 · métricas del 2026-11-17 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Proyecto OWASP para descubrir endpoints a partir del código y mapear la superficie de ataque.

## ¿Qué hace?

Identifica rutas, métodos y parámetros (incluidas API no documentadas) en código de múltiples lenguajes y frameworks, y exporta en JSON, OpenAPI y otros formatos.

## ¿Cómo lo hace?

Analizadores estáticos por framework escritos en Crystal; puede enviar resultados a proxies DAST y usar un LLM opcional para lenguajes no soportados.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ZAP (Zed Attack Proxy)](zaproxy.md) | Noir envía los endpoints descubiertos a ZAP para pruebas dinámicas. | Noir sobre el código; después ZAP sobre la app en laboratorio. |
| [Caido](caido.md) | Caido recibe los endpoints como punto de partida de pruebas manuales. | Noir primero; Caido como proxy. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v1.5.0 (2026-11-02) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/owasp-noir/noir#readme) · [2](https://owasp-noir.github.io/noir/)</sub>

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
brew install noir
```

Comando copiado literalmente de el README (sección «Usage»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://github.com/owasp-noir/noir/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://owasp-noir.github.io/noir/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar OWASP Noir para mi objetivo y necesito pasos guiados. Lee https://github.com/owasp-noir/noir/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con Homebrew como indica el README y analiza el directorio de una aplicación propia..

**Qué comprobar:** Obtienes la lista de endpoints, métodos y parámetros detectados..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- listar todos los endpoints de un repositorio propio antes de un pentest
- pasar endpoints descubiertos a ZAP para un escaneo autorizado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: listar todos los endpoints de un repositorio propio antes de un pentest; pasar endpoints descubiertos a ZAP para un escaneo autorizado | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso dual: analiza solo código propio o con autorización. El análisis con LLM envía fragmentos de código al proveedor configurado.

## Stack y modelos

- **Stack:** Crystal
- **Etiquetas:** `security` `sast` `attack-surface` `api` `crystal`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [owasp-noir/noir](https://github.com/owasp-noir/noir)
- 🌐 Web: <https://owasp-noir.github.io/noir/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/owasp-noir/noir/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
