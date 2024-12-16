"""{{cookiecutter.project_short_description}}"""

# Import release information
import src.{{cookiecutter.package_name}}.release as release

__author__ = release.author
__version__ = release.version

# List of all modules that contain classes needed to be registered with the registry (via a Class.register decorator)
# This code ensures that the modules are imported and hence the decorators are
# executed and the classes/functions registered.
__modules_to_register = []

for m in [None] + __modules_to_register:
    # This try/catch is needed to support reload({{ cookiecutter.package_name }})
    if m is not None:
        try:
            exec('import %s' % m)
            exec('del %s' % m)
        except AttributeError:
            pass
else:
    if m is not None:
        del m
