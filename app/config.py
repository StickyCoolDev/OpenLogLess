import os
from dotenv import load_dotenv

load_dotenv()


def string_to_boolean_conditional(string_value):
    normalized_value = string_value.lower()

    if normalized_value == "true":
        return True
    elif normalized_value == "false":
        return False
    else:
        raise ValueError(f"Invalid string value for boolean conversion: {string_value}")


SQLITE_ECHO: bool = string_to_boolean_conditional(os.getenv("SQLITE_ECHO", "false"))
DB_URL: str = os.getenv("DB_URL", "")
