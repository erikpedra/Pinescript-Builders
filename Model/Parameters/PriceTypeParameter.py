from IParameter import IParameter, ParameterType
from enum import Enum
class PriceType(Enum):
    Bid = 1
    Ask = 2

class PriceTypeParameter(IParameter):
    def __init__(self):
        self.Id = ""
        self.Name = ""
        self.Description = ""
        self.Value = PriceType.Bid

    @property
    def ParameterType(self):
        return ParameterType.PriceType
