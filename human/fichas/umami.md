[🏠 Inicio](../README.md) › [📊 Dashboards, analítica y mapas](../categorias/10-anal-tica-visualizaci-n.md) › Analítica web y de producto

# 📈 Umami

> Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 40.2k | MIT | TypeScript | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** ⚙️ plataforma · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. La analítica básica no exige IA; hosting, base de datos y Umami Cloud pueden costar |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Configura DATABASE_URL y APP_SECRET antes de build; cambia la contraseña inicial cuando lo solicite |
| Coste | El coste depende del proveedor o la ruta. La analítica básica no exige IA; hosting, base de datos y Umami Cloud pueden costar |
| Equipo | Preparación según la ruta elegida. Node >=20.19; pnpm; PostgreSQL >=12.14; configuración .env |

Configura DATABASE_URL y APP_SECRET antes de build; cambia la contraseña inicial cuando lo solicite

## Qué puedes hacer con él

Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics.

## Por qué destaca

Usos propuestos: Medir visitas de una web; Comparar campañas mediante eventos propios.

## Cómo funciona

Configura DATABASE_URL y APP_SECRET antes de build; cambia la contraseña inicial cuando lo solicite

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Node >=20.19
- pnpm
- PostgreSQL >=12.14
- configuración .env

1. Abre las instrucciones originales enlazadas y elige tu sistema operativo y una sola ruta de instalación.
2. Prepara los requisitos de la lista en una carpeta o entorno de prueba. Descargar código y tener el programa funcionando son pasos diferentes.
3. Sigue la entrada documentada de abajo y los pasos restantes de la guía; sustituye rutas y valores de ejemplo por los de tu entorno. Si es un comando del agente,úsalo dentro de ese agente.

**Entrada documentada (bash):**

```
git clone https://github.com/umami-software/umami.git
cd umami
pnpm install
```

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/umami-software/umami/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Umami para mi objetivo y necesito pasos guiados. Lee https://github.com/umami-software/umami/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Añade el script a una página propia de prueba y genera un evento ficticio.

**Qué comprobar:** El panel recibe la visita y el evento del sitio correcto.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Medir visitas de una web
- Comparar campañas mediante eventos propios

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Medir visitas de una web; Comparar campañas mediante eventos propios | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** Configura DATABASE_URL y APP_SECRET antes de build; cambia la contraseña inicial cuando lo solicite

## Stack y modelos

- **Stack:** Node >=20.19; pnpm; PostgreSQL >=12.14; configuración .env
- **Etiquetas:** `analytics` `typescript` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Plausible Analytics](plausible.md) | 29.8k | Analítica web ligera, sin cookies y centrada en la privacidad, en la nube o auto-hospedada. |
| [Matomo](matomo.md) | 22k | Alternativa open source a Google Analytics con control total de los datos. |

## Enlaces

- 🐙 GitHub: [umami-software/umami](https://github.com/umami-software/umami)
- 🌐 Web: <https://umami.is>
- 🧪 Receta: [Analítica de producto con IA](../playbooks/analitica-con-ia.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/umami-software/umami/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
