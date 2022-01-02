import sys
import importlib
from cloud_console_common import log, CONFIGURATION_FILE
from cloud_console_common.plugin import Service, Services
from cloud_console_common.utils import read_yaml_file


def load_plugin(plugin_name: str)->Services:
    """
        conf = {
            "plugin_dir": "string",                             $HOME/.cloud_console/plugins -> PLUGINS_DIR
            "plugins": [
                {
                    "plugin_name_as_string": {                  "cloud-console-aws-plugin"
                        "plugin_package_name": "string",        "aws" -> PLUGINS_DIR/aws
                        "plugin_package_source": "string",      https://github.com/...../aws.zip (can be any URL, as long it is a ZIP file)
                        "plugin_services": {
                            "string1": {                        "ec2" -> PLUGINS_DIR/aws/ec2
                                "module_name": "string",        "instances" -> PLUGINS_DIR/aws/ec2/instances.py
                                "class_name": "string"          "Instances" -> extends Service
                            },
                            "string2": {
                                "module_name": "string",
                                "class_name": "string"  
                            }
                        },
                        "plugin_auth": "string",                "aws_auth" -> The module implementing Auth, for example PLUGINS_DIR/aws/aws_auth.py
                        "plugin_auth_class_name": "string",     "PluginAuth" -> Implements Auth
                        "plugin_auth_config": [
                            {
                                "name1": "string"
                            },
                            {
                                "name2": "string"
                            }
                        ]
                    }
                }
            ]
        }
    """
    
    conf = read_yaml_file(CONFIGURATION_FILE)
    if 'plugin_dir' not in conf:
        raise Exception('plugin_dir nor presend in configuration file "{}"'.format(CONFIGURATION_FILE))
    if 'plugins' not in conf:
        raise Exception('no plugins defined in configuration file "{}"'.format(CONFIGURATION_FILE))
    for plugin_section in conf['plugins']:
        if plugin_name in plugin_section:
            plugin_src_path = '{}/{}'.format(conf['plugin_dir'], plugin_name)
            sys.path.append(plugin_src_path)
            plugin_conf = conf['plugins'][plugin_name]

            plugin_auth_impl = None
            if 'plugin_auth' in plugin_conf:
                auth_params = dict()
                if 'plugin_auth_config' in plugin_conf:
                    auth_params = plugin_conf['plugin_auth_config']
                auth_module = importlib.import_module(plugin_conf['plugin_auth'])
                auth_class_src = getattr(auth_module, plugin_conf['plugin_auth_class_name'])
                if len(auth_params) == 0:
                    plugin_auth_impl = auth_class_src()
                else:
                    plugin_auth_impl = auth_class_src(**auth_params)
            
            plugin_services = Services(auth_impl=plugin_auth_impl, auth_params=auth_params)

            for service_name, plugin_service_data in plugin_conf['plugin_services'].items():
                module_file = '{}/{}/{}/{}'.format(         # SOURCE FILE: $HOME/.cloud_console/plugins/aws/ec2/instances.py
                    conf['plugin_dir'],                     # $HOME/.cloud_console/plugins
                    plugin_conf['plugin_package_name'],     # aws
                    service_name,                           # ec2
                    plugin_service_data['module_name'],     # instances
                )
                module = importlib.import_module(module_file)
                class_src = getattr(module, plugin_service_data['class_name'])
                if isinstance(class_src, Service):
                    plugin_services.register_service(service=class_src(), init_service=True)


    raise Exception('Unable to load service plugin named "{}"'.format(plugin_name))


def install_new_plugin():
    pass


def update_plugin():
    pass


def check_for_plugin_updates():
    pass