import inspect
import enum

class Util:
    @staticmethod
    def replace_parameter(parameter):
        if parameter is None:
            return None
        if parameter.startswith("{") and parameter.endswith("}"):
            return f"instance.parameters.{parameter[1:-1]}"
        return parameter

    @staticmethod
    def get_display_name(enum_value):
        if not inspect.isclass(enum_value) or not issubclass(enum_value, enum.Enum):
            raise ValueError("Argument must be an Enum type")
        try:
            return enum_value.__members__.values()[0]._name_
        except AttributeError:
            return str(enum_value)
