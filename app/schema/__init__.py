from enum import Enum


class LogLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    ERROR = "ERROR"
    WARN = "WARN"
    FATAL = "FATAL"


class UserTier(Enum):
    FREE_PLAN = "free_plan"
    STANDARD_PLAN = "standard_plan"
    PREMIUM_PLAN = "premium_plan"


class TokenPermison(Enum):
    READ = "token_read"
    WRITE = "token_write"
    READ_WRITE = "token_read_write"
