import os
import sys

from setuptools import setup

# It imports release module this way because if it tried to import the whole package
# and some required dependencies were not installed, that would fail
# This is the only way to access the release module without needing all
# dependencies.
sys.path.insert(0, 'src/{{cookiecutter.package_name}}')
import release

sys.path.pop(0)

with open('README.md', 'r') as f:
    long_description = f.read()

with open('LICENSE', 'r') as f:
    license = f.read()

DEV_DEPENDENCIES = [
    'coverage',
{%- if cookiecutter.support_pypi_upload == true %}
    'twine',
{%- endif %}{% if cookiecutter.use_pytest == true %}
    'pytest',
{%- endif %}
]


def parse_requirements_txt(file):
    with open('requirements.txt', "r") as f:
        lines = list(map(str.strip, f.readlines()))
    # remove comment
    lines = [l[:l.find('#')].strip() if '#' in l else l for l in lines if not l.startswith('#')]
    return lines


requirements_dev = parse_requirements_txt('requirements.txt')
requirements_prod = [r for r in requirements_dev if all(not r.startswith(p) for p in DEV_DEPENDENCIES)]

prefix = os.getenv("PYPI_PREFIX", '')
if prefix:
    prefix += '.'

setup(
    name=f'{prefix}{release.name}',
    version=release.version,
    author=release.author,
    author_email=release.author_email,
    description=release.description_short,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=release.url,
    include_package_data=True,
    package_dir={'': 'src'},
    packages=['{{cookiecutter.package_name}}'],
    license=license,
    install_requires=requirements_prod,
    {%- if cookiecutter.support_cli == true %}
    entry_points={
        'console_scripts': [
            "{{cookiecutter.cmd_name}} = src.{{cookiecutter.package_name}}.cli:main",
        ],
    },
    {% endif -%}
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
