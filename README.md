# cookiecutter-templates

All of my self-customized cookiecutter templates.

* [Usage](#usage)
* [Development](#development)

## Usage

The following shows how to install and use `cookiecutter` in CLI. If you want to use it from Python,
please refer to [the doc of cookiecutter](https://github.com/cookiecutter/cookiecutter?tab=readme-ov-file).
The logic is similar.

### Step 1: Install `cookiecutter` [Do it once]

1. Install [pipx](https://pipx.pypa.io/stable/).
2. Run `pipx install cookiecutter`. **Version >=1.7 is required.**

### Step 2: Create project based on the template

For `cookiecutter >= 2.5`, run the command and follow the prompts.

```shell
# Use a GitHub template
pipx run cookiecutter <git_url>
# Example: pipx run cookiecutter https://github.com/your_repo/cookiecutter-templates.git

# Use a local template
pipx run cookiecutter cookiecutter-templates/
```

For `cookiecutter >=1.7 and < 2.5`,

```shell
# Use a GitHub template
pipx run cookiecutter <git_url> --directory <template_name>
# Example: pipx run cookiecutter https://github.com/your_repo/cookiecutter-templates.git --directory pypackage

# Use a local template
pipx run cookiecutter cookiecutter-templates/ --directory <template_name>
```

, where `template_name` is the name of the subdirectory for each template.

If you want to set up some global variables, modify `cookiecutter_conf.yaml` and run the command like this:

```shell
pipx run cookiecutter  --config-file cookiecutter_conf.yaml <git_url>
```

## Development

For development, please check the `README.md` doc in each subdirectory for each template.