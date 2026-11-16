[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Credenciales y privacidad

# ⚙️ authentik

> IdP/SSO open source (MIT núcleo; enterprise/ bajo licencia distinta): OAuth2, SAML, LDAP y flujos visuales.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 26.4k | NOASSERTION | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** hard

**Nivel:** 3 Avanzado — proveedor de identidad con Docker Compose y flujos a configurar · corregido a mano

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Identity provider (MIT + enterprise/ propietaria).

## ¿Qué hace?

Autentica y autoriza usuarios hacia apps.

## ¿Cómo lo hace?

Docker/Helm oficiales.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vaultwarden](vaultwarden.md) | Credenciales de usuario + IdP. | authentik SSO; Vaultwarden passwords. |
| [Caddy](caddy.md) | Caddy protege rutas con forward-auth. | authentik + Caddy. |

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada version/2026.8.5 (2026-10-21) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/goauthentik/authentik#readme) · [2](https://docs.goauthentik.io)</sub>

## Ver similares

Grupo **Proveedores de identidad y SSO**: authentik ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Keycloak](keycloak.md) ⭐ recomendado | 67 | Si buscas esto: idP estándar de la industria (Red Hat/CNCF): OIDC, SAML, federación y admin amplio en Java. |
| 2 | **authentik** (esta ficha) | 64 | Si buscas esto: idP/SSO open source (MIT núcleo; enterprise/ bajo licencia distinta): OAuth2, SAML, LDAP y flujos visuales. |

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

[Instrucciones originales de instalación](https://github.com/goauthentik/authentik/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://goauthentik.io)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar authentik para mi objetivo y necesito pasos guiados. Lee https://github.com/goauthentik/authentik/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Despliega con el Compose de docs.goauthentik.io y crea una aplicación de prueba..

**Qué comprobar:** Login SSO funcionando..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- SSO delante de apps autoalojadas
- MFA centralizado para el lab

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: SSO delante de apps autoalojadas; MFA centralizado para el lab | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Open-core: authentik/enterprise/ con licencia distinta. Núcleo MIT.

## Stack y modelos

- **Stack:** Python, Cargo.toml, Makefile, go.mod, package.json, pyproject.toml
- **Etiquetas:** `idp` `sso`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Keycloak](keycloak.md) | 37.9k | IdP estándar de la industria (Red Hat/CNCF): OIDC, SAML, federación y admin amplio en Java. |

## Enlaces

- 🐙 GitHub: [goauthentik/authentik](https://github.com/goauthentik/authentik)
- 🌐 Web: <https://goauthentik.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/goauthentik/authentik/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
