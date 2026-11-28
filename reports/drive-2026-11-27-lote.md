# Lote de la revisión completa de Drive del 27 de noviembre de 2026

Este lote reúne los candidatos de mayor valor que salieron de la lectura completa de la carpeta de recursos. Cada repositorio pasó la revisión de origen, licencia, paquete publicado, avisos de seguridad y CI sobre el commit de su versión. No se instaló ni ejecutó ningún proyecto, y las primeras pruebas de las fichas quedan propuestas para el entorno de quien lee. Las técnicas y los prompts se redactaron desde fuentes públicas originales.

## Repositorios publicados

Se publicaron nueve fichas ligeras.

- **Skills CLI (Vercel Labs).** Instala, lista y quita skills en Claude Code, Codex y otros agentes, dentro del proyecto. La ficha fija `skills@1.9.1`: el nombre `skills` 1.0.0 de npm es un paquete antiguo sin relación. También pide revisar cada skill ajena antes de instalarla. [Versión](https://github.com/vercel-labs/skills/releases/tag/v1.9.1) · [CI](https://github.com/vercel-labs/skills/actions/runs/45941358982) · [E2E sobre el commit de la versión](https://github.com/vercel-labs/skills/actions/runs/45952567515)
- **Documenso.** Firma electrónica autoalojada. La prueba local usa la instalación de desarrollo con un buzón de correo local y un firmante ficticio. Exige la 2.19.0 o posterior por el aviso [GHSA-3494-9j87-fj64](https://github.com/documenso/documenso/security/advisories/GHSA-3494-9j87-fj64) y separa el núcleo AGPL de las funciones Enterprise. [Versión 2.22.0](https://github.com/documenso/documenso/releases/tag/v2.22.0) · [Pruebas Playwright](https://github.com/documenso/documenso/actions/runs/43345864965)
- **Cap.** Grabación y edición de pantalla en el equipo, sin cuenta en el modo Studio. Es gratis para uso personal; el uso comercial requiere licencia. No hay prueba de captura real en CI sobre esta versión, y la ficha lo indica. [Versión 0.6.3](https://github.com/CapSoftware/Cap/releases/tag/cap-v0.6.3) · [Engine verify](https://github.com/CapSoftware/Cap/actions/runs/43092047100)
- **Pake.** Convierte una web propia en app de escritorio. Exige la 3.17.3 o posterior por dos avisos altos y recomienda reconstruir las apps antiguas. [Versión 3.21.0](https://github.com/tw93/Pake/releases/tag/V3.21.0) · [Quality & Testing](https://github.com/tw93/Pake/actions/runs/45192308113)
- **CodeQL.** Análisis de flujo de datos con code scanning en GitHub. Se puede usar gratis en repositorios públicos con licencia abierta o con fines académicos; el código privado requiere licencia de pago. [Configuración predeterminada](https://docs.github.com/en/code-security/code-scanning/enabling-code-scanning/configuring-default-setup-for-code-scanning) · [CI de codeql-action](https://github.com/github/codeql-action/actions/runs/45419775563)
- **Bandit, gosec y Brakeman.** Analizadores de seguridad para Python, Go y Ruby on Rails, con una prueba sobre un archivo propio con un fallo conocido. Brakeman usa una licencia no OSI: es gratis para el software propio y el uso no comercial. [Bandit 1.9.4](https://github.com/PyCQA/bandit/actions/runs/22385359689) · [gosec 2.30.0](https://github.com/securego/gosec/actions/runs/39929569892) · [Brakeman 8.1.1](https://github.com/presidentbeef/brakeman/releases/tag/v8.1.1)
- **MobSF.** Análisis estático de apps móviles propias, publicado solo en `127.0.0.1` y con contraseña propia. Exige la 4.6.6 o posterior; la ficha usa la 4.6.9. La primera prueba analiza una app de práctica de OWASP. [Versión 4.6.9](https://github.com/MobSF/Mobile-Security-Framework-MobSF/releases/tag/v4.6.9) · [Pruebas](https://github.com/MobSF/Mobile-Security-Framework-MobSF/actions/runs/44250422514)

Se añadieron alternativas simétricas: CodeQL con Semgrep, Documenso con DocuSeal, Cap con OBS Studio y Skills CLI con autoskills.

## Técnicas, prompts y sitios

- **Técnicas.**
  - Llevar un PR hasta la fusión con `/code-review`, `/ship` y `/steward`, con Claude Approvals en modo observe para equipos. [Documentación de /ship](https://code.claude.com/docs/en/ship-command)
  - Evaluar skills con casos reales y pruebas sin la skill. [Uber Engineering](https://www.uber.com/us/en/blog/optimizing-ubers-agent-skills/)
  - Tres comprobaciones antes de instalar un repositorio de GitHub.
  - Hacer un sitio consultable por agentes con Search for Agents. [Cloudflare](https://developers.cloudflare.com/changelog/post/2026-11-25-search-for-agents/)
  - Estimar intención de compra con similitud semántica. [arXiv 2510.08338](https://arxiv.org/abs/2510.08338)
- **Prompts del manual.** Contrato de tarea, nota de traspaso, carpeta de investigación donde lo leído es evidencia y reglas de acciones que siempre se consultan. Son plantillas propias con fuentes oficiales.
- **Sitios.** Teachable Machine y la especificación Agent Skills.
- **Fichas enriquecidas.**
  - VibeVoice indica que el código de su TTS largo se retiró del repositorio y cambia la primera prueba.
  - Astryx indica que pide React 19 y que su versión publicada sigue en 0.x.

## Pendientes

- **Skill_Seekers.** Al mejorar una skill sin clave de API, lanza Claude Code con `--dangerously-skip-permissions` sobre texto extraído de fuentes ajenas. Para reconsiderarlo haría falta que esa ruta pida permisos por defecto. [Código](https://github.com/yusufkaraaslan/Skill_Seekers/blob/development/src/skill_seekers/cli/agent_client.py)
- **googleworkspace/cli.** El proyecto comunitario anuncia que la herramienta oficial gwscli lo sustituye. Su última versión es de marzo y el CI falla. gwscli no publica código ni licencia evaluables.
- **legal-templates.** Las plantillas están en inglés y siguen el derecho de EE. UU. Tienen informes de errores abiertos sin respuesta, entre ellos uno confirmado en el NDA mutuo. Es un riesgo para personas sin formación legal.
- **SuperSplat.** El CI de la versión 3.9.2 solo compila y pasa lint. Falta una prueba funcional ligada a la versión.
- **Understand-Anything.** El panel ejecuta por defecto con `npx` un paquete subido a mano y sin atestación. Los hooks con actualización automática piden al agente actuar sin confirmar.
- **PixelRAG.** La búsqueda no tiene cobertura de CI y `serve` falla en la 0.4.0 sin opciones adicionales; la corrección está en la rama principal y no se ha publicado. En Linux descarga un Chrome compilado a mano sin verificar su suma.
- **Meetily.** Ningún workflow de la 0.5.0 ejecuta pruebas funcionales; solo compila y firma los instaladores.
- **Voicebox.** El CI no ejecuta las pruebas del backend y hay regresiones abiertas en la serie 0.6. La versión 0.6.1 corrige permisos amplios de las anteriores, así que no conviene fijar una versión previa.

Las técnicas y los prompts tienen enlaces a sus fuentes. La revisión de los repositorios corresponde a pruebas de cada proyecto, y la actividad propuesta en cada ficha queda para el entorno de prueba de quien la lea.
