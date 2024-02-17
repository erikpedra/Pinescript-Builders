class FormulaItem:
    """
    Describes argument for the condition.
    """
    def __init__(self):
        self.Value = None
        self.ValueType = None
        self.Substream = None
        self.StreamType = None
        self.PeriodShift = None
        self.PeriodShiftSource = None
        self.UsersInput = None

    NOT_USED = None
    INDICATOR = "indicator"
    INSTRUMENT = "instrument"

    OPERAND = "op"
    STREAM = "stream"
    STREAM_VALUE = "streamValue"
    PARAM = "param"
    VALUE = None

    @staticmethod
    def BuildOperand(value):
        return FormulaItem(
            Value=value,
            ValueType=FormulaItem.OPERAND,
            StreamType=FormulaItem.NOT_USED
        )
