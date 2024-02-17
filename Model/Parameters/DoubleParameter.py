from IParameter import ParameterType
class DoubleParameter:
    def __init__(self):
        self.Id = ""
        self.Name = ""
        self.Description = ""
        self.Value = 0.0

    @property
    def ParameterType(self):
        return ParameterType.Double
