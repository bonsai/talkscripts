#!/usr/bin/env python3
"""pr-gate — 知恵の館 PR の1次判定（RUBRIC v2 スコアで合否）。

`hall-eval.py` を読み込み、与えたエッセイファイルを採点する。
閾値未満が1つでもあれば exit 1（＝PR の check を落として阻止）。

使い方:
  python3 scripts/pr-gate.py 知恵の館/#04-....md [...]
  HALL_THRESHOLD=70 python3 scripts/pr-gate.py <files...>
  # 引数なし: 直近の変更（git diff origin/main...HEAD）から自動抽出
"""
from __future__ import annotations
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
THRESHOLD = float(os.environ.get("HALL_THRESHOLD", "65"))
EXCLUDE = re.compile(r"(RUBRIC|PROMPT|INDEX|README)")


def load_hall():
    HALL = os.path.normpath(os.path.join(HERE, "..", "..", "scripts", "hall-eval.py"))
    spec = importlib.util.spec_from_file_location("hall_eval", HALL)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def changed_files() -> list[str]:
    base = os.environ.get("GITHUB_BASE_REF", "main")
    try:
        out = subprocess.check_output(["git", "diff", "--name-only", f"origin/{base}...HEAD"], text=True)
    except Exception:
        out = ""
    files = [f for f in out.splitlines() if f.startswith("知恵の館/") and f.endswith(".md")]
    return [f for f in files if not EXCLUDE.search(os.path.basename(f))]


def main(argv):
    he = load_hall()
    ref = he.refs()
    files = argv or changed_files()
    if not files:
        print("pr-gate: 対象エッセイなし → PASS")
        return 0
    print(f"pr-gate: 1次判定 (RUBRIC v2, 閾値 {THRESHOLD}, {len(files)}件)")
    bad = []
    for f in files:
        if not os.path.exists(f):
            print(f"  skip (not found): {f}"); continue
        sc, a, L, title = he.evaluate(f, ref)
        ok = sc >= THRESHOLD
        print(f"  [{'PASS' if ok else 'FAIL'}] {sc:>5}  {L:>5}字  {title}")
        if not ok:
            bad.append((f, sc))
    print()
    if bad:
        print("❌ 1次判定 NG（閾値未満）:")
        for f, sc in bad:
            print(f"   - {sc} < {THRESHOLD}  {f}")
        print("\n低スコアは PR を阻止します（改善してから再送してください）。")
        return 1
    print(f"✅ 1次判定 PASS（全 {len(files)} 件 >= {THRESHOLD}）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
