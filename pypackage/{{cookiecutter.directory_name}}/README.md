{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Usage
### Installation
* From source code: `make install`
{% if cookiecutter.support_pypi_upload == true -%}
* From PyPI: `pip install {{ cookiecutter.package_name }}`
{% endif %}

## Development
Install dependencies:
```shell
make deps
```

Run tests:
```shell
make test
```

Other scripts:
```shell
make help
```

## Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
{%- if cookiecutter.__template_url is defined %} and the `pypackage` project template of 
[cookiecutter-templates]({{ cookiecutter.__template_url }}){% endif %}.

