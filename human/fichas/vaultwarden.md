[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Credenciales y privacidad

# ⚙️ vaultwarden

> Servidor no oficial compatible con clientes Bitwarden para alojar una bóveda de credenciales en infraestructura propia.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 70.7k | AGPL-3.0 | Rust | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Puntuación de calidad** 64/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Implementación alternativa no oficial del servidor de Bitwarden escrita en Rust, iniciada por @dani-garcia. Licencia AGPL-3.0. Es muy madura y popular para autoalojar (~71k estrellas, 1.37.5). No está afiliada a Bitwarden: los fallos se reportan a Vaultwarden, no al soporte de Bitwarden.

## ¿Qué hace?

Implementa la API de cliente de Bitwarden para que las apps oficiales funcionen contra tu propio servidor con pocos recursos. Incluye vault personal, organizaciones, adjuntos, Send, 2FA, emergency access, panel de administración y la web vault. Algunas funciones empresariales de Bitwarden no existen o se comportan distinto.

## ¿Cómo lo hace?

Es un servidor Rust que usa SQLite por defecto y admite MySQL/MariaDB o PostgreSQL. Se despliega normalmente con la imagen Docker `vaultwarden/server` detrás de un proxy inverso. Necesita HTTPS, porque los clientes y la web vault dependen de las API criptográficas del navegador, que solo funcionan en contextos seguros. La configuración se hace con variables de entorno, documentadas en la wiki.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Bitwarden Clients](bitwarden-clients.md) | Clientes oficiales (web, extensión, escritorio, CLI) que se conectan a Vaultwarden. | Despliega Vaultwarden con HTTPS y configura la URL del servidor en cada cliente. |
| [coolify](coolify.md) | Desplegar Vaultwarden como servicio de un clic con proxy y certificados (Coolify documenta el servicio Vaultwarden). | Instala Coolify, añade el servicio y asigna un dominio con HTTPS. |
| [AdGuardHome](adguardhome.md) | Resolver un nombre local para el vault en la red de casa con reescrituras DNS. (combinación por arquitectura) | Crea la reescritura DNS hacia tu proxy inverso y emite el certificado para ese nombre. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[authentik](authentik.md) · [HashiCorp Vault](vault.md)

**Notas:** Sin alternativas declaradas. Haz copias de seguridad de la base de datos y de la carpeta `data/`; no expongas `/admin` sin token.

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 1.37.5 (2026-11-01) · licencia declarada AGPL-3.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/dani-garcia/vaultwarden/blob/main/README.md) · [2](https://github.com/dani-garcia/vaultwarden/wiki) · [3](https://coolify.io/docs/services/vaultwarden)</sub>

## Ver similares

Grupo **Gestores de contraseñas**: vaultwarden ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **vaultwarden** (esta ficha) ⭐ recomendado | 64 | Si buscas esto: servidor no oficial compatible con clientes Bitwarden para alojar una bóveda de credenciales en infraestructura propia. |
| 2 | [KeePassXC](keepassxc.md) | 54 | Si buscas esto: gestor de contraseñas local multiplataforma (fork comunitario de KeePassX) con TOTP, SSH agent y navegador. |

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No requiere modelo; hosting, dominio, correo y copias son recursos propios |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Es un servidor alternativo no oficial; la bóveda web necesita HTTPS y contexto seguro; revisa las diferencias respecto al servidor Bitwarden |
| Coste | Sin pago a un modelo en la ruta básica. No requiere modelo; hosting, dominio, correo y copias son recursos propios |
| Equipo | Preparación según la ruta elegida. Docker o binario; dominio y HTTPS; volumen persistente; copias; bóveda ficticia |

Es un servidor alternativo no oficial; la bóveda web necesita HTTPS y contexto seguro; revisa las diferencias respecto al servidor Bitwarden

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Docker o binario
- dominio y HTTPS
- volumen persistente
- copias
- bóveda ficticia

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/dani-garcia/vaultwarden/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar vaultwarden para mi objetivo y necesito pasos guiados. Lee https://github.com/dani-garcia/vaultwarden/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Conecta un cliente Bitwarden a una instancia de prueba y guarda un registro ficticio.

**Qué comprobar:** Puedes reconocer la URL de servidor y recuperar el registro.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Estudiar alojamiento propio de una bóveda
- Evaluar compatibilidad con clientes Bitwarden

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Estudiar alojamiento propio de una bóveda; Evaluar compatibilidad con clientes Bitwarden | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Es un servidor alternativo no oficial; la bóveda web necesita HTTPS y contexto seguro; revisa las diferencias respecto al servidor Bitwarden

## Stack y modelos

- **Stack:** Docker o binario; dominio y HTTPS; volumen persistente; copias; bóveda ficticia
- **Etiquetas:** `privacidad` `server` `rust`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [KeePassXC](keepassxc.md) | 30k | Gestor de contraseñas local multiplataforma (fork comunitario de KeePassX) con TOTP, SSH agent y navegador. |

## Enlaces

- 🐙 GitHub: [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/dani-garcia/vaultwarden/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
