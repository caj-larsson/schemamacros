import typing
import attr
import yaml
import os


@attr.s(repr=False)
class TemplateDir(str):

    def __repr__(self):
        return self.path

    def __str__(self):
        return self.__repr__()

    path: str = attr.ib()

    @path.validator
    def check(self, attribute, value):
        if not os.path.isdir(value):
            raise ValueError("The path %s is not a directory", value)


@attr.s
class Config(object):
    transaction: bool = attr.ib(validator=attr.validators.instance_of(bool))
    schema_template: str = attr.ib(validator=attr.validators.instance_of(str))
    output: str = attr.ib(validator=attr.validators.instance_of(str))
    variables: typing.Mapping[str, str] = attr.ib()
    template_directories: typing.List[TemplateDir] = attr.ib(
        validator=attr.validators.instance_of(list),
        convert=lambda x: list(map(TemplateDir, x)))
    version: str = attr.ib(validator=attr.validators.in_(["1", "1.0"]))


def yaml_load(yaml_text):
    return Config(**yaml.load(yaml_text))
