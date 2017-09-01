import argparse

from nameko.cli.main import setup_yaml_parser, CommandError, ConfigurationError
from ..cli_commands import RunExtra
from . import run


def setup_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    command = RunExtra
    command_parser = subparsers.add_parser(
        command.name, description=command.__doc__)
    command.init_parser(command_parser)
    command_parser.set_defaults(main=command.main)
    return parser


def main():
    parser = setup_parser()
    args = parser.parse_args()
    setup_yaml_parser()
    try:
        run.main(args)
    except (CommandError, ConfigurationError) as exc:
        print("Error: {}".format(exc))
