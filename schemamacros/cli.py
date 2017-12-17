import click
import os
from .config import yaml_load
from .compile import compile as cm


@click.command()
@click.option('--config-path', default="sm-config.yml", help='Configuration file in YAML.')
def compile_schema(config_path):
    cwd = os.getcwd()
    try:
        workdir = os.path.dirname(config_path)
        file_path = os.path.basename(config_path)
        if workdir != '':
            os.chdir(workdir)
        config = yaml_load(open(file_path).read())
        cm(config)
    finally:
        os.chdir(cwd)
