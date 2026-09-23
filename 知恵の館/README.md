# 知恵の館 — House of Wisdom

SF・人工知能・哲学・思想・構想を、**テキスト（エッセイ）から**朗読動画にして届けるシリーズ。
本リポジトリはシリーズの**テキスト（台本）と索引**の集約場所。

- プレイリスト: https://www.youtube.com/playlist?list=PLIZsapbAHEaE
- チャンネル: おしゃれれび
- ナレーション: **VOICEVOX:あんこもん**（さくらの AI Engine / `voicebox-selector-skill`）
- サムネ: `thumbnail-skill`（CF flux + PIL）

## 置き場

| 種別 | 場所 |
|---|---|
| 台本（集約） | `video/知恵の館/texts/`（本ディレクトリ） |
| 索引 | `video/知恵の館/texts/INDEX.md` |
| 生成物（mp3/mp4/サムネ/原画） | `video/YYYY/MM/`（例: `video/2026/09/`） |
| 元エッセイ | `knowledge/raw/untracked/YYYY/MM/` |

## パイプライン（テキスト → 動画）

```
essay.md
  ├─ voicebox.py render --voice ankomon   → MM-<slug>-ankomon.mp3
  ├─ thumb.py gen                          → MM-<slug>-ankomon-thumb.png (+ -art.png)
  ├─ ffmpeg -loop 1 -i thumb.png -i mp3 …   → MM-<slug>-ankomon.mp4   # サムネ＝本編の静止画
  └─ yt-upload/upload.py --thumbnail …      → YouTube（public）
```

## 共通タグ

`知恵の館, House of Wisdom, 高学歴, SF, 人工知能, 哲学, 思想, 構想`
