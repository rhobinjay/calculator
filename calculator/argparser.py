import argparse


def parse():
    parser = argparse.ArgumentParser(
        usage=get_usage(),
        description=get_description())
    add_arguments(parser)
    return parser.parse_args()


def add_arguments(parser):
    arguments = parser.add_argument_group("Required arguments")
    arguments.add_argument(
        '--operation',
        choices=['add', 'subtract'],
        required=True
    )
    arguments.add_argument(
        '--number1',
        required=True,
        type=int
    )
    arguments.add_argument(
        '--number2',
        type=int,
        required=True
    )


def get_usage():
    return "calculator <arguments>"


def get_description():
    return """
        A calculator tool that performs mathematical operations.
    """
