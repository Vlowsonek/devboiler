# devboiler

Szybki generator boilerplatów (szablonów startowych) dla programów, stron internetowych i komponentów. Dostępny jako biblioteka Pythonowa oraz CLI.

## Instalacja

```bash
pip install devboiler
```

## Użycie (CLI)

```bash
# stworzenie pustej klasy Python
devboiler create python-class User

# stworzenie pliku HTML z boilerplatem
devboiler create html index --title "My Homepage"

# stworzenie React komponentu
devboiler create react-component Navbar --type function

# stworzenie struktury projektu w Pythonie
devboiler create project my_app --type python
```

## Użycie (Python API)

```python
from devboiler import create_python_class, create_html_page

create_python_class("User")
create_html_page("index", title="My Homepage")
```

## Rozszerzanie
Szablony znajdują się w `devboiler/templates`. Możesz dodać własne lub zmodyfikować istniejące.

## Licencja
MIT
