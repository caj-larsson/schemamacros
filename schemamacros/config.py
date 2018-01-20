import typing
import attr
from attr import validators as v
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
class TemplatePackage(object):
    package_name: str = attr.ib(validator=v.instance_of(str))
    template_path: str = attr.ib(validator=v.instance_of(str))

    @classmethod
    def from_dict(cls, config_obj):
        return cls(**config_obj)


@attr.s
class TargetConfig(object):
    transaction: bool = attr.ib(validator=v.instance_of(bool))
    schema_template: str = attr.ib(validator=v.instance_of(str))
    output: str = attr.ib(validator=v.instance_of(str))
    variables: typing.Mapping[str, str] = attr.ib()


@attr.s
class ConfigInternal(object):
    template_directories: typing.List[TemplateDir] = attr.ib(
        validator=v.instance_of(list),
        convert=lambda x: list(map(TemplateDir, x)),
        default=[]
    )

    template_packages: typing.List[TemplatePackage] = attr.ib(
        validator=v.instance_of(list),
        convert=lambda x: list(map(TemplatePackage.from_dict, x)),
        default=[]
    )

    variables: typing.Mapping[str, str] = attr.ib(default=dict())

    targets: typing.Mapping[str, str] = attr.ib(default=dict())


@attr.s
class ConfigfileVersion1(object):
    version: str = attr.ib(validator=v.in_(["1", "1.0"]))

    schema_template: str = attr.ib(validator=v.instance_of(str))

    output: str = attr.ib(validator=attr.validators.instance_of(str))

    template_directories: typing.List[TemplateDir] = attr.ib(
        validator=v.instance_of(list)
    )

    transaction: bool = attr.ib(
        validator=v.instance_of(bool),
        default=False
    )

    variables: typing.Mapping[str, str] = attr.ib(default=dict())

    template_packages: typing.List[TemplatePackage] = attr.ib(
        validator=v.instance_of(list),
        default=[]
    )

    def extract(self) -> ConfigInternal:
        target_config = TargetConfig(
            transaction=self.transaction,
            schema_template=self.schema_template,
            output=self.output,
            variables={}
        )
        config = ConfigInternal(
            template_directories=self.template_directories,
            template_packages=self.template_packages,
            variables=self.variables,
            targets={self.output: target_config}
        )
        return config


CONFIG_FILE_VERSIONS = {
    "1": ConfigfileVersion1,
    "1.0": ConfigfileVersion1
}


def build_config_inner(config_dict) -> ConfigInternal:
    if "version" not in config_dict:
        raise ValueError("Config does not have a version")

    version = str(config_dict["version"])

    if version not in CONFIG_FILE_VERSIONS:
        raise ValueError("Version %s is not supported", version)

    versioned_config = CONFIG_FILE_VERSIONS[version](**config_dict)

    return versioned_config.extract()


def yaml_load(yaml_text):
    return build_config_inner(yaml.load(yaml_text))
