[🏠 Inicio](../README.md) › [🧬 Operar, evaluar y medir modelos de IA](../categorias/23-operacion-evaluacion-modelos.md) › Ahorro de contexto y tokens

# 📚 TOON

> Convierte listas de objetos JSON a un texto con encabezado y filas para experimentar con entradas más compactas para modelos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 25.7k | MIT | TypeScript | 2026-11-24 |

**Ejecución** 🏠 local · **Rol** 📚 librería/SDK · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media; requiere programar con él

## ¿Qué es?

TOON es un formato de texto y una biblioteca JavaScript de referencia para codificar datos JSON.

## ¿Qué hace?

Representa listas uniformes con una cabecera común y filas para dejar más visible la forma de los datos.

## ¿Cómo lo hace?

Conserva el modelo de datos de JSON e identifica conjuntos de objetos compatibles con una representación tabular.

Estado en GitHub: activo · último push 2026-11-24 · última versión publicada v4.4.0 (2026-10-08) · licencia declarada MIT (consultado el 2026-11-24).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-24); no se instaló ni ejecutó. Fuentes: [1](https://github.com/toon-format/toon/blob/92d7fc6d8af920afc99d1b6533cfc976c472fe7d/README.md) · [2](https://registry.npmjs.org/@toon-format%2Ftoon/4.4.0) · [3](https://github.com/toon-format/toon/actions/runs/37839997802) · [4](https://github.com/toon-format/toon/security/advisories/GHSA-p95v-992w-h6c3)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. Codificar un objeto en el equipo no necesita un modelo. Invocar uno después tiene su propia cuota. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La ruta básica procesa los datos en tu equipo sin un modelo. |
| Coste | Sin pago a un modelo en la ruta básica. Código MIT. La tarea de ejemplo se ejecuta con herramientas gratuitas en tu equipo. |
| Equipo | Equipo normal; revisar dependencias. Node.js con npm y proyecto que pueda importar módulos ES. |

La ruta básica funciona sin iniciar sesión en un agente de IA.

## Cómo empezar

Pieza para un proyecto de código. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node.js con npm y un proyecto con módulos ES.
- Dos registros JSON ficticios con los mismos campos.

1. Prepara Node.js con npm y un proyecto de prueba que admita módulos ES.
2. Consulta el README de v4.4.0 e instala la versión revisada del paquete oficial. Usa el ejemplo de encode con dos objetos de muestra.
3. Comprueba que el texto contiene los dos objetos y conserva los valores. Mide el tamaño con el tokenizador de tu modelo si después quieres compararlos.

**Entrada documentada (consulta la sintaxis original):**

```
npm install @toon-format/toon
```

El README muestra el comando general. Selecciona la versión revisada 4.4.0 en el registro oficial y sigue los pasos.

[Instrucciones originales de instalación](https://github.com/toon-format/toon/blob/92d7fc6d8af920afc99d1b6533cfc976c472fe7d/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/toon-format/toon/blob/92d7fc6d8af920afc99d1b6533cfc976c472fe7d/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar TOON para mi objetivo y necesito pasos guiados. Lee https://github.com/toon-format/toon/blob/92d7fc6d8af920afc99d1b6533cfc976c472fe7d/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Usa encode con dos registros ficticios que compartan campos, siguiendo el ejemplo del README de la versión 4.4.0..

**Qué comprobar:** La salida conserva ambos registros y enumera los campos en el encabezado. Revisa los valores y compárala con el JSON original..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Representar un inventario ficticio de productos con los mismos tres campos en cada fila.
- Preparar una tabla de registros con idéntica estructura para comparar el tamaño con JSON compacto.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Representar un inventario ficticio de productos con los mismos tres campos en cada fila.; Preparar una tabla de registros con idéntica estructura para comparar el tamaño con JSON compacto. | buscas una aplicación lista y no quieres preparar un proyecto de código |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Usa v4.4.0 para seguir la ruta revisada. El aviso GHSA-p95v-992w-h6c3 afecta a versiones anteriores a 2.3.1. Probar solo con datos propios y medir el tamaño con tu modelo.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `json` `tokens` `typescript` `contexto`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [toon-format/toon](https://github.com/toon-format/toon)
- 🌐 Web: <https://toonformat.dev>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-24. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/toon-format/toon/blob/92d7fc6d8af920afc99d1b6533cfc976c472fe7d/README.md)
- [Fuente 2](https://registry.npmjs.org/@toon-format%2Ftoon/4.4.0)
- [Fuente 3](https://github.com/toon-format/toon/actions/runs/37839997802)
- [Fuente 4](https://github.com/toon-format/toon/security/advisories/GHSA-p95v-992w-h6c3)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
