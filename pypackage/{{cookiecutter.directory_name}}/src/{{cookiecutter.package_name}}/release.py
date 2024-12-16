"""
This module contains all the information related to the current release of the
library including descriptions, version number, authors and contact
information.
"""

# module information
name = '{{cookiecutter.package_name}}'

# author information.
# Used by __init__, doc and setup
author = '{{ cookiecutter.full_name }}'
author_email = '{{ cookiecutter.email }}'
maintainer = '{{ cookiecutter.full_name }}'
maintainer_email = '{{ cookiecutter.email }}'

description_short = '{{ cookiecutter.project_short_description }}'

# URL
url = '{{ cookiecutter.source_url }}'

# ======================= gitRelease information =============================
version = '{{ cookiecutter.initial_version }}'
"""Version information, used by __init__, doc, setup and gitRelease"""
release_name = f"v{version}"
"""The release title"""
release_body = """""".strip()
"""The release body"""
is_draft = False
"""Is this github release a draft"""
is_prerelease = False
"""Is this github release a prerelease"""


# ============================================================================

def validate_version(version):
    try:
        parts = version.split('-')
        main = parts[0]
        # validate main version
        try:
            major, minor, patch = main.split('.')
            assert ".".join(map(str, map(int, [major, minor, patch]))) == main
        except Exception as e:
            raise ValueError('Main version part should be like `major.minor.patch`. '
                             'Each part should be integer without leading 0.')
        # validate prerelease
        if len(parts) > 1:
            assert len(parts) == 2, ("There should at most be 1 `-` in the version name, "
                                     f"but {len(parts) - 1} are given.")
            try:
                pre_l, pre_n = parts[1].split('.')
            except Exception as e:
                raise ValueError('Prerelease part should be like `<pre_release_type>.<pre_release_number>`.')
            assert pre_l in {'alpha', 'beta'}, "Pre-release type could only be {'alpha', 'beta'}"
            assert pre_n.isdigit() and str(int(pre_n)) == pre_n, \
                "Pre-release number should be an integer without leading 0."
    except Exception as e:
        raise ValueError(f'Invalid version: `{version}`.\n'
                         f'{e}')


validate_version(version)
