"""另一个项目调用的入口。

用法（在仓库根目录）:
    python src/estimate.py --list-price 39.8 \\
        --front cover.jpg --back back.jpg --spine spine.jpg \\
        --image page.jpg

必拍是封面、封底、书脊和前、中、后三处内页，见 experiments/label_protocol.md 第 6 节。
模型还没训练，价格系数仍是起点，所以 grade、defects、estimated_price 现在保持为空。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="根据多张书影和原价，返回品相档与估价。")
    parser.add_argument("--list-price", type=float, default=None, help="这本书的原价。可以缺省。")
    parser.add_argument("--front", type=Path, help="封面")
    parser.add_argument("--back", type=Path, help="封底")
    parser.add_argument("--spine", type=Path, help="书脊")
    parser.add_argument("--image", type=Path, action="append", default=[], help="其他角度，可重复")
    return parser


def view_status(path: Path | None) -> dict:
    if path is None:
        return {"path": None, "ok": False, "problem": "未提供"}
    if not path.is_file():
        return {"path": str(path), "ok": False, "problem": "文件不存在"}
    if path.stat().st_size <= 0:
        return {"path": str(path), "ok": False, "problem": "文件是空的"}
    return {"path": str(path), "ok": True, "problem": None}


def main() -> None:
    args = build_parser().parse_args()
    if args.list_price is not None and args.list_price < 0:
        print("原价不能是负数。", file=sys.stderr)
        sys.exit(2)

    named = {
        "front": view_status(args.front),
        "back": view_status(args.back),
        "spine": view_status(args.spine),
    }
    extra = [view_status(path) for path in args.image]
    provided = [item for item in [*named.values(), *extra] if item["path"] is not None]
    if not provided:
        print("至少要有一张图。", file=sys.stderr)
        sys.exit(2)

    broken = [item for item in provided if not item["ok"]]
    result = {
        "status": "no_model" if not broken else "bad_input",
        "list_price": args.list_price,
        "views": named,
        "extra_views": extra,
        "grade": None,
        "grade_scheme": None,
        "defects": [],
        "estimated_price": None,
        "reason": (
            "照片或原价没有给全。"
            if broken or args.list_price is None
            else "品相模型还没训练，价格公式还没定。不把原价当成估价。"
        ),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if broken:
        sys.exit(2)


if __name__ == "__main__":
    main()
