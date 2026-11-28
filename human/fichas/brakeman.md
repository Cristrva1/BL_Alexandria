[🏠 Inicio](../README.md) › [🔍 Analizar software y comprobar su seguridad](../categorias/16-analisis-de-software-y-seguridad.md) › Protección y verificación de software

# 🖥️ Brakeman

> Revisa el código de aplicaciones Ruby on Rails sin ponerlas en marcha y avisa de inyecciones SQL o de comandos, XSS y configuraciones de riesgo.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 7.3k | Brakeman Public Use License | Ruby | 2026-11-27 |

**Ejecución** 🏠 local · **Rol** 🖥️ app · **Setup** 🟢 fácil

**Nivel:** 1 Básico — preparación sencilla

**Puntuación de calidad** 44/100 · métricas del 2026-11-28 · [cómo se calcula](../calidad.md)

> ⚠️ **Licencia y costes:** No es una licencia de código abierto aprobada por la OSI. El texto permite usarlo gratis para analizar tu propio software y para cualquier uso no comercial. Exige una licencia comercial de pago para usos con ventaja comercial o pago a cambio: ofrecerlo como servicio gestionado o SaaS, distribuirlo como producto comercial o dentro de uno, o integrarlo en un producto o servicio de valor añadido. Auditar código de clientes como servicio de pago puede entrar ahí; ante la duda, el LICENSE pide consultar al mantenedor. El código anterior al 15 de junio de 2018 conserva la licencia MIT y las contribuciones se ceden a Synopsys.

## ¿Qué es?

Analizador estático de seguridad para aplicaciones Ruby on Rails.

## ¿Qué hace?

Encuentra inyección SQL y de comandos, XSS, redirecciones abiertas, asignación masiva y otras debilidades, con un nivel de confianza por aviso.

## ¿Cómo lo hace?

Interpreta el código Ruby de la aplicación sin ejecutarlo, rastrea qué datos provienen de la petición y aplica comprobaciones por tipo de vulnerabilidad; el informe sale en texto, HTML, JSON, SARIF y otros formatos.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [OSV-Scanner](osv-scanner.md) | Revisa las gemas de Gemfile.lock contra vulnerabilidades publicadas; Brakeman revisa el código de la aplicación. | — |
| [ZAP (Zed Attack Proxy)](zaproxy.md) | Prueba la aplicación en marcha en tu equipo para confirmar con tráfico real lo que Brakeman señala en el código. | — |
| [DefectDojo](defectdojo.md) | Importa los informes de Brakeman para seguir los hallazgos junto con los de otros escáneres. | — |

Estado en GitHub: activo · último push 2026-11-20 · última versión publicada v8.1.1 (2026-11-20) · licencia declarada NOASSERTION (consultado el 2026-11-27).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-27); no se instaló ni ejecutó. Fuentes: [1](https://github.com/presidentbeef/brakeman/blob/9080ba43d11208d94d6e4d3a8bedbaec018b06f5/README.md) · [2](https://github.com/presidentbeef/brakeman/blob/9080ba43d11208d94d6e4d3a8bedbaec018b06f5/LICENSE.md) · [3](https://github.com/presidentbeef/brakeman/blob/9080ba43d11208d94d6e4d3a8bedbaec018b06f5/COPYING.md) · [4](https://github.com/presidentbeef/brakeman/blob/9080ba43d11208d94d6e4d3a8bedbaec018b06f5/OPTIONS.md) · [5](https://github.com/presidentbeef/brakeman/blob/9080ba43d11208d94d6e4d3a8bedbaec018b06f5/lib/brakeman/checks/check_execute.rb) · [6](https://github.com/presidentbeef/brakeman/blob/9080ba43d11208d94d6e4d3a8bedbaec018b06f5/lib/brakeman/scanner.rb) · [7](https://github.com/presidentbeef/brakeman/blob/9080ba43d11208d94d6e4d3a8bedbaec018b06f5/.circleci/config.yml) · [8](https://github.com/presidentbeef/brakeman/blob/9080ba43d11208d94d6e4d3a8bedbaec018b06f5/Rakefile) · [9](https://github.com/presidentbeef/brakeman/runs/136439493013) · [10](https://github.com/presidentbeef/brakeman/actions/runs/44796664587) · [11](https://github.com/presidentbeef/brakeman/releases/tag/v8.1.1) · [12](https://rubygems.org/gems/brakeman/versions/8.1.1) · [13](https://hub.docker.com/r/presidentbeef/brakeman/tags) · [14](https://github.com/presidentbeef/brakeman/security/advisories) · [15](https://github.com/DefectDojo/django-DefectDojo/tree/cd0a4483a224707f72a0fc3112359089c1446b55/dojo/tools/brakeman)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No necesita clave de API ni conexión durante el análisis. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. Aplica comprobaciones fijas sobre el código. No usa modelos de IA. |
| Coste | Sin pago a un modelo en la ruta básica. Gratis para analizar tu propio software y para uso no comercial. Los usos comerciales que define la licencia (SaaS, producto comercial o servicio de valor añadido) requieren licencia de pago. |
| Equipo | Equipo normal; revisar dependencias. Cualquier equipo con Ruby 3.2 o posterior. |

Un agente de código puede ayudarte a instalar Brakeman y a interpretar los avisos, pero Brakeman se ejecuta en tu equipo sin cuenta ni suscripción de IA.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Un entorno de instalación o servidor y las dependencias indicadas por el README.
- Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.

1. Instala Ruby 3.2 o posterior: Brakeman 8.1.1 lo exige para ejecutarse y analiza aplicaciones Rails de la 2.3 a la 8. No necesitas instalar Rails para la prueba.
2. Instala la versión revisada desde RubyGems con gem install brakeman -v 8.1.1 y comprueba brakeman --version. La imagen Docker presidentbeef/brakeman sigue en 8.1.0 porque su publicación automática para 8.1.1 falló al arrancar.
3. Prepara la carpeta demo de la primera prueba y ejecuta brakeman demo. Cambia la llamada a system("ls", params[:carpeta]), que no pasa por un intérprete de comandos, y repite: el aviso desaparece.

**Entrada documentada (consulta la sintaxis original):**

```
gem install brakeman
```

Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto.

[Instrucciones originales de instalación](https://github.com/presidentbeef/brakeman/blob/main/README.md)

[Abrir la web o descarga indicada por el autor](https://github.com/presidentbeef/brakeman/releases/tag/v8.1.1)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Brakeman para mi objetivo y necesito pasos guiados. Lee https://github.com/presidentbeef/brakeman/blob/main/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea demo/app/controllers/archivos_controller.rb con una clase ArchivosController cuyo método index ejecute system("ls #{params[:carpeta]}") y ejecuta brakeman demo.

**Qué comprobar:** El informe muestra un aviso Command Injection de la comprobación Execute, con confianza High, el archivo y la línea de system.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Revisar una aplicación Rails propia antes de cada versión para encontrar consultas SQL armadas con datos del usuario
- Comparar el informe JSON actual con el anterior para ver qué avisos se corrigieron y cuáles son nuevos

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Revisar una aplicación Rails propia antes de cada versión para encontrar consultas SQL armadas con datos del usuario; Comparar el informe JSON actual con el anterior para ver qué avisos se corrigieron y cuáles son nuevos | Tu aplicación no usa Ruby on Rails o quieres integrarlo en un producto o servicio comercial para terceros sin comprar la licencia. |

**Limitaciones:** Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada. Las pruebas activas requieren un alcance autorizado y un entorno adecuado. Gratis para revisar tus propias aplicaciones o con fines no comerciales; ofrecerlo en un servicio o producto comercial para terceros requiere licencia de pago. Instala 8.1.1 desde RubyGems, porque la imagen Docker sigue en 8.1.0. Revisa cada aviso a mano.

## Stack y modelos

- **Stack:** Ruby, Dockerfile, Gemfile
- **Etiquetas:** `ruby` `rails` `análisis estático` `seguridad`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Enlaces

- 🐙 GitHub: [presidentbeef/brakeman](https://github.com/presidentbeef/brakeman)
- 🌐 Web: <https://brakemanscanner.org/>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-27. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/presidentbeef/brakeman/blob/9080ba43d11208d94d6e4d3a8bedbaec018b06f5/README.md)
- [Fuente 2](https://github.com/presidentbeef/brakeman/blob/9080ba43d11208d94d6e4d3a8bedbaec018b06f5/LICENSE.md)
- [Fuente 3](https://github.com/presidentbeef/brakeman/blob/9080ba43d11208d94d6e4d3a8bedbaec018b06f5/COPYING.md)
- [Fuente 4](https://rubygems.org/gems/brakeman/versions/8.1.1)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
