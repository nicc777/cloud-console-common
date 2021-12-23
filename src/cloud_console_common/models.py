import traceback
import copy
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

    def __init__(self, extract_logic: ExtractLogic=ExtractLogic(), base_data: dict=dict(), **kwargs):
        log.debug(message='kwargs={}'.format(kwargs))
        self.extract_logic = extract_logic
        self.base_data = base_data
        self.args = kwargs.items()

    def execute(self)->dict:
        log.warning(message='This method is a dummy method with no implementation logic - create your own')
        return self.extract_logic.extract(raw_data=self.base_data)


class DataPointBase:

    def __init__(
        self, 
        name: str, 
        label: str=None, 
        initial_value: object=None, 
        remote_call_logic: RemoteCallLogic=RemoteCallLogic(),
        ui_section_name: str='',
        ui_tab_name: str='',
        ui_identifier: str=''
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
        self.display_value = '-'
        self.remote_call_logic = remote_call_logic
        self.ui_section_name = ui_section_name
        self.ui_tab_name = ui_tab_name
        self.ui_identifier = ui_identifier

    def call_remote_api(self):
        return self.remote_call_logic.execute()

    def update_value(self, value: dict=dict()):
        pass

    def update_child_data_point(self, data_point_name: str, value=dict()):
        pass

    def get_ui_display_value(self)->str:
        if self.display_value is not None:
            return str(self.display_value)
        return '-'


class DataPoint(DataPointBase):

    def __init__(
        self, name: str,
        label: str=None,
        initial_value: object=None, 
        remote_call_logic: RemoteCallLogic=RemoteCallLogic(),
        ui_section_name: str='',
        ui_tab_name: str='',
        ui_identifier: str=''
    ):
        super().__init__(
            name=name,
            label=label,
            initial_value=initial_value,
            remote_call_logic=remote_call_logic,
            ui_section_name=ui_section_name,
            ui_tab_name=ui_tab_name,
            ui_identifier=ui_identifier
        ) 

    def add_child_data_point(self, data_point: DataPointBase):
        if data_point is None:
            log.warning(message='data_point cannot be None - ignoring')
            return
        if not isinstance(data_point, DataPointBase):
            log.warning(message='data_point cannot be of type "{}" - ignoring'.format(type(data_point)))
            return
        self.children_data_points[data_point.name] = data_point

    def update_value(self, value: dict=dict()):
        log.debug(message='Updated DataPoint named "{}" with value={}'.format(self.name, value))
        self.remote_call_logic.base_data = value
        self.value = self.call_remote_api()
        self.remote_call_logic.base_data = None
        for idx, data_point in  self.children_data_points.items():
            log.debug(message='Updating child datapoint "{}"'.format(idx))
            self.update_child_data_point(data_point_name=idx, value=value)

    def update_child_data_point(self, data_point_name: str, value=dict()):
        if data_point_name not in self.children_data_points:
            return
        if isinstance(self.children_data_points[data_point_name], DataPointBase):
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
