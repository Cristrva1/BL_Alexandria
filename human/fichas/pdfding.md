[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Herramientas PDF

# 📑 PdfDing

> Gestor, visor y editor de PDF autoalojado (AGPL-3.0) con colecciones, etiquetas, anotaciones y progreso de lectura; se desarrolla en Codeberg.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.8k | AGPL-3.0 | Python | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

## ¿Qué es?

Gestor, visor y editor de PDF autoalojado (AGPL-3.0), creado por mrmn y financiado por el NGI0 Commons Fund de NLnet. Su repositorio canónico es Codeberg (codeberg.org/mrmn/PdfDing), donde sigue activo con la v1.15.0 del 1 de noviembre de 2026; el repositorio de GitHub (mrmn2/PdfDing) está archivado y solo conserva la historia hasta agosto de 2026. Es un proyecto maduro mantenido principalmente por una persona, que se sostiene con donaciones.

## ¿Qué hace?

Permite leer PDF en el navegador desde varios dispositivos y recuerda la posición para continuar donde se dejó. Organiza la colección con espacios de trabajo, colecciones, etiquetas multinivel, favoritos, archivo y acciones masivas, y muestra barras de progreso de lectura. Permite editar PDF añadiendo texto, resaltados, dibujos y firmas reutilizables, y gestionar o exportar resaltados y comentarios en secciones propias. Comparte colecciones o PDF con público externo mediante enlace o código QR con control de acceso opcional. Incluye modo oscuro, modo de color invertido, SSO por OIDC y 2FA (TOTP y WebAuthn). No incluye OCR ni funciones de IA.

## ¿Cómo lo hace?

Aplicación web en Python con Django (según su pyproject.toml en Codeberg, Python ≥3.12), distribuida como imagen Docker `mrmn/pdfding` para amd64 y arm64. La guía oficial la arranca con `docker run` en el puerto 8000, con volúmenes para la base de datos SQLite y los archivos, y variables como `HOST_NAME` y `SECRET_KEY`. También documenta Docker Compose, Podman y Helm, y existe hosting gestionado en PikaPods (~2,70 USD/mes). Las opciones de configuración (incluida la base de datos alternativa) están en docs.pdfding.com/configuration [DATO NO VERIFICADO: soporte de PostgreSQL no confirmado en las páginas revisadas]. Las instrucciones antiguas que apuntan a GitHub ya no reciben cambios.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OCRmyPDF](ocrmypdf.md) | Aplicar OCR a escaneados antes de subirlos para poder buscar y resaltar texto (combinación por arquitectura). | Procesa los archivos antes de importarlos. |
| [paperless-ngx](paperless-ngx.md) | Paperless archiva y clasifica; PdfDing sirve para leer y anotar (combinación por arquitectura). | Decide qué sistema guarda el original para no duplicar. |
| [coolify](coolify.md) | Desplegar el contenedor con dominio y HTTPS (combinación por arquitectura). | Usa la imagen y la documentación de Codeberg. |

**Notas:** Fuente canónica: Codeberg. El repositorio de GitHub está archivado y solo se conserva como identidad de la estrella en el catálogo (`gh`, `github_id`); las estrellas mostradas (~1,8k) son las de GitHub, Codeberg tiene muy pocas. Se retiraron markitdown, ppt-master y reveal.js por falta de relación. Licencia AGPL-3.0: si modificas el código y lo ofreces como servicio, debes publicar los cambios.

Estado en Codeberg: activo · última actividad 2026-11-01 · última versión publicada v1.15.0 (2026-11-01) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

Copia antigua en GitHub: ⚠️ archivado (solo lectura) · último push 2026-08-29 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://codeberg.org/mrmn/PdfDing/src/branch/master/README.md) · [2](https://docs.pdfding.com/getting_started/docker/) · [3](https://codeberg.org/mrmn/PdfDing/src/branch/master/pyproject.toml)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El gestor básico no requiere IA; servidor y almacenamiento son recursos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El desarrollo se ha trasladado a Codeberg; sigue el enlace canónico y la documentación antes de usar instrucciones GitHub antiguas |
| Coste | Sin pago a un modelo en la ruta básica. El gestor básico no requiere IA; servidor y almacenamiento son recursos propios |
| Equipo | Preparación según la ruta elegida. Docker o entorno de la guía; volumen para documentos; cuenta de prueba |

El desarrollo se ha trasladado a Codeberg; sigue el enlace canónico y la documentación antes de usar instrucciones GitHub antiguas

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o entorno de la guía
- volumen para documentos
- cuenta de prueba

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente, úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
docker run --name pdfding \
    -p 8000:8000 \
    -v sqlite_data:/home/nonroot/pdfding/db -v media:/home/nonroot/pdfding/media \
    -e HOST_NAME=127.0.0.1 -e SECRET_KEY=some_secret \
    -e CSRF_COOKIE_SECURE=FALSE -e SESSION_COOKIE_SECURE=FALSE \
    -d \
    mrmn/pdfding:latest
```

Comando copiado literalmente de la documentación oficial enlazada desde el README (sección «Docker»); revisado el 2026-11-16, no ejecutado por Alexandría. Adapta rutas, puertos y variables a tu entorno y sigue el resto de la guía original.

[Instrucciones originales de instalación](https://docs.pdfding.com/getting_started/docker/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar PdfDing para mi objetivo y necesito pasos guiados. Lee https://docs.pdfding.com/getting_started/docker/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sube un PDF ficticio, añade una etiqueta y continúa su lectura en otra sesión.

**Qué comprobar:** Puedes encontrar el documento y su progreso guardado.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Organizar una colección de PDFs
- Consultar documentos desde varios dispositivos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Organizar una colección de PDFs; Consultar documentos desde varios dispositivos | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El repositorio de GitHub está archivado desde que el proyecto se mudó a Codeberg; usa Codeberg y docs.pdfding.com como referencia. Sin OCR ni IA integrados.

## Stack y modelos

- **Stack:** Docker o entorno de la guía; volumen para documentos; cuenta de prueba
- **Etiquetas:** `pdf` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🔗 Codeberg: [mrmn/PdfDing](https://codeberg.org/mrmn/PdfDing)
- 🌐 Web: <https://www.pdfding.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://codeberg.org/mrmn/PdfDing/src/branch/master/README.md)
- [Fuente 2](https://docs.pdfding.com/getting_started/docker/)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
