import pytest
import yaml


@pytest.fixture
def config_dict():
    return {
        "template_directories": [
            "tests/schema/templates",
        ],
        "template_packages": [],
        "variables": {
            "test_var": "FOO"
        },
        "transaction": True,
        "output": "schema_out.sql",
        "version": "1.0",
        "schema_template": "schema.sql"
    }


@pytest.fixture
def config_dict_modules():
    return {
        "template_directories": [],
        "template_packages": [
            {
                "package_name": "tests.schema",
                "template_path": "templates"
            }
        ],
        "variables": {
            "test_var": "FOO"
        },
        "transaction": True,
        "output": "schema_out.sql",
        "version": "1.0",
        "schema_template": "schema.sql"
    }


@pytest.fixture
def config_dict_yaml(config_dict):
    return yaml.dump(config_dict)


@pytest.fixture
def config_yaml():
    return """
version: "1"
template_directories:
    - "tests/schema/templates"
template_packages: []
transaction: True
output: schema_out.sql
variables:
    test_var: "FOO"
schema_template: "schema.sql"
"""


@pytest.fixture
def config11_yaml():
    return """
version: "1.1"
template_directories:
    - "tests/schema/templates"

template_packages: []

targets:
    schema_shadowed_out.sql:
        transaction: True
        schema_template: "schema.sql"
        variables:
            shadowed: "True"

    schema_out.sql:
        schema_template: "schema.sql"

variables:
    test_var: "FOO"
    shadowed: "False"

"""
