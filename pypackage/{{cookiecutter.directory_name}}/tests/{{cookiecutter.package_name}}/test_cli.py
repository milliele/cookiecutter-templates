""""""
import os.path
{%- if cookiecutter.use_pytest == true %}

import pytest
{% else %}
import unittest

{% endif -%}
from click.testing import CliRunner

import src.{{ cookiecutter.package_name }}.cli as m
from src.{{ cookiecutter.package_name }}.release import version

BASE_DIR = os.path.dirname(__file__)


{% if cookiecutter.use_pytest == true-%}
@pytest.fixture()
def runner():
    yield CliRunner()


def test_main(runner):
    res = runner.invoke(m.main, ['--version'])
    assert version == res.output.split(' ')[-1].strip()
    assert 0 == res.exit_code
    res = runner.invoke(m.main, ['-h'])
    assert 0 == res.exit_code
{%- else -%}
class TestMain(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_main(self):
        res = self.runner.invoke(m.main, ['--version'])
        self.assertEqual(version, res.output.split(' ')[-1].strip())
        self.assertEqual(0, res.exit_code)
        res = self.runner.invoke(m.main, ['-h'])
        self.assertEqual(0, res.exit_code)
{%- endif %}
