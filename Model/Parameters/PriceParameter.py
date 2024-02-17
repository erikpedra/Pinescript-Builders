from IParameter import ParameterType

class PriceParameter:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.description = ""
        self.value = 0.0
        
    @property
    def parameter_type(self):
        return ParameterType.Price
