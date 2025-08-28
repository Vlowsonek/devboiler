from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .api import (
    create_python_class,
    create_html_page,
    create_react_component,
    create_project,
)


def _add_common_create_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("name", help="Resource name (e.g., class, file base name, project)")
    parser.add_argument("--directory", "-d", default=".", help="Output directory (default: current)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="devboiler", description="Generate boilerplates quickly")
    sub = p.add_subparsers(dest="command", required=True)

    # create group
    p_create = sub.add_parser("create", help="Create a boilerplate resource")
    sub_create = p_create.add_subparsers(dest="create_type", required=True)

    # python-class
    p_pyclass = sub_create.add_parser("python-class", help="Create a Python class file")
    _add_common_create_args(p_pyclass)
    p_pyclass.add_argument("--filename", help="Optional output filename (defaults to <ClassName>.py)")

    # html
    p_html = sub_create.add_parser("html", help="Create an HTML page")
    _add_common_create_args(p_html)
    p_html.add_argument("--title", default="My Homepage", help="HTML <title> value")

    # react-component
    p_react = sub_create.add_parser("react-component", help="Create a React component")
    _add_common_create_args(p_react)
    p_react.add_argument("--type", choices=["function", "class"], default="function")
    p_react.add_argument("--ext", default="jsx", help="File extension (default: jsx)")

    # project
    p_proj = sub_create.add_parser("project", help="Create a project skeleton")
    _add_common_create_args(p_proj)
    p_proj.add_argument("--type", choices=["python"], default="python")

    return p


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)

    if args.command == "create":
        out_dir = Path(args.directory)
        out_dir.mkdir(parents=True, exist_ok=True)

        if args.create_type == "python-class":
            path = create_python_class(
                args.name,
                filename=args.filename,
                directory=out_dir,
                force=args.force,
            )
            print(str(path))
            return 0

        if args.create_type == "html":
            path = create_html_page(
                args.name,
                title=args.title,
                directory=out_dir,
                force=args.force,
            )
            print(str(path))
            return 0

        if args.create_type == "react-component":
            path = create_react_component(
                args.name,
                type=args.type,
                extension=args.ext,
                directory=out_dir,
                force=args.force,
            )
            print(str(path))
            return 0

        if args.create_type == "project":
            paths = create_project(
                args.name,
                type=args.type,
                directory=out_dir,
                force=args.force,
            )
            for p in paths:
                print(str(p))
            return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())


