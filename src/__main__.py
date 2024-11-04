"""
This is the main module used for running the project as a whole
"""

from src.config import config


def main():
    print(f"Application version: {config.App.VERSION}")
    print(f"Application environment: {config.App.DEVELOPMENT}")
    test("Hello world")


def test(a):
    print(a)


if __name__ == "__main__":
    # parse arguments

    main()


# TODO must enable linting, formatting, type checking and docstring generating
