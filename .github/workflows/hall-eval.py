#!/usr/bin/env python3
"""hall-eval — 知恵の館 評価軸エバリュエータ（RUBRIC v2）

完成品（知恵の館/#0*.md）を基準に**密度ベースで自動校正**し、9軸で採点する。
短く抑制した佳品（#02 型）を過小評価しないよう、頻度は「1000字あたり密度」で見る。

使い方:
  hall-eval <file.md> [...]          # 採点
  hall-eval --dir seed               # ディレクトリ内を採点（降順）
  hall-eval --axis <file.md>         # 軸ごとの内訳
"""
from __future__ import annotations
import glob, os, re, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
HALL = os.path.normpath(os.path.join(HERE, "..", "..", "知恵の館"))

THEME = ["LLM","AI","人工知能","知能","情報","計算","モデル","データ","プログラム","Jev",
         "哲学","思想","仏教","龍樹","SF","文学","小説","言語","記号","読む","本","図書館",
         "人生","無限","選択","記憶","言葉","知恵","構想"]
PROPER = ["シャノン","ボルヘス","ナーガールジュナ","龍樹","落合陽一","チューリング",
          "ウィトゲンシュタイン","ゲーデル","フォン・ノイマン","Jevons","ジュヴォンズ",
          "ソシュール","パース","エラトステネス","バベルの図書館","フッサール",
          "太宰治","太宰","人間失格","AI失格",
          "川端康成","雪国","駒子","国境のトンネル",
          "人工無脳","イライザ","オウム返し","イライザの子孫"]
VOICE = ["私は","私たち","だろう","のだ","と思う","思う","かもしれない","でよい","では",
         "見える","気がする","正直","ひそかに","けさ"]
INSIGHT = ["逆説","パラドックス","ではなく","むしろ","言い換えれば","実は","だが","しかし",
           "皮肉","反転","そもそも","なぜなら","つまり","決まっている"]
MOTIF = ["エントロピー","冗長","不確実","ヌル","館","知恵","計算","情報","記号","確率","決定","埋め込み"]

WEIGHTS = dict(theme=1.3, conn=1.2, voice=1.0, insight=1.4, struct=1.0,
               close=1.2, oral=1.1, title=0.6, motif=1.0)


def _text(path):
    return open(path, encoding="utf-8", errors="replace").read()


def _body(t):
    return "\n".join(l for l in t.splitlines() if l.strip() and not l.startswith("#"))


def _density(count, L):
    return count / (L / 1000.0) if L else 0.0


def _tail(t):
    lines = [l for l in t.splitlines() if l.strip() and not re.match(
        r"^(type|tags|related|duration|notes|created|source|episode|confidence|narration|#|---)", l)]
    return lines[-1] if lines else ""


def refs():
    """完成品から基準密度を求める（自動校正）。"""
    ref = {k: [] for k in ("theme","conn","voice","insight","motif")}
    for f in glob.glob(os.path.join(HALL, "#0*.md")):
        t = _text(f); L = len([c for c in _body(t) if not c.isspace()])
        ref["theme"].append(_density(sum(t.count(k) for k in THEME), L))
        ref["conn"].append(_density(sum(t.count(p) for p in PROPER), L))
        ref["voice"].append(_density(sum(t.count(k) for k in VOICE), L))
        ref["insight"].append(_density(sum(t.count(k) for k in INSIGHT), L))
        ref["motif"].append(_density(sum(t.count(m) for m in MOTIF), L))
    return {k: (statistics.median(v) or 1.0) for k, v in ref.items()}


def evaluate(path, REF):
    t = _text(path); L = len([c for c in _body(t) if not c.isspace()])
    lines = t.splitlines()
    title = next((l for l in lines if l.startswith("# ")), "")
    def dens(count):  # 完成品中央値 → 4.0
        return min(5.0, 4.0 * _density(count, L) / REF_KEY)
    # 密度ベース軸
    a = {}
    for key, words in (("theme",THEME),("conn",PROPER),("voice",VOICE),("insight",INSIGHT),("motif",MOTIF)):
        REF_KEY = REF[key]
        a[key] = round(dens(sum(t.count(w) for w in words)), 2)
    # 構造
    secs = len([l for l in lines if l.startswith("## ") or re.match(r"^\s*\d+\.\s", l) or re.match(r"^(第[一二三四五六七八九十]+[信章手記]|はしがき|序|結び)", l)])
    paras = len([p for p in re.split(r"\n\s*\n|^---$", t, flags=re.M) if len(p.strip()) > 60])
    a["struct"] = round(min(5.0, secs + min(3, paras / 5)), 2)
    # 締めの余韻
    tail = _tail(t)
    a["close"] = 5.0 if (0 < len(tail) <= 70 and tail.endswith(("。","」","だ","る","た","い"))) else 3.0
    # 朗読適性
    paren = len(re.findall(r"[（(][^）)]*[）)]", t)); code = t.count("```")
    a["oral"] = 5.0
    if paren > 6: a["oral"] -= 2
    if code > 0: a["oral"] -= 2
    if not (900 <= L <= 4500): a["oral"] -= 1.5
    a["oral"] = round(max(0.0, a["oral"]), 2)
    # タイトル設計
    a["title"] = 5.0 if re.search(r"—.*[、,]", title) else (3.0 if "—" in title else 1.0)
    total = round(sum(a[k] * WEIGHTS[k] for k in WEIGHTS) / sum(WEIGHTS.values()) * 20, 1)
    return total, a, L, title.strip("# ").strip()



def check(path, REF):
    """台本チェック: 昇格前の自動検査（締めの余韻・朗読適性ほか）。"""
    sc, a, L, title = evaluate(path, REF)
    flags = []
    if a["title"] < 5: flags.append("タイトルが『命題 — 固有名』形式でない")
    if a["oral"] < 5: flags.append(f"朗読適性に難（括弧/コード/尺: {L}字）")
    if a["close"] < 5: flags.append("締めが短い一句になっていない")
    if a["struct"] < 2: flags.append("構造（節/段落）が薄い")
    for k, label in (("theme","テーマ適合"),("conn","概念連結"),("insight","独自視点")):
        if a[k] < 2.5: flags.append(f"{label}が弱い ({a[k]})")
    print(f"[{'OK ' if not flags else 'WARN'}] {sc:>5}  {title}")
    for f in flags: print("       -", f)
    return not flags


def main(argv):
    REF = refs()
    if not argv:
        print(__doc__); return 1
    mode = argv[0]
    if mode == "--dir":
        files = sorted(glob.glob(os.path.join(argv[1], "*.md")))
        files = [f for f in files if os.path.basename(f) != "INDEX.md"]
        rows = sorted(((evaluate(f, REF), f) for f in files), key=lambda x: x[0][0], reverse=True)
        for (sc, a, L, title), f in rows:
            print(f"{sc:>5}  {L:>5}字  {os.path.basename(f)[:44]:<44} {title[:30]}")
        return 0
    if mode == "--check":
        for f in argv[1:]:
            check(f, REF)
        return 0

    show_axis = mode == "--axis"
    files = argv[1:] if show_axis else argv
    for f in files:
        sc, a, L, title = evaluate(f, REF)
        print(f"{sc:>5}  {L:>5}字  {title}")
        if show_axis:
            for k in WEIGHTS:
                print(f"    {k:>8}: {a[k]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
