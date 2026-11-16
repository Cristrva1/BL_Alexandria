[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Libros, podcasts y bibliotecas personales

# ⚙️ Kavita

> Servidor de lectura rápido y multiplataforma para manga, cómics y libros, con lector web, usuarios, OPDS y metadatos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 12.1k | GPL-3.0 | C# | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## ¿Qué es?

Servidor de lectura de código abierto (GPL-3.0) del proyecto Kareadita, con funciones adicionales (Kavita+) para patrocinadores. Activo y multiplataforma.

## ¿Qué hace?

Gestiona y sirve manga, cómics, novelas y libros (CBZ, CBR, PDF, EPUB) con lectores web, metadatos ComicInfo, colecciones, listas de lectura, anotaciones, roles de usuario, OPDS y seguimiento de progreso.

## ¿Cómo lo hace?

Escrito en C# con .NET; se instala con Docker (imagen jvmilazz0/kavita) o binarios para Windows, Linux y macOS. Escanea carpetas organizadas según su guía.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [syncthing](syncthing.md) | Syncthing copia la colección de lectura al servidor donde Kavita la escanea (combinación por arquitectura). | Sincroniza la carpeta; después añádela como biblioteca en Kavita. |
| [audiobookshelf](audiobookshelf.md) | Audiobookshelf cubre audiolibros y pódcasts mientras Kavita sirve cómics y libros (combinación por arquitectura). | Despliega ambos con bibliotecas separadas. |
| [coolify](coolify.md) | La imagen Docker de Kavita se despliega desde Coolify con la biblioteca como volumen (combinación por arquitectura). | Coolify primero; después crea el servicio y monta las carpetas. |

**Notas:** Alternativas (elige una): calibre-web.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada v0.9.1.4 (2026-09-02) · licencia declarada GPL-3.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/Kareadita/Kavita/blob/develop/README.md) · [2](https://wiki.kavitareader.com/)</sub>

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/Kareadita/Kavita/blob/develop/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Kavita para mi objetivo y necesito pasos guiados. Lee https://github.com/Kareadita/Kavita/blob/develop/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega Kavita con Docker, añade una carpeta con un cómic o EPUB y ábrelo en el lector web..

**Qué comprobar:** El archivo aparece en la biblioteca con su portada y se puede leer en el navegador..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- leer tu colección de cómics o manga desde cualquier dispositivo
- compartir una biblioteca de lectura con amigos o familia

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: leer tu colección de cómics o manga desde cualquier dispositivo; compartir una biblioteca de lectura con amigos o familia | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** C#, Dockerfile
- **Etiquetas:** `self-hosted` `csharp` `server` `reading`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Calibre-Web](calibre-web.md) | 18.6k | Aplicación web para explorar, leer y descargar libros electrónicos de una base de datos de Calibre, con usuarios, OPDS y lector en el navegador. |

## Enlaces

- 🐙 GitHub: [Kareadita/Kavita](https://github.com/Kareadita/Kavita)
- 🌐 Web: <http://www.kavitareader.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/Kareadita/Kavita/blob/develop/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
