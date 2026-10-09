"""Split design-system/showcase.html into Claude Design preview cards (previews/*.html)."""
import re, sys, pathlib
root = pathlib.Path(sys.argv[1])
src = (root / "showcase.html").read_text()
head = src[:src.index("<body>")]
script = src[src.index("<script>"):src.index("</script>") + 9]
sections = re.findall(r"<section>.*?</section>", src, re.S)
cards = [  # (file, group, title) in showcase order
    ("colors", "Colors", "Color tokens"),
    ("typography", "Type", "Typography"),
    ("buttons", "Components", "Buttons"),
    ("badges", "Components", "Badges"),
    ("stats", "Components", "Stat cards"),
    ("forms", "Forms", "Form controls"),
    ("alerts", "Components", "Alerts"),
    ("table", "Components", "Tabs, table, avatars"),
    ("overlays", "Components", "Dialog, menu, toast, tooltip"),
    ("radius-spacing", "Spacing", "Radius & spacing"),
]
assert len(sections) == len(cards), (len(sections), len(cards))
out = root / "previews"; out.mkdir(exist_ok=True)
for (name, group, title), sec in zip(cards, sections):
    body = sec.replace("<section>", '<section style="margin-top:0">', 1)
    html = (f'<!-- @dsCard group="{group}" -->\n'
            + head.replace("</head>","").replace("<title>Ember — shadcn design system</title>", f"<title>Ember — {title}</title>")
            + '<style>html{background:oklch(0.99 0.003 75)}html:has(.ember.dark){background:oklch(0.155 0.008 60)}.ember{border:0;border-radius:0}</style>\n'
            + '</head>\n' + f'<body>\n<div class="ember" id="ember">\n{body}\n</div>\n{script}\n</body>\n</html>\n')
    (out / f"{name}.html").write_text(html)
    print("wrote", out / f"{name}.html")
