[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Explotación, C2 y post-explotación

# 🖥️ Evilginx2

> Proxy de phishing que captura credenciales y cookies de sesión (bypass MFA) en simulaciones de ingeniería social autorizadas.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.9k | BSD-3-Clause | Go | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** hard

## ¿Qué es?

Framework MITM de phishing moderno (BSD-3-Clause) de kgretzky; sucesor de Evilginx 2017.

## ¿Qué hace?

Se interpone entre víctima y sitio legítimo, robando tokens de sesión además de passwords.

## ¿Cómo lo hace?

Release Go + dominio/DNS controlados; phishlets YAML por proveedor.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Nuclei](nuclei.md) | Tras el ejercicio, Nuclei puede buscar patrones relacionados en el perímetro propio. | Define el alcance; Nuclei solo sobre activos autorizados. |
| [Wazuh](wazuh.md) | Valida si el SOC detecta el patrón de proxy. | Ejecuta el ejercicio; revisa alertas Wazuh. |
| [Atomic Red Team](atomic-red-team.md) | Complementa con atomics de phishing/inicial access. | Atomic + Evilginx2 en purple team. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (1). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[SET](social-engineer-toolkit.md)

Estado en GitHub: activo · último push 2026-06-10 · última versión publicada v3.3.0 (2024-04-02) · licencia declarada BSD-3-Clause (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/kgretzky/evilginx2#readme)</sub>

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

[Instrucciones originales de instalación](https://github.com/kgretzky/evilginx2/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Evilginx2 para mi objetivo y necesito pasos guiados. Lee https://github.com/kgretzky/evilginx2/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Sigue la documentación oficial de Evilginx para instalar el release en un VPS de laboratorio aislado..

**Qué comprobar:** El phishlet de prueba captura una sesión de un usuario voluntario..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- entrenar al personal con un phishing MFA controlado
- evaluar la detección de reverse-proxy phishing

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: entrenar al personal con un phishing MFA controlado; evaluar la detección de reverse-proxy phishing | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Uso exclusivo sobre sistemas propios o con autorización escrita y dentro del alcance acordado. Acceder sin permiso a sistemas ajenos es delito en la mayoría de países (en México, Código Penal Federal, arts. 211 bis 1 a 211 bis 7); revisa la ley local antes de cada encargo. Riesgo legal/criminal muy alto fuera de simulaciones con consentimiento informado y alcance firmado. Nunca contra terceros sin permiso.

## Stack y modelos

- **Stack:** Go, Makefile, go.mod
- **Etiquetas:** `security` `phishing` `redteam`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [kgretzky/evilginx2](https://github.com/kgretzky/evilginx2)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/kgretzky/evilginx2/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
