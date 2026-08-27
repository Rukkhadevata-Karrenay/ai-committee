from __future__ import annotations
import json
import sys

REQUIRED = {"proposal", "supporting_reasons", "counterarguments", "assumptions", "evidence_needed",
            "security_concerns", "dissenting_views", "confidence", "recommended_next_test"}

def main() -> int:
    value = json.load(sys.stdin)
    missing = sorted(REQUIRED - set(value)) if isinstance(value, dict) else sorted(REQUIRED)
    if missing:
        print(json.dumps({"valid": False, "missing": missing})); return 1
    if not isinstance(value["confidence"], (int, float)) or not 0 <= value["confidence"] <= 1:
        print(json.dumps({"valid": False, "error": "confidence_out_of_range"})); return 1
    print(json.dumps({"valid": True})); return 0

if __name__ == "__main__":
    raise SystemExit(main())
