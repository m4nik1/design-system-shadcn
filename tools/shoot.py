import sys, pathlib
from playwright.sync_api import sync_playwright
ds = pathlib.Path(sys.argv[1]).resolve(); out = pathlib.Path(sys.argv[2]); out.mkdir(exist_ok=True)
errs = []
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 760, "height": 800})
    pg.on("console", lambda m: m.type == "error" and errs.append(m.text))
    pg.on("pageerror", lambda e: errs.append(str(e)))
    for q in ["", "?dark"]:
        pg.goto((ds / "showcase.html").as_uri() + q); pg.wait_for_timeout(1500)
        pg.screenshot(path=str(out / f"showcase{q.replace('?','-')}.png"), full_page=True)
    for f in sorted((ds / "previews").glob("*.html")):
        pg.goto(f.as_uri() + "?dark"); pg.wait_for_timeout(300)
    # interactions
    pg.goto((ds / "showcase.html").as_uri()); pg.wait_for_timeout(500)
    pg.click("text=Overdue"); n = pg.locator("#tbody tr").count()
    pg.click("#themeToggle"); dark = pg.evaluate("document.getElementById('ember').classList.contains('dark')")
    print("overdue rows:", n, "toggle->dark:", dark)
    b.close()
print("errors:", errs or "none")
