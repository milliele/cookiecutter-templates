import subprocess

import pytest

from tests import check_output_inside_dir, bake_in_temp_dir


def get_lines(result):
    output = result.project_path.joinpath('Makefile').read_text()
    return output.split('\n')


def check_make_help(result, support_pypi_upload):
    output = check_output_inside_dir(
        'make help',
        str(result.project_path)
    )
    payload = dict(map(lambda x: tuple(map(str.strip, x.split('\t', maxsplit=1))), output.strip().split('\n')))

    commands = {'help', 'deps', 'coveragerc', 'test', 'integrated-test', 'cov', 'html-cov', 'update-html-cov',
                'dist-clean', 'runtime-clean', 'clean', 'install', 'build'}
    publish = {'publish'}
    answer = commands
    if support_pypi_upload:
        answer |= publish
    assert set(payload.keys()) == commands


def check_phony(result, support_pypi_upload):
    def check_end(pattern):
        found = -1
        for i, line in enumerate(lines):
            if line.strip('\r').endswith(pattern):
                found = i
            if found != -1 and i == found + 1:
                assert line.strip('\r') == ''
            if found != -1 and i == found + 2:
                assert line.strip('\r') == 'all: help'
        assert found != -1

    lines = get_lines(result)
    if support_pypi_upload:
        check_end('build publish')
    else:
        check_end('build')


def check_command(result, support_pypi_upload):
    with pytest.raises(subprocess.CalledProcessError) as cm:
        check_output_inside_dir(
            'make publish',
            str(result.project_path)
        )
    output = cm.value.output.decode('utf-8')
    if support_pypi_upload:
        assert 'twine' in output
    else:
        assert '' == output


@pytest.mark.parametrize('support_pypi_upload', [True, False])
def test_pypi(cookies, support_pypi_upload):
    with bake_in_temp_dir(cookies, extra_context=dict(support_pypi_upload=support_pypi_upload)) as result:
        check_make_help(result, support_pypi_upload)
        check_phony(result, support_pypi_upload)
        check_command(result, support_pypi_upload)


@pytest.mark.parametrize('build_wheel', [True, False])
def test_wheel(cookies, build_wheel):
    with bake_in_temp_dir(cookies, extra_context=dict(build_wheel=build_wheel)) as result:
        lines = get_lines(result)
        if build_wheel:
            assert any(line.strip('\r').endswith('python3 setup.py sdist bdist_wheel') for line in lines)
        else:
            assert any(line.strip('\r').endswith('python3 setup.py sdist') for line in lines)
        assert any('Python Boilerplate' in line for line in lines)
