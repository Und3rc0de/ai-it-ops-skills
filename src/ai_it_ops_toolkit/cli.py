"""Command-line interface for local and CI usage."""

from __future__ import annotations

import argparse
import json
import sys

from .tools import TOOL_HANDLERS, run_tool, to_json


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a safe AI IT Operations helper")
    parser.add_argument("tool", choices=sorted(TOOL_HANDLERS))
    parser.add_argument("--input", default="{}", help="JSON object consumed by the tool")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input)
        if not isinstance(payload, dict):
            raise TypeError("input must be a JSON object")
        print(to_json(run_tool(args.tool, payload)))
    except (TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
