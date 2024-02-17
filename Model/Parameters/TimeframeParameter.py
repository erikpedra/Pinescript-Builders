from IParameter import ParameterType
class TimeframeParameter:
    def __init__(self):
        self.id = None
        self.name = None
        self.description = None
        self.value = None

    @property
    def parameter_type(self):
        return ParameterType.Timeframe
