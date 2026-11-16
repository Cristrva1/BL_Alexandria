[🏠 Inicio](../README.md) › [🗂️ Organizar notas, archivos y servicios personales](../categorias/15-notas-archivos-y-servicios-personales.md) › Credenciales y privacidad

# 🖥️ Bitwarden Clients

> Clientes oficiales de Bitwarden para gestionar credenciales y utilizar funciones como compartir información con Send.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 14.2k | NOASSERTION | TypeScript | 2026-11-14 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla; app o instalador listo para usar

**Puntuación de calidad** 61/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Monorepo de los clientes oficiales de Bitwarden: web vault, extensión de navegador, escritorio y CLI. Lo mantiene Bitwarden, Inc. Es muy maduro (~14k estrellas, desktop-v2026.10.4). GitHub muestra licencia NOASSERTION porque el repo combina GPL-3.0 (por defecto) con la Bitwarden License v1.0 para el código del directorio `bitwarden_license/`.

## ¿Qué hace?

Reúne todas las aplicaciones cliente de Bitwarden salvo las móviles, que viven en `bitwarden/ios` y `bitwarden/android`. Permite guardar, autocompletar y compartir contraseñas, notas, tarjetas, identidades y passkeys con cifrado de extremo a extremo. La CLI (`bw`) da acceso al vault desde scripts.

## ¿Cómo lo hace?

Es TypeScript con Angular para la web y la extensión, y Electron para el escritorio. Los usuarios instalan las versiones publicadas (tiendas de extensiones, instaladores, `npm install -g @bitwarden/cli`), no este repo. Para desarrollar se necesita Node.js y npm, y la documentación de contribución de Bitwarden. Los clientes funcionan contra Bitwarden Cloud, contra un servidor Bitwarden autoalojado o contra servidores compatibles como Vaultwarden.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [vaultwarden](vaultwarden.md) | Usar los clientes oficiales con un servidor autoalojado ligero; Vaultwarden se declara compatible con los clientes oficiales. | Despliega Vaultwarden con HTTPS y, en el cliente, cambia la URL del servidor a la tuya. |
| [activepieces](activepieces.md) | Gestionar colecciones, grupos y miembros de una organización Bitwarden llamando a su API pública de organizaciones con la pieza HTTP (no da acceso a los elementos del vault). (combinación por arquitectura) | Crea la clave de API de la organización y guárdala como secreto en Activepieces. |
| [Claude Code](claude-code.md) | Inyectar secretos en scripts con la CLI `bw` en lugar de escribirlos en archivos. (combinación por arquitectura) (no des al agente la sesión desbloqueada del vault completo) | Instala `@bitwarden/cli` y usa una cuenta o colección limitada para la automatización. |

**Notas:** Sin alternativas declaradas. Revisa la licencia antes de reutilizar código de `bitwarden_license/`.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada desktop-v2026.10.4 (2026-11-05) · licencia declarada no estándar (NOASSERTION) (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/bitwarden/clients/blob/main/README.md) · [2](https://github.com/bitwarden/clients/blob/main/LICENSE.txt) · [3](https://bitwarden.com/help/self-host-an-organization/)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No usa LLM; planes y funciones de servidor tienen condiciones comerciales propias |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Este repositorio contiene clientes y no todo el servidor; las apps móviles viven en repositorios separados |
| Coste | El coste depende del proveedor o la ruta. No usa LLM; planes y funciones de servidor tienen condiciones comerciales propias |
| Equipo | Preparación según la ruta elegida. Cliente oficial de tu sistema; cuenta y servidor elegido; bóveda de prueba |

Este repositorio contiene clientes y no todo el servidor; las apps móviles viven en repositorios separados

## Cómo empezar

Aplicación con interfaz. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Cliente oficial de tu sistema
- cuenta y servidor elegido
- bóveda de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://bitwarden.com/download/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Bitwarden Clients para mi objetivo y necesito pasos guiados. Lee https://bitwarden.com/download/. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Guarda una credencial ficticia y comprueba que puedes recuperarla y sincronizarla.

**Qué comprobar:** El registro aparece solo en la cuenta y bóveda esperadas.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Gestionar credenciales desde extensión y escritorio
- Estudiar un flujo Send con contenido ficticio

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Gestionar credenciales desde extensión y escritorio; Estudiar un flujo Send con contenido ficticio | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Este repositorio contiene clientes y no todo el servidor; las apps móviles viven en repositorios separados

## Stack y modelos

- **Stack:** Cliente oficial de tu sistema; cuenta y servidor elegido; bóveda de prueba
- **Etiquetas:** `privacidad` `app` `typescript`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [bitwarden/clients](https://github.com/bitwarden/clients)
- 🌐 Web: <https://bitwarden.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/bitwarden/clients/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
