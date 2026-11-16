[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Ingeniería inversa y formatos binarios

# 🖥️ YARA

> Motor de reglas para identificar malware y artefactos por patrones de bytes, strings y condiciones lógicas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 10k | BSD-3-Clause | C | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Motor open source (BSD-3-Clause) mantenido en el org VirusTotal para matching de malware.

## ¿Qué hace?

Evalúa reglas declarativas contra ficheros o memoria y reporta coincidencias.

## ¿Cómo lo hace?

Se instala por paquetes o compilando desde fuente; se integra en sandboxes y MISP.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [ghidra](ghidra.md) | YARA localiza candidatos; Ghidra los desensambla. | Match YARA → abrir en Ghidra. |
| [radare2](radare2.md) | Tras un match YARA, inspecciona el binario con radare2. | Match YARA → abrir en radare2. |
| [MISP](misp.md) | Publica reglas YARA como objetos MISP. | Exporta la regla al evento MISP. |
| [Volatility 3](volatility3.md) | Combinación recíproca: Volatility 3 lo enlaza como «Escaneo YARA sobre regiones de memoria con plugins». | Orden indicado desde Volatility 3: Carga reglas YARA en el plugin adecuado. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[capa](capa.md) · [LOKI](loki.md)

Estado en GitHub: activo · último push 2026-10-27 · última versión publicada v4.6.0 (2026-10-27) · licencia declarada BSD-3-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/VirusTotal/yara#readme) · [2](https://virustotal.github.io/yara/)</sub>

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

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/VirusTotal/yara/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://virustotal.github.io/yara/)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar YARA para mi objetivo y necesito pasos guiados. Lee https://github.com/VirusTotal/yara/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Compila YARA siguiendo https://virustotal.github.io/yara/ o usa el paquete del SO, y escanea un fichero de prueba..

**Qué comprobar:** La regla hace match o no según el contenido..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- clasificar muestras de malware de un lab
- bloquear indicadores conocidos en un pipeline de análisis

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: clasificar muestras de malware de un lab; bloquear indicadores conocidos en un pipeline de análisis | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** C
- **Etiquetas:** `security` `malware` `yara`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [VirusTotal/yara](https://github.com/VirusTotal/yara)
- 🌐 Web: <https://virustotal.github.io/yara/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/VirusTotal/yara/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
