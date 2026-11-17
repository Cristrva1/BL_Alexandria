[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Detección, SIEM e IDS

# 🖥️ Fail2ban

> Bloquea IPs tras intentos fallidos de autenticación leyendo logs (ssh, web…); defensa clásica de hosts.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 19k | GPL-2.0 | Python | 2026-11-16 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟡 medio

**Nivel:** 2 Intermedio — preparación media

**Puntuación de calidad** 62/100 · métricas del 2026-11-16 · [cómo se calcula](../calidad.md)

> **Licencia revisada el 2026-11-16:** GPL-2.0. Algunos archivos indican otra licencia en COPYING. Fuente: [LICENSE](https://github.com/fail2ban/fail2ban/blob/master/COPYING). GitHub la marca como NOASSERTION.

## ¿Qué es?

Ban automático por logs (GPL según COPYING; API NOASSERTION).

## ¿Qué hace?

Parsea logs y actualiza firewall.

## ¿Cómo lo hace?

Paquete / source.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [Wazuh](wazuh.md) | Wazuh alerta; Fail2ban responde en el host. | Ambos. |

Estado en GitHub: activo · último push 2026-11-15 · última versión publicada 1.1.1 (2026-08-15) · licencia declarada NOASSERTION (consultado el 2026-11-16).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-16); no se instaló ni ejecutó. Fuentes: [1](https://github.com/fail2ban/fail2ban#readme) · [2](http://www.fail2ban.org)</sub>

## Ver similares

Grupo **Bloqueo de IP por comportamiento**: Fail2ban ocupa la posición 2 de 2 (alternativa). Orden por puntuación de calidad; revisa «Cuándo elegirlo» antes de decidir: no todos cubren lo mismo.

| # | Repo | Puntuación | Cuándo elegirlo |
|---:|---|---:|---|
| 1 | [CrowdSec](crowdsec.md) ⭐ recomendado | 76 | Si buscas esto: iDS/IPS, WAF y detección de bots abiertos con lista de bloqueo colaborativa de IP maliciosas, para Linux, Windows, Docker y Kubernetes. |
| 2 | **Fail2ban** (esta ficha) | 62 | Si buscas esto: bloquea IPs tras intentos fallidos de autenticación leyendo logs (ssh, web…); defensa clásica de hosts. |

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
git clone https://github.com/fail2ban/fail2ban.git
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/fail2ban/fail2ban/blob/master/README.md)

[Abrir la web o descarga indicada por el autor](http://www.fail2ban.org)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Fail2ban para mi objetivo y necesito pasos guiados. Lee https://github.com/fail2ban/fail2ban/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Instala el paquete de tu distro o clona y sigue COPYING/README; activa el jail sshd..

**Qué comprobar:** IPs repetidas quedan baneadas..

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- proteger SSH de un VPS propio
- banear force brute a un panel web

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: proteger SSH de un VPS propio; banear force brute a un panel web | necesitas una instalación sin cuentas ni dependencias adicionales |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado.

## Stack y modelos

- **Stack:** Python, setup.py
- **Etiquetas:** `security`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [CrowdSec](crowdsec.md) | 15.6k | IDS/IPS, WAF y detección de bots abiertos con lista de bloqueo colaborativa de IP maliciosas, para Linux, Windows, Docker y Kubernetes. |

## Enlaces

- 🐙 GitHub: [fail2ban/fail2ban](https://github.com/fail2ban/fail2ban)
- 🌐 Web: <http://www.fail2ban.org>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-16. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/fail2ban/fail2ban/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
