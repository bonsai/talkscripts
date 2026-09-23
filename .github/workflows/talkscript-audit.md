---
emoji: 📊
description: talkscripts の全シリーズの成果物(seed=査読前, 各シリーズ=完成品)を収集し、読んで集計・評価し、レポートissueを作る作業ワークフロー。
intent: 生成物の棚卸しと評価を定期レポート(issue)にし、昇格・改善の判断材料にする
on:
  schedule: daily
  workflow_dispatch:
permissions:
  contents: read
  issues: read
  pull-requests: read
tools:
  github:
    mode: gh-proxy
    toolsets: [default]
safe-outputs:
  create-issue:
    title-prefix: "[talkscripts] 棚卸し"
---

# talkscripts 作業wf（収集 → 読む → 集計 → 評価）

seed（査読前）と各シリーズ（完成品）を収集して読み、集計・評価をとる作業ワークフロー。
**出力はイシュー作成のみ**（ファイルは変更しない）。

## 対象

- **査読前**: `seed/*.md`（全シリーズ共通の種）
- **完成品**: `SERIES.md` に載る各シリーズフォルダの `#NN-*.md`
- **評価軸**: `RUBRIC.md`（共通・9軸）、`.github/workflows/hall-eval.py`（あれば）
- `README.md` / `SERIES.md` / `seed/INDEX.md`

## Task

1. **収集**: `SERIES.md` を読み、各シリーズフォルダの `#NN-*.md` を列挙する。`seed/*.md` も列挙する。

2. **読む**: 各ファイルの frontmatter/メタ（シリーズ・種別・字数）と本文を確認する。

3. **集計**:
   - シリーズ別: 完成品の件数、`#NN` の連番・欠番、字数・推定朗読時間（400字/分）、尺の目安との差。
   - 査読前: `seed/` の件数、類型別、字数分布。
   - 昇格率（`seed` → 完成品）。

4. **評価**:
   - `RUBRIC.md` の 9 軸（重み付き）を各完成品に当てて **0〜100** を出す。シリーズ固有 `RUBRIC.md` があれば加味する。
   - `.github/workflows/hall-eval.py` が動くなら実行して一次スクリーニングに併用（動かなければ RUBRIC を人手適用）。
   - 各作に **A / B / C** を付け、要修正点を1行で添える。

5. **出力**: `create-issue` のみで出す。
   - タイトル: `[talkscripts] 棚卸し YYYY-MM-DD`
   - 本文: シリーズ別の集計表 ＋ 評価表（シリーズ・#NN・score・rank・所見）＋ 次アクション（昇格候補 / 改善 / 新シリーズ提案）。
   - ファイルは作成・変更しない。

6. **noop**: 対象（seed も完成品も）が1件も無い場合は、短い理由で `noop` を返す。

## 言語

日本語。表と箇条書きで簡潔に。
