import click
import os
from .config import yaml_load
from .compile import compile as cm


@click.command()
@click.option('--config-path', default="sm-config.yml", help='Configuration file in YAML.')
@click.argument('targets', required=False)
def compile_schema(config_path, targets):
    cwd = os.getcwd()
    try:
        workdir = os.path.dirname(config_path)
        file_path = os.path.basename(config_path)
        if workdir != '':
            os.chdir(workdir)
        config = yaml_load(open(file_path).read())
        cm(config, targets)
    finally:
        os.chdir(cwd)
