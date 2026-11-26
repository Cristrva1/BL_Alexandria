[🏠 Inicio](../README.md) › [📄 PDF, OCR y procesamiento de documentos](../categorias/13-documentos-presentaciones.md) › Herramientas PDF

# ⚙️ docuseal

> Aplicación para preparar formularios y gestionar la firma electrónica de documentos, con opciones de despliegue propio.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19.1k | AGPL-3.0 | Ruby | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

**Puntuación de calidad** 60/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Plataforma de código abierto (AGPL-3.0) para rellenar y firmar documentos, de DocuSeal. Activa (3.3.6), con nube de pago y funciones Pro.

## ¿Qué hace?

Crea formularios PDF con un editor visual de 12 tipos de campo, admite varios firmantes por documento, envía correos por SMTP, aplica firma electrónica automática y verifica firmas. Incluye gestión de usuarios, firma optimizada para móvil, 7 idiomas de interfaz (firma en 14), API y webhooks, y apps para iOS y Android. Las funciones Pro añaden marca propia, roles, recordatorios, verificación por SMS, campos condicionales, envíos masivos, SSO/SAML y formularios embebidos.

## ¿Cómo lo hace?

Aplicación Ruby on Rails que se despliega con `docker run -p 3000:3000` o Docker Compose; usa SQLite por defecto o PostgreSQL/MySQL, y guarda archivos en disco, AWS S3, Google Storage o Azure.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [activepieces](activepieces.md) | Disparar flujos al completar una firma o crear envíos desde otros sistemas con su API y webhooks (combinación por arquitectura). | Crea la clave de API y el webhook en DocuSeal antes del flujo. |
| [twenty-main](twenty-main.md) | Registrar contratos firmados en las oportunidades del CRM (combinación por arquitectura). | Usa un flujo intermedio con el webhook de DocuSeal. |
| [Stirling-PDF](stirling-pdf.md) | Preparar o convertir documentos antes de enviarlos a firmar (combinación por arquitectura). | Independientes; cambia puertos si coinciden. |
| [pdfcraft](pdfcraft.md) | Combinación recíproca: pdfcraft lo enlaza como «Preparar el PDF (unir, comprimir) antes de enviarlo a firmar (combinación por arquitectura)». | Orden indicado desde pdfcraft: Independientes. |

**Notas:** Para producción usa PostgreSQL en lugar de SQLite y configura SMTP con SPF/DKIM.

Estado en GitHub: activo · último push 2026-11-09 · última versión publicada 3.3.6 (2026-11-09) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/docusealco/docuseal/blob/master/README.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. El núcleo AGPL añade términos; Pro, Cloud y servicios de correo tienen condiciones propias; no exige LLM |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. El ejemplo es para revisar la herramienta con datos de prueba; configura dominio, persistencia y permisos antes de un uso real |
| Coste | El coste depende del proveedor o la ruta. El núcleo AGPL añade términos; Pro, Cloud y servicios de correo tienen condiciones propias; no exige LLM |
| Equipo | Preparación según la ruta elegida. Docker; dominio y correo solo para despliegue real; documento y destinatario ficticios |

El ejemplo es para revisar la herramienta con datos de prueba; configura dominio, persistencia y permisos antes de un uso real

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker
- dominio y correo solo para despliegue real
- documento y destinatario ficticios

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (sh):**

```
docker run --name docuseal -p 3000:3000 -v.:/data docuseal/docuseal
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/docusealco/docuseal/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar docuseal para mi objetivo y necesito pasos guiados. Lee https://github.com/docusealco/docuseal/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una plantilla de prueba con campos de texto y firma y completa una vista de ensayo.

**Qué comprobar:** Puedes revisar el documento resultante y la ubicación de los campos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Preparar formularios internos de prueba
- Evaluar un flujo de firma documental

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Preparar formularios internos de prueba; Evaluar un flujo de firma documental | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** El ejemplo es para revisar la herramienta con datos de prueba; configura dominio, persistencia y permisos antes de un uso real

## Stack y modelos

- **Stack:** Docker; dominio y correo solo para despliegue real; documento y destinatario ficticios
- **Etiquetas:** `pdf` `server` `ruby`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [docusealco/docuseal](https://github.com/docusealco/docuseal)
- 🌐 Web: <https://www.docuseal.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/docusealco/docuseal/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
