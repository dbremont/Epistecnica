#!/usr/bin/env python3
"""
REES tree validator.

The Reality Epistemic Element Set (REES) tree is stored canonically in
src/note/app/data/epistemica/rees.json and rendered by the REES atlas
(rees.html). This script validates that store against the decomposition
contract and prints its statistics. Stdlib only.

Contract (see src/note/README.md and the philosophia guide):
  - every node has a label, type, kind, order, and description;
  - sibling labels are unique, and every root-to-node path is unique;
  - a grouping (type) node never terminates a branch (always has children);
  - a grouping node's type is its own label;
  - an instance may have children (a recursive instance chain); a leaf
    instance's type is its parent's type when the parent is a grouping/root,
    and is its declared type when the parent is an instance;
  - every leaf is an instance; kind/order values are from the fixed sets;
  - the declared stats match the tree.

Usage: python3 bin/rees_check.py
"""

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NOTE = REPO / "src" / "note"
REES = NOTE / "app" / "data" / "epistemica" / "rees.json"

KINDS = {"root", "grouping", "instance"}
ORDERS = {"epistemic", "ontic", "reflexive"}


def walk(node, parent_type, parent_kind, path, out):
    label = node.get("label")
    here = path + [label]
    out.append((node, tuple(here), parent_type, parent_kind))
    for child in node.get("children", []):
        walk(child, node.get("type"), node.get("kind"), here, out)


def check(data):
    errors = []
    seen_paths = set()
    nodes = []

    for root in data.get("roots", []):
        walk(root, "Aggregate", "root", [], nodes)

    for node, path, parent_type, parent_kind in nodes:
        label = node.get("label")
        where = " → ".join(path)

        if not isinstance(label, str) or not label.strip():
            errors.append("node with empty label at %s" % where)
            continue
        if node.get("kind") not in KINDS:
            errors.append("%s: bad kind %r" % (where, node.get("kind")))
        if node.get("order") not in ORDERS:
            errors.append("%s: bad order %r" % (where, node.get("order")))
        if not isinstance(node.get("description"), str) or not node["description"].strip():
            errors.append("%s: missing description" % where)

        if path in seen_paths:
            errors.append("duplicate path: %s" % where)
        seen_paths.add(path)

        if node.get("kind") == "grouping":
            if node.get("type") != label:
                errors.append("%s: grouping type %r != label" % (where, node.get("type")))
            if not node.get("children"):
                errors.append("%s: grouping terminates a branch" % where)
        elif node.get("kind") == "instance":
            if not isinstance(node.get("type"), str) or not node["type"].strip():
                errors.append("%s: missing instance type" % where)
            if (
                not node.get("children")
                and parent_kind != "instance"
                and node.get("type") != parent_type
            ):
                errors.append(
                    "%s: instance type %r != parent type %r"
                    % (where, node.get("type"), parent_type)
                )

    # sibling uniqueness
    def siblings(node):
        labels = [c.get("label") for c in node.get("children", [])]
        if len(labels) != len(set(labels)):
            errors.append("duplicate sibling labels under %r" % node.get("label"))
        for c in node.get("children", []):
            siblings(c)

    for root in data.get("roots", []):
        siblings(root)

    stats = {
        "nodes": len(nodes),
        "groupings": sum(1 for n, _, _, _ in nodes if n.get("kind") == "grouping"),
        "instances": sum(1 for n, _, _, _ in nodes if n.get("kind") == "instance"),
        "branches": len(data.get("roots", [{}])[0].get("children", [])),
        "maxDepth": max((len(p) for _, p, _, _ in nodes), default=0),
    }
    declared = data.get("stats", {})
    for key, value in stats.items():
        if declared.get(key) != value:
            errors.append(
                "stats.%s declared %r, computed %r" % (key, declared.get(key), value)
            )

    return errors, stats


def main():
    if not REES.exists():
        print("ERROR: %s not found" % REES, file=sys.stderr)
        return 1
    try:
        data = json.loads(REES.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print("ERROR: invalid JSON in %s: %s" % (REES, exc), file=sys.stderr)
        return 1

    errors, stats = check(data)
    for err in errors:
        print("[rees] %s" % err, file=sys.stderr)

    print(
        "[rees] ok: %d nodes (%d groupings, %d instances), %d branches, depth %d"
        % (
            stats["nodes"],
            stats["groupings"],
            stats["instances"],
            stats["branches"],
            stats["maxDepth"],
        )
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
