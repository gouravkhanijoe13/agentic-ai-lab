import glob, os, re, subprocess, html, urllib.parse

USER = "gouravkhanijoe13"; REPO = "agentic-ai-lab"; BRANCH = "main"
OUT = "_site"
os.makedirs(OUT, exist_ok=True)

def parse(fn):
    m = re.match(r'Lesson_(\d+)([a-z]?)_(.*)\.ipynb', fn)
    if not m:
        return (9999, '', fn[:-6].replace('_', ' '))
    return (int(m.group(1)), m.group(2), m.group(3).replace('_', ' '))

nbs = sorted(glob.glob("*.ipynb"), key=lambda f: (parse(f)[0], parse(f)[1]))
print(f"Converting {len(nbs)} notebooks to HTML...")
for fn in nbs:
    subprocess.run(["jupyter", "nbconvert", "--to", "html", "--output-dir", OUT, fn], check=True)

cards = []
for fn in nbs:
    num, suf, title = parse(fn)
    label = f"{num}{suf}" if num != 9999 else "•"
    base = os.path.splitext(os.path.basename(fn))[0] + ".html"
    href = urllib.parse.quote(base)
    colab = f"https://colab.research.google.com/github/{USER}/{REPO}/blob/{BRANCH}/{urllib.parse.quote(fn)}"
    t = html.escape(title)
    cards.append(
        '<li class="card" data-t="' + t.lower() + '">'
        '<span class="num">' + label + '</span>'
        '<a class="title" href="' + href + '">' + t + '</a>'
        '<a class="run" href="' + colab + '" target="_blank" rel="noopener">▶ Colab</a>'
        '</li>'
    )

CSS = """
:root{--bg:#0d1117;--card:#161b22;--border:#30363d;--text:#e6edf3;--muted:#9198a1;--accent:#2f81f7;--run:#f9ab00}
@media (prefers-color-scheme:light){:root{--bg:#fff;--card:#f6f8fa;--border:#d0d7de;--text:#1f2328;--muted:#59636e;--accent:#0969da;--run:#bf8700}}
*{box-sizing:border-box}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--text);line-height:1.5}
.wrap{max-width:780px;margin:0 auto;padding:22px 16px 64px}
h1{font-size:1.6rem;margin:.2em 0 .1em}
.sub{color:var(--muted);margin:0 0 14px}
.links a{color:var(--accent);text-decoration:none;margin-right:14px;font-size:.9rem}
.search{width:100%;padding:12px 14px;margin:16px 0;font-size:1rem;border:1px solid var(--border);border-radius:10px;background:var(--card);color:var(--text)}
ul{list-style:none;margin:0;padding:0}
.card{display:flex;align-items:center;gap:12px;padding:12px 14px;border:1px solid var(--border);border-radius:12px;margin-bottom:8px;background:var(--card)}
.num{flex:0 0 auto;min-width:34px;text-align:center;font-weight:700;font-size:.78rem;color:var(--muted);background:var(--bg);border:1px solid var(--border);border-radius:8px;padding:4px 6px}
.title{flex:1 1 auto;color:var(--text);text-decoration:none;font-weight:600}
.title:hover,.title:active{color:var(--accent)}
.run{flex:0 0 auto;color:var(--run);text-decoration:none;font-size:.82rem;font-weight:600;border:1px solid var(--border);border-radius:8px;padding:6px 10px;white-space:nowrap}
footer{color:var(--muted);font-size:.8rem;margin-top:24px;text-align:center}
"""

SCRIPT = """
const q=document.getElementById('q'),items=[...document.querySelectorAll('.card')];
q.addEventListener('input',()=>{const v=q.value.trim().toLowerCase();items.forEach(el=>{el.style.display=el.dataset.t.includes(v)?'':'none';});});
"""

head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>agentic-ai-lab — Lessons</title><style>' + CSS + '</style></head><body><div class="wrap">')
header = ('<h1>\U0001F9EA agentic-ai-lab</h1>'
          '<p class="sub">A hands-on journey into AI / LLM / agent engineering — ' + str(len(nbs)) +
          ' lessons. Tap a lesson to read · tap ▶ Colab to run.</p>'
          '<p class="links"><a href="https://github.com/' + USER + '/' + REPO + '">GitHub repo</a>'
          '<a href="https://github.com/' + USER + '/' + REPO + '/blob/' + BRANCH + '/CURRICULUM.md">Curriculum</a></p>'
          '<input class="search" id="q" placeholder="Search lessons… (e.g. RAG, agent, eval)" autocomplete="off">')
body = '<ul id="list">' + "".join(cards) + '</ul>'
foot = '<footer>Built from notebooks with nbconvert · GitHub Pages</footer></div><script>' + SCRIPT + '</script></body></html>'

with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(head + header + body + foot)
print("Wrote", os.path.join(OUT, "index.html"))
