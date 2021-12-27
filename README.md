# Unit Test

Create a virtual environment and activate:

```shell
python -m venv venv

. venv/bin/activate
```

Install dependencies:

```shell
pip3 install python-dateutil coverage rope build
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