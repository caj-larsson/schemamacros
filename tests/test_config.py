import pytest  # noqa: F401
import schemamacros.config as c


def test_templatedir_exists():
    td = c.TemplateDir("/")
    assert(str(td) == '/')


def test_templatedir_nexists():
    ok = False
    try:
        td = c.TemplateDir("%")  # noqa: F841
    except ValueError:
        ok = True
    assert(ok)


def test_config_dict(config_dict):
    cfg = c.build_config_inner(config_dict)
    assert(cfg is not None)


def test_config_dict_yaml(config_dict, config_dict_yaml):
    c_yaml = c.yaml_load(config_dict_yaml)
    c_dict = c.build_config_inner(config_dict)
    assert(c_yaml == c_dict)
    assert(c_yaml is not None)


def test_config_yaml(config_yaml):
    c_yaml = c.yaml_load(config_yaml)
    assert(c_yaml is not None)

    assert(len(c_yaml.targets.items()) == 1)

    assert(len(c_yaml.template_directories) == 1)
    assert(c_yaml.template_directories == ["tests/schema/templates"])
    assert(len(c_yaml.template_packages) == 0)
