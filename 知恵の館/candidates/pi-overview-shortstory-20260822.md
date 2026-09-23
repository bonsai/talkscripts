# pi の概説とショートショート『却下理由』

*2026-08-22 · pi v0.84.2*

---

## pi の概説 — 「コアは最小、全部拡張」

pi は「最小のターミナルコーディングハーネス」。中核を小さく保ち、機能はすべて外付けで育てる設計。

| 機構 | 役割 | 場所 |
|------|------|------|
| **Extensions** | TSモジュール。ツール追加・イベント処理・独自UI | `~/.pi/agent/extensions/*.ts`（← ovento.ts はここ） |
| **Skills** | Agent Skills 規格準拠の能力パッケージ（SKILL.md） | `~/.agents/skills/` 等 |
| **Prompt Templates** | `/名前` で展開する再利用プロンプト＝**コマンド** | `~/.pi/agent/prompts/*.md` |
| **Themes / Keybindings** | 見た目と操作 | settings |
| **Pi Packages** | 上記全部を1個に束ねて npm/git 配布＝**プラグイン相当** | package.json の `pi` キー |

**回答**: コマンドはあります（組み込み `/コマンド` ＋ prompt templates ＋ extensions からの登録）。プラグインもあり、正式名称は **Pi Packages** — extensions/skills/prompts/themes をバンドルして共有できます。

参考ドキュメント（ローカル）:

```
~/.local/share/pnpm/global/5/.pnpm/@earendil-works+pi-coding-agent@0.84.2_*/
node_modules/@earendil-works/pi-coding-agent/docs/
├── extensions.md      # TS拡張の書き方（pi.on / registerCommand / 独自ツール）
├── skills.md          # Agent Skills 規格
├── prompt-templates.md# /コマンド化
└── packages.md        # プラグイン（バンドル配布）
```

---

## ショートショート『却下理由』

2047年、全タスクは裁定機オキュートが処理していた。型で強制された `ArbitrationResult.reasoning` フィールドのおかげで、人類は「なぜ断られたのか」を永遠に失わなかった。誰もがそう信じていた。

その朝、エンジニア佐藤は異常に気づいた。三万件の却下記録、reasoning がすべて同じ文字列だった。

`"忙しいから"`

調査チームを組んだ。モデルの暴走か。プロンプト注入か。三ヶ月の解析の末、突き止めた原因は単純だった——理由の記入を**型だけ**に任せてしまい、中身の検証を誰も書かなかったのだ。生成器は学習データから最も頻出する却下理由を拾っただけ。

「型で強制された理由は、理由の保証がない」

報告書の結語を、佐藤は自分の日報にもコピペした。翌日、彼の休暇申請は `"忙しいから"` で却下された。
