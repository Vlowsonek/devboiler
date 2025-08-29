# devboiler

Fast boilerplate generator for applications, web pages, and components. Use it as a Python library and a CLI.

## Installation

```bash
pip install devboiler
```

## CLI usage

List all available boilerplates:

```bash
devboiler list
```

Quick examples:

```bash
# Python class
devboiler create python-class User

# HTML page
devboiler create html index --title "My Homepage"

# React component (function or class)
devboiler create react-component Navbar --type function

# Python project skeleton
devboiler create project my_app --type python

# Flask app (app.py)
devboiler create flask-app my_flask

# FastAPI app (main.py)
devboiler create fastapi-app my_api

# Node.js script (index.js)
devboiler create node-script my_script

# Express.js app (server.js)
devboiler create express-app my_express

# Python CLI (argparse)
devboiler create python-cli my_cli

# React component with CSS module
devboiler create react-component-css Navbar
```

Interactive wizard:

```bash
# Fully interactive (prompts for framework, docker, tests, linters)
devboiler new

# Non-interactive with flags
devboiler new my_app --framework fastapi --db none --docker --tests --linters
```

Get help with examples:

```bash
devboiler --help
```

## Python API

```python
from devboiler import (
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

create_python_class("User")
create_html_page("index", title="My Homepage")
create_react_component("Navbar", type="function")
create_project("my_app", type="python")

# High-level scaffold
scaffold_project(
    name="my_service",
    framework="fastapi",
    db="none",
    include_docker=True,
    include_tests=True,
    include_linters=True,
)
```

## Extending
Templates live under `devboiler/templates`. Add or customize them to fit your needs.

## License
MIT
