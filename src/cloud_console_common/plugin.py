from cloud_console_common.models import *

class Auth:

    def __init__(self, **kwargs):
        self.authenticated = False
        self.init_kwargs = kwargs

    def authenticate(self, **kwargs):
        self.authenticated = True


class Service:

    def __init__(
        self,
        service_name: str,
        ui_label: str,
        data_point: DataPoint,
        max_cache_lifetime: int=300,
        service_config: dict=dict()
    ):
        self.service_name = service_name
        self.ui_label = ui_label
        self.data_object_cache = DataObjectCache(
            identifier=service_name, 
            data_point=data_point, 
            max_cache_lifetime=max_cache_lifetime
        )
        self.configuration = service_config


class Services:

    def __init__(self, auth_impl: Auth):
        self.auth = auth_impl
        self.services = dict()

    def register_service(self, service: Service):
        self.services[service.service_name] = service

