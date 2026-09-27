#!/usr/bin/env python3
"""Small deterministic companion for checking an authorization action list."""
import json, sys

LEVELS = {"READ", "DRAFT", "WRITE_REVERSIBLE", "WRITE_IRREVERSIBLE", "EXTERNAL_EXECUTION"}
HIGH = {"WRITE_IRREVERSIBLE", "EXTERNAL_EXECUTION"}

def audit(items):
    findings = []
    for i, item in enumerate(items, 1):
        action = item.get("action", "UNKNOWN")
        scope = item.get("scope", "")
        approval = item.get("approval", False)
        if action not in LEVELS:
            findings.append([i, "BLOCK", "unknown action class"])
        elif not scope:
            findings.append([i, "BLOCK", "missing resource scope"])
        elif action in HIGH and not approval:
            findings.append([i, "ASK", "high-side-effect action needs approval"])
        else:
            findings.append([i, "ALLOW", "bounded action"])
    status = "NO_GO" if any(x[1] == "BLOCK" for x in findings) else ("GO_WITH_GATES" if any(x[1] == "ASK" for x in findings) else "GO")
    return {"status": status, "findings": findings}

if __name__ == "__main__":
    try:
        print(json.dumps(audit(json.load(sys.stdin)), ensure_ascii=False, indent=2))
    except (json.JSONDecodeError, TypeError) as exc:
        print(json.dumps({"status": "NO_GO", "error": str(exc)}, ensure_ascii=False)); sys.exit(2)
