from repo_intelligence.analysis.curation import resolve_enrich_targets


def test_ids_override_only_new() -> None:
    registry = ["n8n", "chatwoot", "nuevo"]
    curated = {"n8n", "chatwoot"}
    assert resolve_enrich_targets(registry, curated, only_new=True, ids=["n8n"]) == ["n8n"]


def test_only_new_without_ids() -> None:
    registry = ["n8n", "nuevo"]
    curated = {"n8n"}
    assert resolve_enrich_targets(registry, curated, only_new=True, ids=None) == ["nuevo"]
