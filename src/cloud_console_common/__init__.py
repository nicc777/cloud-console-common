import inspect
import os
import logging
from pathlib import Path
import traceback


HOME = str(Path.home())
LOG_DIR = '{}/.cloud_console/logs'.format(HOME)
LOG_FILE = '{}/common.log'.format(LOG_DIR)
FILE_LOG_ENABLED = False


if os.path.exists(LOG_DIR) is False:
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
        FILE_LOG_ENABLED = True
    except:
        traceback.print_exc()


def get_default_logger():
    logger = logging.getLogger('cloud-console')
    logger.setLevel(logging.INFO)
    if os.getenv('DEBUG', None) is not None:
        logger.setLevel(logging.DEBUG)
    return logger


def get_file_log_handler():
    ch = logging.FileHandler(filename=LOG_FILE)
    ch.setLevel(logging.INFO)
    if os.getenv('DEBUG', None):
        ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    return ch


def get_default_log_handler():
    if FILE_LOG_ENABLED is True:
        return get_file_log_handler()
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    if os.getenv('DEBUG', None):
        ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    return ch


def id_caller()->list:
    result = list()
    try:
        caller_stack = inspect.stack()[2]
        result.append(caller_stack[1].split(os.sep)[-1]) # File name
        result.append(caller_stack[2]) # line number
        result.append(caller_stack[3]) # function name
    except: # pragma: no cover
        pass
    return result


class Logger:
    def __init__(self, logger=get_default_logger() ,logging_handler=get_default_log_handler()):
        logger.addHandler(logging_handler)
        self.logger = logger

    def _format_msg(self, stack_data: list, message: str)->str:
        if message is not None:
            message = '{}'.format(message)
            if len(stack_data) == 3:
                message = '[{}:{}:{}] {}'.format(
                    stack_data[0],
                    stack_data[1],
                    stack_data[2],
                    message
                )
            return message
        return 'NO_INPUT_MESSAGE'

    def info(self, message: str):
        self.logger.info(
            self._format_msg(
                stack_data=id_caller(), 
                message=message
            )
        )

    def warning(self, message: str):
        self.logger.warning(
            self._format_msg(
                stack_data=id_caller(), 
                message=message
            )
        )

    def error(self, message: str):
        self.logger.error(
            self._format_msg(
                stack_data=id_caller(), 
                message=message
            )
        )

    def debug(self, message: str):
        self.logger.debug(
            self._format_msg(
                stack_data=id_caller(), 
                message=message
            )
        )



log = Logger()


# EOF
