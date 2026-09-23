---
emoji: 🎭
description: talkscripts の台本を産出する。workflow_dispatch で series と seed/ の候補を指定すると、読み上げ向けに整えて <series>/#NN-<slug>.md を追加する PR を作る。PR 本文に全文を貼り、merge でそのシリーズの完成フォルダに登録される。
intent: 査読前(seed)から各シリーズの台本を作り、全文を貼った PR で査読 → merge＝完成登録
on:
  workflow_dispatch:
    inputs:
      series:
        type: string
        description: シリーズ（フォルダ名）。例 知恵の館 / SFショートショート / SF落語
        required: true
      candidate:
        type: string
        description: seed/ の候補ファイル名（例 09-embed-layer-essay-20260924.md）
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
      - "*/*.md"
      - "seed/INDEX.md"
      - "README.md"
      - "SERIES.md"
---

# talkscripts 執筆（seed → PR → シリーズ）

流れ: **seed/（査読前）** ──台本化──▶ **PR（全文を本文に貼る）** ──merge──▶ **`<series>/#NN-….md`（完成）**。
シリーズは `知恵の館` に限らない（`SFショートショート` / `SF落語` …）。台帳は `SERIES.md`。

## Task

1. **定位置の把握**:
   - `SERIES.md`（シリーズ台帳）と `README.md`（フロー）、`RUBRIC.md`（評価軸）を読む。
   - 入力 `series` のフォルダと、その `README.md`（形式・尺）を確認する。
   - 入力 `candidate` を `seed/<candidate>` として読む（無ければ `noop`）。
   - `<series>/` の既存 `#NN-*.md` を見て次の番号 `#NN` を決める（欠番は詰める）。

2. **台本化**（`<series>/#NN-<slug>.md` を新規追加。フォルダが無ければ `SERIES.md` に従い作る）:
   - シリーズの形式に合わせる（例: 知恵の館=エッセイ朗読 / SFショートショート=掌編 / SF落語=落語形式の一人語り）。
   - **読み上げ向けに整える**: 括弧・記号・ルビ・脚注・注釈・URL・絵文字を除去し、数式や記号は読み下す。
   - frontmatter・見出し記号(`#`)は本文から外す。句点で文を切る。元の声・文体を保つ（要約しない）。
   - `slug` が空なら内容から短い英語 slug を付ける。

3. **PR 本文に全文を貼る（必須）**:
   - 追加した台本の**全文をそのまま** PR 本文に貼る（査読者がファイルを開かず読めるように）。
   - 併せて 元 seed・`RUBRIC.md` による score（あれば）・DoD（読み下し済 / 記号除去 / 番号整合 / 全文貼付済）を書く。

4. **Safe Outputs**: 出力は `create-pull-request` のみ。
   - PR タイトル: `[<series>] #NN <title> 台本（査読）`
   - 変更は `<series>/#NN-….md`（＋必要なら `seed/INDEX.md`・`README.md`・`SERIES.md`）に限定する。
   - **merge されるとそのシリーズの完成フォルダに登録される**（＝PR の差分は該当シリーズへの追加）。
   - 同一 `candidate` の PR が open なら新規作成せず、既存 PR への追記方針を提案する。

5. **noop**: 次の場合は短い理由で `noop` を返す。
   - `series` が `SERIES.md` に無い（新シリーズは人格が勝手に作らない。`noop` で提案）
   - `seed/<candidate>` が存在しない / 空
   - 既に同一内容が `#NN` として台本化済み
   - 内容が台本化に適さない（表・コードのみ等）

## 言語

日本語。元テキストの文体・声を保つ。
