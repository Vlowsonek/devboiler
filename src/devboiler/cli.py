from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Optional

from .api import (
    create_python_class,
    create_html_page,
    create_react_component,
    create_project,
    create_flask_app,
    create_fastapi_app,
    create_node_script,
    create_express_app,
    create_python_cli,
    create_react_component_with_css,
    scaffold_project,
)


def _add_common_create_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("name", help="Resource name (e.g., class, file base name, project)")
    parser.add_argument("--directory", "-d", default=".", help="Output directory (default: current)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")


AVAILABLE_BOILERPLATES = [
    ("python-class", "Python class file", "devboiler create python-class User"),
    ("html", "HTML page", "devboiler create html index --title 'My Homepage'"),
    ("react-component", "React component (function/class)", "devboiler create react-component Navbar --type function"),
    ("project", "Project skeleton (python)", "devboiler create project my_app --type python"),
    ("flask-app", "Flask app (app.py)", "devboiler create flask-app my_flask --directory ."),
    ("fastapi-app", "FastAPI app (main.py)", "devboiler create fastapi-app my_api --directory ."),
    ("node-script", "Node.js script (index.js)", "devboiler create node-script my_script --directory ."),
    ("express-app", "Express.js app (server.js)", "devboiler create express-app my_express --directory ."),
    ("python-cli", "Python CLI with argparse", "devboiler create python-cli my_cli --directory ."),
    ("react-component-css", "React component + CSS module", "devboiler create react-component-css Navbar --directory ."),
]


def _build_epilog() -> str:
    lines = [
        "Examples:",
        "  devboiler create python-class User",
        "  devboiler create html index --title 'My Homepage'",
        "  devboiler create react-component Navbar --type function",
        "  devboiler create project my_app --type python",
        "  devboiler create flask-app my_flask",
        "  devboiler create fastapi-app my_api",
        "  devboiler create node-script my_script",
        "  devboiler create express-app my_express",
        "  devboiler create python-cli my_cli",
        "  devboiler create react-component-css Navbar",
        "",
        "See 'devboiler list' for all boilerplates.",
    ]
    return "\n".join(lines)


def _parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="devboiler",
        description="Generate boilerplates quickly",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=_build_epilog(),
    )
    sub = p.add_subparsers(dest="command", required=True)

    # new (wizard) group
    p_new = sub.add_parser("new", help="Interactive project wizard")
    p_new.add_argument("name", nargs="?", help="Project name")
    p_new.add_argument("--framework", choices=["fastapi", "flask", "express", "python"], help="Framework preset")
    p_new.add_argument("--db", choices=["none", "postgres"], default="none", help="Database selection (default: none)")
    p_new.add_argument("--docker", action="store_true", help="Include Dockerfile and docker-compose")
    p_new.add_argument("--tests", action="store_true", help="Include basic tests (pytest)")
    p_new.add_argument("--linters", action="store_true", help="Include basic linter configs (.flake8)")
    p_new.add_argument("--ci", action="store_true", help="Include GitHub Actions CI workflow")
    p_new.add_argument("--pre-commit", dest="pre_commit", action="store_true", help="Include .pre-commit-config.yaml")
    p_new.add_argument("--package-manager", choices=["pip", "poetry"], default="pip", help="Python package manager")
    p_new.add_argument("--directory", "-d", default=".", help="Output directory (default: current)")
    p_new.add_argument("--force", action="store_true", help="Overwrite existing files")
    p_new.add_argument("--non-interactive", action="store_true", help="Do not prompt; require options via flags")

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

    # flask-app
    p_flask = sub_create.add_parser("flask-app", help="Create a minimal Flask app (app.py)")
    _add_common_create_args(p_flask)
    p_flask.add_argument("--filename", default="app.py", help="Output filename (default: app.py)")

    # fastapi-app
    p_fastapi = sub_create.add_parser("fastapi-app", help="Create a minimal FastAPI app (main.py)")
    _add_common_create_args(p_fastapi)
    p_fastapi.add_argument("--filename", default="main.py", help="Output filename (default: main.py)")

    # node-script
    p_node = sub_create.add_parser("node-script", help="Create a Node.js script (index.js)")
    _add_common_create_args(p_node)
    p_node.add_argument("--filename", default="index.js", help="Output filename (default: index.js)")

    # express-app
    p_express = sub_create.add_parser("express-app", help="Create an Express.js app (server.js)")
    _add_common_create_args(p_express)
    p_express.add_argument("--filename", default="server.js", help="Output filename (default: server.js)")

    # python-cli
    p_pycli = sub_create.add_parser("python-cli", help="Create a Python CLI app (argparse)")
    _add_common_create_args(p_pycli)
    p_pycli.add_argument("--filename", default="cli.py", help="Output filename (default: cli.py)")

    # react-component-css
    p_rcc = sub_create.add_parser("react-component-css", help="Create React component with CSS module")
    _add_common_create_args(p_rcc)
    p_rcc.add_argument("--ext", default="jsx", help="Component file extension (default: jsx)")

    # list command
    p_list = sub.add_parser("list", help="List available boilerplates")

    return p


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)

    if args.command == "new":
        def _prompt(text: str, default: Optional[str] = None) -> str:
            if args.non_interactive:
                if default is None:
                    raise SystemExit(f"Missing required option: {text}")
                return default
            prompt_text = f"{text}"
            if default:
                prompt_text += f" [{default}]"
            prompt_text += ": "
            value = input(prompt_text).strip()
            return value or (default or "")

        def _prompt_choice(text: str, choices: list[str], default: Optional[str] = None) -> str:
            if args.non_interactive and getattr(args, text, None) is None and default is None:
                raise SystemExit(f"Missing required option: --{text}")
            if getattr(args, text, None):
                return getattr(args, text)
            if args.non_interactive:
                return default or choices[0]
            choices_str = "/".join(choices)
            while True:
                value = _prompt(f"{text} ({choices_str})", default)
                if value in choices:
                    return value
                print(f"Please choose one of: {choices_str}")

        def _prompt_bool(text: str, default: bool = False) -> bool:
            if args.non_interactive:
                return getattr(args, text.replace(" ", "_"), default)
            suffix = "Y/n" if default else "y/N"
            value = _prompt(f"{text}? ({suffix})", "y" if default else "n").lower()
            return value.startswith("y")

        project_name = args.name or _prompt("Project name")
        if not project_name:
            print("Project name is required")
            return 1

        framework = args.framework or _prompt_choice("framework", ["fastapi", "flask", "express", "python"], "fastapi")
        db = args.db or _prompt_choice("db", ["none", "postgres"], "none")
        include_docker = args.docker or _prompt_bool("Include Docker", True)
        include_tests = args.tests or _prompt_bool("Include tests (pytest)", True)
        include_linters = args.linters or _prompt_bool("Include linters (.flake8)", True)
        include_ci = args.ci or _prompt_bool("Include CI (GitHub Actions)", True)
        include_pre_commit = args.pre_commit or _prompt_bool("Include pre-commit", True)
        package_manager = args.package_manager or _prompt_choice("package_manager", ["pip", "poetry"], "pip")

        created_paths = scaffold_project(
            name=project_name,
            framework=framework,
            db=db,
            include_docker=include_docker,
            include_tests=include_tests,
            include_linters=include_linters,
            directory=Path(args.directory),
            force=args.force,
            include_ci=include_ci,
            include_pre_commit=include_pre_commit,
            package_manager=package_manager,
        )
        for pth in created_paths:
            print(str(pth))
        return 0

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

        if args.create_type == "flask-app":
            path = create_flask_app(
                args.name,
                filename=args.filename,
                directory=out_dir,
                force=args.force,
            )
            print(str(path))
            return 0

        if args.create_type == "fastapi-app":
            path = create_fastapi_app(
                args.name,
                filename=args.filename,
                directory=out_dir,
                force=args.force,
            )
            print(str(path))
            return 0

        if args.create_type == "node-script":
            path = create_node_script(
                args.name,
                filename=args.filename,
                directory=out_dir,
                force=args.force,
            )
            print(str(path))
            return 0

        if args.create_type == "express-app":
            path = create_express_app(
                args.name,
                filename=args.filename,
                directory=out_dir,
                force=args.force,
            )
            print(str(path))
            return 0

        if args.create_type == "python-cli":
            path = create_python_cli(
                args.name,
                filename=args.filename,
                directory=out_dir,
                force=args.force,
            )
            print(str(path))
            return 0

        if args.create_type == "react-component-css":
            paths = create_react_component_with_css(
                args.name,
                extension=args.ext,
                directory=out_dir,
                force=args.force,
            )
            for p in paths:
                print(str(p))
            return 0

    if args.command == "list":
        for key, desc, example in AVAILABLE_BOILERPLATES:
            print(f"{key:20} - {desc}")
        print("\nExamples:")
        for _, __, example in AVAILABLE_BOILERPLATES:
            print(f"  {example}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())


