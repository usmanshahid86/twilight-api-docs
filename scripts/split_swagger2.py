#!/usr/bin/env python3
"""
Split a Swagger 2.0 spec by path prefix and PRUNE definitions to only those used.

Usage:
  pip3 install pyyaml
  python3 scripts/split_swagger2.py openapi.yml specs/chain
"""

import os, re, sys
from copy import deepcopy
import yaml

SPLITS = [
  ("twilight-bridge", ["/twilight-project/nyks/bridge"]),
  ("twilight-fork",   ["/twilight-project/nyks/fork"]),
  ("twilight-volt",   ["/twilight-project/nyks/volt"]),
  ("twilight-zkos",   ["/twilight-project/nyks/zkos"]),

  ("cosmos-auth",       ["/cosmos/auth/"]),
  ("cosmos-bank",       ["/cosmos/bank/"]),
  ("cosmos-tx",         ["/cosmos/tx/"]),
  ("cosmos-staking",    ["/cosmos/staking/"]),
  ("cosmos-gov",        ["/cosmos/gov/"]),
  ("cosmos-tendermint", ["/cosmos/base/tendermint/"]),
  ("cosmos-slashing",   ["/cosmos/slashing/"]),
  ("cosmos-distribution",[ "/cosmos/distribution/"]),
   
  ("tendermint", ["/tendermint/"]), 
  ("ibc", ["/ibc/"]),
]

EMIT_REST_BUCKET = True
REST_BUCKET_NAME = "misc-other"

REF_RE = re.compile(r"^#/definitions/(?P<name>.+)$")

def matches_prefix(path, prefixes):
  return any(path.startswith(p) for p in prefixes)

def iter_refs(node):
  if isinstance(node, dict):
    ref = node.get("$ref")
    if isinstance(ref, str):
      m = REF_RE.match(ref)
      if m:
        yield m.group("name")
    for v in node.values():
      yield from iter_refs(v)
  elif isinstance(node, list):
    for it in node:
      yield from iter_refs(it)

def prune_definitions(spec):
  defs = spec.get("definitions")
  if not isinstance(defs, dict) or not defs:
    return

  needed = set(iter_refs(spec.get("paths", {})))
  queue = list(needed)

  while queue:
    name = queue.pop()
    d = defs.get(name)
    if d is None:
      continue
    for dep in iter_refs(d):
      if dep not in needed:
        needed.add(dep)
        queue.append(dep)

  spec["definitions"] = {k: v for k, v in defs.items() if k in needed}

def set_title(spec, name):
  info = spec.get("info") or {}
  base = (info.get("title") or "Twilight Chain API").strip() or "Twilight Chain API"
  info["title"] = f"{base} — {name}"
  spec["info"] = info

def write_yaml(path, data):
  with open(path, "w", encoding="utf-8") as f:
    yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True)

def main():
  if len(sys.argv) != 3:
    print("Usage: python3 scripts/split_swagger2.py <openapi.yml> <out_dir>")
    sys.exit(1)

  in_path, out_dir = sys.argv[1], sys.argv[2]
  os.makedirs(out_dir, exist_ok=True)

  with open(in_path, "r", encoding="utf-8") as f:
    spec = yaml.safe_load(f)

  if spec.get("swagger") != "2.0":
    raise SystemExit(f"Expected Swagger 2.0 input. Found swagger={spec.get('swagger')!r}")

  all_paths = spec.get("paths") or {}
  assigned = set()

  for name, prefixes in SPLITS:
    out = deepcopy(spec)
    out["paths"] = {p: v for p, v in all_paths.items() if matches_prefix(p, prefixes)}
    if not out["paths"]:
      print(f"skip {name}: 0 paths")
      continue

    prune_definitions(out)
    set_title(out, name)

    out_file = os.path.join(out_dir, f"{name}.yml")
    write_yaml(out_file, out)
    assigned.update(out["paths"].keys())
    print(f"wrote {out_file}: {len(out['paths'])} paths, {len(out.get('definitions', {}))} defs")

  if EMIT_REST_BUCKET:
    rest = deepcopy(spec)
    rest["paths"] = {p: v for p, v in all_paths.items() if p not in assigned}
    if rest["paths"]:
      prune_definitions(rest)
      set_title(rest, REST_BUCKET_NAME)
      out_file = os.path.join(out_dir, f"{REST_BUCKET_NAME}.yml")
      write_yaml(out_file, rest)
      print(f"wrote {out_file}: {len(rest['paths'])} paths, {len(rest.get('definitions', {}))} defs")

if __name__ == "__main__":
  main()