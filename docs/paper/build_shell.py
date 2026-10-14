"""把论文壳打成 PDF。不依赖 LaTeX。

用法（在仓库根目录）:
    python docs/paper/build_shell.py
输出:
    docs/paper/shell.pdf
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "shell.pdf"
PAGE = (1240, 1754)
MARGIN = 80

FONT_CANDIDATES = [
    Path("/System/Library/Fonts/STHeiti Medium.ttc"),
    Path("/System/Library/Fonts/Hiragino Sans GB.ttc"),
    Path("/System/Library/Fonts/Supplemental/Songti.ttc"),
    Path(r"C:\Windows\Fonts\simhei.ttf"),
    Path(r"C:\Windows\Fonts\msyh.ttc"),
]

BLOCKS = [
    ("title", "Untitled"),
    ("meta", "论文壳  cv-research-lab-02"),
    ("body", "Keywords: to be chosen"),
    ("head", "摘要 / Abstract"),
    ("body", "这一页只建壳。摘要以后写任务定义、对照结果、以及模型在哪里失效。本页不填任何实验数字。"),
    ("head", "1 引言 / Introduction"),
    ("body", "任务还没锁定。锁定后写输入、输出，以及明确不做的事。贡献主张见 docs/paper/contributions.md。"),
    ("head", "2 相关工作 / Related Work"),
    ("body", "待写。笔记放在 docs/notes/。别人论文里的数字不进主表。"),
    ("head", "3 方法 / Method"),
    ("body", "待 experiments/ 里写下任务定义后再写。"),
    ("head", "4 实验 / Experiments"),
    ("body", "还没有运行。主表的每一行以后要对上命令、种子、机器和 results/ 里的 CSV。"),
    ("head", "5 结论 / Conclusion"),
    ("body", "数字冻结后再写局限。局限重复任务锁定时点名的失败条件。"),
]


def find_font() -> Path:
    for path in FONT_CANDIDATES:
        if path.is_file():
            return path
    raise FileNotFoundError("没有找到中文字体。把 FONT_CANDIDATES 补成这台机器上的字体路径。")


def wrap(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        buf = ""
        for ch in paragraph:
            trial = buf + ch
            if draw.textlength(trial, font=font) <= width:
                buf = trial
            else:
                if buf:
                    lines.append(buf)
                buf = ch
        lines.append(buf)
    return lines


def main() -> None:
    font_path = find_font()
    fonts = {
        "title": ImageFont.truetype(str(font_path), 36),
        "meta": ImageFont.truetype(str(font_path), 24),
        "head": ImageFont.truetype(str(font_path), 28),
        "body": ImageFont.truetype(str(font_path), 22),
    }
    gaps = {"title": 18, "meta": 14, "head": 16, "body": 10}
    width, height = PAGE
    text_width = width - 2 * MARGIN
    pages: list[Image.Image] = []
    image = Image.new("RGB", PAGE, "white")
    draw = ImageDraw.Draw(image)
    y = MARGIN

    def new_page() -> None:
        nonlocal image, draw, y
        pages.append(image)
        image = Image.new("RGB", PAGE, "white")
        draw = ImageDraw.Draw(image)
        y = MARGIN

    for kind, text in BLOCKS:
        font = fonts[kind]
        gap = gaps[kind]
        if kind == "head":
            y += 12
        for line in wrap(draw, text, font, text_width):
            if y > height - MARGIN:
                new_page()
            draw.text((MARGIN, y), line, fill="black", font=font)
            y += font.size + gap
    pages.append(image)
    pages[0].save(
        OUT,
        "PDF",
        resolution=150.0,
        save_all=True,
        append_images=pages[1:],
    )
    print(OUT)


if __name__ == "__main__":
    main()
