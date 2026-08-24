from pathlib import Path

from repo_intelligence.core.install_mode import decision, install_mode


def test_n8n_is_docker_local() -> None:
    assert install_mode({"id": "n8n", "role": "platform", "setup": "medium"}) == "docker_local"
    assert decision({"id": "n8n", "role": "platform", "setup": "medium"}) == "use_now"


def test_evolution_api_is_docker_local() -> None:
    assert install_mode({"id": "evolution-api", "role": "app", "setup": "medium"}) == "docker_local"


def test_skill_is_reference_only() -> None:
    assert install_mode({"id": "n8n-skills", "role": "skill", "setup": "easy"}) == "reference_only"
    assert decision({"id": "n8n-skills", "role": "skill"}) == "reference"


def test_repomix_is_global() -> None:
    assert install_mode({"id": "repomix", "role": "app", "setup": "easy"}) == "global"
    assert decision({"id": "repomix"}) == "use_now"


def test_markitdown_is_local_project() -> None:
    assert install_mode({"id": "markitdown", "role": "library", "setup": "easy"}) == "local_project"


def test_litellm_is_local_project() -> None:
    assert install_mode({"id": "litellm", "role": "runtime", "setup": "medium"}) == "local_project"


def test_heavy_is_deferred() -> None:
    assert install_mode({"id": "comfyui", "role": "platform", "setup": "heavy"}) == "deferred"
    assert decision({"id": "comfyui", "role": "platform", "setup": "heavy"}) == "defer"


def test_unknown_library_is_reference_only() -> None:
    assert install_mode({"id": "loguru", "role": "library", "setup": "easy"}) == "reference_only"


def test_id_list_wins_over_heavy() -> None:
    # n8n is medium in the index; if someone marks setup heavy, docker_local still wins
    assert install_mode({"id": "n8n", "role": "platform", "setup": "heavy"}) == "docker_local"
