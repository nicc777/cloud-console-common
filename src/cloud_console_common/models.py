import traceback
from cloud_console_common.utils import *
from cloud_console_common import log


class ExtractLogic:

    def __init__(self):
        pass

    def extract(self, raw_data)->dict:
        log.warning(message='This method is a dummy method with no implementation logic - create your own')
        if raw_data is None:
            return dict()
        if isinstance(raw_data, dict):
            return raw_data
        return dict()


class RemoteCallLogic:

    def __init__(self, extract_logic: ExtractLogic=ExtractLogic(), *kwargs):
        log.debug(message='kwargs={}'.format(kwargs))
        self.extract_logic = extract_logic
        self.args = dict()

    def execute(self)->dict:
        log.warning(message='This method is a dummy method with no implementation logic - create your own')
        return self.extract_logic.extract(raw_data=dict())


class DataPointBase:

    def __init__(
        self, 
        name: str, 
        label: str=None, 
        initial_value: object=None, 
        extract_logic: ExtractLogic=ExtractLogic(),
        remote_call_logic: RemoteCallLogic=RemoteCallLogic()
    ):
        if basic_string_validation(input_string=name) is False:
            raise Exception('name basic validation failed. must be a string of 1 to 1024 characters')
        self.name = name
        self.label = name[0:32]
        if label is not None:
            if basic_string_validation(input_string=label, max_len=32) is False:
                raise Exception('If the label is supplied, it must be a string between 1 and 32 characters')
            self.label = label
        self.children_data_points = dict()  # Dictionary of DataPointBase with the "name" of each data point as dictionary index
        self.value = initial_value
        self.extract_logic = extract_logic
        self.remote_call_logic = remote_call_logic

    def call_remote_api(self):
        return self.remote_call_logic.execute()

    def update_value(self, value=dict()):
        pass

    def update_child_data_point(self, data_point_name: str, value=dict()):
        pass


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

    def update_value(self, value=None, set_value_for_children: bool=False):
        log.debug(message='Updated DataPoint named "{}" with value={}'.format(self.name, value))
        if value is None:
            self.value = self.extract_logic.extract(
                raw_data=self.call_remote_api()
            )
            if set_value_for_children is True:
                value = self.value
        else:
            self.value = value
        for idx, data_point in self.children_data_points.items():
            log.debug(message='Updating child datapoint "{}"'.format(idx))
            if isinstance(data_point, DataPointBase):
                data_point.update_value(value=value)

    def update_child_data_point(self, data_point_name: str, value=dict()):
        if data_point_name in self.children_data_points:
            self.children_data_points[data_point_name].update_value(value=value)


class DataObjectCache:
    def __init__(self, identifier: str, data_point: DataPoint=None):
        if basic_string_validation(input_string=identifier)  is False:
            log.error(message='Invalid Identifier')
            raise Exception('Invalid identifier')
        self.identifier = identifier
        self.last_called_timestamp_utc = 0
        self.data_point = data_point

    def update_results(self, results: dict):
        if self.data_point is None:
            raise Exception('data point not yet initialized')
        if results is None:
            return
        if not isinstance(results, dict):
            return 
        self.data_point.update_value(value=results)
        self.last_called_timestamp_utc = get_utc_timestamp(with_decimal=False)
        log.info(message='Updated "{}"'.format(self.identifier))

    def refresh_cache(self, force: bool=False):
        now = get_utc_timestamp(with_decimal=False)
        if ((now - self._cache.last_called_timestamp_utc) > self._max_cache_lifetime) or (force is True):
            log.info(message='Refreshing local data state - data point "{}"'.format(self._data_point.name))
            self.data_point.update_value()
            

# EOF
