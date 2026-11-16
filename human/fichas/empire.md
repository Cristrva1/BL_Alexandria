[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Explotación, C2 y post-explotación

# 🖥️ Empire

> Framework post-explotación/C2 centrado en PowerShell y agentes multiplataforma para labs autorizados.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 5.4k | BSD-3-Clause | PowerShell | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** hard

**Puntuación de calidad** 58/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

## ¿Qué es?

Empire de BC-Security (BSD-3).

## ¿Qué hace?

C2 y post-explotación con módulos.

## ¿Cómo lo hace?

Clone + instalación documentada.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Metasploit Framework](metasploit.md) | Post-ex complementaria. | Elige según payload. |
| [Wazuh](wazuh.md) | Detección del C2. | Empire → Wazuh. |

Estado en GitHub: activo · último push 2026-09-08 · última versión publicada v7.0.2 (2026-09-08) · licencia declarada BSD-3-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/BC-SECURITY/Empire#readme) · [2](https://bc-security.gitbook.io/empire-wiki/)</sub>

## Ver similares

Grupo **Frameworks de C2 y post-explotación**: Empire ocupa la posición 2 de 3 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [Sliver](sliver.md) ⭐ recomendado | 70 | Si buscas esto: framework C2 open source de Bishop Fox para emulación de adversario autorizada: implants multiplataforma y canales mTLS/WireGuard/HTTP/DNS. |
| 2 | **Empire** (esta ficha) | 58 | Si buscas esto: framework post-explotación/C2 centrado en PowerShell y agentes multiplataforma para labs autorizados. |
| 3 | [Mythic](mythic.md) | 50 | Si buscas esto: framework C2 colaborativo con UI: agentes y perfiles C2 se instalan aparte vía mythic-cli. |

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
git clone https://github.com/BC-SECURITY/Empire.git
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/BC-SECURITY/Empire/blob/main/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Empire para mi objetivo y necesito pasos guiados. Lee https://github.com/BC-SECURITY/Empire/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Clona Empire y sigue https://bc-security.gitbook.io/empire-wiki/ para el setup de lab..

**Qué comprobar:** Consola Empire lista..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- listener + stager en un lab Windows
- módulos de post-ex en ejercicio red team

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: listener + stager en un lab Windows; módulos de post-ex en ejercicio red team | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo.

## Stack y modelos

- **Stack:** PowerShell, Dockerfile, pyproject.toml
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Mythic](mythic.md) | 4.9k | Framework C2 colaborativo con UI: agentes y perfiles C2 se instalan aparte vía mythic-cli. |
| [Sliver](sliver.md) | 12.3k | Framework C2 open source de Bishop Fox para emulación de adversario autorizada: implants multiplataforma y canales mTLS/WireGuard/HTTP/DNS. |

## Enlaces

- 🐙 GitHub: [BC-SECURITY/Empire](https://github.com/BC-SECURITY/Empire)
- 🌐 Web: <https://bc-security.gitbook.io/empire-wiki/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/BC-SECURITY/Empire/blob/main/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
