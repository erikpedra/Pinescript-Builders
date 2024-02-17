class StrategyParameter:
    """
    Parameters (could be set by the user).
    """

    def __init__(self):
        self.Id = ""
        self.Name = ""
        self.Description = ""
        self.DefaultValue = ""
        self.ParameterType = ""

    INTEGER = "int"
    PRICE_TYPE = "price_type"
    PRICE_TYPE_BID = "bid"
    PRICE_TYPE_ASK = "ask"
    TIMEFRAME = "timeframe"
    BOOLEAN = "bool"
    STRING = "string"
    PRICE = "price"
    DOUBLE = "double"
    EXTERNAL_PARAMETER = "external_param"
