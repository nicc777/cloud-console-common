from cloud_console_common.models import *

class Auth:

    def __init__(self, **kwargs):
        self.authenticated = False
        self.init_kwargs = kwargs
        self.authenticated_client = None

    def authenticate(self, **kwargs):
        """Authenticate with the remote service. Ideally this will return a usable client object from where the remote service can be consumed.

        :return: Any object suitable for consuming the remote service. For example, in the case of boto3, something like >>> return boto3.client('ec2')
        :rtype: Object
        """
        self.authenticated = True
        self.authenticated_client = None
        return True


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

    def service_init(self, authenticated_client: object=None):
        self.data_object_cache.refresh_cache(force=True, authenticated_client=authenticated_client)

    def get_data_point(self, authenticated_client: object=None)->DataPoint:
        self.data_object_cache.refresh_cache(authenticated_client=authenticated_client)
        return self.data_object_cache.data_point


class Services:

    def __init__(self, auth_impl: Auth, auth_params: dict=dict()):
        self.auth = auth_impl
        self.services = dict()
        self.auth_params = auth_params

    def register_service(self, service: Service, init_service: bool=True):
        self.services[service.service_name] = service
        if init_service is True:
            if len(self.auth_params) > 0:
                self.services[service.service_name].service_init(authenticated_client=self.auth.authenticate(**self.auth_params))
            else:
                self.services[service.service_name].service_init(authenticated_client=self.auth.authenticate())

    def get_service_data_point(self, service_name: str, call_authentication_first: bool=True)->DataPoint:
        if service_name not in self.services:
            raise Exception('Service "{}" not found'.format(service_name))
        if call_authentication_first is True:
            return self.services[service_name].get_data_point(authenticated_client=self.auth.authenticate().authenticated_client)
        return self.services[service_name].get_data_point(authenticated_client=self.auth.authenticated_client)

