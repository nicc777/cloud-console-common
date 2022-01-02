from datetime import datetime
import traceback
from cloud_console_common import log
import yaml

def get_utc_timestamp(with_decimal: bool=False): 
    epoch = datetime(1970,1,1,0,0,0) 
    now = datetime.utcnow() 
    timestamp = (now - epoch).total_seconds() 
    if with_decimal: 
        return timestamp 
    return int(timestamp)


def basic_string_validation(
    input_string: str,
    can_be_none: bool=False,
    can_be_empty: bool= False,
    min_len: int=1,
    max_len: int=1024
)->bool:
    if can_be_none is False:
        if input_string is None:
            return False
    if can_be_empty is False:
        if len(input_string) == 0:
            return False
    if min_len is not None:
        if len(input_string) < min_len:
            return False
    if  max_len is not None:
        if len(input_string) > max_len:
            return False
    return True


def read_yaml_file(file_path: str)->dict:
    data = dict()
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        if data is None:
            log.warning(message='Returned data object was None - converting to empty dict')
            data = dict()
        if not isinstance(data, dict):
            log.warning(message='Returned data object was not a dict - converting to empty dict')
            data = dict()
    except:
        log.error(message='EXCEPTION: {}'.format(traceback.format_exc()))
    return data
