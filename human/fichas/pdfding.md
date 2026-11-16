[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Herramientas PDF

# 📑 PdfDing

> Gestor y visor de PDFs auto-hospedado, ligero, con etiquetas y progreso de lectura.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 1.8k | — | — | 2026-08-23 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Gestor, visor y editor de PDF autoalojado de mrmn2. **El repositorio de GitHub está archivado**: el proyecto se gestiona ahora en Codeberg (codeberg.org/mrmn/PdfDing); último push en GitHub en agosto de 2026.

## ¿Qué hace?

Permite leer PDF en el navegador en varios dispositivos recordando la posición, organizar la colección con espacios de trabajo, colecciones, etiquetas multinivel, favoritos y archivo, editar con texto, resaltados, dibujos y firmas, exportar resaltados y comentarios, compartir por enlace o QR con control de acceso y tomar notas en Markdown. Incluye SSO por OIDC y 2FA (TOTP y WebAuthn).

## ¿Cómo lo hace?

Aplicación web autoalojada pensada para ser mínima y rápida, desplegada con Docker, Docker Compose o Helm, o en PikaPods [DATO NO VERIFICADO: stack y base de datos, no descritos en el README].

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OCRmyPDF](ocrmypdf.md) | Aplicar OCR a escaneados antes de subirlos para poder buscar y resaltar texto (combinación por arquitectura). | Procesa los archivos antes de importarlos. |
| [paperless-ngx](paperless-ngx.md) | Paperless archiva y clasifica; PdfDing sirve para leer y anotar (combinación por arquitectura). | Decide qué sistema guarda el original para no duplicar. |
| [coolify](coolify.md) | Desplegar el contenedor con dominio y HTTPS (combinación por arquitectura). | Usa la imagen y la documentación de Codeberg. |

**Notas:** Actualiza la URL del catálogo a Codeberg. Se retiraron markitdown, ppt-master y reveal.js por falta de relación.

Estado en GitHub: ⚠️ archivado (solo lectura) · último push 2026-08-29 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/mrmn2/PdfDing/blob/master/README.md)</sub>

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

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

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

**Limitaciones:** El repositorio de GitHub está archivado desde que el proyecto se mudó a Codeberg; usa Codeberg y docs.pdfding.com como referencia

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
