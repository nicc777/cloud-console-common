import inspect
import os
import logging, logging.handlers
from pathlib import Path
import traceback
import random
import yaml


CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def generate_random_str(length: int=4):
    if length is None:
        length = 4
    if not isinstance(length, int):
        length = 4
    if length < 1:
        length = 1
    if length > 1024:
        length = 1024
    s = ''
    while len(s) < length:
        s = '{}{}'.format(
            s,
            random.choice(CHARS)
        )
    return s


def generate_unique_run_id():
    run_id = '{}-{}-{}-{}'.format(
        generate_random_str(length=8),
        generate_random_str(length=4),
        generate_random_str(length=4),
        generate_random_str(length=12)
    )
    return run_id


HOME = str(Path.home())
PROJECT_DIR = '{}/.cloud_console'.format(HOME)
PLUGINS_DIR = '{}/plugins'.format(PROJECT_DIR)
LOG_DIR = '{}/logs'.format(PROJECT_DIR)
LOG_FILE = '{}/common.log'.format(LOG_DIR)
FILE_LOG_ENABLED = False
RUN_ID = generate_unique_run_id()
DEBUG = bool(os.getenv('DEBUG', None))
CONFIGURATION_FILE = '{}/configuration.yaml'.format(PROJECT_DIR)


def create_basic_configuration():
    conf = dict()
    conf['plugin_dir'] = PLUGINS_DIR
    with open(CONFIGURATION_FILE, 'w') as file:
        yaml.dump(conf, file)


if os.path.exists(PROJECT_DIR) is False:
    os.makedirs(PROJECT_DIR, exist_ok=True) # If this throws an exception, we want to exit...

if os.path.exists(PLUGINS_DIR) is False:
    os.makedirs(PLUGINS_DIR, exist_ok=True) # If this throws an exception, we want to exit...

if os.path.exists(CONFIGURATION_FILE) is False:
    create_basic_configuration()

if os.path.exists(LOG_DIR) is False:
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
        FILE_LOG_ENABLED = True
    except:
        traceback.print_exc()
else:
    FILE_LOG_ENABLED = True


def get_default_logger():
    logger = logging.getLogger('cloud-console')
    logger.setLevel(logging.INFO)
    if os.getenv('DEBUG', None) is not None:
        logger.setLevel(logging.DEBUG)
    return logger


def get_file_log_handler():
    fh = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=10485760, backupCount=5)
    fh.setLevel(logging.INFO)
    if DEBUG is True:
        fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    return fh


def get_default_log_handler():
    if FILE_LOG_ENABLED is True:
        return get_file_log_handler()
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    if DEBUG is True:
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
                message = '{} [{}:{}:{}] {}'.format(
                    RUN_ID,
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
log.info(message='*** Logging Initiated - FILE_LOG_ENABLED={}   DEBUG={}'.format(FILE_LOG_ENABLED, DEBUG))
log.debug(message='DEBUG ENABLED')


# EOF
