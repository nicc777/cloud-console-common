import traceback
from cloud_console_common.utils import *
from cloud_console_common import log


class DataObjectCache:
    def __init__(self, identifier: str):
        if basic_string_validation(input_string=identifier)  is False:
            log.error(message='Invalid Identifier')
            raise Exception('Invalid identifier')
        self.identifier = identifier
        self.last_called_timestamp_utc = 0
        self.raw_result = dict()

    def update_results(self, results: dict):
        if results is None:
            return
        if not isinstance(results, dict):
            return 
        self.raw_result = results
        self.last_called_timestamp_utc = get_utc_timestamp(with_decimal=False)
        log.info(message='Updated "{}"'.format(self.identifier))


class DataPointBase:

    def __init__(self, name: str, label: str=None, initial_value: object=None):
        if basic_string_validation(input_string=name) is False:
            raise Exception('name basic validation failed. must be a string of 1 to 1024 characters')
        self.name = name
        self.label = name[0:32]
        if label is not None:
            if basic_string_validation(input_string=label, max_len=32) is False:
                raise Exception('If the label is supplied, it must be a string between 1 and 32 characters')
            self.label = label
        self.children_data_points = dict()
        self.value = initial_value


class DataPoint(DataPointBase):

    def __init__(self, name: str, label: str=None, initial_value: object=None):
        super().__init__(name=name, label=label, initial_value=initial_value) 

    def add_child_data_point(self, data_point: DataPointBase):
        if data_point is None:
            log.warning(message='data_point cannot be None - ignoring')
            return
        if not isinstance(data_point, DataPointBase):
            log.warning(message='data_point cannot be of type "{}" - ignoring'.format(type(data_point)))
            return
        self.children_data_points[data_point.name] = data_point


class DataPointExtractLogic:

    """

    """

    def __init__(
        self, 
        name: str, 
        data_point: DataPoint,
        extract_implementation: object,     # Expecting a class with a method called "extract" that takes one named parameter named "raw_data"
        remote_call_implementation: object, # Expecting a class with a method called "execute" taking no parameters
        max_cache_lifetime: int=300         # Refresh every so many seconds
    ):
        self.name = name
        self._data_point = data_point
        if not callable(extract_implementation):
            raise Exception('Extract function must be a valid callable function')
        if not callable(remote_call_implementation):
            raise Exception('Remote function must be a valid callable function')
        self.extract_implementation = extract_implementation
        self.remote_call_implementation = remote_call_implementation
        self._cache = DataObjectCache(identifier='DataPointExtractLogic_{}'.format(name))
        self._max_cache_lifetime = max_cache_lifetime

    def _get_remote_data(self):
        now = get_utc_timestamp(with_decimal=False)
        if (now - self._cache.last_called_timestamp_utc) > self._max_cache_lifetime:
            log.info(message='Refreshing local data state - data point "{}"'.format(self._data_point.name))
            try:
                self._cache.update_results(
                    results=self.extract_implementation.extract(
                        raw_data=self.remote_call_implementation.execute()
                    )
                )
            except:
                log.error(message='EXCEPTION: {}'.format(traceback.format_exc()))
                log.warning(message='Failed to refresh data point - using local data state (STALE)')
        else:
            log.info(message='Using local data state - data point "{}"'.format(self._data_point.name))

    def get_data_point(self, return_only_value: bool=True):
        self._get_remote_data()
        if return_only_value is True:
            return self._data_point.value
        return self._data_point


        


# EOF
