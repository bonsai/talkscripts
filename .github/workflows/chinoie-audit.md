---
emoji: 📊
description: llm-wiki から生成した知恵の館の成果物(床=候補, 館=知恵の館/ の台本)を収集し、読んで集計・評価し、レポートissueを作る作業ワークフロー。
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
    title-prefix: "[知恵の館] 棚卸し"
---

# 知恵の館 作業wf（収集 → 読む → 集計 → 評価）

llm-wiki から生成した成果物を集め、読んで集計し、評価をとる作業ワークフロー。
**出力はイシュー作成のみ**（ファイルは変更しない）。

## 対象

- **床（候補）**: リポジトリ直下の `*.md` と `seed/*.md`（llm-wiki から生成・集約した種）
- **館（完成品）**: `知恵の館/#NN-*.md`（台本化・動画化したもの）
- **評価軸**: `知恵の館/RUBRIC.md`、`scripts/hall-eval.py`（あれば）
- `README.md` / `INDEX.md` / `seed/INDEX.md`（索引・YouTubeリンク・シリーズ定義）

## Task

1. **収集**: 直下 `*.md`・`seed/*.md`（床）と `知恵の館/#NN-*.md`（館）を列挙する。`README.md` から YouTube リンクとエピソード対応を拾う。

2. **読む**: 各ファイルを開き、frontmatter/メタ（種別・字数）と本文を確認する。

3. **集計**:
   - 床: 件数、類型別（エッセイ / SS / 親子対話 / その他）、字数分布。
   - 館: 件数、`#NN` の連番と欠番、各台本の字数・推定朗読時間（400字/分）。
   - 昇格率（床 → `#NN`）。

4. **評価**:
   - `知恵の館/RUBRIC.md` の 9 軸（重み付き）を各館台本に当てて **0〜100** を出す。
   - `scripts/hall-eval.py` が動くなら実行して一次スクリーニングに併用（動かなければ RUBRIC を人手適用）。
   - 各台本に **A / B / C** を付け、要修正点を1行で添える。

5. **出力**: `create-issue` のみで出す。
   - タイトル: `[知恵の館] 棚卸し YYYY-MM-DD`
   - 本文: 集計表（床/館）＋ 評価表（#NN・score・rank・所見）＋ 次アクション（昇格候補/改善点）。
   - ファイル（REPORT.md 等）は作成・変更しない。

6. **noop**: 床も館も1件も無い場合は、短い理由で `noop` を返す。

## 言語

日本語。表と箇条書きで簡潔に。
