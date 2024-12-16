# Prompts

When you create a package, you are prompted to enter these values.

## Templated Values

The following appear in various parts of your generated project.

* `project_name`: Your human-readable project name. Can have uppercase and spaces.
* `directory_name`: The name of the project directory in your local path. Should be a valid directory name on your OS.
* `package_name`: The name of you python package. Lowercase only. Spaces and `-` should be converted into `_`.
* `full_name`: The human-readable full name of the author.
* `email`: Your email address.
* `project_short_description`: A 1-sentence description of what your Python package does.
* `initial_version`: The starting version number of the package.
* `open_source_license`: Choose a license. Options:
    1. MIT License
    1. BSD license
    2. ISC license
    3. Apache Software License 2.0
    4. GNU General Public License v3
    5. Not open source
* `source_url`: the URL to find the source code.

## Options

The following package configuration options set up different features for your project.

* `support_cli`: whether to support CLI commands (via [click](https://github.com/pallets/click/)).
* `cmd_name`: If `support_cli` is true, this is the command name. The Python package can be run as `<cmd_name> -h` in
  CLI. Otherwise it's ineffective.
* `build_wheel`: whether to build wheel (`.whl` file) when packaging the code.
* `support_pypi_upload`: whether to support uploading the package to PyPI.
* `pypi_username`: If `support_pypi_upload` is true, this is the PyPi username to use.
* `use_pytest`: whether to use Pytest.
