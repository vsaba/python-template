from src.config import config


def main():
    print(f"Application version: {config.App.VERSION}")
    print(f"Application environment: {config.App.DEVELOPMENT}")


if __name__ == "__main__":
    # parse arguments

    main()
