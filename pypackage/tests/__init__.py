import os.path
import shlex
import subprocess
from contextlib import contextmanager

from cookiecutter.utils import rmtree

__all__ = [
    'bake_in_temp_dir',
    'check_output_inside_dir'
]

BASE_DIR = os.path.dirname(__file__)
TEMPLATE_PATH = os.path.abspath(os.path.join(BASE_DIR, '..'))


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(template=TEMPLATE_PATH, *args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project_path))


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command)).decode('utf-8')
