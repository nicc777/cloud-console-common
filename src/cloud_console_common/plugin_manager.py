import sys
from cloud_console_common import log, CONFIGURATION_FILE
from cloud_console_common.plugin import Service, Services
from cloud_console_common.utils import read_yaml_file


def load_plugin(plugin_name: str)->Service:
    """
        conf = {
            "plugin_dir": "string",
            "plugins": [
                {
                    "plugin_name_as_string": {
                        "plugin_package_name": "string",
                        "plugin_package_source": "string",
                        "plugin_services": [
                            "string",
                            "string"
                        ],
                        "plugin_auth": "string",
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
    sys.path.append(conf['plugin_dir'])
    for plugin_section in conf['plugins']:
        if plugin_name in plugin_section:
            plugin_conf = conf['plugins'][plugin_name]
            # TODO Complete
    raise Exception('Unable to load service plugin named "{}"'.format(plugin_name))


def install_new_plugin():
    pass


def update_plugin():
    pass


def check_for_plugin_updates():
    pass