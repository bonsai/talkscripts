# talkscripts

朗読・上演の台本リポジトリ（**複数シリーズ**）。**査読前(seed) → PR査読 → 完成(各シリーズ)** の流れで管理する。
台本は「知恵の館」に限らない（SFショートショート、SF落語 …）。

## 構成

```
talkscripts/
├── seed/                 ← 査読前（エッセイ / SS / 対話 の種）。llm-wiki 由来。
│   └── INDEX.md          ← 種の索引（RUBRIC v2 スコア付き）
├── 知恵の館/             ← 完成品（シリーズ: エッセイ朗読）。**merge で登録**。
├── SFショートショート/    ← 完成品（シリーズ: 掌編 SF）
├── SF落語/               ← 完成品（シリーズ: SF 落語）
├── RUBRIC.md             ← 評価軸（9軸・全シリーズ共通）
├── SERIES.md             ← シリーズ台帳（folder / 形式 / 尺 / 命名）
├── scripts/hall-eval.py  ← 評価器（一次スクリーニング）
└── README.md
```

## フロー

```
seed/（査読前・種）
   │ 台本化 → PR を出す（**全文を PR 本文に貼り付ける**）
   ▼
査読（人間 / エージェントが PR でレビュー）
   │ merge
   ▼
<series>/#NN-….md（完成品として登録）
```

- シリーズは [`SERIES.md`](SERIES.md) の台帳で管理（`知恵の館/` `SFショートショート/` `SF落語/` …）。
- 査読前はすべて `seed/` に集約する（直下には置かない）。
- 査読は **PR** で行う。PR 本文に **台本の全文**を貼り、ファイルを開かずに読めるようにする。
- **merge = 完成フォルダ `<series>/` への登録**（PR の差分は `<series>/#NN-….md` を追加する形にする）。
- 評価は共通の [`RUBRIC.md`](RUBRIC.md) の 9 軸＋`scripts/hall-eval.py`。不合格は `seed/` に残す（捨てない）。

## 知恵の館 — House of Wisdom

SF・人工知能・哲学・思想・構想を、テキストから朗読動画にして届けるシリーズ。

| # | タイトル |
|---|---|
| #01 | エントロピーを閉じる — シャノン、LLM、Jev |
| #02 | ぜんぶは読めない。では、何を読むか — ボルヘス、図書館、LLM |
| #03 | ヌルの庭で待つ — 仏教と落合陽一と量子の徒然 |

- プレイリスト: https://www.youtube.com/playlist?list=PLIZsapbAHEaE
- 査読前（種）: `seed/`（索引 `seed/INDEX.md`）
- 完成品: `知恵の館/#NN-….md`
- 評価: `知恵の館/RUBRIC.md` / `scripts/hall-eval.py`
