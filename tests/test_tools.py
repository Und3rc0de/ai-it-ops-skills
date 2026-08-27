from ai_it_ops_toolkit.tools import TOOL_HANDLERS, run_tool, sanitize


def test_all_ten_tools_are_registered():
    assert len(TOOL_HANDLERS) == 10


def test_every_tool_is_read_only_by_contract():
    for name in TOOL_HANDLERS:
        assert run_tool(name, {})["mutations_performed"] is False


def test_sanitizer_masks_common_secret_assignments():
    assert "hunter2" not in sanitize("password=hunter2")


def test_ticket_key_is_stable_and_content_is_sanitized():
    payload = {"component": "api", "environment": "prod", "symptom": "token=abc failed"}
    first = run_tool("technical-support-ticket", payload)
    second = run_tool("technical-support-ticket", payload)
    assert first["details"]["duplicate_key"] == second["details"]["duplicate_key"]
    assert "abc" not in first["details"]["description"]


def test_deployment_is_no_go_when_required_evidence_is_missing():
    result = run_tool("deployment-readiness", {"checks": {"tests": True}})
    assert result["details"]["decision"] == "no-go"
