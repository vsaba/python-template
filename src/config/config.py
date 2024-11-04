import os

from dotenv import load_dotenv

load_dotenv()


class App:
    VERSION = os.environ["APP_VERSION"]
    DEVELOPMENT = os.environ["APP_ENVIRONMENT"]


def test(a: str) -> None:
    pass
