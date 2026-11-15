[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Herramientas PDF

# 📑 Stirling-PDF

> Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 96.6k | NOASSERTION | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El proyecto es open-core; Server y Enterprise tienen planes; la operación PDF básica no exige modelo |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La edición de PDF, firma y redacción tienen efectos distintos: comprueba la salida de la operación elegida antes de sustituir un archivo |
| Coste | El coste depende del proveedor o la ruta. El proyecto es open-core; Server y Enterprise tienen planes; la operación PDF básica no exige modelo |
| Equipo | Preparación según la ruta elegida. Docker o app oficial; PDFs ficticios; almacenamiento persistente si usas servidor |

La edición de PDF, firma y redacción tienen efectos distintos: comprueba la salida de la operación elegida antes de sustituir un archivo

## Qué puedes hacer con él

Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs.

## Por qué destaca

Usos propuestos: Preparar un expediente de prueba; Separar y convertir documentos desde una interfaz.

## Cómo funciona

La edición de PDF, firma y redacción tienen efectos distintos: comprueba la salida de la operación elegida antes de sustituir un archivo

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o app oficial
- PDFs ficticios
- almacenamiento persistente si usas servidor

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
docker run -p 8080:8080 docker.stirlingpdf.com/stirlingtools/stirling-pdf
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/Stirling-Tools/Stirling-PDF/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Stirling-PDF para mi objetivo y necesito pasos guiados. Lee https://github.com/Stirling-Tools/Stirling-PDF/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Une dos PDFs de prueba y verifica orden, páginas y metadatos del resultado.

**Qué comprobar:** El archivo final se abre y contiene las páginas esperadas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar un expediente de prueba
- Separar y convertir documentos desde una interfaz

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar un expediente de prueba; Separar y convertir documentos desde una interfaz | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** La edición de PDF, firma y redacción tienen efectos distintos: comprueba la salida de la operación elegida antes de sustituir un archivo

## Stack y modelos

- **Stack:** Docker o app oficial; PDFs ficticios; almacenamiento persistente si usas servidor
- **Etiquetas:** `pdf` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [OCRmyPDF](ocrmypdf.md) | 35.3k | Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [pdfcraft](pdfcraft.md) | 9.8k | Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada. |

## Enlaces

- 🐙 GitHub: [Stirling-Tools/Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)
- 🌐 Web: <https://stirling.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Stirling-Tools/Stirling-PDF/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
