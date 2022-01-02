# Unit Test

Create a virtual environment and activate:

```shell
python -m venv venv

. venv/bin/activate
```

Install dependencies:

```shell
pip3 install python-dateutil coverage rope build pyyaml
```

Run:

```shell
coverage run --omit="venv/*" --omit="tests/*" tests/test_models.py
```

To obttain the current coverage report:

```shell
coverage report -m
```

# Build

Run the following for a build:

```shell
python3 -m build
```

# Main Configuration File Format

The file structure format is in YAML

Basic structure:

```yaml
---
plugin_dir: string                  # Where plugin packages will be installed - $HOME/.cloud_console/plugins
plugins:
- plugin_name_as_string:            # A user friendly name of the plugin
    plugin_package_name: string     # The name of the package, i.e. MyPackage
    plugin_package_source: string   # URL to the tar.gz package file (local file or on the web)
    plugin_services:
    - string1:                      # NAME 1
        module_name: string         # The module name
        class_name: string          # The class name (extending Service)
    - string2:                      # NAME 2
        module_name: string         # The module name
        class_name: string          # The class name (extending Service)
    plugin_auth: string             # Path to implementation of Auth class, for example MyPackage.MyAuth
    plugin_auth_config:             # Optional custom configuration for Authentication
    - name1: string                 # Custom key/value pair
    - name2: string                 # Custom key/value pair
```
