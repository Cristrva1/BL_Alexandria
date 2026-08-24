from repo_intelligence.extract.readme import clip_sentence, is_junk_line, summarize_readme


def test_skips_html_and_badges_for_activepieces() -> None:
    text = """
<h1 align="center"><a target="_blank" href="https://activepieces.com"><img alt="Activepieces" src="x.png"/></a></h1>
<p align="center"><img src='https://img.shields.io/badge/license-MIT-green' /></p>
<p align="center">
   An open source replacement for Zapier
</p>
"""
    summary = summarize_readme(text, max_chars=220)
    assert "Zapier" in summary
    assert "target=" not in summary
    assert "href=" not in summary
    assert not summary.endswith("...")


def test_n8n_uses_first_real_paragraph() -> None:
    text = """
![Banner image](https://example.com/banner.png)

# n8n - Secure Workflow Automation for Technical Teams

n8n is a workflow automation platform that gives technical teams the flexibility of code with the speed of no-code. With 400+ integrations, native AI capabilities, and a fair-code license, n8n lets you build powerful automations while maintaining full control over your data and deployments.
"""
    summary = summarize_readme(text, max_chars=220)
    assert summary.startswith("n8n is a workflow automation platform")
    assert summary.endswith(".")
    assert len(summary) <= 221


def test_clip_sentence_does_not_cut_mid_word() -> None:
    text = "Organizations build custom applications like dashboards, admin panels, customer 360, IT automation, and service management tools to help their teams work more efficiently."
    clipped = clip_sentence(text, 80)
    assert "..." not in clipped
    assert not clipped.rstrip(".").endswith(("and", "the", "a"))
    assert clipped.endswith(".")
    assert " " not in clipped.split()[-1].rstrip(".")


def test_language_switcher_and_ascii_are_junk() -> None:
    assert is_junk_line("English | 中文 | 日本語")
    assert is_junk_line("██╗ ██╗███████╗ █████╗")
    assert is_junk_line('alt="chat on Discord"></a>')
    assert not is_junk_line("LangChain is a framework for building agents and LLM-powered applications.")
