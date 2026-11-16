"""Document references must survive extraction and retain distinct identities."""
import importlib.util
import json
from pathlib import Path
from zipfile import ZipFile

from repo_intelligence.core.catalog import load_catalog

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("document_import",ROOT/"scripts/import_document_repos.py")
parser=importlib.util.module_from_spec(spec)
spec.loader.exec_module(parser)


def test_reference_parser_keeps_repo_identity_and_rejects_other_urls():
    assert parser.repository_name("https://github.com/Owner/Repo.git/tree/main") == "Owner/Repo"
    assert parser.repository_name("https://github.com/Polymarket/py-sdk.") == "Polymarket/py-sdk"
    assert parser.repository_name("https://github.com/topics/agents") is None
    assert parser.repository_name("https://example.com/github.com/owner/repo") is None
    assert parser.repository_name("https://github.com/OnlyOwner") is None


def test_docx_extraction_includes_table_links_and_separates_inline_paragraphs(tmp_path):
    document=tmp_path/"source.docx"
    xml='''<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:body>
    <w:p><w:r><w:t>Directorio de repositorios</w:t></w:r></w:p>
    <w:p><w:r><w:t>Biblioteca de prompts</w:t></w:r></w:p>
    <w:p><w:r><w:t>Directorio de repositorios</w:t></w:r></w:p>
    <w:p><w:r><w:t>Repositorios: Ejemplos</w:t></w:r></w:p>
    <w:tbl><w:tr><w:tc><w:p><w:r><w:t>Nombre</w:t></w:r></w:p></w:tc></w:tr>
    <w:tr><w:tc><w:p><w:hyperlink r:id="rId1"><w:r><w:t>Un enlace cuyo destino no figura en el texto</w:t></w:r></w:hyperlink></w:p></w:tc></w:tr>
    <w:tr><w:tc><w:p><w:r><w:t>Proyecto sin enlace verificable</w:t></w:r></w:p></w:tc></w:tr></w:tbl>
    <w:p><w:r><w:t>Biblioteca de prompts</w:t></w:r></w:p>
    <w:p><w:r><w:t>https://github.com/Polymarket/py-sdk.</w:t></w:r></w:p>
    <w:p><w:r><w:t>10 ejemplos</w:t></w:r></w:p>
    </w:body></w:document>'''
    rels='''<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Target="https://github.com/owner/repository" TargetMode="External"/></Relationships>'''
    with ZipFile(document,"w") as archive:
        archive.writestr("word/document.xml",xml)
        archive.writestr("word/_rels/document.xml.rels",rels)
    extracted=parser.extract_docx(document)
    assert extracted["repositories"] == ["owner/repository","Polymarket/py-sdk"]
    assert len(extracted["directory"]) == 1
    assert len(extracted["unresolved"]) == 1
    assert extracted["directory"][0]["category"] == "Repositorios: Ejemplos"


def test_import_snapshot_resolves_to_sourced_distinct_catalog_entries():
    snapshot=json.loads((ROOT/"reports/document-import-2026-11-14.json").read_text(encoding="utf8"))
    catalog=load_catalog(ROOT)
    retired={r["id"]:r for r in json.loads((ROOT/"data/retired.json").read_text(encoding="utf8"))["repos"]}
    assert snapshot["added_count"] == len(snapshot["added"])
    assert len({item["github_id"] for item in snapshot["added"]}) == len(snapshot["added"])
    for item in snapshot["added"]:
        if item["id"] in retired:
            assert retired[item["id"]]["github_id"] == item["github_id"]
            continue
        repo=catalog.get(item["id"])
        assert repo["github_id"] == item["github_id"]
        assert repo["gh"] == item["full_name"]
        assert item["readme_blob_sha"] in {repo["access"]["source_blob_sha"],repo.get('editorial_review',{}).get('previous_source_blob_sha')}
        assert repo["sources"]["root_tree_sha"]
        assert repo["added_at"] == snapshot["checked_at"]
    assert catalog.get("google-skills")["github_id"] != catalog.get("skills")["github_id"]
    assert catalog.get("ui-sdk")["github_id"] != catalog.get("ui")["github_id"]
    assert catalog.get("pdf-craft")["github_id"] != catalog.get("pdfcraft")["github_id"]


def test_sensitive_access_and_archive_distinctions_survive_the_import():
    catalog=load_catalog(ROOT)
    assert catalog.get("shannon")["access"]["claude_code"] == "not_documented"
    assert catalog.get("shannon")["access"]["codex"] == "project_integration"
    assert catalog.get("craft-anything")["access"]["codex"] == "unconfirmed"
    assert catalog.get("open-seo")["access"]["api"] == "not_required"
    assert "DataForSEO" in catalog.get("open-seo")["access"]["cost_note"]
    # The archived Polymarket client was retired; its ledger entry points to the live SDK.
    retired={r["id"]:r for r in json.loads((ROOT/"data/retired.json").read_text(encoding="utf8"))["repos"]}
    assert catalog.get("py-clob-client") is None
    assert retired["py-clob-client"]["archived"] is True and retired["py-clob-client"]["replaced_by"] == ["py-sdk"]
    assert catalog.get("py-sdk").get("status") != "archived"
    assert catalog.get("pdf-craft")["access"]["local_model"] == "supported"
