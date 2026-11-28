[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Herramientas PDF

# 🖥️ Documenso

> Plataforma abierta de firma electrónica para enviar un PDF a firmantes por correo y obtener el documento sellado con su registro de auditoría.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.9k | AGPL-3.0 | TypeScript | 2026-11-27 |

**Ejecución** 🔀 híbrido · **Rol** 🖥️ app · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 56/100 · métricas del 2026-11-28 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia y costes:** El núcleo es AGPL-3.0: si modificas Documenso y lo ofreces a otras personas por red, debes publicar tu código. La carpeta packages/ee tiene una licencia comercial; sus funciones (SSO, firma CSC, marca blanca) requieren suscripción Enterprise en producción. La prueba local no las usa.

## ¿Qué es?

Alternativa de código abierto a DocuSign para gestionar firmas electrónicas de documentos PDF.

## ¿Qué hace?

Permite subir un PDF, colocar campos, enviar enlaces de firma, seguir su estado y descargar el documento firmado con la auditoría.

## ¿Cómo lo hace?

Combina una aplicación web en TypeScript con PostgreSQL y un servidor de correo. Al completarse las firmas, sella el PDF con un certificado .p12 propio o con un servicio de firma externo.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Stirling-PDF](stirling-pdf.md) | Une, comprime o convierte el PDF antes de subirlo para firma. | — |
| [paperless-ngx](paperless-ngx.md) | Archiva y busca los PDF firmados y sus registros de auditoría. | — |
| [activepieces](activepieces.md) | Recibe los webhooks de Documenso para avisar o archivar cuando un documento queda firmado. | — |

Estado en GitHub: activo · último push 2026-11-27 · última versión publicada v2.22.0 (2026-11-13) · licencia declarada AGPL-3.0 (consultado el 2026-11-27).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-27); no se instaló ni ejecutó. Fuentes: [1](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/README.md) · [2](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/LICENSE) · [3](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/packages/ee/LICENSE) · [4](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/.github/workflows/ci.yml) · [5](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/.github/workflows/e2e-tests.yml) · [6](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/.github/workflows/publish.yml) · [7](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/.env.example) · [8](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/docker/development/compose.yml) · [9](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/packages/signing/transports/local.ts) · [10](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/apps/docs/content/docs/self-hosting/deployment/docker-compose.mdx) · [11](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/apps/docs/content/docs/self-hosting/configuration/telemetry.mdx) · [12](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/apps/docs/content/docs/compliance/signature-levels.mdx) · [13](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/apps/docs/content/docs/policies/licenses.mdx) · [14](https://github.com/documenso/documenso/releases/tag/v2.22.0) · [15](https://github.com/documenso/documenso/actions/runs/43345864857) · [16](https://github.com/documenso/documenso/actions/runs/43345864965) · [17](https://github.com/documenso/documenso/actions/runs/43345916435) · [18](https://github.com/documenso/documenso/security/advisories/GHSA-3494-9j87-fj64) · [19](https://hub.docker.com/r/documenso/documenso) · [20](https://documenso.com/pricing)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | API de IA opcional. La detección con IA necesita una clave de Google Vertex AI con facturación activa. La imagen Docker envía telemetría anónima salvo que definas DOCUMENSO_DISABLE_TELEMETRY=true. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | Modelo local no documentado. Firmar y sellar no usa modelos. La detección automática de destinatarios y campos es opcional y solo documenta Google Vertex AI; no hay ruta con modelos locales. |
| Coste | Sin pago a un modelo en la ruta básica. La edición Community autoalojada es gratuita bajo AGPL-3.0. La nube de Documenso ofrece un plan gratuito con 5 documentos al mes y planes de pago (consultado el 27 nov 2026). Enterprise y Vertex AI son de pago. |
| Equipo | Preparación según la ruta elegida. Equipo con Docker, Node.js 24 o posterior y al menos 2 GB de RAM libres. La ruta de desarrollo levanta cuatro contenedores. |

No requiere suscripciones de IA. El AGENTS.md del repositorio orienta a agentes que contribuyen al código; no es una integración para usar la aplicación.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.

1. Prepara un equipo con Git, Docker y Docker Compose, Node.js 24 o posterior y npm 11.17 o posterior. La ruta de desarrollo levanta en contenedores PostgreSQL, Inbucket (un buzón de correo local), Redis y Gotenberg.
2. Clona el repositorio en la etiqueta v2.22.0, copia .env.example a .env y ejecuta npm run d. Abre http://localhost:3000. Los correos salientes se leen en http://localhost:9000.
3. Haz la prueba con un PDF propio y un firmante ficticio. Comprueba el estado completado y la firma del PDF descargado. Al terminar, detén los contenedores.

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/documenso/documenso/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/documenso/documenso/releases/tag/v2.22.0)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Documenso para mi objetivo y necesito pasos guiados. Lee https://github.com/documenso/documenso/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En la instalación local de desarrollo, crea una cuenta con un correo ficticio y confírmala desde http://localhost:9000. Sube un PDF propio de una página, añade como firmante a «Firmante Ficticio» <firmante@example.com> con un campo de firma y envíalo..

**Qué comprobar:** En http://localhost:9000 abre el correo del firmante y firma. El documento pasa a completado y el PDF descargado muestra una firma digital hecha con el certificado de ejemplo..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Recoger la firma de un acuerdo de prueba entre dos personas de tu equipo
- Preparar una plantilla con campos de firma y fecha para reutilizarla

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Recoger la firma de un acuerdo de prueba entre dos personas de tu equipo; Preparar una plantilla con campos de firma y fecha para reutilizarla | solo necesitas firmar algún PDF suelto y no quieres mantener un servidor con base de datos y correo. |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Usa la v2.19.0 o posterior; esta ficha usa la v2.22.0. El aviso alto GHSA-3494-9j87-fj64 permite leer nombres y correos de usuarios sin iniciar sesión hasta la 2.17.0. La instalación de desarrollo crea cuentas de ejemplo con contraseñas públicas y firma con un certificado de ejemplo: no la expongas a internet ni firmes documentos reales con ella. Las firmas son electrónicas simples; su validez depende del país y del tipo de documento.

## Stack y modelos

- **Stack:** TypeScript, package.json
- **Etiquetas:** `firma electrónica` `pdf` `autoalojado` `docker` `auditoría`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [docuseal](docuseal.md) | 19.1k | Aplicación para preparar formularios y gestionar la firma electrónica de documentos, con opciones de despliegue propio. |

## Enlaces

- 🐙 GitHub: [documenso/documenso](https://github.com/documenso/documenso)
- 🌐 Web: <https://documenso.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-27. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/README.md)
- [Fuente 2](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/.env.example)
- [Fuente 3](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/docker/development/compose.yml)
- [Fuente 4](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/apps/docs/content/docs/self-hosting/deployment/docker-compose.mdx)
- [Fuente 5](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/apps/docs/content/docs/self-hosting/configuration/advanced/ai-features.mdx)
- [Fuente 6](https://github.com/documenso/documenso/blob/d32d049165db230820465b4f566061ba8fa27012/apps/docs/content/docs/self-hosting/configuration/telemetry.mdx)
- [Fuente 7](https://documenso.com/pricing)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
