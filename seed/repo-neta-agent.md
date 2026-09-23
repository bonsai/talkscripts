# Repo Neta Agent — すべてのrepoからネタを拾う

type: seed
tags: [agent, repo, neta, seed, ontology, discovery, talkscripts]

## 概要

bonsai配下のすべてのrepoを横断して、既存資産から「次に作品化できるネタ」を拾うエージェント。

目的は要約ではない。

**repoに眠っている未発見の接続・違和感・失敗・概念・技術・Issue・README・研究メモを、作品の種として発見する。**

## 入力

- repository
- README
- Issue / PR
- commit
- docs
- seed
- SKILL
- workflow
- 設定ファイル
- repo間の同名概念
- repo間の矛盾
- 最近追加されたもの
- 放置されたもの

## 記号的オントロジ

ネタを文章としてだけでなく、記号として抽出する。

- ENTITY: 人、repo、agent、tool、作品、概念
- ACTION: 作る、壊す、読む、選ぶ、判定する、生成する
- STATE: 未完成、失敗、採用、保留、放置
- RELATION: depends-on、contradicts、resembles、extends、duplicates
- TENSION: 便利/不便、生成/判定、記号/意味、保存/忘却
- QUESTION: なぜ、何が足りない、何を逆転できるか
- SEED: 作品化可能な最小単位

## ネタ抽出

各repoについて、

1. 「何を作っているか」
2. 「何に困っているか」
3. 「何を発明しているか」
4. 「別repoと何が似ているか」
5. 「別repoと何が矛盾するか」
6. 「まだ名前のない概念は何か」
7. 「これを物語・対話・論考にしたら何になるか」

を抽出する。

## 出力

1件のネタを次の形にする。

- title
- source_repos
- entities
- relations
- tension
- question
- seed
- possible_forms: [essay, dialogue, shortstory, podcast, video]
- evidence_paths
- novelty_reason

## 重要な原則

**面白いrepoを探すのではなく、repo同士をぶつけて面白さを作る。**

単独repoの要約より、

repo A × repo B

の「意外な関係」を優先する。

特に、

- 同じ言葉を違う意味で使っている
- 別々のrepoが同じ問題を解いている
- 一方のrepoが他方の前提を壊している
- 技術repoと思想repoが接続できる
- 失敗した実装が別repoのseedになる

を高く見る。

## talkscriptsとの接続

抽出されたSEEDは、そのまま完成原稿にしない。

**repo → observation → ontology → tension → seed → script**

という変換を行う。

現在のtalkscriptsでは、単独読み上げを基本とし、将来的にはspeaker / roleによる読み分けへ拡張する。

そのためSEED段階では、作品本文だけでなく、

- speaker
- role
- concept
- relation
- question

を記号として保持できる設計にする。

## 最初の実験

bonsai配下のrepo群から10件程度を選び、

- 3件以上のrepoを横断するネタ
- 1つのrepoだけでは発見できないネタ
- 既存seedと重複しないネタ

を優先して10 seed生成する。

評価は「正しい要約」ではなく、

**意外性 × 接続数 × 作品化可能性 × 根拠の追跡可能性**

で行う。
