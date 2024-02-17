from IParameter import ParameterType
class StringParameter:
    # String parameter
    def __init__(self):
        self.Id = ""
        self.Name = ""
        self.Description = ""
        self.Value = ""
    
    @property
    def ParameterType(self):
        return ParameterType.String
