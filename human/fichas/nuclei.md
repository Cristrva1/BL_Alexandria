[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Tráfico, rendimiento y pruebas

# 🖥️ Nuclei

> Escáner de vulnerabilidades rápido basado en plantillas YAML de la comunidad para aplicaciones, APIs, redes, DNS y configuraciones cloud.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 33k | MIT | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

## ¿Qué es?

Escáner de vulnerabilidades de código abierto (MIT) de ProjectDiscovery, con ediciones Pro y Enterprise de pago. Muy activo; las plantillas las aporta una comunidad grande.

## ¿Qué hace?

Ejecuta plantillas que simulan pasos reales para confirmar vulnerabilidades y reducir falsos positivos, sobre HTTP, DNS, TCP, SSL, WHOIS, JavaScript y código; se integra en CI/CD y envía resultados a Jira, Splunk, GitHub, Elastic o GitLab.

## ¿Cómo lo hace?

Escrito en Go; se instala con `go install`, Docker o binarios. Las plantillas se descargan y actualizan automáticamente; acepta listas de objetivos por stdin, lo que permite encadenarlo con otras herramientas de ProjectDiscovery.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [subfinder](subfinder.md) | subfinder enumera subdominios que se pasan por stdin a Nuclei; ambos son de ProjectDiscovery. | Ejecuta subfinder; después canaliza la salida a nuclei. |
| [Katana](katana.md) | katana rastrea URLs y endpoints que Nuclei escanea a continuación. | Rastrea con katana; después pasa las URLs a nuclei. |
| [Nmap](nmap.md) | Nmap identifica puertos y servicios y Nuclei comprueba vulnerabilidades concretas en ellos (combinación por arquitectura). | Escanea con Nmap; después lanza nuclei contra los servicios encontrados. |
| [ffuf](ffuf.md) | Combinación recíproca: ffuf lo enlaza como «Las rutas que descubre ffuf se revisan después con plantillas de Nuclei (combinación por arquitectura)». | Orden indicado desde ffuf: Guarda la salida de ffuf; después pasa las URLs a nuclei. |
| [ZAP (Zed Attack Proxy)](zaproxy.md) | Combinación recíproca: ZAP (Zed Attack Proxy) lo enlaza como «Nuclei comprueba CVE concretos mientras ZAP analiza la lógica y las respuestas de la aplicación (combinación por arquitectura)». | Orden indicado desde ZAP (Zed Attack Proxy): Ejecuta ambos escaneos sobre el mismo entorno de pruebas. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (13). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Amass](amass.md) · [Caido](caido.md) · [Evilginx2](evilginx2.md) · [feroxbuster](feroxbuster.md) · [Gobuster](gobuster.md) · [httpx](httpx.md) · [interactsh](interactsh.md) · [Naabu](naabu.md) · [OWASP CRS](coreruleset.md) · [OWASP Juice Shop](juice-shop.md) · [PayloadsAllTheThings](payloadsallthethings.md) · [SecLists](seclists.md) · [WPScan](wpscan.md)

**Notas:** Algunas plantillas son intrusivas; filtra por etiquetas y severidad antes de escanear.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.11.1 (2026-08-08) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/projectdiscovery/nuclei/blob/dev/README.md) · [2](https://docs.projectdiscovery.io/tools/nuclei)</sub>

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

**Entrada documentada (consulta la sintaxis original):**

```
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/projectdiscovery/nuclei/blob/dev/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Nuclei para mi objetivo y necesito pasos guiados. Lee https://github.com/projectdiscovery/nuclei/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` y escanea un objetivo de laboratorio propio con las plantillas por defecto..

**Qué comprobar:** Nuclei lista los hallazgos con su severidad y la plantilla que los detectó..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- revisar tus propios servicios expuestos frente a CVE recientes
- añadir pruebas de regresión de seguridad a un pipeline de CI

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: revisar tus propios servicios expuestos frente a CVE recientes; añadir pruebas de regresión de seguridad a un pipeline de CI | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Úsalo solo contra sistemas propios o con autorización escrita: usarlo contra terceros sin permiso es delito en la mayoría de países.

## Stack y modelos

- **Stack:** Go, Dockerfile, go.mod
- **Etiquetas:** `pruebas` `go` `security` `cli`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)
- 🌐 Web: <https://docs.projectdiscovery.io/tools/nuclei>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/projectdiscovery/nuclei/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
