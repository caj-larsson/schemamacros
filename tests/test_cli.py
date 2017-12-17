import pytest  # noqa: F401
import tempfile
import shutil
import os
import schemamacros.cli as cli

from click.testing import CliRunner


def test_cli_compile():
    with tempfile.TemporaryDirectory() as td:
        dst = os.path.join(td, 'schema')
        shutil.copytree('tests/schema', dst)
        cfg_path = os.path.join(dst, 'sm-config.yml')
        runner = CliRunner()
        result = runner.invoke(cli.compile_schema, ['--config-path', cfg_path])
        assert(result.exit_code == 0)
        output_path = os.path.join(dst, 'schema-out.sql')
        output = open(output_path).read().strip()
    assert(len(output) > 0)
