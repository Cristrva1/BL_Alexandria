[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Redes y transporte

# 🖥️ frp

> Proxy inverso rápido para exponer servidores locales detrás de NAT o cortafuegos a internet, con TCP, UDP, HTTP, HTTPS y modo P2P.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 111k | Apache-2.0 | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Proxy inverso de código abierto (Apache-2.0) creado por fatedier. Muy popular y maduro; el README anuncia una arquitectura v2 en desarrollo.

## ¿Qué hace?

Expone servicios locales a internet a través de un servidor con IP pública: TCP, UDP, HTTP y HTTPS con dominios, modo P2P, multiplexación, cifrado y compresión, autenticación, panel del servidor, métricas Prometheus y plugins.

## ¿Cómo lo hace?

Escrito en Go; se descargan los binarios frps (servidor) y frpc (cliente) y se configuran con TOML, YAML o JSON. Requiere un servidor con IP pública para frps.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Caddy](caddy.md) | Caddy puede poner HTTPS automático delante de los servicios HTTP expuestos con frp en el VPS (combinación por arquitectura). | frps en el VPS; después configura Caddy como proxy hacia el puerto de frp. |
| [Uptime Kuma](uptime-kuma.md) | Uptime Kuma vigila que los servicios publicados por el túnel sigan accesibles (combinación por arquitectura). | Publica el servicio con frp; después añade el monitor. |
| [Home Assistant](home-assistant.md) | frp permite acceder a una instancia de Home Assistant detrás de NAT sin abrir puertos del router (combinación por arquitectura). | Configura un proxy HTTP en frpc hacia Home Assistant; después protege el acceso con HTTPS. |

**Notas:** Alternativas cercanas: headscale o netbird si prefieres una red privada en lugar de publicar servicios.

Estado en GitHub: activo · último push 2026-11-10 · última versión publicada v0.72.0 (2026-11-04) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/fatedier/frp/blob/dev/README.md) · [2](https://gofrp.org/)</sub>

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

[Instrucciones originales de instalación](https://github.com/fatedier/frp/blob/dev/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar frp para mi objetivo y necesito pasos guiados. Lee https://github.com/fatedier/frp/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

En un VPS propio arranca frps y en tu equipo frpc con un proxy TCP para SSH, siguiendo el ejemplo del README..

**Qué comprobar:** Puedes conectar por SSH al equipo local a través del puerto del VPS..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- acceder por SSH a un equipo de casa detrás de NAT
- publicar temporalmente un servicio web local usando tu propio VPS

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: acceder por SSH a un equipo de casa detrás de NAT; publicar temporalmente un servicio web local usando tu propio VPS | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Exponer servicios internos a internet aumenta la superficie de ataque; protégelos con autenticación y cifrado.

## Stack y modelos

- **Stack:** Go, go.mod
- **Etiquetas:** `network` `go` `self-hosted` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [fatedier/frp](https://github.com/fatedier/frp)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/fatedier/frp/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
