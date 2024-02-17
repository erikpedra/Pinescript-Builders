from Model.ParsedModel.IMetaSource import IMetaSource, SourceType

class InstrumentSource(IMetaSource):
    def __init__(self):
        self.source_type = SourceType.Instrument
        self.id = None
        self.timeframe = None
        self.price_type = None
