[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Credenciales y privacidad

# ⚙️ Keycloak

> IdP estándar de la industria (Red Hat/CNCF): OIDC, SAML, federación y admin amplio en Java.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 37.9k | Apache-2.0 | Java | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** hard

**Puntuación de calidad** 67/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

IdP Apache-2.0 de Keycloak.

## ¿Qué hace?

Gestiona identidades, realms y protocolos SSO.

## ¿Cómo lo hace?

Contenedor / Operator / distro.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [HashiCorp Vault](vault.md) | Vault puede federar/OIDC con Keycloak. | Keycloak IdP → Vault. |
| [Caddy](caddy.md) | Apps detrás de Caddy con OIDC. | Keycloak + Caddy. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 26.8.2 (2026-11-05) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/keycloak/keycloak#readme) · [2](https://www.keycloak.org)</sub>

## Ver similares

Grupo **Proveedores de identidad y SSO**: Keycloak ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **Keycloak** (esta ficha) ⭐ recomendado | 67 | Si buscas esto: idP estándar de la industria (Red Hat/CNCF): OIDC, SAML, federación y admin amplio en Java. |
| 2 | [authentik](authentik.md) | 64 | Si buscas esto: idP/SSO open source (MIT núcleo; enterprise/ bajo licencia distinta): OAuth2, SAML, LDAP y flujos visuales. |

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

[Instrucciones originales de instalación](https://github.com/keycloak/keycloak/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://www.keycloak.org)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Keycloak para mi objetivo y necesito pasos guiados. Lee https://github.com/keycloak/keycloak/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Arranca el contenedor oficial de Keycloak en modo dev y abre la admin console..

**Qué comprobar:** Realm de prueba creado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- OIDC para un cluster de apps propias
- federar un LDAP existente

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: OIDC para un cluster de apps propias; federar un LDAP existente | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada.

## Stack y modelos

- **Stack:** Java, pom.xml
- **Etiquetas:** `idp` `sso`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [authentik](authentik.md) | 26.4k | IdP/SSO open source (MIT núcleo; enterprise/ bajo licencia distinta): OAuth2, SAML, LDAP y flujos visuales. |

## Enlaces

- 🐙 GitHub: [keycloak/keycloak](https://github.com/keycloak/keycloak)
- 🌐 Web: <https://www.keycloak.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/keycloak/keycloak/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
