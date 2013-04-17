"""
Configuration management for the different components.
"""


import os
import importlib
import ConfigParser


def get_default_files(name):
    base = os.path.dirname(importlib.import_module(name).__file__)
    return [
        os.path.join(base, 'default-settings.ini'),
        '/etc/{}/{}.conf'.format(name, name),
        os.path.expanduser('~/.{}.conf'.format(name)),
        os.path.join(os.path.realpath('.'), '{}.conf'.format(name)),
    ]


def load_config(name, path=None, defaults=None):
    """
    Loads and parses an INI style configuration file using Python's built-in
    ConfigParser module.

    If path is specified, load it.

    If ``defaults`` (a list of strings) is given, try to load each entry as a
    file, without throwing any error if the operation fails.

    If ``defaults`` is not given, the following locations listed in the
    DEFAULT_FILES constant are tried.

    To completely disable defaults loading, pass in an empty list or ``False``.

    Returns the SafeConfigParser instance used to load and parse the files.
    """

    if defaults is None:
        defaults = get_default_files(name)

    config = ConfigParser.SafeConfigParser(allow_no_value=True)

    if defaults:
        config.read(defaults)

    if path:
        with open(path) as fh:
            config.readfp(fh)

    return config
