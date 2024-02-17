from Model.ParsedModel.Util import Util
from Model.JsonModel.FormulaItem import FormulaItem
class FormulaItemType:
    Stream = 0
    Value = 1
    StreamValue = 2
    Operand = 3
    Parameter = 4

class StreamType:
    NotUsed = 0
    Indicator = 1
    Instrument = 2

class MetaFormulaItem:
    def __init__(self):
        pass

    @staticmethod
    def create(argument):
        if argument is None:
            return None
        return MetaFormulaItem(argument)

    def __init__(self, arg):
        self.substream = arg.substream
        self.value = arg.value
        self.period_shift = Util.replace_parameter(arg.period_shift)
        self.period_shift_source = arg.period_shift_source
        if arg.value_type == FormulaItemType.StreamValue:
            self.value_type = FormulaItemType.StreamValue
        elif arg.value_type == FormulaItemType.Stream:
            self.value_type = FormulaItemType.Stream
        elif arg.value_type == FormulaItemType.Value:
            self.value_type = FormulaItemType.Value
        elif arg.value_type == FormulaItemType.Operand:
            self.value_type = FormulaItemType.Operand
        elif arg.value_type == FormulaItemType.Parameter:
            self.value_type = FormulaItemType.Parameter
        else:
            raise NotImplementedError()

        if arg.stream_type == FormulaItem.NOT_USED:
            self.stream_type = StreamType.Indicator if self.value_type == FormulaItemType.Stream else StreamType.NotUsed
        elif arg.stream_type == FormulaItem.INDICATOR:
            self.stream_type = StreamType.Indicator
        elif arg.stream_type == FormulaItem.INSTRUMENT:
            self.stream_type = StreamType.Instrument
        else:
            raise NotImplementedError()

    @property
    def stream_type(self):
        return self.stream_type

    @property
    def value(self):
        return self.value

    @property
    def value_type(self):
        return self.value_type

    @property
    def substream(self):
        return self.substream

    @property
    def period_shift(self):
        return self.period_shift

    @property
    def period_shift_source(self):
        return self.period_shift_source
