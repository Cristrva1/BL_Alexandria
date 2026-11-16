[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Nube, contenedores e IaC

# 🖥️ Prowler

> Auditoría multi-cloud open source (AWS, Azure, GCP…) de configuración y marcos CIS: CLI Apache-2.0; Cloud/Private Cloud son de pago.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 15.3k | Apache-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

## ¿Qué es?

Herramienta open source (Apache-2.0) de posture cloud; Prowler Cloud/Private Cloud son productos comerciales aparte.

## ¿Qué hace?

Ejecuta cientos de checks de configuración y compliance sobre proveedores cloud y exporta resultados.

## ¿Cómo lo hace?

CLI con `pip install prowler` o Docker; los productos Cloud se contratan aparte (prueba 7 días en prowler.com).

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Trivy](trivy.md) | Trivy cubre imágenes/IaC local; Prowler la posture de la cuenta. | Trivy en CI; Prowler sobre las credenciales cloud. |
| [Semgrep](semgrep.md) | Semgrep revisa código; Prowler la nube desplegada. | Usa ambos en el pipeline de seguridad. |
| [Lynis](lynis.md) | Lynis endurece el host; Prowler la nube. | Audita VMs con Lynis y cuentas con Prowler. |
| [Checkov](checkov.md) | Combinación recíproca: Checkov lo enlaza como «Checkov previene; Prowler audita lo ya desplegado». | Orden indicado desde Checkov: Checkov en CI; Prowler sobre la cuenta. |

## Usado por

Repos que lo citan en sus combinaciones sin que figuren arriba (2). La lista se genera automáticamente; el motivo está en la ficha de cada uno.

[Pacu](pacu.md) · [ScubaGear](scubagear.md)

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada 5.50.0 (2026-11-16) · licencia declarada Apache-2.0 (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/prowler-cloud/prowler#readme) · [2](https://prowler.com) · [3](https://prowler.com/pricing)</sub>

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
pip install prowler
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/prowler-cloud/prowler/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](https://prowler.com)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Prowler para mi objetivo y necesito pasos guiados. Lee https://github.com/prowler-cloud/prowler/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala con `pip install prowler` y ejecuta `prowler aws` con credenciales de una cuenta de prueba..

**Qué comprobar:** Obtienes findings con severidad y referencias de cumplimiento..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- auditar cuentas AWS de laboratorio contra CIS
- generar un informe de posture antes de un ejercicio interno

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: auditar cuentas AWS de laboratorio contra CIS; generar un informe de posture antes de un ejercicio interno | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Open source = CLI/SDK/Local Server Apache-2.0. Prowler Cloud (~99 USD/cuenta·mes) y Private Cloud son de pago.

## Stack y modelos

- **Stack:** Python, Dockerfile, Makefile, docker-compose.yml, pyproject.toml
- **Etiquetas:** `security` `cloud` `aws`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [prowler-cloud/prowler](https://github.com/prowler-cloud/prowler)
- 🌐 Web: <https://prowler.com>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/prowler-cloud/prowler/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
