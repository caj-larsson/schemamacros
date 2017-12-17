# import typing
# import attr
from jinja2 import loaders, Environment


header_tpl = """
-- Generated with schemamacros
"""

schema_block_tpl = """
{% block schema %}
{% endblock %}
"""


def build_layout(transaction, headers=[header_tpl], before_schema="", after_schema=""):
    headers_text = "\n".join(headers)
    if transaction:
        before_schema += "BEGIN;\n"
        after_schema += "COMMIT;\n"

    return headers_text + before_schema + schema_block_tpl + after_schema


def build_loader(paths, transaction):
    fs_loaders = [loaders.FileSystemLoader(path) for path in paths]
    system_loader = loaders.DictLoader({"layout": build_layout(transaction)})

    return loaders.ChoiceLoader(fs_loaders + [system_loader])


def render(config):
    loader = build_loader(config.template_directories, config.transaction)
    env = Environment(loader=loader)
    schema_tpl = env.get_template(config.schema_template)
    return schema_tpl.render(config.variables)


def compile(config):
    schema_text = render(config)
    with open(config.output, 'w') as f:
        f.write(schema_text)
