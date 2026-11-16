[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Nube, contenedores e IaC

# 🖥️ Cosign

> Firma y verificación de contenedores y artefactos (Sigstore): clave o keyless con OIDC.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 6.4k | Apache-2.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Herramienta Sigstore para supply-chain signing.

## ¿Qué hace?

Firma/verifica artefactos OCI.

## ¿Cómo lo hace?

Release / go install.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Trivy](trivy.md) | Trivy escanea; Cosign firma. | Scan → sign. |
| [Syft](syft.md) | SBOM + firma del artefacto. | syft → cosign. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.1.4 (2026-10-20) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/sigstore/cosign#readme)</sub>

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/sigstore/cosign/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Cosign para mi objetivo y necesito pasos guiados. Lee https://github.com/sigstore/cosign/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala Cosign (release o `go install`) y firma una imagen de lab..

**Qué comprobar:** La verificación confirma la firma..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- firmar una imagen interna
- verificar firmas antes del deploy

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: firmar una imagen interna; verificar firmas antes del deploy | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Go, Dockerfile, Makefile, go.mod
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [sigstore/cosign](https://github.com/sigstore/cosign)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/sigstore/cosign/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
