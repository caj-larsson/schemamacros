import pytest  # noqa: F401
import tempfile
import schemamacros.compile as c
import schemamacros.config as cfg
from jinja2 import loaders, Environment


def test_build_loader(config_dict):
    config = cfg.build_config_inner(config_dict)
    loader = c.build_loader(config.template_directories,
                            config.template_packages)

    assert(isinstance(loader, loaders.ChoiceLoader))

    env = Environment(loader=loader)
    tpl = env.get_template("schema.sql")

    assert(tpl is not None)


def test_render(config_dict):
    config = cfg.build_config_inner(config_dict)
    schema_texts = c.render(config)
    print(schema_texts)
    schema_text = schema_texts["schema_out.sql"].strip()

    assert(schema_text != '')
    assert("FOO" in schema_text)


def test_compile(config_dict):
    config = cfg.build_config_inner(config_dict)
    schema_text = c.render(config)["schema_out.sql"].strip()

    with tempfile.NamedTemporaryFile('r') as f:
        config_tmp_dict = dict(config_dict)
        config_tmp_dict["output"] = f.name

        config_tmp = cfg.build_config_inner(config_tmp_dict)
        c.compile(config_tmp)
        schema_text_c = f.read().strip()

    assert(schema_text != '')
    assert(schema_text_c != '' and type(schema_text_c) == str)

    assert(schema_text_c == schema_text)


def test_module_templates(config_dict_modules):
    config = cfg.build_config_inner(config_dict_modules)
    schema_text = c.render(config)["schema_out.sql"].strip()

    with tempfile.NamedTemporaryFile('r') as f:
        config_tmp_dict = dict(config_dict_modules)
        config_tmp_dict["output"] = f.name

        config_tmp = cfg.build_config_inner(config_tmp_dict)
        c.compile(config_tmp)
        schema_text_c = f.read().strip()

    assert(schema_text_c != '' and type(schema_text_c) == str)
    assert(schema_text != '')
    assert(schema_text_c == schema_text)
