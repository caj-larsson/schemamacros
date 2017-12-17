import pytest  # noqa: F401
import tempfile
import schemamacros.compile as c
import schemamacros.config as cfg
from jinja2 import loaders, Environment


def assert_valid_layout(layout_text):
    lines = layout_text.splitlines()
    for line in lines:
        trimmed_line = line.strip()
        valid_const_strings = {"", "BEGIN;", "COMMIT;", "{% block schema %}",
                               "{% endblock %}"}

        assert(trimmed_line in valid_const_strings
               or trimmed_line.startswith("--"))


def test_layout_notxn():
    layout_tpl = c.build_layout(False)
    assert_valid_layout(layout_tpl)
    assert("BEGIN;" not in layout_tpl)


def test_layout_txn():
    layout_tpl = c.build_layout(True)
    assert_valid_layout(layout_tpl)
    assert("BEGIN;" in layout_tpl)


def test_build_loader(config_dict):
    config = cfg.Config(**config_dict)
    loader = c.build_loader(config.template_directories, True)

    assert(isinstance(loader, loaders.ChoiceLoader))
    env = Environment(loader=loader)
    tpl = env.get_template("layout")
    assert(tpl.render().strip() != '')


def test_render(config_dict):
    config = cfg.Config(**config_dict)
    schema_text = c.render(config).strip()

    assert(schema_text != '')
    assert("FOO" in schema_text)


def test_compile(config_dict):
    config = cfg.Config(**config_dict)
    schema_text = c.render(config).strip()

    with tempfile.NamedTemporaryFile('r') as f:
        config.output = f.name
        c.compile(config)
        schema_text_c = f.read().strip()

    assert(schema_text_c != '' and type(schema_text_c) == str)
    assert(schema_text != '')
    assert(schema_text_c == schema_text)
