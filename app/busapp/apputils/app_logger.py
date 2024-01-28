"""
Set up loguru logger

"""

from loguru import logger as applog
import sys

applog.remove(0) # remove the default handler configuration

LOG_LEVEL = "DEBUG"
FILE_NAME="app.log"
log_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS zz}</green> | <level>{level: <8}</level> | <yellow>Line {line: >4} ({file}):</yellow> <b>{message}</b>"
applog.add(sys.stderr, level=LOG_LEVEL, format=log_format, colorize=True, backtrace=True, diagnose=True)
# TODO: reactivate once done
# applog.add(FILE_NAME, level=LOG_LEVEL, format=log_format, colorize=False, backtrace=True, diagnose=True)