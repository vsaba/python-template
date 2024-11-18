"""This is the main module used for running the project as a whole."""

from .config import App


def main() -> None:
    """Main entry into the application, used for starting all the processes."""
    print(f"Application version: {App.VERSION}")
    print(f"Application environment: {App.DEVELOPMENT}")


if __name__ == "__main__":
    main()
