from __future__ import absolute_import

import sys
import os
import argparse
import importlib

from . import logging, settings, subcommands


def build_parser(name, package):
    version = importlib.import_module(package).VERSION

    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--version', action='version',
                        version='%(prog)s ' + version)
    parser.add_argument('-v', '--verbose', default=list(),
                        action='append_const', const=1, help='Increments the' \
                        ' verbosity (can be used multiple times).')
    parser.add_argument('-q', '--quiet', default=list(),
                        action='append_const', const=1, help='Decrements the' \
                        ' verbosity (can be used multiple times).')

    commands = subcommands.load('{}.commands'.format(package))
    subcommands.attach(parser, commands)

    return parser


def main(name, package=None, args=None):
    # Setup logging
    logfile = os.getenv('{}_LOGFILE'.format(name.upper())) or '{}.log'.format(name)
    logger = logging.LoggingSubsystem(logging.INFO, logfile)
    logger.start()

    # Build argument parser and parse command line
    parser = build_parser(name, package)
    args = parser.parse_args(args)

    # Set the verbosity level
    logger.increment_verbosity(len(args.verbose) - len(args.quiet))
    logger.capture_stdout()

    # Load settings
    # TODO: Get path from optional settings args
    path = None
    config = settings.load_config(package, path)

    # Execute command
    args.command.set_logger(logger)
    args.command.set_config(config)
    res = args.command.execute(args)

    # Shutdown logging
    logger.stop(res)

    return res


def entry_point(name=None, package=None):
    if name is None:
        name = sys.argv[0]
    def _main():
        sys.exit(main(name, package, sys.argv[1:]))
    return _main
