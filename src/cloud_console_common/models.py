import traceback
import copy
from cloud_console_common.utils import *
from cloud_console_common import log


class ExtractLogic:
    """Implementation of ExtractLogic that will extract the data from a remote API call
    """

    def __init__(self):
        pass

    def extract(self, raw_data)->dict:
        """Receive the raw data from a remote call. In the case of AWS and the Boto3 library, this should always be a dict.

        .. note:: 

            Typically this method must be customized to suite the needs of the API called

        :param raw_data: The data, usually a dict, returned from a remote API call
        :type raw_data: dict
        :return: The extract logic implementation will return the relevant extracted data portion.
        :rtype: dict
        """
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

    def execute(self, authenticated_client: object=None)->dict:
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

    def call_remote_api(self, authenticated_client: object=None):
        return self.remote_call_logic.execute(authenticated_client=authenticated_client)

    def update_value(self, value: dict=dict()):
        pass

    def update_child_data_point(self, data_point_name: str, value=dict()):
        pass

    def get_ui_display_value(self)->str:
        if self.display_value is not None:
            return str(self.display_value)
        return '-'

    def __str__(self):
        return self.get_ui_display_value()

    def __repr__(self):
        if isinstance(self.value, dict):
            return 'DataPoint: {}: {}'.format(self.name, self.value)
        return 'DataPoint: {}: {}'.format(self.name, repr(self.value))


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

    def update_value(self, value: dict=dict(), authenticated_client: object=None):
        log.debug(message='Updated DataPoint named "{}" with value={}'.format(self.name, value))
        self.remote_call_logic.base_data = value
        self.value = self.call_remote_api(authenticated_client=authenticated_client)
        for idx, data_point in  self.children_data_points.items():
            log.debug(message='Updating child datapoint "{}"'.format(idx))
            self.update_child_data_point(data_point_name=idx, value=self.remote_call_logic.base_data)

    def update_child_data_point(self, data_point_name: str, value=dict(), authenticated_client: object=None):
        if data_point_name not in self.children_data_points:
            return
        if isinstance(self.children_data_points[data_point_name], DataPointBase):
            self.children_data_points[data_point_name].update_value(value=value, authenticated_client=authenticated_client)

    def get_child_by_name(self, name: str)->DataPointBase:
        if name in self.children_data_points:
            return self.children_data_points[name]
        raise Exception('Child DataPoint named "{}" not found'.format(name))

    def get_child_by_label(self, label: str)->list:
        children_data_points = list()
        for child_data_point_name, child_data_point_obj in self.children_data_points.items():
            if child_data_point_obj.label == label:
                children_data_points.append(child_data_point_obj)
        return children_data_points


class DataObjectCache:
    def __init__(self, identifier: str, data_point: DataPoint=None, max_cache_lifetime: int=300):
        if basic_string_validation(input_string=identifier)  is False:
            log.error(message='Invalid Identifier')
            raise Exception('Invalid identifier')
        self.identifier = identifier
        self.last_called_timestamp_utc = 0
        self.data_point = data_point
        self.max_cache_lifetime = max_cache_lifetime

    def update_results(self, results: dict, authenticated_client: object=None):
        if self.data_point is None:
            raise Exception('data point not yet initialized')
        if results is None:
            return
        if not isinstance(results, dict):
            return 
        self.data_point.update_value(value=results, authenticated_client=authenticated_client)
        self.last_called_timestamp_utc = get_utc_timestamp(with_decimal=False)
        log.info(message='Updated "{}"'.format(self.identifier))

    def refresh_cache(self, force: bool=False, authenticated_client: object=None)->bool:
        now = get_utc_timestamp(with_decimal=False)
        if ((now - self.last_called_timestamp_utc) > self.max_cache_lifetime) or (force is True):
            log.info(message='Refreshing local data state - data point "{}"'.format(self.data_point.name))
            self.data_point.update_value(authenticated_client=authenticated_client)
            self.last_called_timestamp_utc = now
            return True
        return False
            

# EOF
