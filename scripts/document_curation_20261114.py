"""Reviewed entries for the user's saved-resource document, 2026-11-14.

This dated editorial migration consumes the primary-source audit prepared by
import_document_repos.py. It adds public, distinct GitHub identities only and
never installs or runs their code. The private source document is not published.
"""
from __future__ import annotations

import base64
from collections import Counter
import json
from pathlib import Path
import re

from repo_intelligence.core.access import access_facts, access_routes
from repo_intelligence.core.catalog import slug

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / "data/reports/document-import-20261114"
DATE = "2026-11-14"

# GitHub identity | category | section | kind | plain-language function.
DATA = """
AcademySoftwareFoundation/OpenRV|12|edicion|app|Reproductor de revisión de video y secuencias de imágenes para comparar tomas y revisar trabajo audiovisual.
achimala/dream-loop|9|skills|skill|Skill que combina Blender, generación de imágenes y revisión por un agente para preparar visuales tridimensionales.
AdguardTeam/AdGuardHome|15|privacidad|server|Servidor DNS para filtrar anuncios y rastreadores de los dispositivos de una red desde una configuración central.
advplyr/audiobookshelf|15|lectura|server|Servidor personal para organizar audiolibros y podcasts, escuchar contenido y conservar el progreso de reproducción.
agentes-chat/agentes-chat|3|asistentes|agent|Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que colaboran con personas y herramientas.
AgriciDaniel/claude-obsidian|15|notas|skill|Instrucciones para que Claude Code clasifique, enlace y consulte fuentes dentro de una bóveda de notas de Obsidian.
AgriciDaniel/claude-seo|2|dominio|skill|Skills de Claude Code para revisar SEO técnico, contenido, presencia en buscadores de IA y otros aspectos de una web.
ai-boost/awesome-harness-engineering|2|guias|reference|Directorio de herramientas y patrones para diseñar el entorno, memoria, evaluación y permisos de agentes de IA.
ai-job-search-dev/ai-job-search|15|personal|skill|Proyecto basado en Claude Code para evaluar vacantes, adaptar currículums y preparar cartas e entrevistas de empleo.
AI4Finance-Foundation/FinRL|14|cuant|framework|Biblioteca y ejemplos para investigar estrategias de trading mediante aprendizaje por refuerzo y simulaciones.
alchaincyf/huashu-motion|12|programatico|skill|Skill para crear videos de presentación de productos con un agente de código, composición, música y revisión visual.
angr/angr|16|reversing|library|Plataforma en Python para analizar programas binarios mediante técnicas como ejecución simbólica y análisis de flujo.
anthropics/claude-agent-sdk-python|3|py|framework|SDK oficial de Python para integrar el bucle de Claude Code, herramientas, sesiones y hooks en una aplicación propia.
anyproto/anytype-ts|15|notas|app|Cliente de escritorio de Anytype para organizar notas, objetos y relaciones en un espacio de conocimiento personal.
AppFlowy-IO/AppFlowy|15|notas|app|Espacio de trabajo para notas, wikis y proyectos colaborativos, con funciones de IA y opciones de alojamiento propio.
arjun988/blender-skills|11|creacion-3d|skill|Skills para guiar a un agente por modelado y preparación de escenas en Blender mediante herramientas y conexiones MCP.
ashima/webgl-noise|9|animacion|library|Rutinas de ruido procedural para shaders de WebGL, útiles para crear texturas y efectos visuales en tiempo real.
AThevon/genjutsu|9|skills|skill|Skills de diseño y animación para agentes que trabajan con interfaces web, Android y plataformas de Apple.
ATK-zk/company-pixel-office|14|aprender|template|Demostración de una oficina de trading en pixel art para estudiar su interfaz y la representación visual de un equipo.
ayghri/i-have-adhd|2|escritura|skill|Skill para que un agente presente primero la respuesta y organice su salida con menos distracciones y rodeos.
bilawalsidhu/gods-eye-view|10|osint|app|Visualizador geoespacial en un globo 3D que reúne fuentes abiertas para explorar información espacial en el navegador.
bitwarden/clients|15|privacidad|app|Clientes oficiales de Bitwarden para gestionar credenciales y utilizar funciones como compartir información con Send.
blender/blender|11|creacion-3d|app|Código de Blender, la aplicación para modelar, animar, renderizar y editar escenas y contenido tridimensional.
breakfastquay/rubberband|12|edicion|library|Biblioteca de audio para modificar duración y tono de una grabación, integrada como código en otras herramientas.
cathrynlavery/diagram-design|13|diagramas|skill|Skill para que un agente cree diagramas explicativos con HTML y SVG, con criterios de composición y legibilidad.
ccxt/ccxt|14|bots|library|Biblioteca que unifica APIs de exchanges para consultar mercados y desarrollar integraciones de trading.
cheaper-inference/OmniRoute|6|serving|server|Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acceso.
chriswritescode-dev/opencode-manager|3|coding|agent|Interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil.
CloudAI-X/threejs-skills|9|skills|skill|Colección de instrucciones para que agentes programen escenas y experiencias 3D en la web con Three.js.
CMU-Perceptual-Computing-Lab/openpose|11|vision|model|Sistema de estimación de pose para detectar puntos del cuerpo, manos, rostro y pies en imágenes o video.
coollabsio/coolify|15|infraestructura|server|Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores propios.
CopilotKit/OpenDots|3|asistentes|agent|Plataforma de asistentes de IA persistentes que coordinan conversaciones, llamadas y servicios conectados.
CoplayDev/unity-mcp|5|servidores|mcp|Servidor MCP que permite a un asistente operar escenas, scripts y recursos dentro de un proyecto del editor Unity.
cursor/plugins|2|catalogos|reference|Especificación y colección oficial de plugins de Cursor para estudiar e instalar extensiones de ese agente.
dani-garcia/vaultwarden|15|privacidad|server|Servidor no oficial compatible con clientes Bitwarden para alojar una bóveda de credenciales en infraestructura propia.
daybrush/scenejs|9|animacion|library|Biblioteca JavaScript para crear y controlar animaciones mediante líneas de tiempo y propiedades de elementos.
disler/claude-code-hooks-mastery|2|metodologia|reference|Ejemplos y material para aprender a configurar hooks de Claude Code y ejecutar comprobaciones en su flujo de trabajo.
dnSpyEx/dnSpy|16|depuracion|app|Depurador y editor de ensamblados .NET para inspeccionar y analizar aplicaciones de esa plataforma.
docusealco/docuseal|13|pdf|server|Aplicación para preparar formularios y gestionar la firma electrónica de documentos, con opciones de despliegue propio.
dograh-hq/dograh|12|voz-agentes|agent|Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configurables.
DozenTwelve/Papermorph|12|programatico|skill|Skill que convierte libros en experiencias web animadas y narradas, con distintas rutas de voz y recursos visuales.
EpicGames/raddebugger|16|depuracion|app|Depurador gráfico nativo para inspeccionar procesos, código y memoria durante el análisis de programas.
ethanplusai/sellbird|1|marketing|agent|Plataforma de prospección por correo que documenta el uso de sesiones de Claude Code o Codex para sus agentes.
eugeniughelbur/obsidian-second-brain|15|notas|skill|Sistema de memoria y notas en Markdown para compartir contexto de trabajo entre agentes y una bóveda de Obsidian.
every-app/open-seo|1|marketing|server|Aplicación de análisis SEO que consulta datos de buscadores mediante DataForSEO y permite alojamiento propio.
eyaltoledano/claude-task-master|3|infra|agent|Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP.
facebookresearch/VideoPose3D|11|vision|model|Implementación de investigación para estimar pose humana 3D desde trayectorias de puntos 2D en secuencias de video.
FlashML-org/FreeToken|8|motores|engine|Herramientas para servir modelos de IA en hardware local mediante las rutas de inferencia y aceleración del proyecto.
freqtrade/freqtrade|14|bots|app|Bot de trading de criptomonedas con herramientas para preparar estrategias, hacer backtesting y operar en simulación.
frida/frida|16|reversing|app|Herramientas de instrumentación dinámica para observar y modificar el comportamiento de programas durante su ejecución.
garrytan/gstack|2|metodologia|skill|Conjunto de skills y herramientas para organizar planificación, implementación, revisión y pruebas con Claude Code.
Gathin23/cleanyourtv|15|personal|app|Herramienta para revisar y retirar aplicaciones preinstaladas de dispositivos Android TV o Google TV mediante ADB.
geeklee/srt-whiteboard-animation|12|programatico|skill|Skill para crear animaciones de pizarra con trazos y contenido organizados a partir de archivos de subtítulos SRT.
GiovanniPasq/agentic-rag-for-dummies|6|rag|template|Ejemplo de RAG con agentes y LangGraph para consultar documentos, con una ruta local basada en Ollama.
gitroomhq/postiz-app|1|marketing|server|Plataforma para preparar, programar y gestionar publicaciones en redes sociales, con integraciones y funciones de IA.
google-ai-edge/mediapipe|11|vision|library|Herramientas de aprendizaje automático para tareas de visión y procesamiento de medios en dispositivos y aplicaciones.
google/elephant-goldfish-model|2|metodologia|skill|Plugin con instrucciones para diseñar y revisar software con agentes mediante contextos y perspectivas complementarias.
google/filament|11|creacion-3d|library|Motor de renderizado físicamente basado para integrar gráficos 3D en aplicaciones móviles, web y de escritorio.
google/skills|2|catalogos|skill|Colección de skills para trabajar con productos y tecnologías de Google desde agentes de programación compatibles.
GoogleChrome/modern-web-guidance|9|skills|skill|Herramienta y skill para que un agente consulte documentación actual sobre prácticas y APIs de desarrollo web.
grafana/k6|16|pruebas|app|Herramienta de pruebas de carga para medir cómo responden aplicaciones y servicios bajo distintos niveles de tráfico.
greensock/gsap-skills|9|skills|skill|Skills oficiales con instrucciones y ejemplos para que agentes creen animaciones y utilicen plugins de GSAP.
guillaumeblanc/ozz-animation|11|creacion-3d|library|Biblioteca C++ y herramientas para preparar y reproducir animación esquelética dentro de motores y aplicaciones.
haydenschmitty/floorplan|7|codigo|skill|Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un proyecto.
HKUDS/Vibe-Trading|14|agentes|agent|Agente de investigación y trabajo con estrategias de trading que utiliza modelos y componentes configurables.
home-assistant/core|15|domotica|server|Motor de Home Assistant para conectar dispositivos y automatizar acciones del hogar con control local.
hummingbot/hummingbot|14|bots|app|Software para desarrollar y ejecutar bots de trading de criptomonedas mediante conectores y estrategias configurables.
hypit-ai/hypit|12|generativo|skill|Skills para agentes que organizan generación y edición de videos mediante modelos, servicios y recursos configurables.
iBotPeaches/Apktool|16|reversing|app|Herramienta para decodificar recursos y reconstruir paquetes APK de Android durante el análisis de una aplicación.
IceWhaleTech/CasaOS|15|infraestructura|server|Entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos domésticos.
icsharpcode/ILSpy|16|reversing|app|Descompilador de .NET para explorar ensamblados y estudiar el código y metadatos de aplicaciones compatibles.
itsfatduck/optimizerDuck|15|personal|app|Aplicación para revisar y ajustar opciones de rendimiento, privacidad y configuración de un equipo con Windows.
Jakeschincariol/instagram-agent-skill|2|dominio|skill|Skills de Claude para investigar ideas, preparar guiones y revisar contenido y publicaciones de una cuenta de Instagram.
Jakeschincariol/linkedin-agent-skill|2|dominio|skill|Skills de Claude para preparar publicaciones, comentarios y planificación de contenidos de una cuenta de LinkedIn.
jaypolanco96/pixel-hedge-fund|14|aprender|template|Demostración de una oficina financiera en pixel art con interfaz de análisis y conexiones configurables a mercados.
JCodesMore/ai-website-cloner-template|9|ia-ui|template|Plantilla para que un agente de código estudie una web de referencia y prepare una implementación de su interfaz.
jub0t/Concat|12|edicion|app|Editor de video local con interfaz y mecanismos de automatización mediante JSON-RPC y herramientas MCP.
K-Dense-AI/scientific-agent-skills|2|dominio|skill|Colección de skills y recursos para que agentes realicen tareas de investigación científica con herramientas de dominio.
kaankiziltug/logo-design-skill|9|skills|skill|Skill para diseñar logotipos con un agente, desde la idea y las referencias hasta SVG y comprobaciones de diseño.
karakeep-app/karakeep|15|notas|server|Gestor autoalojado de marcadores, notas e imágenes con búsqueda y funciones opcionales de clasificación mediante IA.
kepano/40-questions|15|personal|reference|Colección de preguntas para revisar un año o una década y reflexionar sobre objetivos, hábitos y decisiones personales.
kepano/defuddle|4|crawlers|library|Biblioteca para extraer el contenido principal de una página y convertirlo en texto o Markdown utilizable.
kepano/flexoki|9|estilos|reference|Paleta de color para texto, código e interfaces que puede servir de referencia al definir un sistema visual.
kepano/kepano-obsidian|15|notas|template|Plantilla de una bóveda de Obsidian para estudiar una forma de organizar notas e información personal.
kepano/obsidian-minimal|15|notas|app|Tema configurable de Obsidian para ajustar la apariencia y reducir distracciones al trabajar con notas.
KeygraphHQ/shannon|16|agentes|agent|Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autorizado.
konvajs/konva|9|componentes|library|Biblioteca de canvas para construir editores gráficos, diagramas e interfaces con formas y objetos interactivos.
kornia/kornia|11|vision|library|Biblioteca de visión por computador para incorporar geometría, transformaciones y procesamiento de imágenes en PyTorch.
kyjwang/PixelFund-AI|14|aprender|template|Aplicación de simulación bursátil con agentes e interfaz en pixel art para explorar carteras y operaciones virtuales.
l0ng-ai/openidea|3|coding|app|Entorno de desarrollo con editor, depurador, Git y herramientas para trabajar con código en distintos lenguajes.
latent-spaces/brag|12|programatico|skill|Skills para que un agente convierta un proyecto o sitio en un video breve de lanzamiento con composición y música.
LaurieWired/GhidraMCP|5|servidores|mcp|Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y analizar programas binarios.
lemomo-ai/lemo-opuscar|12|programatico|skill|Colección de estilos e instrucciones para crear piezas audiovisuales por código con Claude Code.
Leonxlnx/earshot|12|edicion|mcp|Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP.
LottieFiles/motion-design-skill|9|skills|skill|Skill con principios de ritmo, transiciones y composición del movimiento para diseñar animaciones de interfaces.
Lumiwealth/lumibot|14|cuant|framework|Framework de Python para desarrollar estrategias, realizar backtesting y conectar simulación u operación con brokers.
lyogavin/airllm|8|motores|engine|Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus componentes.
Maciek-roboblog/Claude-Code-Usage-Monitor|6|observabilidad|app|Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a partir de la información disponible.
magnitudedev/magnitude|8|motores|engine|Motor de inferencia local que adapta su ejecución al hardware y ofrece conexiones para agentes y aplicaciones.
maillab/cloud-mail|1|marketing|server|Plataforma de correo basada en servicios de Cloudflare para gestionar buzones y funciones de mensajería de un dominio.
majidmanzarpour/threejs-game-skills|9|skills|skill|Skills para que un agente construya juegos de navegador con Three.js, interfaz y recursos visuales o sonoros opcionales.
mementum/backtrader|14|cuant|framework|Biblioteca de Python para definir estrategias y estudiar su comportamiento mediante backtesting de datos de mercado.
metafizzy/zdog|9|animacion|library|Motor de gráficos pseudo-3D que permite dibujar y animar ilustraciones sencillas mediante canvas o SVG.
mitmproxy/mitmproxy|16|pruebas|app|Proxy interactivo para inspeccionar tráfico HTTP y HTTPS al depurar aplicaciones o realizar pruebas autorizadas.
mlightcad/awesome-cad|11|creacion-3d|reference|Directorio de programas, bibliotecas y recursos de diseño asistido por computadora organizados por especialidad.
morluto/awesome-reverse-engineering|16|referencias|reference|Directorio de herramientas y recursos para aprender análisis de binarios, aplicaciones, firmware y protocolos.
morluto/rea|16|agentes|skill|Herramientas e instrucciones para estudiar el comportamiento y la estructura de software mediante agentes de código.
mromidev/claude-animated-shorts|12|programatico|skill|Skill de Claude para crear cortos animados por código combinando personajes y escenas con Three.js y Remotion.
musistudio/claude-code-router|6|serving|server|Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control local.
mvanhorn/mvanhorn|2|guias|reference|Perfil público de mvanhorn para consultar sus proyectos, herramientas y contribuciones de desarrollo.
myshell-ai/MeloTTS|12|tts|model|Biblioteca de texto a voz con modelos y ejemplos para sintetizar narración en varios idiomas compatibles.
NandhaKishorM/laya|7|modelos|model|Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados.
NationalSecurityAgency/ghidra|16|reversing|app|Conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria.
nautechsystems/nautilus_trader|14|cuant|framework|Motor de trading y backtesting con arquitectura orientada a eventos para investigar y desarrollar estrategias.
Nutlope/hallmark|9|skills|skill|Skill de diseño para agentes que ayuda a construir interfaces con decisiones visuales más específicas y coherentes.
Nutlope/jev-fraud|3|experimentos|template|Demostración de clasificación con modelos y servicios de IA para estudiar un flujo de detección de fraude.
obsidianmd/jsoncanvas|15|notas|reference|Especificación abierta de JSON Canvas para describir nodos y conexiones de un lienzo visual en un archivo.
obsidianmd/obsidian-clipper|15|notas|app|Extensión oficial para capturar páginas y fragmentos de la web y guardarlos como notas en Obsidian.
obsidianmd/obsidian-help|15|notas|reference|Documentación oficial de Obsidian para aprender sus funciones, configuración y formas de organizar una bóveda.
obsidianmd/obsidian-importer|15|notas|app|Plugin oficial para convertir datos de otras aplicaciones en archivos Markdown que puedes abrir en Obsidian.
obsidianmd/obsidian-releases|15|notas|app|Repositorio de distribución de Obsidian y sus listados de plugins y temas; no contiene el código completo de la aplicación.
obsidianmd/obsidian-sample-plugin|15|notas|template|Plantilla oficial para programar un plugin de Obsidian con una estructura inicial y configuración de desarrollo.
obsidianmd/obsidian-skills|15|notas|skill|Skills para que un agente trabaje con Obsidian y sus formatos de notas, bases de datos y lienzos.
onyx-dot-app/onyx|6|rag|agent|Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con conectores y control de acceso.
oomol-lab/pdf-craft|13|ocr|library|Herramienta para convertir libros escaneados en PDF a documentos editables mediante rutas de OCR y procesamiento.
open-mmlab/mmpose|11|vision|model|Herramientas y modelos de estimación de pose, incluidos RTMPose y otras variantes para analizar movimiento humano.
OpenDroneMap/ODM|10|geoespacial|app|Herramientas para convertir fotografías aéreas en mapas, nubes de puntos, modelos 3D y modelos de elevación.
openfilm/openfilm|12|programatico|skill|Herramientas y skill para que un agente cree proyectos de video y permita editar después sus elementos.
openkursar/hello-halo|3|asistentes|agent|Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con cuentas de IA o proveedores API.
paperless-ngx/paperless-ngx|13|gestion|server|Gestor documental autoalojado para importar, reconocer texto, buscar y archivar documentos escaneados.
patch-gg/pixelfx|9|animacion|library|Colección de efectos de pixel art hechos con código y una skill para ayudar a generar efectos propios.
pencil2d/pencil|12|edicion|app|Aplicación para crear animación 2D dibujada a mano mediante herramientas de dibujo y una línea de tiempo.
petergyang/no-ai-slop|2|escritura|skill|Skill para revisar escritura y eliminar patrones repetitivos o frases poco específicas en textos generados con IA.
piqnt/planck.js|9|animacion|library|Motor de física 2D para simular cuerpos, colisiones y uniones dentro de juegos o aplicaciones JavaScript.
pmndrs/react-three-rapier|9|animacion|library|Integración del motor de física Rapier con React Three Fiber para añadir simulación a escenas tridimensionales.
polakowo/vectorbt|14|cuant|framework|Biblioteca de análisis cuantitativo para explorar señales y comparar estrategias sobre datos de mercado.
Polymarket/py-clob-client|14|bots|library|Cliente Python antiguo para la API de órdenes de Polymarket; está archivado y conviene revisar su sucesor.
Polymarket/py-sdk|14|bots|library|SDK Python de Polymarket para integrar funciones de su plataforma mediante las APIs y credenciales correspondientes.
qybaihe/bla|16|defensa|app|Herramientas para aplicar protecciones y comprobar superficies de software frente a análisis automatizado por agentes.
radareorg/radare2|16|reversing|app|Conjunto de herramientas de consola para inspeccionar, desensamblar y depurar programas y archivos binarios.
regl-project/regl|9|animacion|library|Biblioteca funcional para organizar comandos de renderizado WebGL y dibujar gráficos acelerados en una aplicación web.
rizinorg/rizin|16|reversing|app|Herramientas para analizar binarios y estudiar programas mediante desensamblado, depuración y otras funciones de consola.
SakanaAI/fugu|3|asistentes|agent|Ejemplos y acceso a un sistema multiagente de Sakana que se consume como un servicio de modelos mediante API.
shepherd-agents/shepherd|3|infra|framework|Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus recorridos.
shubham-goel/4D-Humans|11|vision|model|Implementación de investigación para reconstruir y seguir personas en 3D a partir de imágenes o secuencias de video.
skylot/jadx|16|reversing|app|Descompilador de archivos DEX y APK para explorar código Java reconstruido y recursos de aplicaciones Android.
slavingia/skills|2|dominio|skill|Skills basadas en ideas de The Minimalist Entrepreneur para orientar trabajo de negocio y emprendimiento con un agente.
storytold/craft-anything|16|agentes|app|Herramientas para estudiar cómo funciona una aplicación y ayudar a construir una implementación propia con agentes.
supabase/supabase|15|infraestructura|server|Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplicaciones.
superdesigndev/treg|5|servidores|mcp|Registro y conexión de herramientas para agentes que organiza acceso a servicios, cuentas y credenciales de proveedores.
syncthing/syncthing|15|archivos|app|Aplicación para sincronizar archivos entre dispositivos directamente y controlar qué carpetas se comparten.
Tejashmakwana/motionmaxxing|12|programatico|skill|Skill para mejorar composición, ritmo y movimiento de videos creados con agentes y herramientas de código.
tensorflow/tfjs-models|11|vision|library|Colección de modelos preparados para TensorFlow.js que permite integrar tareas de aprendizaje automático en aplicaciones.
THU-MAIC/OpenMAIC|15|aprendizaje|agent|Aplicación educativa con varios agentes que prepara clases y actividades mediante modelos y recursos configurables.
Universal-Debloater-Alliance/universal-android-debloater-next-generation|15|personal|app|Interfaz para revisar y retirar paquetes preinstalados de dispositivos Android mediante ADB y listas de aplicaciones.
usestrix/strix|16|agentes|agent|Agente de pruebas de seguridad para aplicaciones, con rutas de API, modelos locales y acceso documentado de ChatGPT.
Vanilagy/mediabunny|12|edicion|library|Biblioteca TypeScript para leer, escribir y convertir archivos de audio y video directamente en aplicaciones web.
vercel-labs/json-render|9|ia-ui|library|Framework para generar interfaces desde una representación JSON y un catálogo de componentes definido por el desarrollador.
vercel-labs/ui|9|ia-ui|library|Colección de comportamientos y recursos para que agentes construyan interfaces con patrones de interacción definidos.
viettranx/3dviz-pro-max|9|skills|skill|Skill para convertir ideas en escenas y visualizaciones 3D con Three.js o Blender desde un agente de código.
Vincentwei1021/video-shotcraft|12|programatico|skill|Skill para crear videos de producto editables con Remotion, composición de planos, movimiento y trabajo de sonido.
virgiliojr94/book-to-skill|2|metodologia|skill|Herramientas para convertir un libro técnico en PDF en una skill que un agente pueda consultar durante el trabajo.
volcengine/OpenViking|6|memoria|server|Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información.
WebODM/WebODM|10|geoespacial|server|Interfaz para procesar fotografías aéreas y obtener mapas y modelos con el ecosistema de OpenDroneMap.
WerWolv/ImHex|16|reversing|app|Editor hexadecimal para inspeccionar archivos binarios, identificar estructuras y describir formatos mediante patrones.
wheresryan22/anatomy|9|skills|skill|Skill para crear ilustraciones isométricas e interactivas de máquinas y sistemas con SVG y efectos visuales opcionales.
x64dbg/x64dbg|16|depuracion|app|Depurador de Windows para inspeccionar programas en ejecución y estudiar instrucciones, memoria y llamadas.
xiph/rnnoise|12|edicion|model|Biblioteca de reducción de ruido de audio que utiliza una red neuronal para mejorar señales de voz localmente.
yohanshin/WHAM|11|vision|model|Implementación de investigación para reconstruir movimiento humano tridimensional a partir de secuencias de video.
zanwei/design-dna|9|skills|skill|Skill para analizar referencias visuales, extraer decisiones de diseño y generar interfaces con un estilo coherente.
zeux/meshoptimizer|11|creacion-3d|library|Biblioteca para optimizar geometría y reducir el coste de almacenar y renderizar mallas tridimensionales.
zhuyansen/awesome-ai-reverse-engineering|16|referencias|reference|Directorio de herramientas de ingeniería inversa y análisis de software que pueden trabajar con agentes de IA.
zju3dv/EasyMocap|11|vision|model|Herramientas y ejemplos para capturar y reconstruir movimiento humano a partir de cámaras y secuencias de imágenes.
ZSeven-W/dsh-android|3|coding|plugin|Plugin de DeepSeek Harness para operar un emulador o dispositivo Android y revisar aplicaciones desde el agente.
ZSeven-W/dsh-game-studio|3|coding|plugin|Plugin de DeepSeek Harness para preparar y probar juegos pequeños con una interfaz de trabajo dentro del agente.
ZSeven-W/dsh-ios|3|coding|plugin|Plugin de DeepSeek Harness para desarrollar y operar aplicaciones en simuladores iOS o dispositivos compatibles.
ZSeven-W/dsh-noema|6|memoria|plugin|Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración.
ZSeven-W/dsh-qa|7|calidad|plugin|Plugin de DeepSeek Harness para explorar aplicaciones, guardar evidencia y preparar recorridos de pruebas reproducibles.
"""


def rows():
    result = {}
    for line in DATA.strip().splitlines():
        name, category, section, kind, one = line.split("|", 4)
        assert 60 <= len(one) <= 175, (name, len(one))
        result[name.lower()] = dict(name=name, cat=int(category), sub=section, kind=kind, one=one)
    return result


def names(value):
    return set(value.lower().split())


FORCED_IDS = {
    "google/skills":"google-skills", "slavingia/skills":"minimalist-entrepreneur-skills",
    "home-assistant/core":"home-assistant", "vercel-labs/ui":"ui-sdk",
    "bitwarden/clients":"bitwarden-clients",
}
DISPLAY = {"home-assistant/core":"Home Assistant", "vercel-labs/ui":"UI SDK (Vercel)",
           "bitwarden/clients":"Bitwarden Clients", "anyproto/anytype-ts":"Anytype Desktop",
           "obsidianmd/obsidian-releases":"Obsidian: distribución y extensiones"}
READY = names("openrv anytype-ts appflowy bitwarden-clients blender dnspy raddebugger ilspy optimizerduck obsidian-minimal obsidian-clipper obsidian-importer obsidian-releases pencil imhex x64dbg syncthing openidea hello-halo")
LOCAL = names("openpose videopose3d freetoken mediapipe kornia airllm magnitude melotts laya mmpose 4d-humans tfjs-models rnnoise wham easymocap finrl")
LOCAL_CHOICE = names("agentic-rag-for-dummies onyx pdf-craft openmaic openviking shannon strix vibe-trading omniroute craft-anything")
OPTIONAL = names("appflowy karakeep postiz-app json-render earshot dograh")
REQUIRED = names("opendots claude-task-master jev-fraud fugu")
PROVIDER = names("opencode-manager vibe-trading claude-code-router")
MCP_EXTRA = names("claude-task-master dograh onyx craft-anything bla")
MODEL_FAMILY = names("openpose videopose3d freetoken airllm magnitude melotts laya mmpose 4d-humans tfjs-models wham easymocap finrl")
ROLE = {"skill":"skill", "reference":"directory", "library":"library", "app":"app", "server":"platform", "model":"runtime", "mcp":"runtime", "agent":"app", "framework":"library", "engine":"runtime", "template":"library", "plugin":"library"}

ENTRY_COMMANDS = {
    "claude-agent-sdk-python":"pip install claude-agent-sdk",
    "papermorph":"npx skills add DozenTwelve/Papermorph --skill papermorph --agent claude-code",
    "hypit":"npx skills add hypit-ai/hypit -g",
    "brag":"npx skills add https://github.com/latent-spaces/brag --skill brag-slim",
    "openfilm":"npx skills add openfilm/openfilm",
    "laya":"python -m pip install laya", "pdf-craft":"python -m pip install pdf-craft",
    "ui-sdk":"npm install @ui-sdk/react @ui-sdk/core", "design-dna":"npx skills add zanwei/design-dna",
    "ccxt":"pip install ccxt", "konva":"npm install konva", "airllm":"pip install airllm",
    "backtrader":"pip install backtrader", "vectorbt":"pip install vectorbt", "mediabunny":"npm install mediabunny",
    "defuddle":"npm install defuddle", "planck-js":"npm install planck",
}

NEW_CATEGORIES = [
    {"num":15,"title":"Organizar notas, archivos y servicios personales","emoji":"🗂️",
     "desc":"Notas, sincronización, privacidad, aprendizaje y servidores personales. Distingue una aplicación lista, un plugin y la infraestructura que debes administrar.",
     "file":"human/categorias/15-notas-archivos-y-servicios-personales.md",
     "subs":[{"key":key,"title":title} for key,title in [
         ("notas","Notas, bóvedas y conocimiento personal"),("archivos","Sincronización y gestión de archivos"),
         ("privacidad","Credenciales y privacidad"),("infraestructura","Alojamiento y backend"),
         ("lectura","Libros, podcasts y bibliotecas personales"),("domotica","Automatización del hogar"),
         ("personal","Herramientas y organización personal"),("aprendizaje","Aprendizaje asistido")]]},
    {"num":16,"title":"Analizar software y comprobar su seguridad","emoji":"🔍",
     "desc":"Depuradores, descompiladores, análisis de binarios y agentes de pruebas. Trabaja sobre software propio o con autorización y separa análisis, modificación y pruebas activas.",
     "file":"human/categorias/16-analisis-de-software-y-seguridad.md",
     "subs":[{"key":key,"title":title} for key,title in [
         ("reversing","Ingeniería inversa y formatos binarios"),("depuracion","Depuración e inspección de procesos"),
         ("pruebas","Tráfico, rendimiento y pruebas"),("agentes","Análisis y pruebas con agentes"),
         ("defensa","Protección y verificación de software"),("referencias","Directorios y aprendizaje")]]},
]
NEW_GOALS = [
    {"id":"notas","title":"Organizar notas y conocimiento","description":"Elegir una aplicación o un conjunto pequeño de extensiones para guardar, enlazar y consultar información.",
     "starters":["obsidian-releases","anytype-ts","appflowy"],"guided":["obsidian-releases","anytype-ts","appflowy","claude-obsidian","obsidian-second-brain"],"categories":[15],"keywords":["notas","obsidian","boveda","conocimiento personal"]},
    {"id":"servicios","title":"Alojar servicios propios","description":"Entender qué aplicación vas a alojar, qué servidor necesita y qué servicios y cuentas se configuran aparte.",
     "starters":["coolify","casaos","home-assistant"],"guided":["coolify","casaos","home-assistant","vaultwarden","audiobookshelf"],"categories":[15],"keywords":["servidor propio","autoalojar","selfhost","domotica","nube personal"]},
    {"id":"seguridad","title":"Analizar software y su seguridad","description":"Escoger entre inspeccionar código, estudiar un binario o ejecutar pruebas en un entorno autorizado.",
     "starters":["ghidra","jadx","shannon"],"guided":["ghidra","jadx","imhex","shannon","strix"],"categories":[16],"keywords":["seguridad","ingenieria inversa","pentest","depurar","binario"]},
    {"id":"3d","title":"Crear escenas y proyectos 3D","description":"Elegir una aplicación visual, una biblioteca o instrucciones para un agente; revisar por separado modelos y recursos externos.",
     "starters":["blender","3dviz-pro-max","unity-mcp"],"guided":["blender","3dviz-pro-max","blender-skills","threejs-skills","unity-mcp"],"categories":[9,11],"keywords":["3d","blender","escena","modelado","motion capture"]},
]


def access_profile(entry, source, text):
    rid, kind = entry["id"], entry["kind"]
    a = access_facts({})
    a.update(mode="software", api="not_required", local_model="not_applicable", cost="no_model_fee", hardware="ordinary", review="documented", checked_at=DATE,
             scope="Función básica descrita en el README; modelos, servicios opcionales y despliegues se revisan por separado.",
             api_note="La función básica es software o material que no necesita llamar a un modelo de IA.",
             local_note="La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.",
             cost_note="No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos.",
             hardware_note="Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.",
             sources=[source["html_url"]], source_blob_sha=source["sha"])
    if kind == "reference":
        a.update(mode="reference", scope="Leer la documentación, especificación o directorio. Los ejemplos enlazados tienen sus propios requisitos.")
    if kind in {"skill","plugin"}:
        a.update(mode="agent_extension", cost="host_plan",
                 api_note="Las instrucciones o el plugin utilizan el acceso del agente anfitrión; las herramientas conectadas pueden requerir credenciales propias.",
                 subscription_note="Consume el acceso y los límites del agente donde lo configures. No incluye servicios externos de generación, datos o alojamiento.",
                 local_note="Estas instrucciones no incluyen un modelo. El modelo y su ubicación dependen del agente anfitrión.",
                 cost_note="Necesitas acceso al agente compatible. Comprueba además los recursos, APIs y servicios que active cada función.")
        # These entries are reviewed agent extensions, not arbitrary occurrences
        # of client names in an application's source tree or sponsor list.
        if kind == "skill":
            if re.search(r"claude(?:[ -]code)?",text,re.I): a["claude_code"]="host"
            if re.search(r"\bcodex\b",text,re.I): a["codex"]="host"
        else:
            a["other_access"]="Plugin para DeepSeek Harness (DSH). La cuenta, API o modelo se configura en ese anfitrión; no se declara instalación nativa en Claude Code o Codex."
    if kind == "mcp":
        a.update(mode="agent_extension", claude_code="connector", codex="connector", cost="host_plan",
                 api_note="El servidor aporta herramientas a un cliente MCP; el cliente aporta el modelo. Revisar los servicios que usa cada herramienta.",
                 cost_note="El modelo se consume en el cliente MCP. Programas, licencias y servicios conectados pueden tener requisitos y tarifas independientes.",
                 subscription_note="Configura este servidor en un cliente MCP compatible, incluido Claude Code o Codex. Sus servicios y permisos se preparan aparte.")
    if rid in LOCAL or kind == "engine":
        a.update(local_model="supported", hardware="model_dependent",
                 api_note="La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.",
                 local_note="El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.",
                 cost_note="La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos.",
                 hardware_note="RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.")
    if rid in OPTIONAL:
        a.update(api="optional", cost="choice", api_note="La función básica y las funciones de IA se configuran por separado; activar un proveedor puede añadir credenciales y consumo.")
    if rid in PROVIDER:
        a.update(api="depends", cost="choice", local_model="not_documented",
                 cost_note="El código de la aplicación no incluye el consumo de su proveedor. Comprueba plan, cuotas, infraestructura y servicios conectados.",
                 api_note="El agente o la pasarela necesita un proveedor. Comprueba en su configuración la ruta de sesión, API o modelo elegida.")
    if rid in LOCAL_CHOICE:
        a.update(api="optional", cost="choice", local_model="supported", hardware="model_dependent",
                 cost_note="La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan.",
                 api_note="El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos.",
                 local_note="Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos.")
    if rid in REQUIRED:
        a.update(api="required", cost="usage_based", local_model="not_documented",
                 api_note="La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla.",
                 cost_note="Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo.")
    if rid == "claude-agent-sdk-python":
        a.update(api="optional", cost="choice", claude_code="native",
                 cost_note="El uso consume el acceso de Claude configurado: límites del plan o créditos y facturación de API. El paquete del SDK no incluye una cuenta ni uso ilimitado.",
                 api_note="El SDK utiliza Claude Code. Comprueba su autenticación: una sesión del plan y una API key son rutas distintas.",
                 subscription_note="La documentación oficial distingue el uso del SDK con un plan compatible del acceso por API y sus límites.")
        a["sources"].append("https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan")
    if rid in {"agentes-chat","hello-halo","sellbird"}:
        a.update(api="optional" if rid!="sellbird" else "not_required", cost="choice",
                 cost_note="El razonamiento consume el plan o proveedor configurado. Alojamiento, conectores y otros servicios se evalúan aparte.",
                 claude_code="project_integration", codex="project_integration",
                 api_note="El README documenta usar una cuenta o sesión del agente, además de las otras rutas que admita el producto.",
                 subscription_note="Es una integración descrita por este proyecto. Configura la ruta concreta y comprueba sus límites; no se presenta como acceso universal a todas las APIs.")
        if rid == "agentes-chat": a["subscription_note"] += " El autor indica que la integración con Codex sigue en pruebas."
        if rid == "sellbird": a["cost_note"]="El razonamiento usa tu plan de Claude Code o Codex; correo, búsqueda de contactos, verificación de direcciones y otros servicios tienen requisitos y posibles tarifas propios."
    if rid in {"shannon","openviking"}:
        a["codex"]="project_integration"
        a["subscription_note"]="El README documenta una ruta de autenticación de Codex. Comprueba la configuración y las limitaciones de esa ruta; otras funciones y proveedores se configuran aparte."
    if rid == "shannon":
        a["claude_code"]="not_documented"
        a["subscription_note"] += " La versión actual declara que no usa suscripciones de Claude Code; la documentación remite a 1.9.0 para la ruta antigua."
    if rid == "strix":
        a["other_access"]="El README documenta iniciar sesión con ChatGPT Plus/Pro, además de API y modelos locales. No se afirma que instalar la CLI de Codex sea su método de acceso."
    if rid == "craft-anything":
        a.update(claude_code="project_integration", codex="unconfirmed",
                 subscription_note="Construir utiliza el programa Claude Code instalado y su sesión. El adaptador de Codex existe, pero el autor indica que no se ha verificado en una instalación real. Los endpoints locales se describen para preguntas y análisis.")
    if rid == "onyx":
        a.update(claude_code="connector",codex="connector",
                 subscription_note="Los agentes pueden consultar Onyx mediante MCP. El modelo y el procesamiento de Onyx conservan su configuración y sus costes; la sesión del cliente no los sustituye.")
    if rid == "dograh":
        a.update(claude_code="connector",codex="connector",hardware="ordinary",
                 api_note="El inicio documentado incluye claves generadas y una pila gestionada; también permite conectar proveedores propios. No se deduce de ello que sus modelos sean locales.",
                 subscription_note="La skill de configuración puede ayudar a instalar y el servidor MCP permite gestionar agentes. La voz y el razonamiento de las llamadas utilizan la pila de Dograh o los proveedores configurados.",
                 cost_note="Revisar el acceso a la pila de Dograh y los proveedores de voz, modelos y telefonía; sus tarifas no se cubren automáticamente con el plan del agente.")
    if rid in {"open-seo","treg"}:
        a.update(cost="choice", api_note="La función principal conecta servicios externos; sus claves no equivalen necesariamente a una API de un modelo de lenguaje.")
        a["cost_note"] = "OpenSEO autoalojado necesita una clave de DataForSEO y su consumo se paga al proveedor. La modalidad alojada tiene condiciones propias." if rid=="open-seo" else "Las herramientas del registro pueden consumir saldo o cuentas de servicios. El modelo se usa en el cliente MCP; verifica ambos costes por separado."
    if rid == "earshot":
        a.update(local_model="supported",hardware="ordinary",cost="choice",api="optional",
                 cost_note="Los modelos de audio locales consumen CPU, memoria y disco. La crítica opcional mediante Gemini tiene el acceso y las cuotas de ese proveedor.",
                 local_note="El análisis de audio se ejecuta con modelos locales en CPU. La crítica con LLM es una función opcional separada.",
                 api_note="La herramienta opcional llm_critique utiliza GEMINI_API_KEY; las herramientas locales de audio no implican ese consumo.")
    if rid == "pixelfund-ai":
        a.update(api="unconfirmed",cost="unconfirmed",local_model="unconfirmed",review="pending",
                 api_note="El README describe agentes y simulación, pero no resuelve qué acceso a modelos exige cada proveedor. Revisa la guía SETUP y su configuración antes de asumir coste cero.")
    if rid == "omniroute":
        a.update(claude_code="project_integration",codex="project_integration",
                 subscription_note="El proyecto documenta conexiones de proveedores y modos de enrutamiento con cuotas de planes. Configura únicamente cuentas admitidas y revisa cada ruta; auto/thrifty puede utilizar alternativas de pago.")
    if rid == "magnitude":
        a["subscription_note"]="El motor local puede conectarse a agentes como Codex o Claude Code como backend. Eso no convierte la suscripción del agente en el acceso de Magnitude: la inferencia se realiza con tus modelos y recursos locales."
    if rid == "hypit":
        a.update(api="optional",cost="choice",local_model="supported",
                 api_note="Las instrucciones se usan en el agente. El README permite configurar la generación con HypiHub, APIs propias o modelos locales; cada ruta se prepara aparte.",
                 local_note="El autor menciona modelos locales como una ruta de generación. Confirma la compatibilidad de cada etapa y los recursos necesarios.")
    if rid in {"dream-loop","huashu-motion","papermorph","threejs-game-skills"}:
        a["cost_note"] += " La generación externa de imágenes, clips, música o voces es una configuración distinta: el plan del agente no incluye automáticamente esas generaciones."
    if rid == "pixelfx":
        a["subscription_note"]="Los efectos de código no necesitan un LLM. La skill opcional para crear efectos consume el modelo y los límites de tu agente."
    if entry["cat"] == 14:
        a["cost_note"] += " Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista."
    if rid in {"bitwarden-clients","vaultwarden","obsidian-releases"}:
        a["cost_note"] += " Consulta por separado la licencia de la aplicación y las funciones o servicios alojados de pago; un repositorio de distribución no demuestra que toda la aplicación tenga código abierto."
    return a


def starting(entry, source, text, access, metadata):
    rid,kind=entry["id"],entry["kind"]
    audience="ready_app" if rid in READY else "agent" if kind in {"skill","plugin","mcp"} else "reading" if kind=="reference" else "developer" if kind in {"library","framework","template"} else "setup"
    prereq=[]
    if kind=="reference":
        steps=["Abre el material original y localiza la sección relacionada con tu tarea.","Elige una referencia o ejemplo; revisa sus requisitos y su procedencia antes de instalar nada.","Conserva solo las piezas que necesitas y consulta la ficha de cada proyecto enlazado."]
    elif kind in {"skill","plugin"}:
        prereq=["El agente compatible indicado por el proyecto y acceso activo al modelo de ese agente."]
        steps=["Abre la instalación del README y elige la ruta para el agente que utilizas.","Añade la skill o el plugin concreto; prepara los programas y servicios que indique su documentación.","Pide una primera tarea pequeña sobre archivos de prueba y comprueba qué herramientas y cuentas activa."]
    elif kind=="mcp":
        prereq=["Un cliente MCP compatible y el programa o servicio que va a controlar la herramienta."]
        steps=["Prepara el servidor y sus dependencias siguiendo la configuración del README.","Añade el comando o la URL en el cliente MCP y configura los permisos y credenciales de los servicios conectados.","Comprueba que aparecen sus herramientas y prueba una consulta pequeña antes de permitir modificaciones."]
    elif audience=="ready_app":
        prereq=["Un sistema compatible y una copia de datos o archivos para la primera prueba."]
        steps=["Abre las descargas o la web de la aplicación enlazadas por el autor; elige la versión para tu sistema.","Sigue su guía de inicio y configura únicamente la función que necesitas probar.","Abre un archivo o caso pequeño, guarda un resultado y comprueba que puedes recuperarlo antes de importar material real."]
    elif kind in {"library","framework","template"}:
        prereq=["Un entorno de desarrollo compatible con el lenguaje y los requisitos del README."]
        steps=["Prepara un proyecto o una copia de ejemplo siguiendo los requisitos originales.","Instala las dependencias documentadas y configura los datos, modelos o servicios necesarios para ese ejemplo.","Ejecuta la prueba mínima y revisa la salida antes de integrar la pieza en tu aplicación."]
    elif kind in {"model","engine"}:
        prereq=["Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida."]
        steps=["Elige el modelo y el backend que documenta el proyecto para tu sistema.","Prepara las dependencias y los pesos; no uses una cifra promocional como garantía para tu hardware.","Procesa una muestra pequeña y revisa calidad, tiempo y memoria antes de aumentar el tamaño de la tarea."]
    else:
        prereq=["Un entorno de instalación o servidor y las dependencias indicadas por el README."]
        steps=["Elige la instalación documentada: aplicación, paquete, contenedor o despliegue desde código.","Prepara sus dependencias y configura el acceso y los servicios descritos en la ficha.","Arranca un ejemplo pequeño y verifica el resultado antes de importar datos, conectar servicios reales o programar tareas."]
    if rid.startswith("obsidian-") or rid in {"claude-obsidian","kepano-obsidian"}:
        prereq.append("Obsidian y una bóveda de prueba; instalar una extensión no equivale a instalar la aplicación principal.")
    if entry["cat"]==16:
        prereq.append("Software o sistemas propios o con autorización, y un entorno de prueba separado del uso real.")
    if entry["cat"]==14:
        steps=["Elige un ejemplo de consulta de datos, backtesting o simulación que no envíe órdenes reales.","Prepara datos de prueba y, si el proveedor lo requiere, una cuenta y credenciales de solo lectura; revisa sus cuotas por separado.","Comprueba los resultados y el coste observado. La ejecución con fondos es otra configuración y no se activa como parte de esta primera prueba."]
    if rid.startswith("dsh-"):
        prereq.append("DeepSeek Harness y los controladores específicos que indica el plugin.")
    if rid=="dsh-ios":prereq.append("Un Mac con el entorno de desarrollo de Apple para el simulador o el dispositivo iOS.")
    if rid=="dsh-android":prereq.append("ADB y un emulador o dispositivo Android preparado para desarrollo.")
    command=ENTRY_COMMANDS.get(rid,"")
    if command and command not in text:command=""
    entry_url=""
    if audience=="ready_app":
        website=metadata.get("homepage") or ""
        if website.startswith("https://") and website in text:entry_url=website
        releases=metadata["html_url"]+"/releases"
        if releases in text:entry_url=releases
    if rid=="pdf-craft":
        entry_url="https://pdfcraft.ai/pdf-craft/"
        steps=["Elige entre la web del autor, OCR remoto con credenciales propias o inferencia local con GPU.","Prueba un PDF corto; OCR, traducción y extracción de metadatos tienen configuraciones de modelo independientes.","Abre el Markdown o EPUB generado y revisa el orden, texto y tablas antes de convertir un libro completo."]
    custom={
        "blender":["Para usar el programa, elige una distribución preparada de Blender; compilar este espejo de código es una ruta para desarrolladores.","Abre una escena de prueba y aprende a mover objetos, cámara e iluminación con la guía de inicio del autor.","Guarda el archivo y renderiza una imagen pequeña antes de añadir plugins, modelos o agentes."],
        "obsidian-releases":["Instala Obsidian mediante sus distribuciones; este repositorio reúne versiones y listados de extensiones, no el código completo de la aplicación.","Crea una bóveda de prueba y escribe dos notas con un enlace entre ellas.","Añade un plugin o tema solo cuando necesites su función, y comprueba cómo guarda los datos."],
        "anytype-ts":["Elige el instalador de Anytype para tu sistema en las descargas del proyecto.","Crea un espacio de prueba y añade unas notas y relaciones para entender su modelo de objetos.","Revisa exportación, sincronización y opciones de cuenta antes de trasladar tu información."],
        "appflowy":["Elige la aplicación de escritorio del autor para probar el producto antes de preparar un despliegue propio.","Crea una página y una pequeña tabla o tablero con datos de prueba.","Comprueba por separado sincronización, colaboración y acceso a las funciones de IA que quieras activar."],
        "ghidra":["Descarga la distribución de Ghidra y prepara la versión de Java indicada en sus instrucciones.","Crea un proyecto de prueba e importa un binario propio o de un ejercicio autorizado.","Revisa el análisis y la descompilación antes de añadir extensiones o un servidor MCP."],
        "unity-mcp":["Prepara un proyecto de prueba en Unity y la extensión y servidor que documenta el README.","Configura el servidor en tu cliente MCP y comprueba que aparecen sus herramientas.","Pide primero una consulta de la escena y después un cambio pequeño sobre una copia del proyecto."],
        "sellbird":["Elige Claude Code o Codex, comprueba su sesión activa y revisa la guía de configuración de Sellbird.","Configura un producto y datos de prueba; verifica por separado las cuentas de correo y servicios de contactos.","Genera y revisa un borrador antes de configurar envío real o tareas de seguimiento."],
        "coolify":["Prepara un servidor de prueba que cumpla los requisitos y revisa la instalación oficial de Coolify.","Conecta un proyecto pequeño y crea un despliegue con su configuración de dominio y variables.","Comprueba el resultado, persistencia y recuperación antes de alojar servicios que utilices a diario."],
        "home-assistant":["Elige una distribución o método de instalación de Home Assistant adecuado para tu equipo; este repositorio es el motor Core.","Configura una instancia de prueba y añade una integración de un dispositivo que controles.","Crea una automatización sencilla y comprueba su activación antes de automatizar más dispositivos."],
        "paperless-ngx":["Prepara la instalación documentada, normalmente con Docker Compose, y revisa sus volúmenes y requisitos.","Importa un documento de prueba y comprueba el reconocimiento de texto y la búsqueda.","Verifica descarga, organización y copias de los documentos antes de migrar tu archivo."],
        "claude-agent-sdk-python":["Prepara un entorno de Python compatible e instala el SDK; el README indica que incluye la CLI de Claude Code.","Elige la autenticación admitida y verifica si utilizarás sesión del plan o acceso de API.","Ejecuta una consulta mínima del ejemplo y revisa la salida antes de habilitar más herramientas."],
        "shannon":["Prepara una aplicación propia de laboratorio y el alcance de prueba antes de configurar el agente.","Elige el proveedor: la versión actual documenta Codex, APIs y modelos locales; la ruta de suscripción de Claude Code corresponde a una versión antigua.","Ejecuta una comprobación pequeña en el laboratorio y revisa la evidencia y el consumo antes de ampliar el alcance."],
    }
    if rid in custom:steps=custom[rid]
    return {"kind":"reference" if kind=="reference" else "skill" if kind=="skill" else "mcp" if kind=="mcp" else "source", "audience":audience,
            "prerequisites":prereq,"steps":steps,"command":command,"command_status":"documented" if command else "readme",
            "entry_url":entry_url,"source":source["html_url"],"checked_at":DATE,
            "note":"Comando de entrada seleccionado y presente en la fuente revisada; consulta la instalación completa y sus requisitos. No se ha ejecutado este proyecto."}


def main():
    import argparse
    from curate_discovery import in_goal
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("--apply",action="store_true");args=parser.parse_args()
    compact=json.loads((ROOT/"INDICE_IA.json").read_text(encoding="utf8"));detail=json.loads((ROOT/"INDICE_IA.detalle.json").read_text(encoding="utf8"))
    records=json.loads((AUDIT/"repositories.json").read_text(encoding="utf8"));curated=rows()
    candidates={record["metadata"]["full_name"].lower():record for record in records if record["status"]=="new"}
    assert set(candidates)==set(curated), (set(candidates)-set(curated),set(curated)-set(candidates))
    assert len({row["metadata"]["id"] for row in candidates.values()})==len(candidates)
    reserved={slug(repo["id"]) for repo in compact["repos"]};known={repo.get("github_id"):repo["id"] for repo in compact["repos"] if repo.get("github_id")}
    assigned={}
    for name,record in candidates.items():
        if record["metadata"]["id"] in known:
            assigned[name]=known[record["metadata"]["id"]];continue
        rid=FORCED_IDS.get(name) or slug(record["metadata"]["name"])
        if slug(rid) in reserved:rid=slug(name)
        assert slug(rid) not in reserved,rid
        reserved.add(slug(rid));assigned[name]=rid
    for cat in NEW_CATEGORIES:
        if not any(old["num"]==cat["num"] for old in compact["categories"]):compact["categories"].append(cat)
    extra_sections={10:("geoespacial","Fotogrametría y mapas desde imágenes"),11:("creacion-3d","Creación, renderizado y animación 3D"),13:("gestion","Gestión y archivo de documentos")}
    for cat in compact["categories"]:
        if cat["num"] in extra_sections:
            key,title=extra_sections[cat["num"]]
            if not any(sub["key"]==key for sub in cat["subs"]):cat["subs"].append({"key":key,"title":title})
    goals=compact["discovery"]["goals"]
    for goal in NEW_GOALS:
        if not any(old["id"]==goal["id"] for old in goals):goals.append(goal)
    added=[]
    for name,row in candidates.items():
        meta,source=row["metadata"],row["readme"]
        if meta["id"] in known:continue
        entry={**curated[name],"id":assigned[name]};rid=entry["id"];text=base64.b64decode(source["content"]).decode("utf8",errors="replace")
        access=access_profile(entry,source,text);start=starting(entry,source,text,access,meta)
        category=next(cat for cat in compact["categories"] if cat["num"]==entry["cat"])
        assert entry["sub"] in {sub["key"] for sub in category["subs"]}
        repo={"id":rid,"name":DISPLAY.get(name,meta["name"]),"cat":entry["cat"],"sub":entry["sub"],"role":ROLE[entry["kind"]],
              "exec":"hybrid" if access["api"] in {"optional","required","depends"} and entry["kind"] not in {"skill","plugin","reference"} else "local",
              "setup":"heavy" if rid in MODEL_FAMILY or entry["kind"]=="server" else "easy" if rid in READY or entry["kind"]=="reference" else "medium",
              "mcp":entry["kind"]=="mcp" or rid in MCP_EXTRA,"prov":["local"] if access["local_model"]=="supported" else [],
              "tags":list(dict.fromkeys([entry["sub"],entry["kind"],slug(meta.get("language") or "reference")])),
              "lib":False,"pick":rid in {"anytype-ts","ghidra"},"one":entry["one"],"alt":[],
              "stars":meta["stargazers_count"],"github_id":meta["id"],"gh":meta["full_name"],"lang":meta.get("language"),
              "license":(meta.get("license") or {}).get("spdx_id"),"added_at":DATE,"github_checked":DATE}
        if meta.get("archived"):repo["status"]="archived"
        repo["routes"]=access_routes({"access":access})
        repo["goals"]=[goal["id"] for goal in goals if in_goal(goal["id"],repo,goal["starters"])]
        if entry["cat"]==15 and entry["sub"]=="notas":repo["goals"].append("notas")
        if entry["kind"]=="server" and entry["cat"] in {1,13,15}:repo["goals"].append("servicios")
        if entry["cat"]==16:repo["goals"].append("seguridad")
        if entry["sub"]=="creacion-3d" or rid in names("3dviz-pro-max blender-skills threejs-skills threejs-game-skills unity-mcp dream-loop anatomy"):repo["goals"].append("3d")
        if entry["kind"]=="reference" and "aprender" not in repo["goals"]:repo["goals"].append("aprender")
        repo["goals"]=list(dict.fromkeys(repo["goals"]))
        how={"skill":"El agente lee instrucciones del proyecto y utiliza las herramientas y dependencias que declares para la tarea.",
             "reference":"Se consulta como documentación o referencia; cada ejemplo o proyecto enlazado se evalúa por separado.",
             "mcp":"Un cliente MCP invoca las herramientas del servidor para trabajar con el programa o servicio conectado.",
             "model":"Carga los modelos y datos del ejemplo para realizar inferencia o investigación con el backend elegido.",
             "engine":"Carga y sirve modelos mediante el backend local y las opciones de hardware que documenta el proyecto.",
             "plugin":"Se instala dentro de DeepSeek Harness para añadir herramientas y una interfaz a ese entorno.",
             "server":"Un servicio y su interfaz gestionan los datos y conexiones configurados en tu despliegue.",
             "library":"Tu aplicación incorpora la biblioteca y llama sus funciones; no es un programa independiente con una interfaz lista.",
             "framework":"El desarrollador adapta sus ejemplos y componentes dentro de un proyecto con sus propios datos y servicios.",
             "template":"Se utiliza como punto de partida: se prepara el entorno del ejemplo y se adapta su código a la tarea.",
             "app":"La aplicación ofrece las herramientas de su interfaz o CLI después de preparar la distribución y sus dependencias.",
             "agent":"La aplicación coordina modelos y herramientas; el acceso de cada componente se configura antes de ejecutar sus tareas."}[entry["kind"]]
        files=[item["path"] for item in row["tree"].get("tree",[]) if item.get("type")=="blob"]
        manifests=[path for path in files if path in {"pyproject.toml","package.json","Cargo.toml","CMakeLists.txt","go.mod","Dockerfile","docker-compose.yml","compose.yaml"}]
        stack=", ".join([value for value in [meta.get("language"),*manifests] if value])
        limits="Revisar la versión, la licencia y los requisitos del README. La revisión es documental y no acredita una instalación ejecutada."
        if entry["cat"]==16:limits+=" Las pruebas activas y modificaciones requieren un alcance autorizado y un entorno adecuado."
        if entry["cat"]==14:limits+=" No se verificó rentabilidad ni operación con fondos. Distingue demostración, backtesting, simulación y conexión real."
        if meta.get("archived"):limits+=" El repositorio está archivado; comprueba el reemplazo y el soporte de sus dependencias."
        avoid="buscas una aplicación lista y no quieres preparar un proyecto de código" if entry["kind"] in {"library","framework","template"} else "necesitas un producto autónomo y esta pieza requiere un anfitrión compatible" if entry["kind"] in {"skill","plugin","mcp"} else "necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución" if entry["kind"]!="reference" else "necesitas una aplicación lista para ejecutar en lugar de material de consulta"
        d={"name":repo["name"],"cat":repo["cat"],"sub":repo["sub"],"desc":entry["one"],"how":how,
           "install":"Sigue la instalación y el ejemplo mínimo en "+source["html_url"],"cases":[entry["one"]],"stack":stack,
           "choose_if":"buscas esta función: "+entry["one"],"avoid_if":avoid,"limits":limits,"combines_with":[],"alternatives":[],
           "repo":meta["html_url"],"homepage":meta.get("homepage"),"license":repo["license"],"lang":repo["lang"],"updated":DATE,
           "doc":"human/fichas/"+slug(rid)+".md","access":access,"getting_started":start,"first_step":start["steps"][0],
           "sources":{"readme_blob_sha":source["sha"],"root_tree_sha":row["tree"]["sha"],"readme_url":source["html_url"],"github_checked":DATE,"collection":"saved-resources-document"}}
        compact["repos"].append(repo);detail["repos"][rid]=d;added.append({"id":rid,"full_name":meta["full_name"],"github_id":meta["id"],"readme_blob_sha":source["sha"]})
        if args.apply:
            folder=ROOT/"data/extracted"/rid;folder.mkdir(parents=True,exist_ok=True)
            (folder/"readme.md").write_text(text,encoding="utf8")
            (folder/"access-review.json").write_text(json.dumps({"id":rid,"gh":meta["full_name"],"checked_at":row["checked_at"],"url":source["html_url"],"blob_sha":source["sha"],"path":source["path"],"error":None,"evidence":[]},ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    by_id={repo["id"]:repo for repo in compact["repos"]}
    alternatives=[("anytype-ts","appflowy"),("claude-obsidian","obsidian-second-brain"),("radare2","rizin"),("ghidra","radare2"),
                  ("onyx","anything-llm"),("pdf-craft","marker"),("backtrader","nautilus-trader"),("threejs-skills","3dviz-pro-max"),("py-clob-client","py-sdk")]
    for left,right in alternatives:
        if left not in by_id or right not in by_id:continue
        a,b=by_id[left],by_id[right]
        if right not in a["alt"] and left not in b["alt"] and len(a["alt"])<5 and len(b["alt"])<5:
            a["alt"].append(right);b["alt"].append(left)
        detail["repos"][left]["alternatives"]=a["alt"];detail["repos"][right]["alternatives"]=b["alt"]
    for left,right in [("vaultwarden","bitwarden-clients"),("ghidramcp","ghidra"),("webodm","odm"),("unity-mcp","blender"),("blender-skills","blender"),("openviking","claude-code"),("obsidian-skills","obsidian-releases"),("pdf-craft","unlimited-ocr")]:
        if left in by_id and right in by_id:
            target=detail["repos"][left].setdefault("combines_with",[])
            if right not in target:target.append(right)
    for goal in NEW_GOALS:
        for rid in goal["starters"]+goal["guided"]:
            assert rid in by_id,rid
            target=by_id[rid].setdefault("goals",[])
            if goal["id"] not in target:target.append(goal["id"])
    for cat in compact["categories"]:
        cat["count"]=sum(repo["cat"]==cat["num"] and not repo.get("alias_of") for repo in compact["repos"])
    public=[repo for repo in compact["repos"] if repo.get("gh") and not repo.get("alias_of")]
    compact["meta"].update(title=f"Índice IA — {len(public)} repos curados de IA, automatización y herramientas",updated=DATE,document_checked=DATE)
    collection=[{"id":assigned[name],"full_name":row["metadata"]["full_name"],"github_id":row["metadata"]["id"],"readme_blob_sha":row["readme"]["sha"]} for name,row in candidates.items()]
    report={"checked_at":DATE,"source":"Documento de recursos aportado por el usuario; original conservado fuera del contenido público.",
            "existing_reference_count":sum(record["status"]=="existing" for record in records),"added_count":len(collection),"added":collection,
            "total_public_repositories":len(public),"corrections":[{"reference":"anthropic/skills","resolved":"anthropics/skills","catalog_id":"anthropic-skills","reason":"Errata de propietario; el proyecto correcto ya estaba catalogado."}],
            "resolved_unlinked":[{"name":"RTMPose","resolved":"open-mmlab/mmpose","reason":"Modelo incluido en MMPose; no se duplica como repositorio."},{"name":"Bitwarden Send","resolved":"bitwarden/clients","reason":"Función de los clientes oficiales, no repositorio independiente."}],
            "unresolved_names":["Conductor AI","Cybersecurity Skills","Kimi K2.7 Code","AgentOS - WhatsApp AI Agent Builder","Creative Architect"],
            "notes":["No se ejecutó el software catalogado.","No se importaron repos enlazados únicamente desde README de terceros: el alcance es el documento del usuario.","El SDK nuevo de Polymarket aparece en el texto; se conserva su cliente antiguo como archivado, con identidad propia."]}
    print({"new":len(added),"public_total":len(public),"categories":len([cat for cat in compact["categories"] if cat["num"]>0]),"goals":len(goals),"apply":args.apply})
    if args.apply:
        (ROOT/"INDICE_IA.json").write_text(json.dumps(compact,ensure_ascii=False,indent=1)+"\n",encoding="utf8")
        (ROOT/"INDICE_IA.detalle.json").write_text(json.dumps(detail,ensure_ascii=False,indent=1)+"\n",encoding="utf8")
        (ROOT/"reports/document-import-2026-11-14.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf8")


if __name__ == "__main__": main()
