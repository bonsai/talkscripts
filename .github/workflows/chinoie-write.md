---
emoji: 🏛️
description: 知恵の館シリーズの朗読台本を産出する。workflow_dispatch で候補ファイル(直下の *.md)を指定すると、読み上げ向け台本 #NN-<slug>.md に整えて PR を作る。
intent: 候補エッセイ/SS を朗読向け台本に整え、人間がレビューできる PR にする
on:
  workflow_dispatch:
    inputs:
      candidate:
        type: string
        description: 候補ファイル名（リポジトリ直下の *.md, 例 09-embed-layer-essay-20260924.md）
        required: true
      slug:
        type: string
        description: 台本 slug（#NN-<slug>.md の <slug>。空なら内容から命名）
        required: false
concurrency:
  job-discriminator: "${{ github.run_id }}"
permissions:
  contents: read
  pull-requests: read
  issues: read
tools:
  github:
    mode: gh-proxy
    toolsets: [default]
safe-outputs:
  create-pull-request:
    allowed-files:
      - "*.md"
---

# 知恵の館 執筆（候補 → 朗読台本）

## Task

1. **定位置の把握**:
   - `README.md`（シリーズ定義・命名）と `INDEX.md`（朗読原稿候補の索引）を読む。
   - 直下の既存 `#NN-*.md` を確認し、次に使う番号 `#NN` を決める（欠番があれば詰める）。
   - 入力 `candidate` のファイルを読む（直下に無ければ `noop`）。

2. **台本化**（`#NN-<slug>.md` をリポジトリ直下に作成）:
   - **読み上げ向けに整える**: 括弧・記号・ルビ・脚注・注釈・URL・絵文字を除去し、数式や記号は読み下す。
   - frontmatter・見出し記号(`#`)は本文から外す（メタは残してよいが読み上げ対象にしない）。
   - **エッセイの声を保つ**。要約せず、冗長の削ぎ落としと読み下しに留める。句点で文を切る。
   - `slug` が空なら内容から短い英語 slug を付ける。

3. **索引の更新**: `INDEX.md` の「昇格済み（直下・#NN）」に `#NN <slug>` を追記する。

4. **Safe Outputs**: 生成結果は `create-pull-request` のみで出す。
   - PR タイトル: `[知恵の館] #NN <title> 台本`
   - 本文に 元候補・要点・DoD チェックリスト（読み下し済 / 記号除去 / 目次番号整合）を書く。
   - 変更は直下の `*.md` に限定する。
   - 同一 `candidate` の PR が open なら新規作成せず、既存 PR への追記方針を提案する。

5. **noop**: 次の場合は短い理由で `noop` を返す。
   - `candidate` が存在しない / 空
   - 既に同一内容が `#NN` として台本化済み
   - 内容が台本化に適さない（表・コードのみ等）

## 言語

日本語。エッセイ本来の文体・声を保つ。
