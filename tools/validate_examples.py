#!/usr/bin/env python3
"""Check example Creator Continuity Records against the local schema.

This is intentionally small and check-only. It uses no external packages and
does not attempt to implement full JSON Schema validation.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "creator_continuity_record.schema.json"
EXAMPLES_DIR = ROOT / "examples"


def load_json(path: Path) -> object:
    try:
        with path.open(encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path}: invalid JSON: {exc}") from exc
    except OSError as exc:
        raise ValueError(f"{path}: could not read file: {exc}") from exc


def require_object(value: object, path: Path) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return value


def validate_example(
    path: Path,
    record: dict[str, object],
    schema: dict[str, object],
) -> list[str]:
    errors: list[str] = []
    required = schema.get("required", [])
    properties = schema.get("properties", {})

    if not isinstance(required, list) or not all(isinstance(item, str) for item in required):
        return [f"{SCHEMA_PATH}: required must be a list of strings"]

    if not isinstance(properties, dict):
        return [f"{SCHEMA_PATH}: properties must be an object"]

    missing = sorted(field for field in required if field not in record)
    if missing:
        errors.append(f"missing required fields: {', '.join(missing)}")

    if schema.get("additionalProperties") is False:
        unexpected = sorted(set(record) - set(properties))
        if unexpected:
            errors.append(f"unexpected top-level fields: {', '.join(unexpected)}")

    status_property = properties.get("continuity_status", {})
    status_enum = status_property.get("enum", []) if isinstance(status_property, dict) else []
    status = record.get("continuity_status")
    if status not in status_enum:
        errors.append(f"continuity_status must be one of {status_enum!r}; got {status!r}")

    scope_property = properties.get("continuity_scope", {})
    scope_enum = scope_property.get("enum", []) if isinstance(scope_property, dict) else []
    scope = record.get("continuity_scope")
    if scope not in scope_enum:
        errors.append(f"continuity_scope must be one of {scope_enum!r}; got {scope!r}")

    return [f"{path}: {error}" for error in errors]


def main() -> int:
    errors: list[str] = []

    try:
        schema = require_object(load_json(SCHEMA_PATH), SCHEMA_PATH)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    example_paths = sorted(EXAMPLES_DIR.glob("*.json"))
    if not example_paths:
        print(f"{EXAMPLES_DIR}: no example JSON files found", file=sys.stderr)
        return 1

    for path in example_paths:
        try:
            record = require_object(load_json(path), path)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        errors.extend(validate_example(path, record, schema))

    if errors:
        print("FAIL: example validation failed", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"PASS: validated {len(example_paths)} example records against {SCHEMA_PATH.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
