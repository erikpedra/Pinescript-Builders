from IParameter import ParameterType
class BoolParameter:
    """
    Boolean parameter
    """
    def __init__(self):
        self.Id = ""
        self.Name = ""
        self.Description = ""
        self.Value = False
        
    @property
    def ParameterType(self):
        return ParameterType.Boolean
