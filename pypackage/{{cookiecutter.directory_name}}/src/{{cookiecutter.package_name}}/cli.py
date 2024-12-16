"""Run the {{ cookiecutter.project_name }}.

This script defines the CLI of {{ cookiecutter.project_name }}.

Check the instructions: ::

    {{cookiecutter.cmd_name}} -h
"""

import click

from src.{{ cookiecutter.package_name }} import __version__

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(__version__)
def main():
    pass


if __name__ == '__main__':
    main()