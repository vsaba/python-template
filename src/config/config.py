"""Configuration module used for loading the environment variables from the .env file.

Provides classes which can be easily imported into other modules for easier use of
environment variables
"""

import os

from dotenv import load_dotenv

load_dotenv()


class App:
    """App module providing the main environment variables for a project"""

    VERSION = os.environ["APP_VERSION"]
    DEVELOPMENT = os.environ["APP_ENVIRONMENT"]
