[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Libros, podcasts y bibliotecas personales

# ⚙️ Calibre-Web

> Aplicación web para explorar, leer y descargar libros electrónicos de una base de datos de Calibre, con usuarios, OPDS y lector en el navegador.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 18.6k | GPL-3.0 | Fluent | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 42/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Aplicación de código abierto (GPL-3.0) de janeczku, fork del proyecto library de mutschler. Madura y activa; requiere una base de datos de Calibre válida.

## ¿Qué hace?

Ofrece una interfaz web limpia para navegar, buscar, leer y descargar libros de una biblioteca de Calibre, con usuarios y permisos, estanterías, edición de metadatos, catálogo OPDS para lectores, sincronización con Kobo y envío a Kindle por correo.

## ¿Cómo lo hace?

Escrito en Python; se instala con `pip install calibreweb` (Python 3.7+) o con imágenes Docker de la comunidad. La conversión de formatos requiere tener Calibre instalado.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [syncthing](syncthing.md) | Syncthing mantiene sincronizada la carpeta de la biblioteca de Calibre entre el escritorio y el servidor de Calibre-Web (combinación por arquitectura). | Sincroniza la biblioteca con Syncthing; después apunta Calibre-Web a la copia del servidor. |
| [Pandoc](pandoc.md) | Pandoc convierte documentos propios a EPUB antes de añadirlos a la biblioteca (combinación por arquitectura). | Convierte con Pandoc; después añade el EPUB a Calibre. |
| [coolify](coolify.md) | Calibre-Web se despliega en contenedor con la biblioteca montada como volumen desde Coolify (combinación por arquitectura). | Coolify primero; después despliega una imagen de Calibre-Web y monta la biblioteca. |

**Notas:** Alternativas (elige una): kavita.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 0.6.27 (2026-08-08) · licencia declarada GPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/janeczku/calibre-web/blob/master/README.md)</sub>

## Ver similares

Grupo **Bibliotecas de libros y cómics**: Calibre-Web ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Kavita](kavita.md) ⭐ recomendado | 57 | Si buscas esto: servidor de lectura rápido y multiplataforma para manga, cómics y libros, con lector web, usuarios, OPDS y metadatos. |
| 2 | **Calibre-Web** (esta ficha) | 42 | Si buscas esto: aplicación web para explorar, leer y descargar libros electrónicos de una base de datos de Calibre, con usuarios, OPDS y lector en el navegador. |

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

1. Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.
2. Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.
3. Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas.

**Entrada documentada (consulta la sintaxis original):**

```
pip install calibreweb
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/janeczku/calibre-web/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Calibre-Web para mi objetivo y necesito pasos guiados. Lee https://github.com/janeczku/calibre-web/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install calibreweb`, apunta a una biblioteca de Calibre de prueba y abre un libro en el lector web..

**Qué comprobar:** El catálogo muestra los libros con portadas y el lector abre el EPUB..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- acceder a tu biblioteca de Calibre desde el móvil o el e-reader
- compartir una biblioteca de libros con la familia con cuentas separadas

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: acceder a tu biblioteca de Calibre desde el móvil o el e-reader; compartir una biblioteca de libros con la familia con cuentas separadas | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Fluent, pyproject.toml, requirements.txt
- **Etiquetas:** `self-hosted` `python` `server` `reading`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Kavita](kavita.md) | 12.1k | Servidor de lectura rápido y multiplataforma para manga, cómics y libros, con lector web, usuarios, OPDS y metadatos. |

## Enlaces

- 🐙 GitHub: [janeczku/calibre-web](https://github.com/janeczku/calibre-web)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/janeczku/calibre-web/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
