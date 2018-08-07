# schemamacros

Checkout the [blogpost](https://blog.caj.me/introducing-schemamacros.html#introducing-schemamacros)

schemamacros is essentially just a slightly opinionated way to run Jinja2
templates. I made this to do interpolation, concatenation and maybe some
proper templating in my SQL-schemas.


## Installation

```
pip install schemamacros
```

## Usage

Check the YAML based config format in `tests/schema/sm-config.yml`

Run `sm-compile` to build the schema with the implicit config `./sm-config.yml`
or add `--config-path <a file path>`. The output will end up in the same basedir 
as the config file.
