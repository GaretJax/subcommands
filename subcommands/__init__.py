"""
A simple framework to build command line utilities.

To use it, follow these steps:

    1) Create an entry_point.txt file with the following content:

       [console_scripts]
       prog_name = package.scripts.prog_name:main

    2) Inside your package, create a 'scripts' package containing a
       prog_name module. Inside the module put the following code:

       import subcommands
       main = subcommands.entrypoint()

       Or, if you want to customize the name of the program:

       import subcommands
       main = subcommands.entry_point('prog_name')

    3) In your root __init__.py file, define the version of your program:

       VERSION = '0.8.1a'

    4) If you need a settings file, create a default_settings.ini file in
       the root of your package (make sure to include it in the
       distribution package as well) containing the default directives in
       INI format.

    5) Create a commands subpackage inside your package and add a module
       for each subcommand you want to implement.
"""

from .main import entry_point
from .subcommands import Command

__all__ = ['entry_point', 'Command',]
