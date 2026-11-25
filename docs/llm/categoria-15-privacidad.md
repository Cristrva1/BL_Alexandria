# Alexandría para agentes · Credenciales y privacidad

Categoría 15 «Organizar notas, archivos y servicios personales» › subcategoría `privacidad`. 10 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=15&sub=privacidad · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `pi-hole` | Sumidero DNS para bloquear anuncios y rastreadores en toda la red sin instalar… | 1 Básico | 68 | EUPL-1.2 (OSI copyleft) | recomendado |
| `authentik` | IdP/SSO open source (MIT núcleo; enterprise/ bajo licencia distinta): OAuth2… | 3 Avanzado | 67 | MIT + licencia Enterprise (authentik/enterprise/) (open-core) | recomendado |
| `keycloak` | IdP estándar de la industria (Red Hat/CNCF): OIDC, SAML, federación y admin… | 3 Avanzado | 67 | Apache-2.0 (OSI permisiva) | alternativa |
| `vaultwarden` | Servidor no oficial compatible con clientes Bitwarden para alojar una bóveda de… | 2 Intermedio | 67 | AGPL-3.0 (OSI copyleft) | recomendado |
| `vault` | Gestión de secretos y cifrado como servicio: dinámicos, KV, PKI. | 3 Avanzado | 64 | BUSL-1.1 (source-available) | sin grupo |
| `age` | Cifrado de ficheros moderno y simple (clave/recipient) sin OpenPGP: CLI pequeña… | 1 Básico | 61 | BSD-3-Clause (OSI permisiva) | sin grupo |
| `bitwarden-clients` | Clientes oficiales de Bitwarden para gestionar credenciales y utilizar… | 1 Básico | 61 | GPL-3.0 + Bitwarden License (bitwarden_license/) (OSI copyleft) | sin grupo |
| `adguardhome` | Servidor DNS para filtrar anuncios y rastreadores de los dispositivos de una… | 1 Básico | 59 | GPL-3.0 (OSI copyleft) | alternativa |
| `sops` | Cifra secretos en YAML/JSON/ENV para GitOps con claves age, PGP o KMS… | 1 Básico | 55 | MPL-2.0 (OSI copyleft) | sin grupo |
| `keepassxc` | Gestor de contraseñas local multiplataforma (fork comunitario de KeePassX) con… | 1 Básico | 54 | GPL-2.0 o GPL-3.0 (OSI copyleft) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Pi-hole (`pi-hole`)

- **Repo:** https://github.com/pi-hole/pi-hole · EUPL-1.2 · nivel 1 · 68/100 · recomendado en «Bloqueo de anuncios por DNS»
- **Qué es:** Bloqueador de anuncios por DNS de código abierto (EUPL-1.2 según su archivo de licencia) mantenido por Pi-hole LLC y la comunidad desde 2014. Muy maduro.
- **Cuándo elegirlo:** Casos: bloquear anuncios en smart TV y apps móviles de toda la casa; ver qué dominios consultan los dispositivos de tu red.
- **Requisitos:** nivel 1: preparación sencilla; Shell; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -sSL https://install.pi-hole.net | bash` — fuente: https://github.com/pi-hole/pi-hole/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Pi-hole en una máquina Linux de prueba o contenedor y apunta el DNS de un equipo a ella. Éxito: El panel muestra consultas bloqueadas y las webs cargan sin anuncios.
- **Combina con:** `home-assistant` [15/domotica], `grafana` [10/bi], `coolify` [22/infraestructura], `wg-easy` [22/redes]
- **Alternativas:** `adguardhome`
- **Riesgos y avisos:** Alternativas (elige una): adguardhome. Instalar con `curl | bash` ejecuta un script remoto: revísalo antes.

### authentik (`authentik`)

- **Repo:** https://github.com/goauthentik/authentik · MIT + licencia Enterprise (authentik/enterprise/) · nivel 3 · 67/100 · recomendado en «Proveedores de identidad y SSO»
- **Qué es:** Identity provider (MIT + enterprise/ propietaria).
- **Cuándo elegirlo:** Casos: SSO delante de apps autoalojadas; MFA centralizado para el lab.
- **Requisitos:** nivel 3: proveedor de identidad con Docker Compose y flujos a configurar; Python, Cargo.toml, Makefile, go.mod, package.json, pyproject.toml; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up -d` — fuente: https://github.com/goauthentik/authentik/blob/main/website/docs/install-config/install/docker-compose.mdx
- **Primera prueba propuesta (no ejecutada):** Despliega con el Compose de docs.goauthentik.io y crea una aplicación de prueba. Éxito: Login SSO funcionando.
- **Combina con:** `vaultwarden`, `caddy` [22/infraestructura]
- **Alternativas:** `keycloak`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### Keycloak (`keycloak`)

- **Repo:** https://github.com/keycloak/keycloak · Apache-2.0 · nivel 3 · 67/100 · alternativa en «Proveedores de identidad y SSO»
- **Qué es:** IdP Apache-2.0 de Keycloak.
- **Cuándo elegirlo:** Casos: OIDC para un cluster de apps propias; federar un LDAP existente.
- **Requisitos:** nivel 3: servidor de identidad: realms, clientes y certificados; Java, pom.xml; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/keycloak/keycloak/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca el contenedor oficial de Keycloak en modo dev y abre la admin console. Éxito: Realm de prueba creado.
- **Combina con:** `vault`, `caddy` [22/infraestructura]
- **Alternativas:** `authentik`

### vaultwarden (`vaultwarden`)

- **Repo:** https://github.com/dani-garcia/vaultwarden · AGPL-3.0 · nivel 2 · 67/100 · recomendado en «Gestores de contraseñas»
- **Qué es:** Implementación alternativa no oficial del servidor de Bitwarden escrita en Rust, iniciada por @dani-garcia. Licencia AGPL-3.0. Es muy madura y popular para autoalojar (~71k estrellas, 1.37.5).
- **Cuándo elegirlo:** Casos: Estudiar alojamiento propio de una bóveda; Evaluar compatibilidad con clientes Bitwarden.
- **Requisitos:** nivel 2: un contenedor; requiere HTTPS y copias de seguridad; Docker o binario; dominio y HTTPS; volumen persistente; copias; bóveda ficticia; hardware prerequisites; API de IA: no; Docker o binario; dominio y HTTPS; volumen persistente; copias; bóveda ficticia.
- **Instalación (documentada en la fuente; no ejecutada):** `docker pull vaultwarden/server:latest` — fuente: https://github.com/dani-garcia/vaultwarden/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta un cliente Bitwarden a una instancia de prueba y guarda un registro ficticio Éxito: Puedes reconocer la URL de servidor y recuperar el registro
- **Combina con:** `bitwarden-clients`, `coolify` [22/infraestructura], `adguardhome`
- **Alternativas:** `keepassxc`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Sin alternativas declaradas. Haz copias de seguridad de la base de datos y de la carpeta `data/`; no expongas `/admin` sin token. Es un servidor alternativo no oficial; la bóveda web necesita HTTPS y contexto seguro; revisa las diferencias respecto al servidor Bitwarden.

### HashiCorp Vault (`vault`)

- **Repo:** https://github.com/hashicorp/vault · BUSL-1.1 · nivel 3 · 64/100
- **Qué es:** Gestor de secretos de HashiCorp/IBM bajo Business Source License 1.1 desde la 1.15 (source-available, no OSI); cada versión pasa a MPL-2.0 a los 4 años. OpenBao es el fork MPL-2.0.
- **Cuándo elegirlo:** Casos: centralizar secretos de un entorno propio; emitir credenciales dinámicas de DB de lab.
- **Requisitos:** nivel 3: gestión de secretos: unseal, políticas y almacenamiento; Go, Dockerfile, Makefile, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/hashicorp/vault/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Arranca Vault en modo dev (`vault server -dev`) según docs y escribe un secreto KV. Éxito: Lees el secreto con la CLI.
- **Combina con:** `sops`, `age`, `vaultwarden`
- **Riesgos y avisos:** BSL (source-available): no es OSI; revisa usos comerciales y la fecha de cambio de licencia. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

### age (`age`)

- **Repo:** https://github.com/FiloSottile/age · BSD-3-Clause · nivel 1 · 61/100
- **Qué es:** Herramienta de cifrado de FiloSottile (BSD-3).
- **Cuándo elegirlo:** Casos: cifrar un backup antes de subirlo; claves age para SOPS.
- **Requisitos:** nivel 1: preparación sencilla; Go, go.mod; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `brew install age` — fuente: https://github.com/FiloSottile/age/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala age (release/paquetes) y cifra un fichero de lab. Éxito: Descifrado con la clave privada.
- **Combina con:** `sops`, `vault`

### Bitwarden Clients (`bitwarden-clients`)

- **Repo:** https://github.com/bitwarden/clients · GPL-3.0 + Bitwarden License (bitwarden_license/) · nivel 1 · 61/100
- **Qué es:** Monorepo de los clientes oficiales de Bitwarden: web vault, extensión de navegador, escritorio y CLI. Lo mantiene Bitwarden, Inc. Es muy maduro (~14k estrellas, desktop-v2026.10.4).
- **Cuándo elegirlo:** Casos: Gestionar credenciales desde extensión y escritorio; Estudiar un flujo Send con contenido ficticio.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Cliente oficial de tu sistema; cuenta y servidor elegido; bóveda de prueba; hardware prerequisites; API de IA: no; Cliente oficial de tu sistema; cuenta y servidor elegido; bóveda de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/bitwarden/clients.git` — fuente: https://contributing.bitwarden.com/getting-started/clients/
- **Primera prueba propuesta (no ejecutada):** Guarda una credencial ficticia y comprueba que puedes recuperarla y sincronizarla Éxito: El registro aparece solo en la cuenta y bóveda esperadas
- **Combina con:** `vaultwarden`, `activepieces` [1/motores], `claude-code` [20/terminal]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Revisa la licencia antes de reutilizar código de `bitwarden_license/`. Este repositorio contiene clientes y no todo el servidor; las apps móviles viven en repositorios separados.

### AdGuardHome (`adguardhome`)

- **Repo:** https://github.com/AdguardTeam/AdGuardHome · GPL-3.0 · nivel 1 · 59/100 · alternativa en «Bloqueo de anuncios por DNS»
- **Qué es:** Servidor DNS de bloqueo de anuncios y rastreadores para toda la red, de AdGuard. Licencia GPL-3.0. Es muy maduro (~38k estrellas, v0.107.80) y sigue en la serie 0.107 desde hace años.
- **Cuándo elegirlo:** Casos: Filtrar dominios en una red propia; Estudiar consultas y reglas DNS.
- **Requisitos:** nivel 1: un binario o contenedor con asistente web de configuración; Equipo servidor; acceso de configuración DNS; cliente de prueba; hardware prerequisites; API de IA: no; Equipo servidor; acceso de configuración DNS; cliente de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `curl -s -S -L https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/scripts/install.sh | sh -s -- -v` — fuente: https://github.com/AdguardTeam/AdGuardHome/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Configura un único dispositivo de prueba y revisa una consulta en el registro DNS Éxito: Puedes identificar si el dominio se permitió o bloqueó y por qué regla
- **Combina con:** `home-assistant` [15/domotica], `activepieces` [1/motores], `vaultwarden`, `casaos` [22/infraestructura], `cleanyourtv` [15/personal], `optimizerduck` [15/personal]
- **Alternativas:** `pi-hole`
- **Riesgos y avisos:** Sin alternativas declaradas en el catálogo (Pi-hole no está catalogado). Bloquear por DNS no sustituye a un bloqueador en el navegador. El filtrado DNS no bloquea todo anuncio ni sustituye otras protecciones; no cambies toda la red para la primera prueba.

### SOPS (`sops`)

- **Repo:** https://github.com/getsops/sops · MPL-2.0 · nivel 1 · 55/100
- **Qué es:** Secrets OPerationS (MPL-2.0).
- **Cuándo elegirlo:** Casos: cifrar secrets de Kubernetes en Git; rotar claves age de un repo.
- **Requisitos:** nivel 1: preparación sencilla; Go, Makefile, go.mod; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/getsops/sops/blob/main/README.rst
- **Primera prueba propuesta (no ejecutada):** Instala sops (release) y cifra un YAML de lab con age. Éxito: El fichero en Git permanece cifrado.
- **Combina con:** `age`, `vault`

### KeePassXC (`keepassxc`)

- **Repo:** https://github.com/keepassxreboot/keepassxc · GPL-2.0 o GPL-3.0 · nivel 1 · 54/100 · alternativa en «Gestores de contraseñas»
- **Qué es:** Password manager local (GPL según COPYING; API NOASSERTION).
- **Cuándo elegirlo:** Casos: cofre local para el equipo de lab; TOTP + contraseñas sin nube.
- **Requisitos:** nivel 1: preparación sencilla; C++, CMakeLists.txt; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/keepassxreboot/keepassxc.git` — fuente: https://github.com/keepassxreboot/keepassxc/blob/develop/INSTALL.md
- **Primera prueba propuesta (no ejecutada):** Instala KeePassXC desde keepassxc.org y crea una base .kdbx de prueba. Éxito: Entradas guardadas y desbloqueables.
- **Combina con:** `sops`
- **Alternativas:** `vaultwarden`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION).

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-15-privacidad.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Credenciales y privacidad», lee `docs/alexandria/categoria-15-privacidad.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-15-privacidad.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
