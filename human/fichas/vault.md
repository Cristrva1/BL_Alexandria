[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Credenciales y privacidad

# ⚙️ HashiCorp Vault

> Gestión de secretos y cifrado como servicio: dinámicos, KV, PKI. BSL 1.1 desde 1.15+ (IBM); no es OSI open source puro.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 36.5k | NOASSERTION | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** hard

> ⚠️ **Licencia y costes:** Vault no es open source según la definición OSI: desde la versión 1.15.0 usa Business Source License 1.1 (licenciante IBM). Permite uso en producción salvo ofrecerlo a terceros como servicio que compita con las versiones de pago; cada versión pasa a MPL-2.0 a los 4 años de publicarse. Alternativa con licencia abierta: OpenBao (openbao/openbao, fork MPL-2.0 de la Linux Foundation, ~9.000★), que aún no está en el catálogo.

## ¿Qué es?

Gestor de secretos de HashiCorp/IBM bajo Business Source License 1.1 desde la 1.15 (source-available, no OSI); cada versión pasa a MPL-2.0 a los 4 años. OpenBao es el fork MPL-2.0.

## ¿Qué hace?

Almacena, genera y audita secretos y certificados.

## ¿Cómo lo hace?

Binario oficial / Docker / Helm.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [SOPS](sops.md) | Sops cifra en Git; Vault centraliza runtime. | Sops en repo; Vault en runtime. |
| [age](age.md) | Age para ficheros simples; Vault para org. | Elige según escala. |
| [vaultwarden](vaultwarden.md) | Vaultwarden es passwords de usuario; Vault secretos de infra. | Complementarios. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Keycloak](keycloak.md)

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v2.2.2 (2026-11-12) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/hashicorp/vault#readme) · [2](https://developer.hashicorp.com/vault)</sub>

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

[Instrucciones originales de instalación](https://github.com/hashicorp/vault/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://www.vaultproject.io/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar HashiCorp Vault para mi objetivo y necesito pasos guiados. Lee https://github.com/hashicorp/vault/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca Vault en modo dev (`vault server -dev`) según docs y escribe un secreto KV..

**Qué comprobar:** Lees el secreto con la CLI..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- centralizar secretos de un entorno propio
- emitir credenciales dinámicas de DB de lab

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: centralizar secretos de un entorno propio; emitir credenciales dinámicas de DB de lab | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Business Source License 1.1 (IBM) desde Vault 1.15.0: uso productivo permitido salvo ofrecerlo como servicio competidor de pago. No es licencia OSI.

## Stack y modelos

- **Stack:** Go, Dockerfile, Makefile, go.mod
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [hashicorp/vault](https://github.com/hashicorp/vault)
- 🌐 Web: <https://developer.hashicorp.com/vault>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/hashicorp/vault/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
