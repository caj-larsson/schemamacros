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
        "output": ".",
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
        "output": ".",
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
output: "."
variables:
    test_var: "FOO"
schema_template: "schema.sql"
"""
