import os

REMOVE_PATHS = [
{%- if cookiecutter.support_cli != true %}
    'src/{{ cookiecutter.package_name }}/cli.py',
    'tests/{{ cookiecutter.package_name }}/test_cli.py',
{% endif -%}
{%- if "Not open source" == cookiecutter.open_source_license %}
    'LICENSE',
{% endif -%}
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)
