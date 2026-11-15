"""Add three source-verified references after the dated taxonomy migration.

Uses cached GitHub metadata/README and the exact official model card, never clones
or runs the catalogued projects. The two ambiguous names remain in the report.
"""
import base64
from collections import Counter
import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

from repo_intelligence.core.access import access_routes

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-11-14"
CACHE = ROOT / "data/reports/pending-names-20261114"


def read_url(url):
    with urlopen(url, timeout=45) as response:
        return response.read()


def main():
    compact = json.loads((ROOT/"INDICE_IA.json").read_text(encoding="utf8"))
    detail = json.loads((ROOT/"INDICE_IA.detalle.json").read_text(encoding="utf8"))
    assert compact["meta"].get("taxonomy_revision") == "2026-11-14-32"
    identities = {r["id"] for r in compact["repos"]}
    added = []

    def add(rid, name, cat, sub, role, one, access, start, extra, full_name=None, model=None):
        if rid in identities:
            return
        if full_name:
            record = json.loads((CACHE/"github"/(full_name.replace("/","--")+".json")).read_text(encoding="utf8"))
            meta, source = record["metadata"], record["readme"]
            assert not meta["private"] and meta["full_name"].lower() == full_name.lower()
            text = base64.b64decode(source["content"]).decode("utf8")
            repo_url, source_url, blob = meta["html_url"], source["html_url"], source["sha"]
            provenance = dict(readme_blob_sha=blob,root_tree_sha=record["tree"]["sha"],readme_url=source_url,github_checked=DATE)
            metadata = dict(gh=meta["full_name"],github_id=meta["id"],stars=meta["stargazers_count"],license=(meta.get("license") or {}).get("spdx_id") or "Revisar LICENSE",lang=meta.get("language") or "Markdown")
        else:
            repo_url = "https://huggingface.co/"+model
            info = json.loads(read_url("https://huggingface.co/api/models/"+model))
            revision = info["sha"]
            text_bytes = read_url(repo_url+"/raw/"+revision+"/README.md")
            text = text_bytes.decode("utf8")
            blob = hashlib.sha1(b"blob "+str(len(text_bytes)).encode()+b"\0"+text_bytes).hexdigest()
            source_url = repo_url+"/blob/"+revision+"/README.md"
            provenance = dict(readme_blob_sha=blob,model_revision=revision,readme_url=source_url,model_checked=DATE)
            metadata = dict(repository_host="huggingface",model_id=model,license="Modified MIT; revisar condiciones",lang="Pesos de modelo")
            (CACHE/"kimi-model.json").write_text(json.dumps(dict(id=model,revision=revision,readme_blob_sha=blob),indent=2)+"\n",encoding="utf8")
        command = start.get("command", "")
        assert not command or command in text, (rid,command)
        access.update(checked_at=DATE,review="documented",source_blob_sha=blob,sources=[source_url]+access.get("sources",[]))
        start.update(source=source_url,checked_at=DATE,entry_url=start.get("entry_url") or repo_url,command_status="documented" if command else "readme")
        repo = dict(id=rid,name=name,cat=cat,sub=sub,role=role,exec="hybrid",setup="heavy" if model else "easy",mcp=False,
            prov=extra.pop("prov",[]),tags=extra.pop("tags",[]),lib=False,pick=False,one=one,alt=[],added_at=DATE,
            goals=extra.pop("goals",[]),**metadata)
        repo["routes"] = access_routes({"access":access})
        card = dict(name=name,cat=cat,sub=sub,desc=one,repo=repo_url,homepage=extra.pop("homepage",None),license=repo["license"],lang=repo["lang"],updated=DATE,
            doc=f"human/fichas/{rid}.md",access=access,getting_started=start,first_step=start["steps"][0],sources={**provenance,"collection":"pending-document-references"},
            alternatives=[],combines_with=[],**extra)
        compact["repos"].append(repo)
        detail["repos"][rid] = card
        identities.add(rid)
        folder = ROOT/"data/extracted"/rid
        folder.mkdir(parents=True,exist_ok=True)
        (folder/"readme.md").write_text(text,encoding="utf8")
        (folder/"access-review.json").write_text(json.dumps(dict(id=rid,checked_at=DATE,url=source_url,blob_sha=blob,error=None,evidence=[]),ensure_ascii=False,indent=2)+"\n",encoding="utf8")
        added.append(dict(id=rid,url=repo_url,readme_blob_sha=blob))

    add("creative-architect","Creative Architect",27,"skills","skill",
        "Plugin de dirección de arte para Claude Code: prepara fotos de producto, UGC y anuncios con proveedores de imagen o video.",
        dict(api="optional",local_model="not_documented",claude_code="host",codex="not_documented",cost="choice",hardware="ordinary",mode="agent_extension",
            scope="Plugin para dirigir piezas creativas dentro de Claude Code; también puede entregar solo el prompt.",
            api_note="Para preparar briefs y prompts utiliza tu agente. Para generar conecta Higgsfield, Magnific u OpenAI con la cuenta, conector o API que corresponda.",
            subscription_note="Las instrucciones se ejecutan en Claude Code con tu acceso habitual; los créditos de generación del proveedor se revisan por separado.",
            local_note="El plugin vive en tu equipo; la documentación no ofrece un generador local de imágenes o video.",
            cost_note="Plugin MIT. Consume tu agente y, si generas medios, los créditos o tarifas del proveedor elegido.",
            hardware_note="Git y Claude Code para el plugin; los servicios conectados tienen sus propios requisitos.",
            sources=["https://www.tododeia.com/community/creative-architect"]),
        dict(kind="skill",audience="agent",prerequisites=["Git y Claude Code funcionando","Cuenta en un proveedor solo si vas a generar medios"],
            steps=["Abre una carpeta de trabajo en Claude Code y añade el marketplace del proyecto.","Instala creative-architect@creative-architect y recarga los plugins.","Pide primero un brief o prompt; conecta un proveedor y revisa sus créditos antes de generar una pieza."],
            command="claude plugin marketplace add Hainrixz/creative-architect\nclaude plugin install creative-architect@creative-architect",
            note="El README aún dice privado, pero GitHub lo marca público en la revisión. Revisa los permisos si cambia. La revisión es documental; no se instaló el plugin."),
        dict(prov=["anthropic","openai"],tags=["direccion-de-arte","fotos-producto","ugc","claude-code","creative-architect"],
            goals=["imagenes","video","skills"],homepage="https://www.tododeia.com/community/creative-architect",
            how="El agente convierte la idea y las referencias de producto en un brief; usa el proveedor conectado para producir y revisar la pieza.",
            install="Añade el marketplace con los comandos documentados; instala el plugin y recarga Claude Code.",stack="Plugin Claude Code; Markdown; conectores o API de medios",
            cases=["Preparar fotos de producto","Escribir un brief de UGC y anuncios"],
            choose_if="ya usas Claude Code y buscas una guía de dirección de arte con proveedores conectables",
            avoid_if="necesitas generación local documentada o un plugin nativo de Codex",
            limits="No incluye créditos de imagen o video. El README conserva una nota de acceso privado que discrepa de la visibilidad pública verificada en GitHub."),
        full_name="Hainrixz/creative-architect")

    add("cybersecurity-skills","Cybersecurity Skills (comunidad)",16,"skills","skill",
        "Biblioteca comunitaria de skills para análisis de seguridad, defensa y pruebas autorizadas con Claude Code, Codex y otros agentes.",
        dict(api="not_required",local_model="not_applicable",claude_code="host",codex="host",cost="host_plan",hardware="ordinary",mode="agent_extension",
            scope="Instrucciones y ejemplos que se cargan en un agente compatible; no es un escáner autónomo ni un proyecto de Anthropic.",
            api_note="La biblioteca de instrucciones no requiere una clave propia de IA; el modelo pertenece al agente que utilices.",
            subscription_note="Claude Code y Codex CLI aparecen expresamente como clientes compatibles; se consume el acceso de tu agente.",
            local_note="La biblioteca no sirve un modelo. El cliente y las herramientas de la skill elegida determinan la ejecución.",
            cost_note="Código Apache-2.0; el agente, los laboratorios y servicios de cada skill pueden tener costes.",
            hardware_note="Consulta las dependencias de una sola skill; algunos análisis necesitan herramientas o un laboratorio adicional."),
        dict(kind="skill",audience="agent",prerequisites=["Agente compatible con skills","Un sistema propio o un laboratorio con permiso de pruebas"],
            steps=["Abre el catálogo y elige una skill para una necesidad concreta de defensa o análisis.","Revisa su SKILL.md, las herramientas y el alcance autorizado antes de instalarla.","Usa el instalador documentado, selecciona tu agente y realiza una prueba pequeña en un laboratorio."],
            command="npx skills add mukul975/Anthropic-Cybersecurity-Skills",
            note="Proyecto comunitario independiente, sin afiliación a Anthropic. No se ejecutaron las herramientas de seguridad."),
        dict(prov=[],tags=["cybersecurity","seguridad","skills","claude-code","codex","comunidad"],goals=["seguridad"],
            how="El agente consulta el procedimiento de la skill y utiliza las herramientas de análisis indicadas para el alcance que hayas definido.",
            install="El README documenta npx skills add; selecciona el cliente y las skills que necesitas.",stack="agentskills.io; Markdown; ejemplos y herramientas según la skill",
            cases=["Guiar un análisis defensivo","Organizar procedimientos de revisión en un laboratorio"],
            choose_if="buscas procedimientos de seguridad para un agente compatible y puedes revisar su alcance y dependencias",
            avoid_if="esperas una auditoría automática garantizada o una herramienta oficial de Anthropic",
            limits="El nombre original incluye Anthropic, pero el autor declara expresamente que es independiente. Las pruebas activas requieren autorización."),
        full_name="mukul975/Anthropic-Cybersecurity-Skills")

    add("kimi-k2-7-code","Kimi K2.7 Code",24,"modelos","runtime",
        "Modelo de Moonshot AI orientado a programación y uso de herramientas; sus pesos oficiales se publican en Hugging Face.",
        dict(api="optional",local_model="supported",claude_code="not_documented",codex="not_documented",cost="choice",hardware="gpu",mode="software",
            scope="Pesos y guía de despliegue del modelo exacto K2.7 Code. El repositorio de pesos está en Hugging Face, no en un GitHub con ese nombre.",
            api_note="La ficha oficial ofrece una API de Moonshot y alternativas de inferencia con pesos propios.",
            subscription_note="La ficha no acredita ejecución con tu suscripción de Claude Code o Codex; usar esos agentes para instalarlo es otra decisión.",
            local_note="Se documenta inferencia con vLLM, SGLang o KTransformers. Comprueba la variante y la guía antes de descargar.",
            cost_note="API e infraestructura tienen costes según la ruta; disponer de pesos no equivale a cómputo gratuito.",
            hardware_note="Modelo de gran tamaño: requiere preparación y hardware especializado; no se recomienda descargarlo sin revisar la guía."),
        dict(kind="source",audience="setup",prerequisites=["Elegir API o despliegue propio","Revisar licencia de pesos y requisitos del motor"],
            steps=["Abre la ficha oficial y decide si necesitas API o pesos para inferencia propia.","Si eliges despliegue propio, revisa docs/deploy_guidance.md antes de reservar equipo o descargar pesos.","Prueba una petición pequeña y comprueba consumo y respuesta antes de integrarlo en tu flujo."],
            command="",note="Es un repositorio oficial de modelo en Hugging Face. No se descargaron los pesos ni se probó su inferencia."),
        dict(prov=["local"],tags=["kimi","moonshot","modelo","programacion","pesos-abiertos","huggingface"],goals=["local"],
            homepage="https://www.kimi.com/code",how="Un motor de inferencia carga los pesos; tu aplicación le envía solicitudes por su interfaz. Moonshot también ofrece acceso por API.",
            install="Sigue la guía de despliegue enlazada desde la ficha oficial para el motor y el hardware elegidos.",stack="Pesos del modelo; vLLM, SGLang o KTransformers",
            cases=["Evaluar un modelo para tareas de programación"],choose_if="puedes evaluar una API o administrar inferencia de un modelo grande",
            avoid_if="buscas un chat local sencillo para un portátil o acceso ya cubierto por tu plan de otro proveedor",
            limits="La licencia de pesos y la infraestructura se revisan por separado. Kimi-K2 en GitHub es un proyecto relacionado de la familia, no la publicación exacta K2.7 Code."),
        model="moonshotai/Kimi-K2.7-Code")

    # New memberships use existing explicit goals only, never invent route IDs.
    valid_goals = {g["id"] for g in compact["discovery"]["goals"]}
    for repo in compact["repos"]:
        assert set(repo.get("goals",[])) <= valid_goals, (repo["id"],repo.get("goals"))
    public = [r for r in compact["repos"] if r["cat"] > 0 and not r.get("alias_of")]
    counts = Counter(r["cat"] for r in public)
    for c in compact["categories"]:
        if c["num"] > 0: c["count"] = counts[c["num"]]
    for goal in compact["discovery"]["goals"]:
        goal["categories"] = sorted({r["cat"] for r in public if goal["id"] in r.get("goals",[]) or r["id"] in goal["starters"]+goal["guided"]})
    compact["meta"].update(title=f"Índice IA — {len(public)} repos curados de IA, automatización y herramientas",updated=DATE)
    for filename,value in [("INDICE_IA.json",compact),("INDICE_IA.detalle.json",detail)]:
        (ROOT/filename).write_text(json.dumps(value,ensure_ascii=False,indent=1)+"\n",encoding="utf8")
    print(dict(added=added,total_public=len(public)))


if __name__ == "__main__":
    main()
