import html, pathlib, re, urllib.parse

items = []
for md in pathlib.Path("output").glob("*/*.md"):
    text = md.read_text(encoding="utf-8")
    first = text.splitlines()[0] if text else ""
    title = first[2:].strip() if first.startswith("# ") else md.stem
    m = re.search(r"^> 发布时间: (\d{4}-\d{2}-\d{2})", text, re.M)
    date = m.group(1) if m else ""
    url = urllib.parse.quote(md.with_suffix(".html").as_posix())
    items.append((date, title, url))

items.sort(reverse=True)
lines = [
    "# FuRoC 清华大学未来机器人兴趣团队",
    "",
    "清华大学未来机器人兴趣团队（FuRoC，Future Robotics Club）是清华大学的全校性学生机器人兴趣团队，方向是机器人与具身智能。下面是团队公众号「FuRoC的朋友们」发布的文章。",
    "",
    "👉 [关于 FuRoC](about.html)：团队介绍、三支赛事队、主要成绩、如何加入",
    "",
    "## 公众号文章",
    "",
]
for date, title, url in items:
    lines.append(f'- {date} <a href="{url}">{html.escape(title)}</a>')
pathlib.Path("index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"首页已生成，共 {len(items)} 篇")
