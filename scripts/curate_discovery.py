"""Editorial navigation migration: user goals, shelf descriptions and first-seen dates."""
import json
from pathlib import Path
import subprocess
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]

CATEGORIES={
 1:('Automatizar negocios y comunicación','Conecta aplicaciones, organiza clientes, atiende mensajes o programa procesos. Empieza por un motor de flujos; añade canales y CRM según tu objetivo.'),
 2:('Mejorar tu agente: skills y prompts','Instrucciones, plugins y métodos que añades a un agente que ya utilizas. Distingue una skill concreta de un directorio que solo enlaza a otras.'),
 3:('Crear y usar agentes de IA','Agentes listos para trabajar y frameworks para construir los tuyos. Un agente de código se utiliza; un framework se integra dentro de una aplicación.'),
 4:('Buscar y extraer información web','Buscadores, crawlers y navegadores. Usa un crawler para extraer páginas, un navegador para interactuar y un agente para investigar con un modelo.'),
 5:('Conectar herramientas con MCP','SDKs, servidores y conectores que dejan a un agente usar herramientas. El servidor MCP aporta acciones o datos; el modelo pertenece al cliente.'),
 6:('Memoria, conocimiento y operación de IA','Guarda memoria, consulta documentos con RAG, sirve modelos y evalúa resultados. Una base vectorial y un sistema RAG completo resuelven capas distintas.'),
 7:('Entender código, trabajar con datos y entrenar modelos','Herramientas para analizar código, procesar datos, aprender machine learning y entrenar modelos. Separa los ejemplos de aprendizaje de las librerías que integras.'),
 8:('Usar modelos y asistentes locales','Motores de modelos, clientes de chat y espacios de trabajo. Instalar una interfaz local no garantiza que el modelo sea local: comprueba su backend.'),
 9:('Diseñar y construir interfaces','Componentes, estilos, animación, diseño visual y herramientas para crear pantallas. Las librerías de UI no necesitan por sí solas una API de IA.'),
 10:('Analizar datos, crear dashboards y mapas','Herramientas para explorar datos, crear gráficos, medir productos y visualizar fuentes abiertas. El chat con datos sí puede añadir un modelo; un gráfico convencional no lo necesita.'),
 11:('Generar imágenes y trabajar con visión','Generación, restauración, detección, segmentación y etiquetado de imágenes. Revisa por separado la licencia de los pesos y el hardware del modelo.'),
 12:('Crear audio, voz y video','Transcribe, sintetiza voz, edita o genera video. El montaje local y la generación mediante un proveedor son rutas con requisitos diferentes.'),
 13:('Trabajar con documentos y presentaciones','Extrae texto, aplica OCR, transforma PDFs o crea diapositivas. Empieza por el formato de entrada y el resultado que necesitas.'),
}
GOALS=[
 ('programar','Programar con un agente','Elegir una herramienta de desarrollo y mejorar su flujo sin construir un agente desde cero.',['codex','claude-code','opencode'],[2,3,7],['programar','codigo','coding','desarrollo','vibe coding','asistente de codigo']),
 ('automatizar','Automatizar tareas y conectar apps','Diseñar flujos con disparadores, acciones y seguimiento.',['n8n','activepieces','node-red'],[1,5],['automatizar','automatizacion','workflow','flujo','zapier','integraciones']),
 ('whatsapp','Atender clientes por WhatsApp','Conectar el canal, decidir el flujo y pasar a una persona cuando haga falta.',['evolution-api','waha','chatwoot'],[1],['whatsapp','clientes','ventas','mensajes','bot de whatsapp']),
 ('documentos','Preguntar a documentos','Extraer el contenido y elegir una solución de búsqueda o RAG.',['docling','anything-llm','ragflow'],[6,8,13],['documentos','pdf','rag','manuales','preguntar a mis archivos','conocimiento']),
 ('investigar','Investigar un tema con fuentes','Combinar búsqueda y síntesis con trazabilidad de las fuentes.',['local-deep-research','gpt-researcher','deer-flow'],[3,4],['investigar','research','investigacion','buscar informacion','fuentes','informe']),
 ('local','Usar IA con modelos locales','Elegir un motor, un modelo y una interfaz que funcionen con tu equipo.',['ollama','jan','open-webui'],[8,6],['local','offline','sin conexion','ollama','privacidad','sin api']),
 ('web','Crear una web o aplicación','Elegir componentes y añadir IA solo si el producto la necesita.',['ui','tailwindcss','assistant-ui'],[9],['web','interfaz','ui','frontend','pagina','aplicacion','landing']),
 ('video','Crear o editar videos','Elegir entre editar material, programar escenas o generar clips.',['remotion','moviepy','ffmpeg'],[12],['video','videos','reels','shorts','montaje','editar video','animacion']),
 ('voz','Transcribir audio a texto','Obtener texto o subtítulos a partir de una grabación.',['whisper-cpp','faster-whisper','whisperx'],[12],['audio','transcribir','transcripcion','stt','subtitulos']),
 ('narrar','Crear voz a partir de texto','Convertir un guion en narración con una ruta local o un servicio.',['kokoro','supertonic','edge-tts'],[12],['voz','tts','narracion','narrar','sintesis','texto a voz']),
 ('imagenes','Generar o mejorar imágenes','Elegir una interfaz y revisar modelos, pesos y requisitos de GPU.',['comfyui','fooocus','rembg'],[11],['imagenes','imagen','image','fotos','vision','generar imagen','upscale']),
 ('presentaciones','Crear una presentación','Decidir si necesitas PowerPoint editable o diapositivas web.',['ppt-master','presenton','slidev'],[13],['presentaciones','presentacion','ppt','powerpoint','slides','diapositivas']),
 ('diagramas','Dibujar un diagrama','Explicar una idea con un dibujo, un esquema o un diagrama por código.',['excalidraw','mermaid','tldraw'],[9,13],['diagrama','diagramas','dibujar','esquema','mapa mental']),
 ('datos','Explorar datos y crear dashboards','Elegir una herramienta de BI o una librería de gráficos.',['metabase','superset','streamlit'],[10,7],['datos','dashboard','tablero','bi','analytics','analitica','graficos']),
 ('mcp','Dar herramientas a mi agente','Buscar un servidor existente antes de programar un conector.',['context7','playwright-mcp','github-mcp-server'],[5],['mcp','conector','herramientas','servidor mcp','conectar agente']),
 ('skills','Mejorar Claude Code o Codex','Añadir instrucciones concretas al agente y conservar un conjunto pequeño.',['superpowers','agent-skills','impeccable'],[2,9],['skills','plugins','prompts','mejorar agente','claude code','codex']),
 ('aprender','Aprender a construir con IA','Empezar por un curso o ejemplo antes de desplegar una plataforma.',['generative-ai-for-beginners','ai-engineering-hub','llms-from-scratch'],[2,7],['aprender','curso','tutorial','principiante','ejemplos','desde cero']),
 ('finanzas','Investigar mercados y estrategias','Consultar herramientas y ejemplos financieros distinguiendo análisis, backtesting y ejecución.',['qlib','dexter','tradingagents'],[14],['finanzas','financiero','trading','bolsa','acciones','cripto','mercados','inversion']),
]
CORRECTIONS={
 'jan':('Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz.','Permite descargar modelos para inferencia local o utilizar conexiones remotas documentadas.','Comprueba el modelo y backend activo: el modo local necesita recursos de tu equipo y la ruta remota conserva sus propios requisitos de acceso.'),
 'opencut':('Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescribe.','La versión clásica permite probar el flujo de edición; la nueva arquitectura sigue otra ruta de desarrollo.','El README diferencia opencut.app y opencut-classic de la reescritura en curso; comprueba qué versión necesitas antes de compilar.'),
 'whisper':('Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo.','Carga un modelo de voz y procesa el audio para generar una transcripción.','El idioma, el tamaño del modelo y la calidad del audio condicionan el resultado.'),
 'faster-whisper':('Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización.','Carga modelos Whisper compatibles y permite configurar dispositivo y precisión de inferencia.','Puede reducir requisitos frente a otras implementaciones; mide calidad y rendimiento con tu propio audio.'),
 'n8n-mcp':('Servidor MCP que permite a un agente consultar nodos, esquemas y ejemplos de n8n para preparar workflows.','Expone herramientas de documentación y, con la configuración correspondiente, de gestión de workflows.','El cliente MCP y la instancia de n8n conservan sus propios requisitos de acceso.'),
 'n8n-skills':('Skills para ayudar a un agente a construir, revisar y depurar workflows de n8n con sus nodos y herramientas.','Aportan instrucciones y criterios para trabajar con el formato y las conexiones de n8n.','La skill no sustituye la instancia de n8n ni las credenciales de los servicios de un workflow.'),
 'awesome-n8n-templates':('Colección de plantillas de n8n para estudiar o importar automatizaciones de servicios y tareas habituales.','Agrupa ejemplos que se adaptan a una instancia de n8n y a sus credenciales.','Cada workflow tiene dependencias y posibles consumos externos que debes revisar antes de activarlo.'),
 'remotion':('Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos.','Representa cada fotograma mediante componentes y genera el archivo de video a partir de la composición.','El render no requiere por sí solo una API de IA; revisa las condiciones de licencia del proyecto.'),
 'whisperx':('Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes.','Combina reconocimiento de voz, alineación y componentes de diarización configurables.','Las etapas, modelos y credenciales requeridos cambian según las funciones que actives.'),
 'supertonic':('Motor de texto a voz que ofrece modelos y ejemplos para sintetizar audio en dispositivos y navegadores compatibles.','Procesa texto con un modelo de voz local mediante los runtimes y ejemplos que distribuye el proyecto.','El soporte por idioma, dispositivo y variante debe comprobarse en la documentación actual.'),
 'kokoro':('Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles.','Un pipeline de síntesis transforma texto en audio usando los pesos y voces seleccionados.','Comprueba los idiomas, dependencias de audio y condiciones de la variante que utilices.'),
 'luxtts':('Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local.','Genera audio a partir de texto y del contexto de voz configurado.','La velocidad y el consumo de memoria dependen de la variante y del hardware.'),
 'vibevoice':('Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio.','Ofrece variantes con capacidades y rutas de inferencia diferentes.','Elige una variante concreta antes de asumir idiomas, duración, hardware o soporte de tiempo real.'),
 'generative-ai-for-beginners':('Curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificial generativa.','Organiza lecciones y ejercicios que introducen modelos, prompts y aplicaciones.','Leer el curso no requiere una API; ejecutar cada práctica puede requerir servicios o modelos específicos.'),
 'claude-plugins-official':('Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code.','Instalas los plugins concretos desde el cliente y configuras sus dependencias o servicios.','Cada plugin puede tener requisitos distintos; el marketplace completo no es una aplicación que debas desplegar.'),
 'agent-skills':('Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes.','Organiza instrucciones y controles de calidad para distintas fases del desarrollo.','Instala las piezas que necesitas mediante la ruta de tu agente y revisa las dependencias de cada skill.'),
 'fluxer':('Aplicación de mensajería instantánea y llamadas de voz para comunidades, con código abierto y opciones de alojamiento propio.','Reúne conversaciones de texto, voz y funciones comunitarias en clientes web y de escritorio.','Organiza canales y comunicación de grupos; no es un generador de audio o video.'),
 'videofy-minimal':('Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revisión.','La interfaz coordina la obtención del artículo, guion, imágenes, narración y render del video.','La ruta documentada requiere APIs de OpenAI y ElevenLabs aunque la interfaz y el montaje se ejecuten en tu equipo.'),
 'ecc':('Colección de plugins, skills, hooks y convenciones para organizar el trabajo de agentes de código en un proyecto.','Agrupa instrucciones y automatizaciones para planificación, implementación y revisión.','Se integra con distintos agentes mediante rutas de instalación específicas; no es una plataforma de modelos locales.'),
 'open-generative-ai':('Estudio abierto de generación de imagen y video que utiliza modelos ofrecidos mediante servicios de MuAPI.','Reúne interfaces y flujos de generación en una aplicación que llama a proveedores externos.','El código de la interfaz está disponible; las generaciones y otras modalidades del servicio tienen requisitos y tarifas propios.'),
 'ppt-master':('Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos.','El agente prepara y genera las diapositivas con las herramientas del proyecto.','Necesita un agente con acceso a un modelo; los servicios opcionales de imágenes o contenido se revisan por separado.'),
 'flowise':('Constructor visual para diseñar aplicaciones de IA conectando modelos, herramientas, memoria y fuentes de datos.','Representa componentes y conexiones en un flujo que se configura y ejecuta desde una interfaz.','La instalación de Flowise y el acceso al modelo son decisiones separadas.'),
 'chart-js':('Librería JavaScript para dibujar gráficos en canvas dentro de una página o aplicación web.','Recibe datos y configuración para renderizar gráficos de líneas, barras, áreas y otros tipos.','No utiliza un modelo de IA para generar los gráficos.'),
 'tesseract':('Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idioma.','Procesa imágenes y produce texto reconocible que puedes buscar, copiar o integrar en otros programas.','La precisión depende del idioma, el escaneo y la preparación de la imagen.'),
}
GUIDED={
 'programar':['codex','claude-code','opencode','goose'],
 'automatizar':['n8n','activepieces','node-red','windmill'],
 'whatsapp':['chatwoot','waha','evolution-api','n8n'],
 'documentos':['anything-llm','open-webui','ragflow','open-notebook','surfsense','private-gpt','pageindex'],
 'investigar':['local-deep-research','gpt-researcher','deer-flow','storm','open-deep-research'],
 'local':['jan','ollama','open-webui','cherry-studio','chatbox','librechat'],
 'web':['onlook','plasmic','penpot','openui','ui','assistant-ui'],
 'video':['lossless-cut','openscreen','opencut','obs-studio','remotion','hyperframes','ffmpeg','moviepy'],
 'voz':['whisper-cpp','faster-whisper','whisperx','whisper'],
 'narrar':['kokoro','supertonic','edge-tts','chatterbox','omnivoice-studio'],
 'imagenes':['comfyui','fooocus','invokeai','stable-diffusion-webui','rembg'],
 'presentaciones':['ppt-master','presenton','slidev','marp','reveal.js'],
 'diagramas':['excalidraw','mermaid','tldraw'],
 'datos':['metabase','superset','streamlit','redash','gradio'],
 'mcp':['context7','playwright-mcp','github-mcp-server','n8n-mcp'],
 'skills':['superpowers','agent-skills','impeccable','marketingskills'],
 'aprender':['generative-ai-for-beginners','ai-engineering-hub','llms-from-scratch','ai-agents-for-beginners'],
 'finanzas':['qlib','dexter','tradingagents'],
}

def in_goal(key, r, starters):
 if r['id'] in starters or r['id'] in GUIDED.get(key,[]):return True
 cat,sub=r['cat'],r.get('sub','')
 rules={
  'programar':(cat==3 and sub=='coding') or (cat==7 and sub in {'codigo','calidad'}),
  'automatizar':cat==1 and sub in {'motores','n8n','internas'},
  'whatsapp':cat==1 and sub in {'whatsapp','chatbots','crm'},
  'documentos':(cat==6 and sub in {'rag','vectores'}) or (cat==8 and sub in {'workspaces','notebooklm'}) or (cat==13 and sub in {'conversion','ocr','pdf'}),
  'investigar':(cat==3 and sub=='research') or (cat==4 and sub in {'crawlers','llm','busqueda'}),
  'local':cat==8,
  'web':cat==9,
  'video':cat==12 and sub in {'edicion','programatico','generativo'},
  'voz':cat==12 and sub=='stt',
  'narrar':cat==12 and sub=='tts',
  'imagenes':cat==11,
  'presentaciones':cat==13 and sub=='slides',
  'diagramas':(cat==13 and sub=='diagramas') or r['id'] in {'excalidraw','tldraw'},
  'datos':cat==10 or (cat==7 and sub=='datos'),
  'mcp':cat==5 or bool(r.get('mcp')),
  'skills':cat==2 or (cat in {9,12} and r.get('role')=='skill'),
  'aprender':r.get('role')=='directory' or (cat==7 and sub=='aprender'),
  'finanzas':cat==14,
 }
 return rules.get(key,False)


def main():
 c=json.loads((ROOT/'INDICE_IA.json').read_text(encoding='utf8'));d=json.loads((ROOT/'INDICE_IA.detalle.json').read_text(encoding='utf8'))
 first_seen={}
 revisions=subprocess.check_output(['git','log','--reverse','--format=%H','--','INDICE_IA.json'],cwd=ROOT,encoding='utf8').splitlines()
 for sha in revisions:
  try: old=json.loads(subprocess.check_output(['git','show',sha+':INDICE_IA.json'],cwd=ROOT,encoding='utf8',stderr=subprocess.DEVNULL))
  except (subprocess.CalledProcessError,json.JSONDecodeError):continue
  stamp=subprocess.check_output(['git','show','-s','--format=%cI',sha],cwd=ROOT,encoding='utf8').strip()
  date=datetime.fromisoformat(stamp).astimezone(ZoneInfo('America/Mexico_City')).date().isoformat()
  for r in old.get('repos',[]):
   if isinstance(r,dict) and r.get('id'): first_seen.setdefault(r['id'],date)
 for cat in c['categories']:
  if cat['num'] in CATEGORIES:cat['title'],cat['desc']=CATEGORIES[cat['num']]
 if not any(cat['num']==14 for cat in c['categories']):
  c['categories'].append({'num':14,'title':'Investigar finanzas y mercados','emoji':'📈','desc':'Agentes de investigación, análisis cuantitativo, backtesting y bots de ejemplo. Distingue una explicación o simulación de una operación con fondos reales.','file':'human/categorias/14-investigar-finanzas-y-mercados.md','subs':[{'key':'agentes','title':'Agentes de investigación financiera'},{'key':'cuant','title':'Modelos y backtesting cuantitativo'},{'key':'bots','title':'Bots y conexiones a exchanges'},{'key':'aprender','title':'Ejemplos y aprendizaje'}]})
 finance={'daily-stock-analysis':'agentes','autohedge':'agentes','dexter':'agentes','finceptterminal':'agentes','quantharness':'agentes','tradingagents':'agentes','qlib':'cuant','chartanalyst':'cuant','binance-trader':'bots','crypto-trader':'bots','intellitrader':'bots','open-sol-bot':'bots','machine-learning-for-trading':'aprender','stocks-analyst':'aprender'}
 for r in c['repos']:
  rid=r['id'];detail=d['repos'][rid]
  if rid in finance:r['cat']=detail['cat']=14;r['sub']=detail['sub']=finance[rid]
  if rid in {'qlib','dexter'}:r['pick']=True
  if rid in CORRECTIONS:
   one,how,desc=CORRECTIONS[rid];r['one']=one;detail.update(desc=one+' '+desc,how=how)
  if rid=='ppt-master':r['role']='skill'
  r['added_at']=first_seen.get(rid,'2026-11-14')
  if rid not in {'guia','tools'} and not r.get('alias_of'):
   r['goals']=[key for key,_,_,starters,cats,aliases in GOALS if in_goal(key,r,starters)]
   detail['first_step']=detail.get('getting_started',{}).get('steps',['Consultar la fuente original.'])[0]
 counts=Counter(r['cat'] for r in c['repos'])
 for cat in c['categories']:cat['count']=counts[cat['num']]
 c['discovery']={'goals':[{'id':key,'title':title,'description':desc,'starters':starters,'guided':GUIDED[key],'categories':cats,'keywords':aliases} for key,title,desc,starters,cats,aliases in GOALS],
  'principles':['Empieza por un resultado concreto y compara pocas opciones.','Revisa acceso, coste y equipo antes de instalar.','Las estrellas miden popularidad; no acreditan adecuación ni calidad.'],
  'default_goal':'programar','reviewed_at':'2026-11-14'}
 c['meta']['fields']['added_at']='primera aparición del id en el historial de Git de Alexandria (fecha de Ciudad de México)'
 c['meta']['fields']['goals']='rutas por resultado, definidas en discovery.goals'
 for name,data in [('INDICE_IA.json',c),('INDICE_IA.detalle.json',d)]: (ROOT/name).write_text(json.dumps(data,ensure_ascii=False,indent=1)+'\n',encoding='utf8')
 print('Discovery:',len(GOALS),'goals;',len(c['categories'])-1,'shelves;',len(finance),'finance repos moved')

if __name__=='__main__':main()
