import pytest  # noqa: F401
import schemamacros.config


def test_templatedir_exists():
    td = schemamacros.config.TemplateDir("/")
    assert(str(td) == '/')


def test_templatedir_nexists():
    ok = False
    try:
        td = schemamacros.config.TemplateDir("%")  # noqa: F841
    except ValueError:
        ok = True
    assert(ok)


def test_config_dict(config_dict):
    cfg = schemamacros.config.Config(**config_dict)
    assert(cfg is not None)


def test_config_dict_yaml(config_dict, config_dict_yaml):
    c_yaml = schemamacros.config.yaml_load(config_dict_yaml)
    c_dict = schemamacros.config.Config(**config_dict)
    assert(c_yaml == c_dict)
    assert(c_yaml is not None)


def test_config_yaml(config_yaml):
    c_yaml = schemamacros.config.yaml_load(config_yaml)
    assert(c_yaml is not None)
