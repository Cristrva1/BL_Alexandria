[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Reconocimiento y superficie de ataque

# 🖥️ httpx

> Sondea URLs y hosts HTTP/HTTPS a gran velocidad: códigos, títulos, tecnologías y cadenas de redirección para filtrar activos vivos.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10.6k | MIT | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Puntuación de calidad** 76/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Toolkit HTTP multipropósito de ProjectDiscovery, pareja natural de Subfinder y Nuclei.

## ¿Qué hace?

Envía sondas HTTP concurrentes a hosts o CIDR y reporta estado, título, tecnologías y redirecciones.

## ¿Cómo lo hace?

Binario Go (`go install …/httpx@latest` o release); se alimenta de listas de hosts y produce salidas parseables.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [subfinder](subfinder.md) | httpx filtra qué FQDN descubiertos por Subfinder están vivos. | Primero Subfinder; después httpx sobre la lista. |
| [Nuclei](nuclei.md) | Nuclei escanea las URLs vivas que httpx confirma. | httpx primero; Nuclei con `-l` sobre la salida. |
| [Amass](amass.md) | Amass entrega hosts que httpx filtra por HTTP vivo. | Amass primero; httpx sobre la lista. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[dnsx](dnsx.md) · [interactsh](interactsh.md)

Estado en GitHub: activo · último push 2026-11-13 · última versión publicada v1.12.0 (2026-09-08) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/projectdiscovery/httpx#readme) · [2](https://docs.projectdiscovery.io/tools/httpx)</sub>

## Ver similares

Grupo **Sondeo y escaneo de reconocimiento**: httpx ocupa la posición 1 de 2 (recomendado). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | **httpx** (esta ficha) ⭐ recomendado | 76 | Si buscas esto: sondea URLs y hosts HTTP/HTTPS a gran velocidad: códigos, títulos, tecnologías y cadenas de redirección para filtrar activos vivos. |
| 2 | [Naabu](naabu.md) | 62 | Si buscas esto: escáner de puertos SYN/CONNECT/UDP en Go, ligero y pensado para encadenarse con Nmap y con Nuclei. |

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
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/projectdiscovery/httpx/blob/dev/README.md)

[Abrir la web o descarga indicada por el autor](https://docs.projectdiscovery.io/tools/httpx)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar httpx para mi objetivo y necesito pasos guiados. Lee https://github.com/projectdiscovery/httpx/blob/dev/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest` y sonda un listado de hosts propios..

**Qué comprobar:** Obtienes líneas con código, título y URL final..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- filtrar qué hosts de un listado de recon responden HTTP
- obtener títulos y tecnologías de un alcance autorizado

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: filtrar qué hosts de un listado de recon responden HTTP; obtener títulos y tecnologías de un alcance autorizado | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** Go, Dockerfile, Makefile, go.mod
- **Etiquetas:** `security` `http` `recon` `go`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Naabu](naabu.md) | 6.4k | Escáner de puertos SYN/CONNECT/UDP en Go, ligero y pensado para encadenarse con Nmap y con Nuclei. |

## Enlaces

- 🐙 GitHub: [projectdiscovery/httpx](https://github.com/projectdiscovery/httpx)
- 🌐 Web: <https://docs.projectdiscovery.io/tools/httpx>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/projectdiscovery/httpx/blob/dev/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
