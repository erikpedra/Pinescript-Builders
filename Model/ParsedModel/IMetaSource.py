from enum import Enum

class SourceType(Enum):
    Indicator = 1
    Instrument = 2
    MainInstrument = 3

class IMetaSource:
    def __init__(self, source_type, id):
        self.source_type = source_type
        self.id = id
