import typing
from .config import ConfigInternal, TargetConfig
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


def build_loader(paths, packages):
    fs_loaders = [loaders.FileSystemLoader(path) for path in paths]
    package_loaders = [loaders.PackageLoader(package.package_name, package.template_path)
                       for package in packages]

    return loaders.ChoiceLoader(fs_loaders + package_loaders)


def render_abstract(template: str,
                    loader: loaders.BaseLoader,
                    variables: typing.Mapping[str, str]):

    env = Environment(loader=loader)
    schema_tpl = env.get_template(template)
    return schema_tpl.render(variables)


def render_target(project_loader: loaders.BaseLoader,
                  project_variables: typing.Mapping[str, str],
                  target: TargetConfig):

    variables = dict(project_variables)
    variables.update(target.variables)

    layout = build_layout(target.transaction)
    layout_loader = loaders.DictLoader({"layout": layout})
    target_loader = loaders.ChoiceLoader([project_loader, layout_loader])

    render_text = render_abstract(target.schema_template,
                                  target_loader,
                                  variables)
    return render_text


def render(config: ConfigInternal, targets=None):
    if targets is None:
        targets = config.targets.keys()

    loader = build_loader(config.template_directories,
                          config.template_packages)
    output = {outpath: render_target(loader,
                                     config.variables,
                                     target)
              for outpath, target in config.targets.items()
              if outpath in targets}

    return output


def compile(config: ConfigInternal, targets=None):
    if targets is None:
        targets = config.targets.keys()

    for outpath, schema_text in render(config, targets).items():
        with open(outpath, 'w') as f:
            f.write(schema_text)
            f.flush()
