{% if cookiecutter.use_pytest == true-%}
""""""
import os.path

import pytest

import src.{{ cookiecutter.package_name }}.release as r

BASE_DIR = os.path.dirname(__file__)


@pytest.mark.parametrize(
    ["versions", 'msg', 'no_error'],
    [
        ([
             '1.2.3',
             '1.2.3-alpha.0',
             '1.2.3-alpha.1',
             '1.2.3-beta.0',
             '1.2.3-beta.1',
         ], '', True),
        ([
             '1,2',
             '1.4',
             '01.32.5',
             'a.b.c'
         ], 'Main version part should be like `major.minor.patch`. Each part should be integer without leading 0.',
         False),
        (['1.2.3-al-al'], "There should at most be 1 `-` in the version name, but 2 are given.", False),
        (['1.2.3-al3'], "Prerelease part should be like `<pre_release_type>.<pre_release_number>`.", False),
        (['1.2.3-bd.3'], "Pre-release type could only be {'alpha', 'beta'}", False),
        (['1.2.3-alpha.b'], "Pre-release number should be an integer without leading 0.", False),
        (['1.2.3-alpha.05'], "Pre-release number should be an integer without leading 0.", False),
    ]
)
def test_validate_version(versions, msg, no_error):
    if no_error:
        for v in versions:
            r.validate_version(v)
    else:
        for v in versions:
            with pytest.raises(ValueError) as cm:
                r.validate_version(v)
            assert f"Invalid version: `{v}`.\n{msg}" == cm.value.args[0]
{% else -%}
""""""
import os.path
import unittest

import src.{{ cookiecutter.package_name }}.release as r

BASE_DIR = os.path.dirname(__file__)


class TestReleaseInfo(unittest.TestCase):
    def test_validate_version(self):
        def test_core(versions, msg, no_error=False):
            if no_error:
                for v in versions:
                    r.validate_version(v)
            else:
                for v in versions:
                    with self.assertRaises(ValueError) as cm:
                        r.validate_version(v)
                    self.assertEqual(f"Invalid version: `{v}`.\n{msg}", cm.exception.args[0])

        safe_versions = [
            '1.2.3',
            '1.2.3-alpha.0',
            '1.2.3-alpha.1',
            '1.2.3-beta.0',
            '1.2.3-beta.1',
        ]
        test_core(safe_versions, '', no_error=True)

        main_part_errors = [
            '1,2',
            '1.4',
            '01.32.5',
            'a.b.c'
        ]
        test_core(main_part_errors, 'Main version part should be like `major.minor.patch`. '
                                    'Each part should be integer without leading 0.')

        test_core(['1.2.3-al-al'],
                  "There should at most be 1 `-` in the version name, but 2 are given.")
        test_core(['1.2.3-al3'],
                  "Prerelease part should be like `<pre_release_type>.<pre_release_number>`.")
        test_core(['1.2.3-bd.3'], "Pre-release type could only be {'alpha', 'beta'}")
        test_core(['1.2.3-alpha.b'], "Pre-release number should be an integer without leading 0.")
        test_core(['1.2.3-alpha.05'], "Pre-release number should be an integer without leading 0.")
{%- endif %}