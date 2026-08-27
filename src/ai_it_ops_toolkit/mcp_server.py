"""Optional MCP transport exposing the ten deterministic tools."""

from __future__ import annotations

from .tools import TOOL_HANDLERS, run_tool


def build_server():
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError as error:
        raise RuntimeError("Install the MCP extra: pip install -e .[mcp]") from error

    server = FastMCP("AI IT Operations Toolkit")

    def make_handler(tool_name: str):
        def invoke(payload: dict) -> dict:
            return run_tool(tool_name, payload)

        invoke.__name__ = tool_name.replace("-", "_")
        invoke.__doc__ = f"Run the {tool_name} read-only assessment helper."
        return invoke

    for name in TOOL_HANDLERS:
        server.tool(name=name)(make_handler(name))
    return server


def main() -> None:
    build_server().run()


if __name__ == "__main__":
    main()
