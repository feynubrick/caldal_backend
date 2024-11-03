from humps import camelize
from ninja import Schema


class CamelCaseConfig(Schema.Config):
    alias_generator = camelize
    populate_by_name = True


class CamelCaseSchemaMixin:
    class Config(CamelCaseConfig, Schema.Config):
        pass


class CamelCaseSchema(CamelCaseSchemaMixin, Schema):
    pass
