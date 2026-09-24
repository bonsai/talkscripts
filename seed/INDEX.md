# seed — 原稿の種

`talkscripts/seed/` = 台本の種。ローカル (llm-wiki) は cp、gh repo は link。
スコアは **RUBRIC v2**（`.github/workflows/hall-eval.py`、完成品で自動校正）

## シリーズ

| folder | 尺 | 件数 |
|--------|------|------|
| 2027-series | 短め | 10 |
| jev | 短め | 2 |
| borges | 短め | 1 |
| shannon | 短め | 1 |
| embed-layer | 短め | 1 |
| nagarjuna | 短め | 1 |
| furui | 短め | 1 |
| sf-translation | 短め | 1 |
| package-managers | 短め | 1 |
| repo-neta | 短め | 1 |
| shortstory | 1〜3分 | 5 |
| conversation | 短め | 4 |

```
seed/
├── 2027-series/    ← 熟年プログラマの回想・Jade
├── shannon/        ← シャノン、エントロピー、情報理論
├── nagarjuna/      ← 仏教、ナーガルジュナ、量子、空
├── borges/         ← ボルヘス、バベルの図書館、読書
├── embed-layer/    ← embed-layer、エージェントとユーザー
├── jev/            ← Jev、決定エンジン、semgrep
├── furui/          ← エラトステネスの篩、素数
├── sf-translation/ ← SF 小説の翻訳語
├── package-managers/ ← winget, choco, scoop, APT
├── repo-neta/      ← リポジトリからネタを拾うエージェント
├── shortstory/     ← 掌編 SF
└── conversation/   ← 親子対話
```

## 2027-series — 熟年プログラマの回想

| score | chars | ファイル | タイトル |
|------:|------:|----------|----------|
| 65.2 | 1074 | `essay-essay.md` | 仕事の言葉、七つの器 — 2027 年、熟年プログラマの回想 |
| 54.7 | 1021 | `essay-tsonan_blade_essay.md` | データ形式の六つの季節 — 2027 年、熟年プログラマの回想 |
| 54.6 | 1031 | `essay-2027-test-tsonan-blade-essay.md` | データ形式の六つの季節 — 2027 年、熟年プログラマの回想 |
| 51.4 | 478 | `essay-essay_1_jp.md` | Jade can Envision: 結晶化する意志と、動的 |
| 45.9 | 1280 | `essay-mistake.md` | 間違いの値打ち — 熟年プログラマの回想 |
| 31.5 | 398 | `essay-essay_2_ch.md` | 确定论的终结与流体计算的黎明 |
| 30.0 | 422 | `essay-essay_1_ch.md` | Jade 的愿景：结晶化的意志与动态秩序的地平线 |
| 30.0 | 902 | `essay-essay_2_en.md` | The End of Determinism and the |
| 28.5 | 839 | `essay-essay_1_en.md` | Jade can Envision: Crystallize |

## shannon — シャノン、エントロピー

| score | chars | ファイル | タイトル |
|------:|------:|----------|----------|
| 77.3 | 4009 | `09-entropy-shannon-llm-jev-essay-20260924.md` | エントロピーを閉じる — シャノン、LLM、Jev |

## nagarjuna — 仏教、ナーガルジュナ、量子

| score | chars | ファイル | タイトル |
|------:|------:|----------|----------|
| 65.6 | 2659 | `09-null-nagarjuna-ochiai-essay-20260924.md` | ヌルの庭で待つ — 仏教と落合陽一と量子の徒然 |

## borges — ボルヘス、バベルの図書館

| score | chars | ファイル | タイトル |
|------:|------:|----------|----------|
| 86.8 | 966 | `09-borges-library-llm-reading-essay-20260924.md` | ぜんぶは読めない。では、何を読むか — ボルヘス、図書館、L |

## embed-layer — embed-layer

| score | chars | ファイル | タイトル |
|------:|------:|----------|----------|
| 65.7 | 1219 | `09-embed-layer-essay-20260924.md` | 貯める世界から、結ぶ世界へ — embed-layer の前と後 |

## jev — Jev、決定エンジン

| score | chars | ファイル | タイトル |
|------:|------:|----------|----------|
| 79.9 | 3355 | `09-jev-redundancy-uncertainty-essay-20260924.md` | 冗長さを捨て、不確実性を数字にする — Jev 論 |
| 61.1 | 2389 | `jev-semgrep-essay.md` | 意味で grep する — Jev semgrep を解剖す |

## furui — エラトステネスの篩、素数

| score | chars | ファイル | タイトル |
|------:|------:|----------|----------|
| 79.7 | 1819 | `furui-essay.md` | 篩は言葉を振るう — エラトステネスから furui へ |

## sf-translation — SF 小説の翻訳語

| score | chars | ファイル | タイトル |
|------:|------:|----------|----------|
| 69.9 | 1636 | `sf_translation_essay.md` | SF 小説の醍醐味は翻訳語の大胆さにあった |

## package-managers — パッケージマネージャ

| score | chars | ファイル | タイトル |
|------:|------:|----------|----------|
| 38.2 | 2337 | `package_manager_essay.md` | winget / choco / scoop / APT |

## repo-neta — 全リポジトリからネタを拾う

| ファイル | タイトル |
|----------|----------|
| `repo-neta-agent.md` | Repo Neta Agent |

## shortstory — 掌編 SF

| ファイル | タイトル |
|----------|----------|
| `pi-overview-shortstory-20260822.md` | pi overview short story |
| `shortstory-alignment-20260825.md` | alignment short story |
| `shortstory-green-20260825.md` | green short story |
| `shortstory-itsumo-no-asa-20260825.md` | いつものおはよう |
| `shortstory-matsu-hitotachi-20260825.md` | 待つ人々 |

## conversation — 親子対話

| ファイル | タイトル |
|----------|----------|
| `親子対話_CRXインストール失敗談_20260919.md` | CRX インストール失敗談 |
| `親子対話_CRXインストール戦記_話2_UIP_20260919.md` | CRX インストール戦記 話 2：UIP |
| `親子対話_CRXインストール戦記_話3_永続化_20260920.md` | CRX インストール戦記 話 3：永続化 |
| `親子対話_八岐の大蛇_Pythonで書くべきか_20260920.md` | 八岐の大蛇：Python で書くべきか |

## リモート seed（link, gh repo 由来）

- [bonsai/idol-lab :: theory/idol-folklore-essay.html](https://github.com/bonsai/idol-lab/blob/HEAD/theory/idol-folklore-essay.html)
- [bonsai/hermes-skills :: creative/creative-essay-philosophy/SKILL.md](https://github.com/bonsai/hermes-skills/blob/HEAD/creative/creative-essay-philosophy/SKILL.md)
- [bonsai/pi-skills :: skills/mouse-survival-essay/SKILL.md](https://github.com/bonsai/pi-skills/blob/HEAD/skills/mouse-survival-essay/SKILL.md)
- [bonsai/mushochika :: INDEX.md](https://github.com/bonsai/mushochika/blob/HEAD/INDEX.md)
- [bonsai/ants-essay :: README.md](https://github.com/bonsai/ants-essay/blob/HEAD/README.md)
- [bonsai/idol-lab :: README.md](https://github.com/bonsai/idol-lab/blob/HEAD/README.md)
- [bonsai/pi-skills :: README.md](https://github.com/bonsai/pi-skills/blob/HEAD/README.md)
- [bonsai/mushochika :: identity.md](https://github.com/bonsai/mushochika/blob/HEAD/identity.md)
- [bonsai/pi-skills :: HANDOVER.md](https://github.com/bonsai/pi-skills/blob/HEAD/HANDOVER.md)
- [bonsai/pi-skills :: ISSUE_LOG.md](https://github.com/bonsai/pi-skills/blob/HEAD/ISSUE_LOG.md)
- [bonsai/mushochika :: virtues-7.md](https://github.com/bonsai/mushochika/blob/HEAD/virtues-7.md)
- [bonsai/world-ontology :: atlas/atlas.js](https://github.com/bonsai/world-ontology/blob/HEAD/atlas/atlas.js)
- [bonsai/ants-essay :: context_index.md](https://github.com/bonsai/ants-essay/blob/HEAD/context_index.md)
- [bonsai/mensetsukan :: mensetsukan.md](https://github.com/bonsai/mensetsukan/blob/HEAD/mensetsukan.md)
- [bonsai/larry :: larry.md](https://github.com/bonsai/larry/blob/HEAD/larry.md)
- [bonsai/WX :: agents/writer.md](https://github.com/bonsai/WX/blob/HEAD/agents/writer.md)
- [bonsai/talkscripts :: 知恵の館/README.md](https://github.com/bonsai/talkscripts/blob/HEAD/知恵の館/README.md)
- [bonsai/world-ontology :: atlas/atlas.css](https://github.com/bonsai/world-ontology/blob/HEAD/atlas/atlas.css)
- [bonsai/wiki :: journal/docs/wiki-schema.md](https://github.com/bonsai/wiki/blob/HEAD/journal/docs/wiki-schema.md)
- [bonsai/workflow :: scans/wf_repos_new.txt](https://github.com/bonsai/workflow/blob/HEAD/scans/wf_repos_new.txt)
- [bonsai/idol-lab :: theory/研究計画.md](https://github.com/bonsai/idol-lab/blob/HEAD/theory/研究計画.md)
- [bonsai/wiki :: raw/06/2026-06-25-wiki-building.md](https://github.com/bonsai/wiki/blob/HEAD/raw/06/2026-06-25-wiki-building.md)
- [bonsai/cho-han :: docs/index.html](https://github.com/bonsai/cho-han/blob/HEAD/docs/index.html)
- [bonsai/CL4R1T4S :: META/Llama4_WhatsApp.txt](https://github.com/bonsai/CL4R1T4S/blob/HEAD/META/Llama4_WhatsApp.txt)
- [bonsai/YonerAI :: docs/SYSTEM_ARCHITECTURE.md](https://github.com/bonsai/YonerAI/blob/HEAD/docs/SYSTEM_ARCHITECTURE.md)
- [bonsai/oppo-research :: books.md](https://github.com/bonsai/oppo-research/blob/HEAD/books.md)
- [bonsai/ants-essay :: gleam-visual/index.html](https://github.com/bonsai/ants-essay/blob/HEAD/gleam-visual/index.html)
- [bonsai/idol-lab :: theory/不揃いのアイドル.md](https://github.com/bonsai/idol-lab/blob/HEAD/theory/不揃いのアイドル.md)
- [bonsai/idol-portal :: index.html](https://github.com/bonsai/idol-portal/blob/HEAD/index.html)
- [bonsai/wiki :: REORGANIZE.md](https://github.com/bonsai/wiki/blob/HEAD/REORGANIZE.md)