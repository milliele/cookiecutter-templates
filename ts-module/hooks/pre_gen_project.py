import re
import sys

MODULE_REGEX = r'^[\-a-zA-Z][\-a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.package_name }}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid TS/JS module name. '
          'Please do not use a _ and use - instead' % module_name)
    # Exit to cancel project
    sys.exit(1)
