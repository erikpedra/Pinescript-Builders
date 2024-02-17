from IParameter import ParameterType
class ExternalParameter:
    """
    Reference to another parameter.
    """
    
    def __init__(self):
        self.Id = None
        self.Name = None
        self.Description = None
        self.Value = None
    
    @property
    def ParameterType(self):
        return ParameterType.External
