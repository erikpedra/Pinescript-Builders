class ParameterType:
    Integer = 0
    PriceType = 1
    Timeframe = 2
    Boolean = 3
    String = 4
    Price = 5
    Double = 6
    External = 7

class IParameter:
    def __init__(self, id, name, description, parameter_type):
        self.id = id
        self.name = name
        self.description = description
        self.parameter_type = parameter_type
