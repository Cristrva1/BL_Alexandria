[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Directorios y aprendizaje

# 📂 SecLists

> Colección OWASP de wordlists y payloads (dirs, users, passwords, fuzzing) de referencia para pruebas autorizadas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 74.8k | MIT | PHP | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 📂 catálogo/recurso · **Setup** 🟢 fácil

## ¿Qué es?

Proyecto de Daniel Miessler (MIT) adoptado por OWASP como set de wordlists de pentest.

## ¿Qué hace?

Reúne diccionarios listos para descubrimiento, fuerza bruta y fuzzing en ejercicios autorizados.

## ¿Cómo lo hace?

Solo hace falta clonar o descomprimir; no es un binario.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ffuf](ffuf.md) | SecLists alimenta ffuf. | Clona SecLists; pasa la wordlist a ffuf. |
| [hashcat](hashcat.md) | Diccionarios de SecLists alimentan ataques de contraseña en lab. | SecLists primero; Hashcat con la lista autorizada. |
| [Nuclei](nuclei.md) | Algunas plantillas Nuclei usan wordlists externas. | Configura la ruta a SecLists. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (4). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[dirsearch](dirsearch.md) · [feroxbuster](feroxbuster.md) · [Gobuster](gobuster.md) · [THC Hydra](thc-hydra.md)

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 2026.2 (2026-10-27) · licencia declarada MIT (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/danielmiessler/SecLists#readme) · [2](https://owasp.org/www-project-seclists/)</sub>

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

Material para leer. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Abre el material original y localiza la sección relacionada con tu tarea.
2. Elige una referencia o ejemplo; revisa sus requisitos y su procedencia antes de instalar nada.
3. Conserva solo las piezas que necesitas y consulta la ficha de cada proyecto enlazado.

**Entrada documentada (consulta la sintaxis original):**

```
git clone --depth 1 https://github.com/danielmiessler/SecLists.git
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/danielmiessler/SecLists/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/danielmiessler/SecLists)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar SecLists para mi objetivo y necesito pasos guiados. Lee https://github.com/danielmiessler/SecLists/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona con `git clone --depth 1 https://github.com/danielmiessler/SecLists.git` y apunta ffuf a una lista..

**Qué comprobar:** El fuzzer usa el diccionario seleccionado..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- fuzzear rutas de una app web de lab con la lista Discovery
- probar contraseñas comunes solo contra cuentas de prueba

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: fuzzear rutas de una app web de lab con la lista Discovery; probar contraseñas comunes solo contra cuentas de prueba | necesitas una aplicación lista para ejecutar en lugar de material de consulta |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** PHP
- **Etiquetas:** `security` `wordlists`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [PayloadsAllTheThings](payloadsallthethings.md) | 82.7k | Enciclopedia práctica de payloads y técnicas web (XSS, SQLi, SSRF…) mantenida por la comunidad de pentest. |

## Enlaces

- 🐙 GitHub: [danielmiessler/SecLists](https://github.com/danielmiessler/SecLists)
- 🌐 Web: <https://www.owasp.org/index.php/OWASP_Internet_of_Things_Project>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/danielmiessler/SecLists/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
