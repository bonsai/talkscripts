---
emoji: 📊
description: llm-wiki から生成した知恵の館の成果物(床=直下の候補, 館=知恵の館/ の台本)を収集し、読んで集計・評価し、REPORT.md とレポートissueを作る作業ワークフロー。
intent: 生成物の棚卸しと評価を定期レポートにし、昇格・改善の判断材料にする
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
  create-pull-request:
    allowed-files:
      - "REPORT.md"
      - "INDEX.md"
---

# 知恵の館 作業wf（収集 → 読む → 集計 → 評価）

llm-wiki から生成した成果物を集め、読んで集計し、評価をとる作業ワークフロー。

## 対象

- **床**: リポジトリ直下の候補 `*.md`（llm-wiki から生成・集約したもの）
- **館**: `知恵の館/#NN-*.md`（完成した朗読台本）
- `README.md` / `INDEX.md`（索引・YouTubeリンク・シリーズ定義）

## Task

1. **収集**: 直下の候補 `*.md` と `知恵の館/#NN-*.md` を列挙する。`README.md` から YouTube リンクとエピソード対応を拾う。

2. **読む**: 各ファイルを開き、frontmatter/メタ（種別・字数）と本文を確認する。

3. **集計**:
   - 候補: 件数、類型別（エッセイ / SS / 親子対話）、字数分布。
   - 館: 件数、`#NN` の連番と欠番、各台本の字数・推定朗読時間（400字/分）。
   - 昇格率（候補 → `#NN`）。

4. **評価**（各台本、観点を明示）:
   - 読み上げ適性: 括弧・記号・ルビ・URL・絵文字の残存 / 句点で文が切れているか / メタ行は末尾か。
   - 尺の目安: 3分=約1200字、8分=約3200字（400字/分）。想定尺との差。
   - 総合ランク **A / B / C** を付け、要修正点を1行で添える。

5. **出力**:
   - `REPORT.md` を更新（集計表 + 評価表 + 次アクション）し、`create-pull-request` で出す。
   - 要約を `create-issue`（`[知恵の館] 棚卸し YYYY-MM-DD`）として投稿する。
   - 変更は `REPORT.md`・`INDEX.md` に限定する。

6. **noop**: 対象（候補も台本も）が1件も無い場合は、短い理由で `noop` を返す。

## 言語

日本語。表と箇条書きで簡潔に。
