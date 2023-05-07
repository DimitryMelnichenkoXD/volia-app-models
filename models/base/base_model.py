from pydantic import BaseModel


class BaseConfig(BaseModel):
    class Config:
        use_enum_values = True


class InBaseApiModel(BaseConfig):
    def get_condition(self):
        condition: dict = self.dict() or {}
        condition = {key: value for key, value in condition.items() if value is not None}
        return condition


class OutBaseApiModel(BaseConfig):
    pass
