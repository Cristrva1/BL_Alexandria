[🏠 Inicio](../README.md) › [🕸️ Infraestructura, despliegue y herramientas para agentes](../categorias/22-infraestructura-despliegue.md) › Redes y transporte

# ⚙️ Pangolin Community Edition

> Controla qué personas pueden entrar a aplicaciones propias mediante un proxy y reglas de acceso administradas por tu equipo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 23.9k | NOASSERTION | TypeScript | 2026-11-22 |

**Ejecución** 🔀 híbrido · **Rol** ⚙️ plataforma · **Setup** 🔴 pesado

**Nivel:** 3 Avanzado — preparación pesada

> ⚠️ **Licencia y costes:** Alcance de la recomendación: Community Edition (AGPL-3.0). El repositorio incluye archivos bajo la Fossorial Commercial License; no se extiende a ellos la licencia comunitaria.

## ¿Qué es?

Una plataforma para dar acceso identificado a aplicaciones y servicios propios.

## ¿Qué hace?

Controla qué personas pueden entrar a aplicaciones propias mediante un proxy y reglas de acceso administradas por tu equipo.

## ¿Cómo lo hace?

El servidor recibe la conexión, comprueba quién puede usar el recurso y lo redirige hacia la aplicación configurada.

Estado en GitHub: activo · último push 2026-11-20 · última versión publicada 1.27.1 (2026-11-20) · licencia declarada NOASSERTION (consultado el 2026-11-22).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-22); no se instaló ni ejecutó. Fuentes: [1](https://github.com/fosrl/pangolin/blob/0e011f57f751c77a906eba7fde3cd8765290ab01/README.md) · [2](https://docs.pangolin.net/self-host/quick-install) · [3](https://github.com/fosrl/pangolin/blob/0e011f57f751c77a906eba7fde3cd8765290ab01/LICENSE) · [4](https://github.com/fosrl/pangolin/blob/0e011f57f751c77a906eba7fde3cd8765290ab01/SECURITY.md) · [5](https://github.com/fosrl/pangolin/blob/0e011f57f751c77a906eba7fde3cd8765290ab01/install/config/docker-compose.yml) · [6](https://docs.pangolin.net/self-host/how-to-update) · [7](https://github.com/fosrl/pangolin/releases/tag/1.27.1) · [8](https://github.com/fosrl/pangolin/blob/main/LICENSE) · [9](https://github.com/fosrl/pangolin/security/advisories/GHSA-3cxv-w5ph-7p6h) · [10](https://github.com/fosrl/pangolin/security/advisories/GHSA-9784-q2hc-2qqq) · [11](https://github.com/fosrl/pangolin/security/advisories/GHSA-v6q2-c45v-8vx8) · [12](https://github.com/fosrl/pangolin/security/advisories/GHSA-hpcv-689w-jrg3) · [13](https://github.com/fosrl/pangolin/security/advisories/GHSA-w92q-9g55-f4r2) · [14](https://github.com/fosrl/pangolin/security/advisories/GHSA-fhv5-xx8r-wxfg) · [15](https://github.com/fosrl/pangolin/security/advisories/GHSA-3cfx-v2f2-3mqq) · [16](https://github.com/fosrl/pangolin/security/advisories/GHSA-9vcq-r7wr-9r3r) · [17](https://github.com/fosrl/pangolin/security/advisories/GHSA-5ph5-x9xv-86fv) · [18](https://github.com/fosrl/pangolin/security/advisories/GHSA-5772-vhpw-ppr8) · [19](https://github.com/fosrl/pangolin/security/advisories/GHSA-m664-jx49-xhw7) · [20](https://github.com/fosrl/pangolin/security/advisories/GHSA-5h3v-3645-78xj) · [21](https://github.com/fosrl/pangolin/security/advisories/GHSA-9xxh-cx3p-fx3m) · [22](https://github.com/fosrl/pangolin/security/advisories/GHSA-3pr6-pcvv-9jrp) · [23](https://github.com/fosrl/pangolin/security/advisories/GHSA-j32m-3vr4-9ghw)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La primera prueba no llama a un modelo de IA. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La función descrita no depende de un modelo de IA. |
| Coste | El coste depende del proveedor o la ruta. Community Edition se puede autoalojar sin pagar una licencia comercial por esa edición; VPS, dominio y operación pueden costar. Cloud y Enterprise tienen condiciones aparte. El proxy de prueba no usa IA. |
| Equipo | Preparación según la ruta elegida. Servidor Linux de prueba, Docker, configuración de DNS y TLS según la guía, y una cuenta inicial de administración. |

La ruta descrita no utiliza una suscripción de IA.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Servidor Linux de prueba, Docker, configuración de DNS y TLS según la guía, y una cuenta inicial de administración.

1. Sigue la guía para Community Edition en un servidor de prueba y confirma que la imagen del servidor corresponde al release 1.27.1 o posterior.
2. Configura un recurso web de ejemplo con autenticación; prueba una cuenta autorizada y otra sin acceso.
3. Comprueba el resultado: la cuenta autorizada abre la web de ejemplo y a la otra se le deniega el acceso.

Consulta la guía vinculada y la versión revisada. No se ejecutó el proyecto.

[Instrucciones originales de instalación](https://docs.pangolin.net/self-host/quick-install)

[Abrir la web o descarga indicada por el autor](https://docs.pangolin.net/self-host/quick-install)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Pangolin Community Edition para mi objetivo y necesito pasos guiados. Lee https://docs.pangolin.net/self-host/quick-install. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Configura un recurso web de ejemplo con autenticación; prueba una cuenta autorizada y otra sin acceso..

**Qué comprobar:** La cuenta autorizada abre la web de ejemplo y a la otra se le deniega el acceso..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Comprobar el acceso de una cuenta de prueba a una web ficticia.
- Comparar qué ven dos cuentas con roles distintos.

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Comprobar el acceso de una cuenta de prueba a una web ficticia.; Comparar qué ven dos cuentas con roles distintos. | no quieres mantener un servidor, sus copias de seguridad y sus actualizaciones |

**Limitaciones:** Los 15 avisos publicados del servidor indican correcciones hasta 1.27.0; el tag 1.27.1 desciende de esa versión. Si activas Gerbil, su contenedor solicita NET_ADMIN. Mantén el token de instalación privado y revisa por separado las versiones de Gerbil, Traefik y clientes. La revisión no acredita ausencia de fallos ni una instalación probada.

## Stack y modelos

- **Stack:** TypeScript, Dockerfile, Makefile, compose.yaml, package.json
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Enlaces

- 🐙 GitHub: [fosrl/pangolin](https://github.com/fosrl/pangolin)
- 🌐 Web: <https://pangolin.net>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-22. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/fosrl/pangolin/blob/0e011f57f751c77a906eba7fde3cd8765290ab01/README.md)
- [Fuente 2](https://docs.pangolin.net/self-host/quick-install)
- [Fuente 3](https://github.com/fosrl/pangolin/blob/0e011f57f751c77a906eba7fde3cd8765290ab01/LICENSE)
- [Fuente 4](https://github.com/fosrl/pangolin/blob/0e011f57f751c77a906eba7fde3cd8765290ab01/SECURITY.md)
- [Fuente 5](https://github.com/fosrl/pangolin/blob/0e011f57f751c77a906eba7fde3cd8765290ab01/install/config/docker-compose.yml)
- [Fuente 6](https://docs.pangolin.net/self-host/how-to-update)
- [Fuente 7](https://github.com/fosrl/pangolin/releases/tag/1.27.1)
- [Fuente 8](https://github.com/fosrl/pangolin/blob/main/LICENSE)
- [Fuente 9](https://github.com/fosrl/pangolin/security/advisories/GHSA-3cxv-w5ph-7p6h)
- [Fuente 10](https://github.com/fosrl/pangolin/security/advisories/GHSA-9784-q2hc-2qqq)
- [Fuente 11](https://github.com/fosrl/pangolin/security/advisories/GHSA-v6q2-c45v-8vx8)
- [Fuente 12](https://github.com/fosrl/pangolin/security/advisories/GHSA-hpcv-689w-jrg3)
- [Fuente 13](https://github.com/fosrl/pangolin/security/advisories/GHSA-w92q-9g55-f4r2)
- [Fuente 14](https://github.com/fosrl/pangolin/security/advisories/GHSA-fhv5-xx8r-wxfg)
- [Fuente 15](https://github.com/fosrl/pangolin/security/advisories/GHSA-3cfx-v2f2-3mqq)
- [Fuente 16](https://github.com/fosrl/pangolin/security/advisories/GHSA-9vcq-r7wr-9r3r)
- [Fuente 17](https://github.com/fosrl/pangolin/security/advisories/GHSA-5ph5-x9xv-86fv)
- [Fuente 18](https://github.com/fosrl/pangolin/security/advisories/GHSA-5772-vhpw-ppr8)
- [Fuente 19](https://github.com/fosrl/pangolin/security/advisories/GHSA-m664-jx49-xhw7)
- [Fuente 20](https://github.com/fosrl/pangolin/security/advisories/GHSA-5h3v-3645-78xj)
- [Fuente 21](https://github.com/fosrl/pangolin/security/advisories/GHSA-9xxh-cx3p-fx3m)
- [Fuente 22](https://github.com/fosrl/pangolin/security/advisories/GHSA-3pr6-pcvv-9jrp)
- [Fuente 23](https://github.com/fosrl/pangolin/security/advisories/GHSA-j32m-3vr4-9ghw)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
